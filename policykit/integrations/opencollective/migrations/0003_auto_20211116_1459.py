# Generated by Django 3.2.2 on 2021-11-16 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('opencollective', '0002_expensedeleted_expensepaid_expenseunapproved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expenseapproved',
            old_name='json_data',
            new_name='raw_data',
        ),
        migrations.RenameField(
            model_name='expensecreated',
            old_name='json_data',
            new_name='raw_data',
        ),
        migrations.RenameField(
            model_name='expensedeleted',
            old_name='json_data',
            new_name='raw_data',
        ),
        migrations.RenameField(
            model_name='expensepaid',
            old_name='json_data',
            new_name='raw_data',
        ),
        migrations.RenameField(
            model_name='expenserejected',
            old_name='json_data',
            new_name='raw_data',
        ),
        migrations.RenameField(
            model_name='expenseunapproved',
            old_name='json_data',
            new_name='raw_data',
        ),
    ]
