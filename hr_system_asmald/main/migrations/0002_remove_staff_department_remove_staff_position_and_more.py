# Generated by Django 4.2.2 on 2023-06-26 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='department',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='position',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Position',
        ),
        migrations.DeleteModel(
            name='Staff',
        ),
    ]
