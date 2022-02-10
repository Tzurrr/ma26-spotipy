import uuid
import music.track
from exeptions.spotipy_exeptions import *
import copy

class Album:
    def __init__(self, album: dict):
        self.album = {}
        self.album_metadata = {}
        self.tracks = []
        self.album_metadata["album_name"] = album.get('track').get("album").get("name")
        self.album_metadata["album_id"] = album.get('track').get("album").get("id")

        temp_album = copy.deepcopy(album)
        temp_album.get("track").pop("album")
        self.tracks.append(music.track.track(temp_album))