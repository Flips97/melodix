from django.core.management.base import BaseCommand
from main_app.models import Song

class Command(BaseCommand):
    help = 'Seed the database with a list of songs'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding songs...'))

        # Your list of songs with details
        songs_data = [
        {"name": "Who Let the Dogs Out", "artist": "Baha Men", "album": "Who Let the Dogs Out"},
        {"name": "Black Dog", "artist": "Led Zeppelin", "album": "Led Zeppelin IV"},
        {"name": "Hound Dog", "artist": "Elvis Presley", "album": "Single Release"},
        {"name": "Diamond Dogs", "artist": "David Bowie", "album": "Diamond Dogs"},
        {"name": "Atomic Dog", "artist": "George Clinton", "album": "Computer Games"},
        {"name": "Dog Days Are Over", "artist": "Florence + The Machine", "album": "Lungs"},
        {"name": "Dog Eat Dog", "artist": "AC/DC", "album": "Let There Be Rock"},
        {"name": "Walking the Dog", "artist": "Rufus Thomas", "album": "Walking the Dog"},
        {"name": "Hair of the Dog", "artist": "Nazareth", "album": "Hair of the Dog"},
        {"name": "I Wanna Be Your Dog", "artist": "The Stooges", "album": "The Stooges"},
        {"name": "Doggy Dog World", "artist": "Snoop Dogg", "album": "Doggystyle"},
        {"name": "Walking the Dog", "artist": "Fun", "album": "Aim and Ignite"},
        {"name": "Doghouse Blues", "artist": "Gary Moore", "album": "Close as You Get"},
        {"name": "Me and You and a Dog Named Boo", "artist": "Lobo", "album": "Of a Simple Man"},
        {"name": "Gimme Back My Dog", "artist": "Slobberbone", "album": "Everything You Thought Was Right Was Wrong Today"},
        {"name": "Dog on Wheels", "artist": "Belle and Sebastian", "album": "Dog on Wheels EP"},
        {"name": "Dog's Life", "artist": "Eels", "album": "Daisies of the Galaxy"},
        {"name": "The Puppy Song", "artist": "Harry Nilsson", "album": "Harry"},
        {"name": "Diamond Dogs (Again)", "artist": "Beck", "album": "Record Club: The Velvet Underground & Nico"},
        {"name": "Year of the Dog Again", "artist": "DMX", "album": "Year of the Dog...Again"}
        ]

        # Seed the database
        for song_data in songs_data:
            Song.objects.create(**song_data)

        self.stdout.write(self.style.SUCCESS('Songs seeded successfully!'))



