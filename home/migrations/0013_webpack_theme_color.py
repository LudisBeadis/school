# Generated by Django 4.1.4 on 2022-12-24 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_webpack_facebook_webpack_telegram'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpack',
            name='theme_color',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]