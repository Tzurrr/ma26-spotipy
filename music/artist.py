import copy
from music.album import Album
class artist:
    artist_data = {}
    used = []
    albums = []
    def __init__(self, overalldata:dict, ord):
        self.artist_data["artist_id"] = overalldata.get('track').get("artists")[ord].get("id")
        self.artist_data["artist_name"] = overalldata.get('track').get("artists")[ord].get("name")


        overalldata.get("track").pop("artists")
        if overalldata not in self.used:
            self.used.append(overalldata)
            self.albums.append(Album(copy.deepcopy(overalldata)))

