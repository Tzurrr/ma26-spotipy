import read.reader
import Parser.parser


class navigator:
    b = Parser.parser.parser.parse(Parser.parser.parser)
    def get_every_artist(self):
        b = Parser.parser.parser.parse(Parser.parser.parser)
        while True:
            try:
                c = next(b)
                print(c.artist_data)
            except StopIteration:
                break

    # Check if there's an artist with two albums to see if its still working
    def print_by_artist_uid(self, uid, popular=False):
        songs = []
        a = read.reader.read()
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
                    if len(songs) < 9:
                        print(songs)
                    else:
                        for i in range(10):
                            print(songs[i])
                    break

    def songs_in_album_by_album_uid(self, uid):
        while True:
            try:
                temp = next(self.b)
                for i in temp.albums:
                    if i.album_metadata.get("album_id") == uid:
                        for i in temp.albums:
                            print(i.album_metadata)
                            for j in i.tracks:
                                print(j.track)
            except StopIteration:
                break

# navigator.get_every_artist(navigator)
# navigator.print_by_artist_uid(navigator, "2iEvnFsWxR0Syqu2JNopAd", popular=True)
# navigator.songs_in_album_by_album_uid(navigator, "7KZkFAtkse1rKL9HdFTCuh")