# Generated by Django 2.1.4 on 2018-12-17 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0075_pisregistration_responsefile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pisregistration',
            name='responseFile',
        ),
    ]