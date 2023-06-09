# Generated by Django 3.2.2 on 2021-09-02 15:10

from django.db import migrations, models
import django.db.models.deletion
import policyengine.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('policyengine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlackCommunity',
            fields=[
                ('communityplatform_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.communityplatform')),
                ('team_id', models.CharField(max_length=150, unique=True, verbose_name='team_id')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('policyengine.communityplatform',),
        ),
        migrations.CreateModel(
            name='SlackJoinConversation',
            fields=[
                ('governableaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.governableaction')),
                ('channel', models.CharField(max_length=150, verbose_name='channel')),
                ('users', models.CharField(max_length=15, verbose_name='users')),
            ],
            options={
                'permissions': (('can_execute_slackjoinconversation', 'Can execute slack join conversation'),),
            },
            bases=('policyengine.governableaction',),
        ),
        migrations.CreateModel(
            name='SlackKickConversation',
            fields=[
                ('governableaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.governableaction')),
                ('user', models.CharField(max_length=15, verbose_name='user')),
                ('channel', models.CharField(max_length=150, verbose_name='channel')),
            ],
            options={
                'permissions': (('can_execute_slackkickconversation', 'Can execute slack kick conversation'),),
            },
            bases=('policyengine.governableaction',),
        ),
        migrations.CreateModel(
            name='SlackPinMessage',
            fields=[
                ('governableaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.governableaction')),
                ('channel', models.CharField(max_length=150, verbose_name='channel')),
                ('timestamp', models.CharField(max_length=32)),
            ],
            options={
                'permissions': (('can_execute_slackpinmessage', 'Can execute slack pin message'),),
            },
            bases=('policyengine.governableaction',),
        ),
        migrations.CreateModel(
            name='SlackPostMessage',
            fields=[
                ('governableaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.governableaction')),
                ('text', models.TextField()),
                ('channel', models.CharField(max_length=150, verbose_name='channel')),
                ('timestamp', models.CharField(blank=True, max_length=32)),
            ],
            options={
                'permissions': (('can_execute_slackpostmessage', 'Can execute slack post message'),),
            },
            bases=('policyengine.governableaction',),
        ),
        migrations.CreateModel(
            name='SlackRenameConversation',
            fields=[
                ('governableaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.governableaction')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
                ('channel', models.CharField(max_length=150, verbose_name='channel')),
                ('previous_name', models.CharField(max_length=80)),
            ],
            options={
                'permissions': (('can_execute_slackrenameconversation', 'Can execute slack rename conversation'),),
            },
            bases=('policyengine.governableaction',),
        ),
        migrations.CreateModel(
            name='SlackScheduleMessage',
            fields=[
                ('governableaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.governableaction')),
                ('text', models.TextField()),
                ('channel', models.CharField(max_length=150, verbose_name='channel')),
                ('post_at', models.IntegerField(verbose_name='post at')),
            ],
            options={
                'permissions': (('can_execute_slackschedulemessage', 'Can execute slack schedule message'),),
            },
            bases=('policyengine.governableaction',),
        ),
        migrations.CreateModel(
            name='SlackUser',
            fields=[
                ('communityuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.communityuser')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('policyengine.communityuser',),
            managers=[
                ('objects', policyengine.models.PolymorphicUserManager()),
            ],
        ),
    ]
