# Generated by Django 3.2.5 on 2023-04-19 23:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_rename_user_message_sender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='message',
            name='translator',
        ),
    ]