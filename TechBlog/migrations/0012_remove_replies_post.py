# Generated by Django 4.2.2 on 2023-07-13 12:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TechBlog', '0011_remove_comment_parent_replies'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='replies',
            name='post',
        ),
    ]
