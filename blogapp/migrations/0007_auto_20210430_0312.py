# Generated by Django 3.1.7 on 2021-04-30 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0006_auto_20210429_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
