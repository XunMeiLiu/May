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
            name='GithubCommunity',
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
            name='GithubUser',
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
