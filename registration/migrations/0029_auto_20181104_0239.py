# Generated by Django 2.1.1 on 2018-11-03 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0028_auto_20181030_2353'),
    ]

    operations = [
        migrations.RenameField(
            model_name='wikimediaphotographyregistration',
            old_name='wikimediaUserID',
            new_name='wikimediaUsername',
        ),
    ]
