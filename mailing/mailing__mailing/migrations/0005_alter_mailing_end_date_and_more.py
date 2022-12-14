# Generated by Django 4.1.4 on 2022-12-08 15:36

import datetime
from django.db import migrations, models
import mailing__mailing.models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing__mailing', '0004_alter_mailing_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 9, 15, 36, 2, 231665, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='properties_filter',
            field=models.JSONField(blank=True, default=mailing__mailing.models.Mailing.properties_filter_default, null=True),
        ),
    ]
