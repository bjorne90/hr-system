# Generated by Django 3.2.19 on 2023-05-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduling', '0002_auto_20230509_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshift',
            name='name',
            field=models.CharField(default='Default Name', max_length=100),
        ),
    ]
