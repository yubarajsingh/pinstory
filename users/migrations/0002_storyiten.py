# Generated by Django 4.0.1 on 2022-01-11 03:29

from django.db import migrations, models
import django.db.models.deletion
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoryIten',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iten', models.JSONField(default=users.models.get_default_something)),
                ('photo', models.ImageField(default=True, null=True, upload_to='images')),
                ('storyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.story')),
            ],
        ),
    ]