import time


class FileCard:

    def __init__(self, name, gender, context=None, relationships=None):
        super().__init__()

        self.name = name
        self.gender = gender
        self.context = context
        self.relationships = relationships
        self.created = time.time()
        self.touched = time.time()

    def touch(self):
        self.touched = time.time()