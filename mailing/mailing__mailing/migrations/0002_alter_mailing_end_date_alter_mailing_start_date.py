# Generated by Django 4.1.4 on 2022-12-08 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing__mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 9, 15, 33, 13, 748797, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 8, 15, 33, 13, 748797, tzinfo=datetime.timezone.utc)),
        ),
    ]