# Generated by Django 4.1 on 2022-11-09 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_application', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tourapplication',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='참가신청일시'),
        ),
    ]
