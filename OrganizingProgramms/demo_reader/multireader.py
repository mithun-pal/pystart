# demo_reader.multireader.py

import os
from demo_reader.compressed import bzipped, gzipped

ext_map = {
    ".bz2": bzipped.opener,
    ".gz": gzipped.opener
}


class MultiReader:
    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = ext_map.get(extension, open)
        self.f = opener(filename, "rt")

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()