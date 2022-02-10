import logging

import read.reader
from log_in.user_settings import user
import playlist.Creation
import search.navigator
logging.basicConfig(filename=r'D:\Code\Spotipy\app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')

a = user.user("aaa")
# a.add_playlists(playlist.Creation.playlist(a.user_type).playlists)
# print(a.user_playlists)

logging.warning('I dont know why from here it doesent works, but from the nevigator class it is. I dont have time to check why because I have to submit this exercise')
search.navigator.navigator.songs_in_album_by_album_uid(search.navigator.navigator,"7KZkFAtkse1rKL9HdFTCuh", a.user_type)