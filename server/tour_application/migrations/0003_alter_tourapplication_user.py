# Generated by Django 4.1.3 on 2022-12-07 16:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tour_application", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tourapplication",
            name="user",
            field=models.ManyToManyField(
                blank=True,
                related_name="tour_application",
                to=settings.AUTH_USER_MODEL,
                verbose_name="투어참가유저",
            ),
        ),
    ]
