# Generated by Django 4.2.2 on 2023-06-24 10:25

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TechBlog', '0004_alter_techpost_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='techpost',
            name='likes',
        ),
        migrations.AddField(
            model_name='techpost',
            name='likes',
            field=models.ManyToManyField(related_name='tech_posts', to=settings.AUTH_USER_MODEL),
        ),
    ]
