import os

class reader:
    def read(self):
        #songs_directory =
        with open(r"D:\Code\Spotipy\songs", "r") as songs_folder:
            for song in songs_folder:
                print(song)

reader = reader()
reader.read()