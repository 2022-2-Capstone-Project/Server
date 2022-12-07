# Generated by Django 4.1.3 on 2022-12-07 12:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tour_theme", "0001_initial"),
        ("tour", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tour",
            name="profile_id",
            field=models.ForeignKey(
                db_column="profile_id",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="생성유저",
            ),
        ),
        migrations.AddField(
            model_name="tour",
            name="theme_id",
            field=models.ForeignKey(
                db_column="theme_id",
                on_delete=django.db.models.deletion.CASCADE,
                to="tour_theme.tourtheme",
                verbose_name="테마이름",
            ),
        ),
    ]
