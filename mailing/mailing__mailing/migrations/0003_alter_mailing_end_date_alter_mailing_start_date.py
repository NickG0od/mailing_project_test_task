# Generated by Django 4.1.4 on 2022-12-08 15:33

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mailing__mailing', '0002_alter_mailing_end_date_alter_mailing_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 9, 15, 33, 36, 501725, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
