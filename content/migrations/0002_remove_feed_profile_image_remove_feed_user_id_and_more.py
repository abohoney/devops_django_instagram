# Generated by Django 4.2.1 on 2023-05-14 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feed',
            name='profile_image',
        ),
        migrations.RemoveField(
            model_name='feed',
            name='user_id',
        ),
        migrations.AddField(
            model_name='feed',
            name='email',
            field=models.EmailField(default=2, max_length=254),
            preserve_default=False,
        ),
    ]
