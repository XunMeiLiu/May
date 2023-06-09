# Generated by Django 3.2.2 on 2022-10-17 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('policyengine', '0011_auto_20221016_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='PolicyVariable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('label', models.TextField()),
                ('default_value', models.TextField()),
                ('value', models.TextField(blank=True)),
                ('prompt', models.TextField(blank=True)),
                ('type', models.CharField(choices=[('number', 'number'), ('string', 'string')], default='string', max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='policy',
            name='variables',
        ),
        migrations.AddField(
            model_name='policy',
            name='variables',
            field=models.ManyToManyField(blank=True, related_name='variables', to='policyengine.PolicyVariable'),
        ),
    ]
