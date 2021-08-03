# Generated by Django 3.2.2 on 2021-07-23 14:48

from django.db import migrations, models
import django.db.models.deletion

import json
import os
import datetime


dirname = f"downloaded_policies_{datetime.datetime.now().isoformat()}"
os.mkdir(dirname)

def download(policy):
    filename = str(policy.community) + "_" + policy.name
    filename = filename.replace(" ", "_")
    print(f"Downloading policy backup before migrating: {filename}")
    data = {
        "name": policy.name,
        "description": policy.description,
        "filter": policy.filter,
        "initialize": policy.initialize,
        "check": policy.check,
        "notify": policy.notify,
        "success": policy.success,
        "fail": policy.fail,
    }
    jsonString = json.dumps(data, indent=4)
    jsonFile = open(f"{dirname}/{filename}.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()

def migrate_policies(apps, schema_editor):
    """
    Migrate policies from old PlatformPolicy and ConstitionPolicy tables into the new Policy table.
    """
    from policyengine.models import Policy, CommunityPlatform
    PlatformPolicy = apps.get_model('policyengine', 'PlatformPolicy')
    for policy in PlatformPolicy.objects.all():
        download(policy)
        if policy.name is None:
            print("skipping unnamed policy")
            continue
        print(f"\nMigrating pp {policy.name}")
        community = CommunityPlatform.objects.get(pk=policy.community.pk)
        Policy.objects.create(
            kind=Policy.PLATFORM,
            filter=policy.filter,
            initialize=policy.initialize,
            check=policy.check,
            notify=policy.notify,
            success=policy.success,
            fail=policy.fail,
            community=community,
            name=policy.name,
            description=policy.description,
            is_active=policy.is_active,
            modified_at=policy.modified_at,
        )
    ConstitutionPolicy = apps.get_model('policyengine', 'ConstitutionPolicy')
    for policy in ConstitutionPolicy.objects.all():
        download(policy)
        if policy.name is None:
            print("skipping unnamed policy")
            continue
        print(f"\nMigrating cp {policy.name}")
        community = CommunityPlatform.objects.get(pk=policy.community.pk)
        Policy.objects.create(
            kind=Policy.CONSTITUTION,
            filter=policy.filter,
            initialize=policy.initialize,
            check=policy.check,
            notify=policy.notify,
            success=policy.success,
            fail=policy.fail,
            community=community,
            name=policy.name,
            description=policy.description,
            is_active=policy.is_active,
            modified_at=policy.modified_at,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('policyengine', '0002_proposal_governance_process_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.CharField(choices=[('platform', 'platform'), ('constitution', 'constitution')], max_length=30)),
                ('filter', models.TextField(blank=True, default='')),
                ('initialize', models.TextField(blank=True, default='')),
                ('check', models.TextField(blank=True, default='')),
                ('notify', models.TextField(blank=True, default='')),
                ('success', models.TextField(blank=True, default='')),
                ('fail', models.TextField(blank=True, default='')),
                ('name', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('bundled_policies', models.ManyToManyField(blank=True, related_name='member_of_bundle', to='policyengine.Policy')),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.communityplatform', verbose_name='community')),
                ('data', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='policyengine.datastore', verbose_name='data')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(migrate_policies),
        migrations.RemoveField(
            model_name='constitutionpolicy',
            name='community',
        ),
        migrations.RemoveField(
            model_name='constitutionpolicy',
            name='data',
        ),
        migrations.RemoveField(
            model_name='platformpolicy',
            name='community',
        ),
        migrations.RemoveField(
            model_name='platformpolicy',
            name='data',
        ),
        migrations.RemoveField(
            model_name='platformpolicybundle',
            name='bundled_policies',
        ),
        migrations.RemoveField(
            model_name='platformpolicybundle',
            name='community',
        ),
        migrations.RemoveField(
            model_name='platformpolicybundle',
            name='data',
        ),
        migrations.DeleteModel(
            name='ConstitutionPolicyBundle',
        ),
        migrations.DeleteModel(
            name='PlatformPolicyBundle',
        ),
        migrations.AlterField(
            model_name='policykitchangeconstitutionpolicy',
            name='constitution_policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.policy'),
        ),
        migrations.AlterField(
            model_name='policykitchangeplatformpolicy',
            name='platform_policy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='policyengine.policy'),
        ),
        migrations.AlterField(
            model_name='policykitrecoverconstitutionpolicy',
            name='constitution_policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.policy'),
        ),
        migrations.AlterField(
            model_name='policykitrecoverplatformpolicy',
            name='platform_policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.policy'),
        ),
        migrations.AlterField(
            model_name='policykitremoveconstitutionpolicy',
            name='constitution_policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.policy'),
        ),
        migrations.AlterField(
            model_name='policykitremoveplatformpolicy',
            name='platform_policy',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='policyengine.policy'),
        ),
        migrations.DeleteModel(
            name='ConstitutionPolicy',
        ),
    ]