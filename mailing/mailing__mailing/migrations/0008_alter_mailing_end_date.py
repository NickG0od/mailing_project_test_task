# Generated by Django 4.1.4 on 2022-12-08 15:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing__mailing', '0007_alter_mailing_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 9, 15, 41, 59, 951507, tzinfo=datetime.timezone.utc)),
        ),
    ]