from django.core.management.base import BaseCommand
from main_app.models import Song

class Command(BaseCommand):
    help = 'Seed the database with a list of songs'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding songs...'))

        # Your list of songs with details
        songs_data = [
            {"name": "Rolling in the Deep", "artist": "Adele", "album": "21"},
            {"name": "Somebody That I Used to Know", "artist": "Gotye ft. Kimbra", "album": "Making Mirrors"},
            {"name": "Radioactive", "artist": "Imagine Dragons", "album": "Night Visions"},
            {"name": "Shake It Off", "artist": "Taylor Swift", "album": "1989"},
            {"name": "Havana", "artist": "Camila Cabello ft. Young Thug", "album": "Camila"},
            {"name": "Shape of You", "artist": "Ed Sheeran", "album": "÷"},
            {"name": "Despacito", "artist": "Luis Fonsi ft. Daddy Yankee", "album": "Vida"},
            {"name": "Uptown Funk", "artist": "Mark Ronson ft. Bruno Mars", "album": "Uptown Special"},
            {"name": "Someone You Loved", "artist": "Lewis Capaldi", "album": "Divinely Uninspired"},
            {"name": "Bad Romance", "artist": "Lady Gaga", "album": "The Fame Monster"},
            {"name": "Bohemian Rhapsody", "artist": "Queen", "album": "A Night at the Opera"},
            {"name": "Old Town Road", "artist": "Lil Nas X ft. Billy Ray Cyrus", "album": "7 EP"},
            {"name": "Sicko Mode", "artist": "Travis Scott", "album": "Astroworld"},
            {"name": "Savage Love", "artist": "Jawsh 685 & Jason Derulo", "album": "Singles"},
            {"name": "Blinding Lights", "artist": "The Weeknd", "album": "After Hours"},
            {"name": "Watermelon Sugar", "artist": "Harry Styles", "album": "Fine Line"},
            {"name": "Dance Monkey", "artist": "Tones and I", "album": "The Kids Are Coming"},
            {"name": "Stressed Out", "artist": "Twenty One Pilots", "album": "Blurryface"},
            {"name": "Counting Stars", "artist": "OneRepublic", "album": "Native"},
            {"name": "Chandelier", "artist": "Sia", "album": "1000 Forms of Fear"},
            {"name": "Hotline Bling", "artist": "Drake", "album": "Views"},
            {"name": "Sucker", "artist": "Jonas Brothers", "album": "Happiness Begins"},
            {"name": "The Box", "artist": "Roddy Ricch", "album": "Please Excuse Me For Being"},
            {"name": "Sunflower", "artist": "Post Malone ft. Swae Lee", "album": "Spider-Man"},
            {"name": "Circles", "artist": "Post Malone", "album": "Hollywood's Bleeding"},
            {"name": "Truth Hurts", "artist": "Lizzo", "album": "Cuz I Love You"},
            {"name": "Señorita", "artist": "Shawn Mendes & Camila Cabello", "album": "Shawn Mendes"},
            {"name": "Shape of You", "artist": "Ed Sheeran", "album": "÷"},
            {"name": "Happier", "artist": "Marshmello ft. Bastille", "album": "Happier"},
            {"name": "WAP", "artist": "Cardi B ft. Megan Thee Stallion", "album": "WAP"},
            {"name": "Memories", "artist": "Maroon 5", "album": "Memories"},
            {"name": "Sucker for Pain", "artist": "Lil Wayne, Wiz Khalifa & Imagine Dragons", "album": "Suicide Squad: The Album"},
            {"name": "Lucid Dreams", "artist": "Juice WRLD", "album": "Goodbye & Good Riddance"},
            {"name": "Faded", "artist": "Alan Walker", "album": "Different World"},
            {"name": "SAD!", "artist": "XXXTENTACION", "album": "17"},
            {"name": "ROXANNE", "artist": "Arizona Zervas", "album": "ROXANNE"},
            {"name": "Taki Taki", "artist": "DJ Snake", "album": "Taki Taki"},
            {"name": "Believer", "artist": "Imagine Dragons", "album": "Evolve"},
            {"name": "Havana", "artist": "Camila Cabello ft. Young Thug", "album": "Camila"},
            {"name": "Rockstar", "artist": "Post Malone ft. 21 Savage", "album": "beerbongs & bentleys"},
            {"name": "High Hopes", "artist": "Panic! At The Disco", "album": "Pray for the Wicked"},
            {"name": "Suge", "artist": "DaBaby", "album": "Baby on Baby"},
            {"name": "I Like It", "artist": "Cardi B, Bad Bunny & J Balvin", "album": "Invasion of Privacy"},
            {"name": "All of Me", "artist": "John Legend", "album": "Love in the Future"},
            {"name": "Without Me", "artist": "Halsey", "album": "Without Me"},
            {"name": "Lucid Dreams", "artist": "Juice WRLD", "album": "Goodbye & Good Riddance"},
            {"name": "Bang Bang", "artist": "Jessie J, Ariana Grande & Nicki Minaj", "album": "Sweet Talker"},
            {"name": "Ride", "artist": "Twenty One Pilots", "album": "Blurryface"},
            {"name": "Bang Bang", "artist": "Jessie J, Ariana Grande & Nicki Minaj", "album": "Sweet Talker"},
            {"name": "I Don't Care", "artist": "Ed Sheeran & Justin Bieber", "album": "No.6 Collaborations Project"},
            {"name": "Bad and Boujee", "artist": "Migos ft. Lil Uzi Vert", "album": "Culture"},
            {"name": "Havana", "artist": "Camila Cabello ft. Young Thug", "album": "Camila"},
            {"name": "SICKO MODE", "artist": "Travis Scott", "album": "ASTROWORLD"},
            {"name": "Shut Up and Dance", "artist": "WALK THE MOON", "album": "TALKING IS HARD"},
            {"name": "Love Me Like You Do", "artist": "Ellie Goulding", "album": "Fifty Shades of Grey"},
            {"name": "Bad Guy", "artist": "Billie Eilish", "album": "WHEN WE ALL FALL ASLEEP"},
            {"name": "Sugar", "artist": "Maroon 5", "album": "V"},
            {"name": "No Tears Left To Cry", "artist": "Ariana Grande", "album": "Sweetener"},
            {"name": "Party in the USA", "artist": "Miley Cyrus", "album": "The Time of Our Lives"},
            {"name": "Say So", "artist": "Doja Cat", "album": "Hot Pink"},
            {"name": "Wrecking Ball", "artist": "Miley Cyrus", "album": "Bangerz"},
            {"name": "Bang Bang", "artist": "Jessie J, Ariana Grande & Nicki Minaj", "album": "Sweet Talker"},
            {"name": "Thrift Shop", "artist": "Macklemore & Ryan Lewis ft. Wanz", "album": "The Heist"},
            {"name": "Dark Horse", "artist": "Katy Perry ft. Juicy J", "album": "Prism"},
            {"name": "Wake Me Up", "artist": "Avicii", "album": "True"},
            {"name": "WAP", "artist": "Cardi B ft. Megan Thee Stallion", "album": "WAP"},
            {"name": "Firework", "artist": "Katy Perry", "album": "Teenage Dream"},
            {"name": "Sucker for Pain", "artist": "Lil Wayne", "album": "Suicide Squad: The Album"},
            {"name": "Radioactive", "artist": "Imagine Dragons", "album": "Night Visions"},
            {"name": "Shake It Off", "artist": "Taylor Swift", "album": "1989"},
            {"name": "Old Town Road", "artist": "Lil Nas X ft. Billy Ray Cyrus", "album": "7 EP"},
            {"name": "Sicko Mode", "artist": "Travis Scott", "album": "Astroworld"},
            {"name": "Savage Love", "artist": "Jawsh 685 & Jason Derulo", "album": "Singles"},
            {"name": "Blinding Lights", "artist": "The Weeknd", "album": "After Hours"},
            {"name": "Watermelon Sugar", "artist": "Harry Styles", "album": "Fine Line"},
            {"name": "Dance Monkey", "artist": "Tones and I", "album": "The Kids Are Coming"},
        ]


        # Seed the database
        for song_data in songs_data:
            Song.objects.create(**song_data)

        self.stdout.write(self.style.SUCCESS('Songs seeded successfully!'))



