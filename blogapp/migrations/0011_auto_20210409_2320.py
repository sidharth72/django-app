# Generated by Django 3.1.7 on 2021-04-10 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blogapp', '0010_auto_20210409_2254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='post_data',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
