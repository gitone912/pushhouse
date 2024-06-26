# Generated by Django 4.1.6 on 2023-02-24 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0002_alter_subscription_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
