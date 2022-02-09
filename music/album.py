import uuid


class Album:
    album_metadata = {}
    artists_data = []
    def __init__(self, album: dict, tracks: list):
        self.album_metadata["album_name"] = album.get("name")
        self.album_metadata["album_id"] = album.get("id")

        for track in tracks:
            track_data = {}
            track_data["track_id"] = track.get("id")
            track_data["track_name"] = track.get("name")
            track_data["track_popularity"] = track.get("popularity")
            self.artists_data.append(track_data)

