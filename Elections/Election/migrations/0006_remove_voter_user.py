# Generated by Django 3.1.2 on 2020-10-22 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Election', '0005_voter_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voter',
            name='user',
        ),
    ]
