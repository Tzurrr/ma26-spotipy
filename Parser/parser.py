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
