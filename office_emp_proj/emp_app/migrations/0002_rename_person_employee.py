# Generated by Django 5.0.4 on 2024-04-25 17:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('emp_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Employee',
        ),
    ]
