# Generated by Django 5.0.1 on 2024-02-07 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='group',
        ),
    ]