# Generated by Django 3.2.2 on 2021-09-02 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluationLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_str', models.CharField(blank=True, max_length=150)),
                ('action_str', models.CharField(blank=True, max_length=150)),
                ('logger_name', models.CharField(max_length=100)),
                ('level', models.PositiveSmallIntegerField(choices=[(0, 'NotSet'), (20, 'Info'), (30, 'Warning'), (10, 'Debug'), (40, 'Error'), (50, 'Fatal')], db_index=True, default=40)),
                ('msg', models.TextField(verbose_name='Message')),
                ('trace', models.TextField(blank=True, null=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
            ],
            options={
                'verbose_name': 'Logging',
                'verbose_name_plural': 'Logging',
                'ordering': ('-create_datetime',),
            },
        ),
    ]
