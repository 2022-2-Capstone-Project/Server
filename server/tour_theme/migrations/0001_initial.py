# Generated by Django 4.1.3 on 2022-11-25 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TourTheme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_created=True, blank=True, null=True)),
                ('title', models.CharField(max_length=100)),
                ('estimated', models.IntegerField()),
                ('participants', models.PositiveIntegerField()),
                ('start_place', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('checkpoints', models.TextField(blank=True, null=True)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=500)),
            ],
        ),
    ]
