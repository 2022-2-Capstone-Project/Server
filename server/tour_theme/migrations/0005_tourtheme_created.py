# Generated by Django 4.1.2 on 2022-11-01 04:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_theme', '0004_alter_tourtheme_estimated'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourtheme',
            name='created',
            field=models.DateTimeField(auto_created=True, blank=True, default=datetime.datetime(2022, 11, 1, 13, 38, 40, 366232)),
            preserve_default=False,
        ),
    ]