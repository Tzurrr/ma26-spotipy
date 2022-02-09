import uuid
import music.track
from exeptions.spotipy_exeptions import *
import copy

class Album:
    album = {}
    album_metadata = {}
    tracks = []
    def __init__(self, album: dict):
        self.album_metadata["album_name"] = album.get('track').get("album").get("name")
        self.album_metadata["album_id"] = album.get('track').get("album").get("id")

        temp_track = copy.deepcopy(album)
        temp_track.get("track").pop("album")
        self.tracks.append(music.track.track(temp_track))

    def get_tracks(self):
        return self.tracks