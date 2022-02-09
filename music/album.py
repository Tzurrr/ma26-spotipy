import uuid
import music.track
from exeptions.spotipy_exeptions import *
import copy

class Album:
    album = {}
    album_metadata = {}
    tracks = []
    used =[]
    def __init__(self, album: dict):
        self.album_metadata["album_name"] = album.get('track').get("album").get("name")
        self.album_metadata["album_id"] = album.get('track').get("album").get("id")


        if album not in self.tracks:
            self.used.append(album)
            album.get("track").pop("album")
            self.tracks.append(music.track.track(copy.deepcopy(album)))