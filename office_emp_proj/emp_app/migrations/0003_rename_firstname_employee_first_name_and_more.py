# Generated by Django 5.0.4 on 2024-04-28 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0002_rename_person_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='firstname',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='employee',
            old_name='lastname',
            new_name='last_name',
        ),
    ]