# Generated by Django 3.2.9 on 2021-12-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_checkout_zip_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='checkout',
            name='zipcode',
            field=models.IntegerField(default=''),
        ),
    ]
