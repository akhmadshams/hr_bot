# Generated by Django 4.2.2 on 2023-07-13 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_delete_gender_staff_contract_id_staff_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='gender',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
