# Generated by Django 4.0 on 2022-01-16 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='storyiten',
            name='body',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='storyiten',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]