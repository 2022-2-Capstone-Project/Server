# Generated by Django 4.1.3 on 2022-12-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tour_theme", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tourtheme",
            name="is_premium",
            field=models.BooleanField(default=False),
        ),
    ]