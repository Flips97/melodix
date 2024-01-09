from django.core.management.base import BaseCommand
from main_app.models import Song

class Command(BaseCommand):
    help = 'Seed the database with a list of songs'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding songs...'))

        # Your list of songs with details
        songs_data = [
            {"name": "Rolling in the Deep", "artist": "Adele", "album": "21"},
        ]


        # Seed the database
        for song_data in songs_data:
            Song.objects.create(**song_data)

        self.stdout.write(self.style.SUCCESS('Songs seeded successfully!'))



