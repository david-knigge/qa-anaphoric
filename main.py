import spacy
import argparse
import wikipedia

from entity_store import Store, Entity
from nlp import Parser


rules = {
    Entity.Type.LOC: ["there", "it", "this", "these", "that", "those", "here", "its", "itself"],
    Entity.Type.ORG: ["there", "it", "this", "these", "that", "those", "here", "its", "itself"],
    Entity.Type.MISC: ["there", "it", "this", "these", "that", "those", "here", "its", "itself"],
    Entity.Type.MALE: ["i", "you", "he", "me", "you", "him", "your", "his", "myself", "yourself", "himself"],
    Entity.Type.FEMALE: ["i", "you", "she", "me", "you", "her", "your", "her", "myself", "yourself", "herself"],
    Entity.Type.PLURAL: ["we", "they", "them", "our", "their", "ourselves", "yourselves", "themselves"]
}

attributes = {
    Entity.Type.LOC: "type",
    Entity.Type.ORG: "type",
    Entity.Type.MISC: "type",
    Entity.Type.MALE: "gender",
    Entity.Type.FEMALE: "gender",
    Entity.Type.PLURAL: "multiplicity"
}


def main(**kwargs):

    nlp = spacy.load('en_core_web_sm')

    s = Store()
    p = Parser()

    while True:
        text = str(input("Enter a sentence: "))

        if text == "quit":
            exit(0)

        entities = p.get_entities(text)
        for ent in entities:

            try:
                summ = wikipedia.summary(ent[0])
            except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.WikipediaException):
                summ = ""

            if ent[1] == "PERSON":
                gender = s.wolfram_alpha_query("What is the gender of {}?".format(ent[0]))
                if gender[0] == "male":
                    gender = Entity.Type.MALE
                elif gender[0] == "female":
                    gender = Entity.Type.FEMALE
                s.add_entity(Entity(
                    name=ent[0],
                    type=Entity.Type.PER,
                    gender=gender,
                    summary=p.transform([summ]),
                    loc=(ent[2][1], ent[2][2])
                ))
            elif ent[1] in ["LOC", "GPE"]:
                s.add_entity(Entity(
                    name=ent[0],
                    type=Entity.Type.LOC,
                    summary=p.transform([summ]),
                    loc=(ent[2][1], ent[2][2])
                ))
            elif ent[1] in ["ORG"]:
                s.add_entity(Entity(
                    name=ent[0],
                    type=Entity.Type.ORG,
                    summary=p.transform([summ]),
                    loc=(ent[2][1], ent[2][2])
                ))
            elif ent[1] == "MISC":
                s.add_entity(Entity(
                    name=ent[0],
                    type=Entity.Type.MISC,
                    summary=p.transform([summ]),
                    loc=(ent[2][1], ent[2][2])
                ))

        anaphora = p.get_anaphora(text)

        for anaphor, an_context, an_index in anaphora:

            most_likely = None
            h_prob = -1

            f_list = []
            for rule, anaphor_list in rules.items():

                if anaphor in anaphor_list:
                    f_list.append([attributes[rule], rule])

            for entity in s.get_any(Store.Filter(f_list)):

                prob = p.sim(an_context, entity.summary)

                if prob > h_prob:
                    h_prob = prob
                    most_likely = entity

            if most_likely:
                print("POSSIBLE MATCH: '{}' at word index {} -> '{}' at word index {} --- {}".format(anaphor, an_index, most_likely.name, most_likely.loc, h_prob))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'QA with focus on anaphoric relations')
    args = parser.parse_args()

    main(*vars(args))
