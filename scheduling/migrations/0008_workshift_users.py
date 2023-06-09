# Generated by Django 3.2.18 on 2023-05-22 00:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('scheduling', '0007_workshift_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='workshift',
            name='users',
            field=models.ManyToManyField(related_name='workshifts', through='scheduling.Booking', to=settings.AUTH_USER_MODEL),
        ),
    ]
