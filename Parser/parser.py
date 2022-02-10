import copy

from music.artist import artist
from read.reader import read

class parser:
    def parse(self):
        count = 0
        a = read()
        while True:
            try:
                temp = next(a)
                if len(temp.get('track').get("artists")) == 1:
                    yield (artist(temp))
                else:
                    count = 0
                    for i in range(len(temp.get('track').get("artists"))):
                        yield (artist(copy.deepcopy(temp), count))
                        count += 1
            except StopIteration:
                break


# a = parser.parse(parser)
# c = 0
# while c < 3:
#     try:
#         b = (next(a))
#         print(b.artist_data)
#         artist_data = b
#         print(b.albums[len(b.albums)-1].album_metadata)
#         c+=1
#     except StopIteration:
#         break