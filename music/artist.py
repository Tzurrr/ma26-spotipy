import copy
from music.album import Album

class artist:
    def __init__(self, overalldata:dict, ord=0):
        self.artist_data = {}
        self.albums = []

        self.artist_data["artist_id"] = overalldata.get('track').get("artists")[ord].get("id")
        self.artist_data["artist_name"] = overalldata.get('track').get("artists")[ord].get("name")

        temp = copy.deepcopy(overalldata)
        temp.get("track").pop("artists")
        # if overalldata not in self.used:
        #     self.used.append(temp)
        self.albums.append(Album(temp))

