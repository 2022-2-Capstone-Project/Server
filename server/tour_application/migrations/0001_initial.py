# Generated by Django 4.1.3 on 2022-11-25 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tour', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TourApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('participants_on_site', models.IntegerField(blank=True, default=0)),
                ('tour_finished', models.BooleanField(blank=True, default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='참가신청일시')),
                ('tour', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tour_application', to='tour.tour', verbose_name='투어')),
            ],
            options={
                'verbose_name': '투어신청서',
                'verbose_name_plural': '투어신청서',
                'db_table': 'tour_application',
            },
        ),
    ]
