# Generated by Django 4.2.2 on 2023-07-17 13:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TechBlog', '0015_rename_blogcomment_techblogcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techpost',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
