# Generated by Django 4.2.2 on 2023-06-19 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_delete_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('country_code', models.CharField(max_length=5, null=True)),
                ('unique_session_id', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='EmailSubscriber',
        ),
    ]