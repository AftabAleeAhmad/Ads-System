# Generated by Django 4.2.4 on 2023-08-29 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Ads_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ad',
            old_name='name',
            new_name='ad_name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='loc_name',
        ),
    ]
