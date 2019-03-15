from enum import Enum, auto
from pprint import pformat


class Entity:

    age = 0

    class Type(Enum):
        PER = auto()
        LOC = auto()
        ORG = auto()
        MISC = auto()

    def __init__(self, name: str, type: Type, **dyn_props) -> None:
        super().__init__()

        self.name = name
        self.type = type
        self.age_created = Entity.age
        self.age_touched = Entity.age
        Entity.age += 1

        for prop in dyn_props:
            setattr(self, prop, dyn_props[prop])

    def touch(self):
        self.age_touched = Entity.age
        Entity.age += 1

    def __str__(self) -> str:
        return pformat(self.__dict__, indent=2, width=1)

    def __repr__(self) -> str:
        return self.__str__()


class Stack:

    stored_entities = []

    class Filter:
        def __init__(self, search_filter: list) -> None:
            self.filter = []
            for k, v in search_filter:
                self.filter.append({"attr": k, "val": v})

    def __init__(self):
        super().__init__()

    def add_entity(self, entity: Entity):
        self.stored_entities.append(entity)

    def get_any(self, sf: Filter) -> filter:
        return filter(lambda x: (any(getattr(x, f["attr"]) == f["val"] for f in sf.filter)), self.stored_entities)

    def get_all(self, sf: Filter) -> filter:
        return filter(lambda x: (all(getattr(x, f["attr"]) == f["val"] for f in sf.filter)), self.stored_entities)

    def __str__(self):
        return "{} ENTITIES:\n".format(len(self.stored_entities)) + pformat(
            sorted(self.stored_entities, key=lambda x: x.age_touched, reverse=True)
        )


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
    print(p)
    pass

f2 = Stack.Filter([
    [
        "name", "henk"
    ],
    [
        "type", Entity.Type.PER
    ]
])

for p in s.get_all(f2):
    #print(p)
    p.touch()
    #print(p)

print(s)