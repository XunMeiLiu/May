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
            name='RedditCommunity',
            fields=[
                ('communityplatform_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.communityplatform')),
                ('team_id', models.CharField(max_length=150, unique=True, verbose_name='team_id')),
                ('access_token', models.CharField(max_length=300, unique=True, verbose_name='access_token')),
                ('refresh_token', models.CharField(max_length=500, null=True, verbose_name='refresh_token')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('policyengine.communityplatform',),
        ),
        migrations.CreateModel(
            name='RedditMakePost',
            fields=[
                ('governableaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.governableaction')),
                ('title', models.CharField(max_length=500, null=True, verbose_name='title')),
                ('text', models.TextField()),
                ('kind', models.CharField(default='self', max_length=30, verbose_name='kind')),
                ('name', models.CharField(max_length=100, null=True, verbose_name='name')),
                ('communityaction_ptr', models.CharField(max_length=100, null=True, verbose_name='ptr')),
            ],
            options={
                'permissions': (('can_execute_redditmakepost', 'Can execute reddit make post'),),
            },
            bases=('policyengine.governableaction',),
        ),
        migrations.CreateModel(
            name='RedditUser',
            fields=[
                ('communityuser_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.communityuser')),
                ('refresh_token', models.CharField(max_length=500, null=True, verbose_name='refresh_token')),
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
