import read.reader

class nevigator:
    a = read.reader.read()
    def print_all(self):
        while True:
            try:
                print(next(self.a).artist_data)
            except StopIteration:
                break

    def find_artist(self, name):
        while True:
            try:
                temp = next(self.a)
                if temp.artist_data.get('artist_name') == name:
                    for album in temp.albums:
                        return album.album_metadata
                    #return ([album.album_metadata for album in temp.albums])

            except StopIteration:
                break


print(nevigator.find_artist(nevigator, "Sarit Hadad"))
#nevigator.print_all()
#for artist in reader.available_artists:
#    print(artist.artist_data)
    # for album in artist.albums:
    #     print(album.album_metadata)
    # for album in artist.albums:
    #     print(album.tracks)
    #     for track in album.tracks:
    #         print(track.track)