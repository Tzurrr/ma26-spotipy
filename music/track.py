from exeptions.spotipy_exeptions import *


class track:
    track = {}
    def __init__(self, track: dict):
        if self.track != {}:
            raise CantInsertTwoTracksIntoOneExeption("Cant Insert Two Tracks Into One")
        else:
            self.track = track