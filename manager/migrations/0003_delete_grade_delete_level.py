# Generated by Django 4.1.4 on 2022-12-31 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_level_grade'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Grade',
        ),
        migrations.DeleteModel(
            name='Level',
        ),
    ]
