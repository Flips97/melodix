# Generated by Django 5.0 on 2024-01-03 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_playlist_songs_alter_playlist_user_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='discription',
            field=models.TextField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]