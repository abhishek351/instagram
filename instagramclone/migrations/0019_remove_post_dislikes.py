# Generated by Django 3.2.4 on 2021-09-03 02:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagramclone', '0018_auto_20210903_0701'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
    ]