# Generated by Django 3.0 on 2021-01-20 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_role_full_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='full_name',
            new_name='role_word',
        ),
    ]
