# Generated by Django 4.2.2 on 2023-07-01 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TechBlog', '0007_techblogcomment_delete_blogcomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TechBlogComment',
        ),
    ]
