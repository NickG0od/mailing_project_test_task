# Generated by Django 4.1.4 on 2022-12-09 11:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing__mailing', '0013_alter_mailing_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 10, 11, 13, 24, 35155, tzinfo=datetime.timezone.utc)),
        ),
    ]
