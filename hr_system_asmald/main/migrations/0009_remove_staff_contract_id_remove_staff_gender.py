# Generated by Django 4.2.2 on 2023-07-13 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_gender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='contract_id',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='gender',
        ),
    ]
