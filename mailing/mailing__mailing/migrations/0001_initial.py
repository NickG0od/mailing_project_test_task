# Generated by Django 4.1.4 on 2022-12-08 15:33

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('msg_text', models.CharField(blank=True, max_length=255, null=True)),
                ('properties_filter', models.JSONField(blank=True, default=[{'operator_code': None}, {'tag': None}], null=True)),
                ('end_date', models.DateTimeField(default=datetime.datetime(2022, 12, 9, 15, 33, 1, 841258, tzinfo=datetime.timezone.utc))),
            ],
        ),
    ]
