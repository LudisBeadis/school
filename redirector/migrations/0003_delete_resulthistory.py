# Generated by Django 4.1.4 on 2023-01-05 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('redirector', '0002_history_testhistory_resulthistory'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ResultHistory',
        ),
    ]
