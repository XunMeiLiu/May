# Generated by Django 3.2.2 on 2021-11-10 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('policyengine', '0003_choicevote'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebhookTriggerAction',
            fields=[
                ('baseaction_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='policyengine.baseaction')),
                ('json_data', models.JSONField(blank=True, null=True)),
                ('event_type', models.CharField(blank=True, max_length=50, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('policyengine.baseaction', models.Model),
        ),
    ]
