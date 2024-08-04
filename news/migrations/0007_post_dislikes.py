# Generated by Django 4.2.14 on 2024-08-04 16:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0006_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.ManyToManyField(related_name='news_post_dislikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
