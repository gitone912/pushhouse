# Generated by Django 4.1.6 on 2023-02-27 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_remove_newdata_id_newdata_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newdata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
