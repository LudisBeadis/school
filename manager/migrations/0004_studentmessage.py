# Generated by Django 4.1.4 on 2022-12-31 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_delete_grade_delete_level'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='manager/post')),
                ('title', models.CharField(max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('message', models.TextField(max_length=1000, null=True)),
                ('link_name', models.CharField(blank=True, max_length=20)),
                ('link', models.URLField(blank=True)),
            ],
        ),
    ]
