# Generated by Django 4.1.4 on 2022-12-08 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing__client', '0003_alter_client_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='mobile_operator_code',
            field=models.CharField(max_length=3, validators=[django.core.validators.RegexValidator(message="Operator code must be entered in the format: 'XXX' where X: 0-9.", regex='^\\d{3,3}$')]),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone_number',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '7XXXXXXXXXX' where X: 0-9.", regex='^[7]\\d{10,10}$')]),
        ),
    ]
