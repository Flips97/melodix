from django.core.management.base import BaseCommand
from main_app.models import Song

class Command(BaseCommand):
    help = 'Seed the database with a list of songs'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Seeding songs...'))

        # Your list of songs with details
        songs_data = [
            {"name": "Blinding Lights", "artist": "The Weeknd", "album": "After Hours"},
            {"name": "Watermelon Sugar", "artist": "Harry Styles", "album": "Fine Line"},
            {"name": "Levitating", "artist": "Dua Lipa", "album": "Future Nostalgia"},
            {"name": "Save Your Tears", "artist": "The Weeknd", "album": "After Hours"},
            {"name": "Peaches", "artist": "Justin Bieber", "album": "Justice"},
            {"name": "good 4 u", "artist": "Olivia Rodrigo", "album": "SOUR"},
            {"name": "Kiss Me More", "artist": "Doja Cat ft. SZA", "album": "Planet Her"},
            {"name": "Montero (Call Me By Your Name)", "artist": "Lil Nas X", "album": "Montero"},
            {"name": "Deja Vu", "artist": "Olivia Rodrigo", "album": "SOUR"},
            {"name": "Leave The Door Open", "artist": "Silk Sonic (Bruno Mars, Anderson .Paak)", "album": "An Evening with Silk Sonic"},
            {"name": "Peaches", "artist": "Justin Bieber ft. Daniel Caesar, Giveon", "album": "Justice"},
            {"name": "Butter", "artist": "BTS", "album": "Butter (SINGLE)"},
            {"name": "Happier Than Ever", "artist": "Billie Eilish", "album": "Happier Than Ever"},
            {"name": "Bad Habits", "artist": "Ed Sheeran", "album": "Bad Habits (SINGLE)"},
            {"name": "Stay", "artist": "The Kid LAROI, Justin Bieber", "album": "Stay (SINGLE)"},
            {"name": "Good Days", "artist": "SZA", "album": "Good Days (SINGLE)"},
            {"name": "Levitating (Remix)", "artist": "Dua Lipa ft. DaBaby", "album": "Levitating (Remix)"},
            {"name": "Heat Waves", "artist": "Glass Animals", "album": "Dreamland"},
            {"name": "Stay", "artist": "The Kid LAROI, Justin Bieber", "album": "F*CK LOVE 3: OVER YOU"},
            {"name": "Save Your Tears (Remix)", "artist": "The Weeknd, Ariana Grande", "album": "Save Your Tears (Remix)"},
            {"name": "DÁKITI", "artist": "Bad Bunny, Jhay Cortez", "album": "EL ÚLTIMO TOUR DEL MUNDO"},
            {"name": "drivers license", "artist": "Olivia Rodrigo", "album": "SOUR"},
            {"name": "Without You", "artist": "The Kid LAROI", "album": "F*CK LOVE 3: OVER YOU"},
            {"name": "Heartbreak Anniversary", "artist": "Giveon", "album": "Take Time"},
            {"name": "Therefore I Am", "artist": "Billie Eilish", "album": "Therefore I Am (SINGLE)"},
            {"name": "Mood", "artist": "24kGoldn ft. iann dior", "album": "El Dorado"},
            {"name": "Industry Baby", "artist": "Lil Nas X, Jack Harlow", "album": "Industry Baby (SINGLE)"},
            {"name": "Kiss Me More", "artist": "Doja Cat ft. SZA", "album": "Planet Her"},
            {"name": "Good 4 U", "artist": "Olivia Rodrigo", "album": "SOUR"},
            {"name": "Telepatía", "artist": "Kali Uchis", "album": "Sin Miedo (del Amor y Otros Demonios) ∞"},
            {"name": "Favorito", "artist": "Camilo", "album": "Favorito (SINGLE)"},
            {"name": "The Business", "artist": "Tiësto", "album": "The Business (SINGLE)"},
            {"name": "Savage Love (Laxed – Siren Beat)", "artist": "Jawsh 685 x Jason Derulo", "album": "Savage Love (Laxed – Siren Beat) (SINGLE)"},
            {"name": "Astronaut In The Ocean", "artist": "Masked Wolf", "album": "Astronaut In The Ocean (SINGLE)"},
            {"name": "Yonaguni", "artist": "Bad Bunny", "album": "Yonaguni (SINGLE)"},
            {"name": "Levitating", "artist": "Dua Lipa", "album": "Future Nostalgia (The Moonlight Edition)"},
            {"name": "Life Goes On", "artist": "BTS", "album": "BE"},
            {"name": "MONTERO (Call Me By Your Name)", "artist": "Lil Nas X", "album": "MONTERO"},
            {"name": "Diamonds Dancing", "artist": "Drake, Future", "album": "Certified Lover Boy"},
            {"name": "Sicko Mode", "artist": "Travis Scott", "album": "ASTROWORLD"},
            {"name": "MONTERO (Call Me By Your Name)", "artist": "Lil Nas X", "album": "MONTERO"},
            {"name": "Save Your Tears", "artist": "The Weeknd, Ariana Grande", "album": "Save Your Tears (Remix)"},
            {"name": "Kiss Me More", "artist": "Doja Cat ft. SZA", "album": "Planet Her"},
            {"name": "Permission To Dance", "artist": "BTS", "album": "Butter (SINGLE)"},
            {"name": "Mood", "artist": "24kGoldn ft. iann dior", "album": "El Dorado"},
            {"name": "SUN GOES DOWN", "artist": "Lil Nas X", "album": "SUN GOES DOWN (SINGLE)"},
            {"name": "Levitating (Remix)", "artist": "Dua Lipa ft. DaBaby", "album": "Levitating (Remix)"},
            {"name": "Butter", "artist": "BTS", "album": "Butter (SINGLE)"},
            {"name": "Kiss Me More", "artist": "Doja Cat ft. SZA", "album": "Planet Her"},
            {"name": "Save Your Tears", "artist": "The Weeknd, Ariana Grande", "album": "Save Your Tears (Remix)"},
            {"name": "Levitating", "artist": "Dua Lipa ft. DaBaby", "album": "Levitating (Remix)"},
            {"name": "Kiss Me More", "artist": "Doja Cat ft. SZA", "album": "Planet Her"},
            {"name": "Save Your Tears", "artist": "The Weeknd, Ariana Grande", "album": "Save Your Tears (Remix)"},
            {"name": "Levitating", "artist": "Dua Lipa ft. DaBaby", "album": "Levitating (Remix)"},
            {"name": "Kiss Me More", "artist": "Doja Cat ft. SZA", "album": "Planet Her"},
            {"name": "Save Your Tears", "artist": "The Weeknd, Ariana Grande", "album": "Save Your Tears (Remix)"},
            {"name": "Levitating", "artist": "Dua Lipa ft. DaBaby", "album": "Levitating (Remix)"},
            {"name": "Kiss Me More", "artist": "Doja Cat ft. SZA", "album": "Planet Her"},
            {"name": "Save Your Tears", "artist": "The Weeknd, Ariana Grande", "album": "Save Your Tears (Remix)"},
            {"name": "Levitating", "artist": "Dua Lipa ft. DaBaby", "album": "Levitating (Remix)"},
            {"name": "Kiss Me More", "artist": "Doja Cat ft. SZA", "album": "Planet Her"},
            {"name": "Save Your Tears", "artist": "The Weeknd, Ariana Grande", "album": "Save Your Tears (Remix)"},
            {"name": "Levitating", "artist": "Dua Lipa ft. DaBaby", "album": "Levitating (Remix)"},
            {"name": "Kiss Me More", "artist": "Doja Cat ft. SZA", "album": "Planet Her"},
            {"name": "Save Your Tears", "artist": "The Weeknd, Ariana Grande", "album": "Save Your Tears (Remix)"},
            {"name": "Levitating", "artist": "Dua Lipa ft. DaBaby", "album": "Levitating (Remix)"},
            {"name": "Kiss Me More", "artist": "Doja Cat ft. SZA", "album": "Planet Her"},
            {"name": "Save Your Tears", "artist": "The Weeknd, Ariana Grande", "album": "Save Your Tears (Remix)"},
            {"name": "Levitating", "artist": "Dua Lipa ft. DaBaby", "album": "Levitating (Remix)"},
            {"name": "Kiss Me More", "artist": "Doja Cat ft. SZA", "album": "Planet Her"},
            {"name": "Save Your Tears", "artist": "The Weeknd, Ariana Grande", "album": "Save Your Tears (Remix)"},
            {"name": "Levitating", "artist": "Dua Lipa ft. DaBaby", "album": "Levitating (Remix)"},
        ]


        # Seed the database
        for song_data in songs_data:
            Song.objects.create(**song_data)

        self.stdout.write(self.style.SUCCESS('Songs seeded successfully!'))



