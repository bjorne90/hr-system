# Generated by Django 3.2.18 on 2023-05-16 23:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0004_auto_20230510_1103'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='users',
            field=models.ManyToManyField(related_name='bookings', to=settings.AUTH_USER_MODEL),
        ),
    ]
