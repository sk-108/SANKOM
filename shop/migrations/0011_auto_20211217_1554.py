# Generated by Django 3.2.9 on 2021-12-17 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20211217_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='zipcode',
        ),
        migrations.AddField(
            model_name='checkout',
            name='zip_code',
            field=models.CharField(default='', max_length=100),
        ),
    ]
