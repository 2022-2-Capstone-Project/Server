# Generated by Django 4.1.2 on 2022-11-01 08:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tour_theme', '0006_remove_profile_bookmarks_remove_profile_followers_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=30)),
                ('user_type', models.CharField(choices=[('JR', 'Junior'), ('SR', 'Senior')], default='JR', max_length=2)),
                ('reputation', models.PositiveIntegerField(default=0)),
                ('bookmarks', models.ManyToManyField(blank=True, to='tour_theme.tourtheme')),
                ('followers', models.ManyToManyField(blank=True, related_name='follow', to='user.profile')),
                ('follows', models.ManyToManyField(blank=True, related_name='follower', to='user.profile')),
                ('likes', models.ManyToManyField(blank=True, to='tour_theme.tour')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
