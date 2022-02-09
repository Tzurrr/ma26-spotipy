import copy
from music.album import Album
class artist:
    artist_data = {}
    albums = []
    def __init__(self, artist: dict, overalldata:dict):
        self.artist_data["artist_id"] = artist.get("id")
        self.artist_data["artist_name"] = artist.get("name")

        temp_album = copy.deepcopy(overalldata)
        temp_album.get("track").pop("artists")

        if Album(temp_album) in self.albums:
            pass
        else:
            self.albums.append(Album(temp_album))

    def get_albums(self):
        return self.albums