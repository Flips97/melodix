# Generated by Django 5.0 on 2024-01-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_rename_discription_playlist_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='artist',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
