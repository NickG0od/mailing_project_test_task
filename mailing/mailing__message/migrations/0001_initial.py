# Generated by Django 4.1.4 on 2022-12-08 15:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mailing__client', '0004_alter_client_mobile_operator_code_and_more'),
        ('mailing__mailing', '0009_alter_mailing_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sending_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('sending_status', models.IntegerField(choices=[(1, 'Success'), (0, 'Failure'), (-1, 'Pending'), (-2, 'Canceled')], default=0, max_length=1)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing__client.client')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing__mailing.mailing')),
            ],
        ),
    ]
