# Generated by Django 3.1.7 on 2021-05-14 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_post_intro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile_img',
        ),
    ]
