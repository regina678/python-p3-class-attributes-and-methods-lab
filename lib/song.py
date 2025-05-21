class Song:
    # Class attributes
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Call class methods from __init__
        self.add_song_to_count()
        self.add_to_genres(genre)
        self.add_to_artists(artist)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1


# Example usage
song1 = Song("Song A", "Artist 1", "Pop")
song2 = Song("Song B", "Artist 2", "Rock")
song3 = Song("Song C", "Artist 1", "Pop")
song4 = Song("Song D", "Artist 3", "Country")

print("Total Songs:", Song.count)                     # 4
print("Unique Genres:", Song.genres)                  # ['Pop', 'Rock', 'Country']
print("Unique Artists:", Song.artists)                # ['Artist 1', 'Artist 2', 'Artist 3']
print("Genre Counts:", Song.genre_count)              # {'Pop': 2, 'Rock': 1, 'Country': 1}
print("Artist Counts:", Song.artist_count)            # {'Artist 1': 2, 'Artist 2': 1, 'Artist 3': 1}

