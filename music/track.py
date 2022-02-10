from exeptions.spotipy_exeptions import *


class track:

    def __init__(self, track: dict):
        self.track = {}
        if self.track != {}:
            raise CantInsertTwoTracksIntoOneExeption("Cant Insert Two Tracks Into One")
        self.track = track
