# Generated by Django 4.1.6 on 2023-02-26 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_userdata'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='userdata',
            name='updated_at',
        ),
    ]
