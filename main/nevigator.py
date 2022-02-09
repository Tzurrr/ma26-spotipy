import read.reader


class nevigator:
    a = read.reader.read()
    def read_all(self):
        while True:
            try:
                temp =next(self.a)
                print(temp.artist_data)
                for i in temp.albums:
                    print(i.album_metadata)

            except StopIteration:
                break
    def find_an_artist(self, artist_name):
        was = ""
        while True:
            try:
                temp =next(self.a)
                if temp.artist_data.get('artist_name') == artist_name:
                    for i in temp.albums:
                        print(i.album_metadata)
                        for j in i.tracks:
                            print(j.track)
                           # yield i.album_metadata
            except StopIteration:
                break

    def find_artists_albums(self, artist_name):
        was = ""
        while True:
            try:
                temp = next(self.a)
                if temp.artist_data.get('artist_name') == artist_name:
                    for i in temp.albums:
                        yield i.album_metadata
            except StopIteration:
                break
#nevigator.read_all(nevigator)
#a = nevigator.find_an_artist(nevigator, "Sarit Hadad")
a = nevigator.find_artists_albums(nevigator, "Sarit Hadad")
while True:
    try:
        print(next(a))
    except StopIteration:
        break
#     b = []
#     counter = 0
#
#     def print_all(self):
#         while True:
#             try:
#                 print(next(self.a).artist_data)
#             except StopIteration:
#                 break
#
#     def get_all(self, num):
#         for i in range(7):
#             try:
#                 next(self.a)
#             except StopIteration:
#                 break
#
#     def find_artist(self, name):
#         while True:
#             try:
#                 temp = next(self.a)
#                 if temp.artist_data.get('artist_name') == name:
#                     return self.counter
#                     # return ([album.album_metadata for album in temp.albums])
#                 self.counter +=1
#             except StopIteration:
#                 break
#
# print(nevigator.find_artist(nevigator, "Atar Mayner"))
# nevigator.print_all(nevigator)
#
# # for i in nevigator.b:
#     print(i.artist_data)

# for artist in reader.available_artists:
#    print(artist.artist_data)
# for album in artist.albums:
#     print(album.album_metadata)
# for album in artist.albums:
#     print(album.tracks)
#     for track in album.tracks:
#         print(track.track)
