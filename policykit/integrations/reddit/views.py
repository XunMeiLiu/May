from django.shortcuts import render, redirect
from django.http import HttpResponse
from policykit.settings import SERVER_URL, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET
from integrations.reddit.models import RedditCommunity, RedditUser, REDDIT_USER_AGENT
from policyengine.models import *
from policyengine.utils import render_starterkit_view, default_boolean_vote_message
from django.contrib.auth import login, authenticate
from django.views.decorators.csrf import csrf_exempt
from urllib import parse
import urllib.request
import json
import base64
import logging


logger = logging.getLogger(__name__)


# Create your views here.

def oauth(request):
    logger.info(request)

    state = request.GET.get('state')
    code = request.GET.get('code')
    error = request.GET.get('error')

    logger.info(code)

    if error == 'access_denied':
        # error message stating that the sign-in/add-to-reddit didn't work
        response = redirect('/login?error=cancel')
        return response

    data = parse.urlencode({
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': SERVER_URL + '/reddit/oauth',
        }).encode()

    req = urllib.request.Request('https://www.reddit.com/api/v1/access_token', data=data)

    credentials = ('%s:%s' % (REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET))
    encoded_credentials = base64.b64encode(credentials.encode('ascii'))

    req.add_header("Authorization", "Basic %s" % encoded_credentials.decode("ascii"))
    req.add_header("User-Agent", REDDIT_USER_AGENT)

    resp = urllib.request.urlopen(req)
    res = json.loads(resp.read().decode('utf-8'))

    logger.info(res)

    if state == "policykit_reddit_user_login":
        user = authenticate(request, oauth=res, platform="reddit")
        if user:
            login(request, user)
            response = redirect('/main')
            return response
        else:
            response = redirect('/login?error=invalid_login')
            return response

    elif state == "policykit_reddit_mod_install":
        req = urllib.request.Request('https://oauth.reddit.com/subreddits/mine/moderator')
        req.add_header('Authorization', 'bearer %s' % res['access_token'])
        req.add_header("User-Agent", REDDIT_USER_AGENT)
        resp = urllib.request.urlopen(req)
        reddit_info = json.loads(resp.read().decode('utf-8'))

        logger.info(reddit_info)
        titles = []

        for item in reddit_info['data']['children']:
            if item['data']['title'] != '':
                titles.append(item['data']['display_name'])

        if len(titles) > 0:
            context = {
                "subreddits": titles,
                "access_token": res['access_token'],
                "refresh_token": res['refresh_token']
            }
            return render(request, "policyadmin/configure.html", context)

    response = redirect('/login?error=no_subreddits_with_mod_privileges_found')
    return response

@csrf_exempt
def init_community_reddit(request):
    title = request.POST['subreddit']
    access_token = request.POST['access_token']
    refresh_token = request.POST['refresh_token']

    s = RedditCommunity.objects.filter(team_id=title)

    community = None

    if not s.exists():
        community = RedditCommunity.objects.create(
            community_name=title,
            team_id=title,
            access_token=access_token,
            refresh_token=refresh_token,
        )
    else:
        community = s[0]
        community.community_name = title
        community.team_id = title
        community.access_token = access_token
        community.refresh_token = refresh_token
        community.save()

        response = redirect('/login?success=true')
        return response

    return render_starterkit_view(request, community.community.pk)

@csrf_exempt
def action(request):
    json_data = json.loads(request.body)
    logger.info('RECEIVED ACTION')
    logger.info(json_data)

def initiate_action_vote(proposal, users, text=None):
    from policyengine.models import LogAPICall
    policy = proposal.policy
    action = proposal.action
    policy_message = text or default_boolean_vote_message(proposal.policy)

    values = {
              'ad': False,
              'api_type': 'json',
              'kind': 'self',
              'sr': action.community.community_name,
              'text': policy_message,
              'title': 'Vote on action'
              }

    res = LogAPICall.make_api_call(policy.community, values, 'api/submit')

    logger.info(res)


    proposal.vote_post_id = res['json']['data']['name']
    proposal.save()
