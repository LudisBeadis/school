# Generated by Django 4.1.4 on 2022-12-31 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_alter_studentmessage_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentmessage',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='manager.manager'),
        ),
    ]