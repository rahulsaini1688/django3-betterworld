# Generated by Django 3.1.5 on 2021-01-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0005_auto_20210121_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(default='Portfolio/images/Watch-this-space.jpg', upload_to='Portfolio/images'),
        ),
    ]
