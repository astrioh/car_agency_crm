# Generated by Django 3.0 on 2021-01-20 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_remove_role_role_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='role',
            name='full_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
