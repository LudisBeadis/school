# Generated by Django 4.1.5 on 2023-01-13 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redirector', '0005_delete_resulthistory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicyear',
            name='year',
            field=models.IntegerField(),
        ),
    ]
