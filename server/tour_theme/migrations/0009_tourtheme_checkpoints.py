# Generated by Django 4.1.2 on 2022-11-12 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_theme', '0008_alter_tourtheme_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourtheme',
            name='checkpoints',
            field=models.TextField(blank=True, null=True),
        ),
    ]
