# Generated by Django 4.2.1 on 2023-06-02 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myparking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='parking_spot',
        ),
    ]
