# Generated by Django 3.1.5 on 2021-01-19 21:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='blog_post_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]