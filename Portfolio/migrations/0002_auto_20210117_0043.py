# Generated by Django 3.1.5 on 2021-01-17 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Projects',
        ),
    ]