# Generated by Django 4.2.2 on 2023-07-18 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_tag_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='tab_blog', to='blog.tag_blog'),
        ),
    ]