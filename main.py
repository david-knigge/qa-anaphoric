import spacy
import argparse
import wikipedia

from entity_store import Store, Entity
from nlp import Parser


rules = {
    Entity.Type.PER: ["i", "you", "he", "she", "we", "they", "me", "you", "him", "her", "us", "them", "my", "your", "his",
                      "our", "their", "myself", "yourself", "himself", "herself", "ourselves", "yourselves", "themselves"
                      ],
    Entity.Type.LOC: ["there", "it", "this", "these", "that", "those", "here", "its", "itself"],
    Entity.Type.ORG: ["there", "it", "this", "these", "that", "those", "here", "its", "itself"],
    Entity.Type.MISC: ["there", "it", "this", "these", "that", "those", "here", "its", "itself"],


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

            try:
                gender = s.wolfram_alpha_query("What is the gender of {}?".format(ent[0]))
                s.add_entity(Entity(name=ent[0], type=Entity.Type.PER, gender=gender, summary=p.transform([summ])))

            except AttributeError:
                if ent[1] == ["LOC", "GPE"]:
                    s.add_entity(Entity(name=ent[0], type=Entity.Type.LOC, summary=p.transform([summ])))
                elif ent[1] in ["ORG"]:
                    s.add_entity(Entity(name=ent[0], type=Entity.Type.ORG, summary=p.transform([summ])))
                elif ent[1] == "MISC":
                    s.add_entity(Entity(name=ent[0], type=Entity.Type.MISC, summary=p.transform([summ])))

        anaphora = p.get_anaphora(text)

        for anaphor, an_context in anaphora:

            most_likely = None
            h_prob = 0

            for entity in s.stored_entities:

                if anaphor.lower() in rules[entity.type]:

                    prob = p.sim(an_context, entity.summary)
                    #print(anaphor, entity.name, prob)
                    if prob > h_prob:
                        h_prob = prob
                        most_likely = entity

            if most_likely:
                print("POSSIBLE MATCH: {} -> {} --- {}".format(anaphor, most_likely.name, h_prob))
        print("Male entities: ", s.get_all_male())
        print("Female entities: ", s.get_all_female())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'QA with focus on anaphoric relations')
    args = parser.parse_args()

    main(*vars(args))
