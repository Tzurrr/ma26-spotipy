import playlist.Creation


class user:
    user_playlists = []
    def __init__(self, user_name:str, type="r"):
        self.user_name = user_name
        self.user_type = type
    def add_playlists(self, playlist: list):
        self.user_playlists.append(playlist)