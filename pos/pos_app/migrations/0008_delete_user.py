# Generated by Django 5.0.1 on 2024-02-22 05:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos_app', '0007_alter_user_owner'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]