# Generated by Django 4.1.7 on 2023-04-22 11:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_account_is_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_favorite',
        ),
    ]
