import time
from enum import Enum, auto


class Entity:

    class Type(Enum):
        PER = auto()
        LOC = auto()
        ORG = auto()
        MISC = auto()

    def __init__(self, name: str, type: Type, **dyn_props) -> None:
        super().__init__()

        self.name = name
        self.type = type
        self.time_created = time.time()
        self.time_touched = time.time()

        for prop in dyn_props:
            setattr(self, prop, dyn_props[prop])


class Stack:

    stored_entities = []

    class Filter:
        def __init__(self, search_filter: list) -> None:
            self.filter = []
            for k, v in search_filter:
                self.filter.append({
                    "attr": k,
                    "val": v
                })

    def __init__(self):
        super().__init__()

    def add_entity(self, entity: Entity):
        self.stored_entities.append(entity)

    def get_any(self, sf: Filter):
        return filter(lambda x: (any(getattr(x, f["attr"]) == f["val"] for f in sf.filter)), self.stored_entities)

    def get_all(self, sf: Filter):
        return filter(lambda x: (all(getattr(x, f["attr"]) == f["val"] for f in sf.filter)), self.stored_entities)


s = Stack()
s.add_entity(Entity(name="henk", type=Entity.Type.PER))
s.add_entity(Entity(name="anita", type=Entity.Type.PER))
s.add_entity(Entity(name="peter", type=Entity.Type.PER))
s.add_entity(Entity(name="white house", type=Entity.Type.LOC))

f = Stack.Filter([
    [
        "type", Entity.Type.PER
    ],
    [
        "type", Entity.Type.LOC
    ]
])

for p in s.get_any(f):
    print(getattr(p, "name"))

f2 = Stack.Filter([
    [
        "name", "henk"
    ],
    [
        "type", Entity.Type.PER
    ]
])

for p in s.get_all(f2):
    print(getattr(p, "name"))
