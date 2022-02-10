import copy
import logging

from music.album import Album
logging.basicConfig(filename=r'D:\Code\Spotipy\app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

class artist:
    def __init__(self, overalldata:dict, ord=0):
        self.artist_data = {}
        self.albums = []

        self.artist_data["artist_id"] = overalldata.get('track').get("artists")[ord].get("id")
        self.artist_data["artist_name"] = overalldata.get('track').get("artists")[ord].get("name")

        #logging.INFO("created a copy in order to not ruin the main dict")
        temp = copy.deepcopy(overalldata)
        temp.get("track").pop("artists")
        self.albums.append(Album(temp))

