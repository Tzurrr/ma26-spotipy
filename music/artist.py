class artist:
    artist_data = {}
    albums = []

    def __init__(self, artists: list, album: dict):
        for artist in artists:
            self.artist_data["artist_id"] = artist.get("id")
            self.artist_data["artist_name"] = artist.get("name")

        self.albums.append(album)