# Generated by Django 2.1.1 on 2018-10-13 23:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0018_auto_20181007_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='battleofbandsregistration',
            old_name='videoFile',
            new_name='audioVideoFile',
        ),
        migrations.RenameField(
            model_name='battleofbandsregistration',
            old_name='videoFileLink',
            new_name='audioVideoFileLink',
        ),
    ]
