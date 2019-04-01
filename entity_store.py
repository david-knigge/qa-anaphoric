from enum import Enum, auto
from pprint import pformat
import wolframalpha


# Store entity attributes
class Entity:

    age = 0

    # Possible entity types
    class Type(Enum):
        PER = auto()
        LOC = auto()
        ORG = auto()
        MISC = auto()
        MALE = auto()
        FEMALE = auto()
        PLURAL = auto()
        UNDECIDED = auto()

    # Set entity attributes
    def __init__(self, name: str, type: Type, **dyn_props) -> None:
        super().__init__()

        self.name = name
        self.type = type
        self.age_created = Entity.age
        self.age_touched = Entity.age
        Entity.age += 1
        self.gender = ""
        for prop in dyn_props:
            setattr(self, prop, dyn_props[prop])

    # Reset time this entity has been touched last
    def touch(self):
        self.age_touched = Entity.age
        Entity.age += 1

    # Return formatted string containing details on the entity.
    def __str__(self) -> str:
        return pformat(self.__dict__, indent=2, width=1)

    def __repr__(self) -> str:
        return self.__str__()


# Stores set of entities found in the document.
class Store:

    stored_entities = []

    # Create a search filter, takes a list of key value pairs, where the keys are attributes of the entity to filter on
    # and the values are the values of these attiributes.
    class Filter:
        def __init__(self, search_filter: list) -> None:
            self.filter = []
            for k, v in search_filter:
                self.filter.append({"attr": k, "val": v})

    def __init__(self):
        super().__init__()

    # Add a new entity to the store if it is not contained in the list already.
    def add_entity(self, entity: Entity):
        if not list(self.get_all(self.Filter([["name", entity.name]]))):
            self.stored_entities.append(entity)

    # Return entites that possess any of the filter attribute value pairs
    def get_any(self, sf: Filter) -> filter:
        return filter(lambda x: (any(getattr(x, f["attr"], None) == f["val"] for f in sf.filter)), self.stored_entities)

    # Return entities that possess all of the filter attribute value pairs
    def get_all(self, sf: Filter) -> filter:
        return filter(lambda x: (all(getattr(x, f["attr"], None) == f["val"] for f in sf.filter)), self.stored_entities)

    # Print formatted representation
    def __str__(self):
        return "{} ENTITIES:\n".format(len(self.stored_entities)) + pformat(
            sorted(self.stored_entities, key=lambda x: x.age_touched, reverse=True)
        )

    # Query wolfram api
    def wolfram_alpha_query(self, query: str):
        wa = wolframalpha.Client("VH5LXL-ALTVYGQVU3")
        return [result.text for result in wa.query(query).results]

# s = Stack()
# s.add_entity(Entity(name="henk", type=Entity.Type.PER))
# s.add_entity(Entity(name="anita", type=Entity.Type.PER))
# s.add_entity(Entity(name="peter", type=Entity.Type.PER))
# s.add_entity(Entity(name="white house", type=Entity.Type.LOC))
#
# f = Stack.Filter([
#     [
#         "type", Entity.Type.PER
#     ],
#     [
#         "type", Entity.Type.LOC
#     ]
# ])
#
# s.get_any(f)
#
# f2 = Stack.Filter([
#     [
#         "name", "henk"
#     ],
#     [
#         "type", Entity.Type.PER
#     ]
# ])
#
# s.get_all(f2)

