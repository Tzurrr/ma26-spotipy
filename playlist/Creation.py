import itertools
import Parser.parser
from exeptions.spotipy_exeptions import *
from read.reader import read


class playlist:
    playlists = []
    a = read()

    def __init__(self, user_type="r"):
        if user_type == "r":
            if len(self.playlists) >= 5:
                raise PlayListBoundReached("a non-premium user can only have 5 playlists")
            self.playlists.append(self.playlist_creation(song_limit=20))
        else:
            while True:
                self.playlists.append(self.playlist_creation())

    def playlist_creation(self, song_limit=itertools.count(0)):
        songs = []
        playlist = {}
        name = input("enter the playlist name")
        for playlist1 in self.playlists:
            if playlist1.get('name') == name:
                raise PlaylistAlreadyExists("a playlist with that name is already exists")

        playlist['name'] = name

        for i in range(song_limit):
            user_input = input("enter the songs you want to have")
            if user_input == "exit":
                break
            songs.append(user_input)

        count = 0
        while True:
            try:
                count += 1
                temp = next(self.a)
                if temp.get('track').get("name") in songs:
                    playlist[f"song number {count}"] = temp.get('track').get("name")
                    songs.remove(temp.get('track').get("name"))
                    count += 1
                if count == 3:
                    raise StopIteration
            except StopIteration:
                print(f"didnt find those songs: {songs}")
                return playlist

# a = playlist
# a()
# print(a.playlists)
#
