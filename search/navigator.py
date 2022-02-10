import itertools

import read.reader
import Parser.parser


class navigator:
    b = Parser.parser.parser.parse(Parser.parser.parser)
    def get_every_artist(self, user_type='r'):
        b = Parser.parser.parser.parse(Parser.parser.parser)
        if user_type == 'r':
            count = 5
        else:
            count = itertools.count(0)

        for i in range(count):
            try:
                c = next(b)
                print(c.artist_data)
            except StopIteration:
                break

    # Check if there's an artist with two albums to see if it's still works
    def print_by_artist_uid(self, uid, popular=False, user_type ="r"):
        songs = []
        a = read.reader.read()
        if user_type == "r":
            limit = 5
        else:
            limit = 10

        while True:
            try:
                temp = next(a)
                for i in range(len(temp.get('track').get("artists"))):
                    if temp.get('track').get("artists")[i].get('id') == uid:
                        if popular == False:
                            print(temp.get('track').get("album").get('name'))
                        songs.append((temp.get('track').get("name"), temp.get('track').get("id"), temp.get('track').get("popularity")))
            except StopIteration:
                if popular == False:
                    break
                else:
                    songs.sort(key=lambda x:x[2], reverse=True)
                    if len(songs) < limit-1:
                        print(songs)
                    else:
                        for i in range(limit):
                            print(songs[i])
                    break

    def songs_in_album_by_album_uid(self, uid, user_type='r'):
        if user_type == 'r':
            count = 5
        else:
            count = itertools.count(0)

        for i in range(count):
            try:
                temp = next(self.b)
                for j in temp.albums:
                    if j.album_metadata.get("album_id") == uid:
                        for a in temp.albums:
                            print(a.album_metadata)
                            for k in a.tracks:
                                print(k.track)
            except StopIteration:
                break

# navigator.get_every_artist(navigator)
# navigator.print_by_artist_uid(navigator, "2iEvnFsWxR0Syqu2JNopAd", popular=True)
# navigator.songs_in_album_by_album_uid(navigator, "7KZkFAtkse1rKL9HdFTCuh")