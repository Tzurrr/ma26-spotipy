import os
import yaml
import json

from music.artist import artist

with open(r"D:\Code\Spotipy\config.yaml") as a_yaml_file:
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    path = parsed_yaml_file["SONG_DIRECTORY_PATH"].get("PATH")


class reader:
    available_artists = []
    def read(self, some_key_to_filter_on = None):
        for file in os.listdir(path):
            f = os.path.join(path, file)
            with open(f, "r") as song:
                temp_songs_dict = json.load(song)
                for artist_data in temp_songs_dict.get('track').get("artists"):
                    self.available_artists.append(artist(artist_data, temp_songs_dict))


reader = reader()
reader.read()