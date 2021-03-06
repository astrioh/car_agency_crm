# Generated by Django 3.0 on 2021-01-20 20:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=30)),
                ('middlename', models.CharField(max_length=30)),
                ('sex', models.CharField(max_length=10)),
                ('birthday', models.DateField()),
                ('pass_series', models.CharField(max_length=5)),
                ('pass_number', models.CharField(max_length=10)),
                ('inn', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(max_length=30)),
                ('address', models.CharField(blank=True, max_length=80, null=True)),
                ('phone', models.CharField(max_length=20)),
                ('active', models.BooleanField()),
                ('id_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employees.Role')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
