
import os
from whoosh.index import create_in, open_dir, exists_in
from whoosh.fields import Schema, TEXT, STORED


class Search:

    def __init__(self, max_distance, index_path):
        self.max_distance = max_distance
        self.index_path = index_path
        self.schema = self.create_schema()
        self.index = self.create_index

    @staticmethod
    def create_schema():
        return Schema(
            add_id=STORED,
            street=TEXT(stored=True),
            cep=TEXT(stored=True),
            city=TEXT(stored=True)
        )

    def create_index(self):
        if os.path.exists(self.index_path):
            return open_dir(self.index_path)
        else:
            os.mkdir(self.index_path)
            return create_in(self.index_path, self.schema)




