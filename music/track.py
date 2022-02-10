import logging

from exeptions.spotipy_exeptions import *
logging.basicConfig(filename=r'D:\Code\Spotipy\app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')


class track:

    def __init__(self, track: dict):
        self.track = {}
        if self.track != {}:
            logging.WARN("handeled exeption")
            raise CantInsertTwoTracksIntoOneExeption("Cant Insert Two Tracks Into One")
        self.track = track
