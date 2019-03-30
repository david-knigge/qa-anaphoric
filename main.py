import spacy
import argparse
import wikipedia
import nltk

from entity_store import Store, Entity
from gold_text import Checker
from nlp import Parser


rules = {
    Entity.Type.LOC: ["there", "it", "this", "these", "that", "those", "here", "its", "itself"],
    Entity.Type.ORG: ["there", "it", "this", "these", "that", "those", "here", "its", "itself"],
    Entity.Type.MISC: ["there", "it", "this", "these", "that", "those", "here", "its", "itself"],
    Entity.Type.MALE: ["i", "you", "he", "me", "you", "him", "your", "his", "myself", "yourself", "himself"],
    Entity.Type.FEMALE: ["i", "you", "she", "me", "you", "her", "your", "her", "myself", "yourself", "herself"],
    Entity.Type.PLURAL: ["we", "they", "them", "our", "their", "ourselves", "yourselves", "themselves"],
    Entity.Type.UNDECIDED: ["i", "you", "he", "she", "me", "you", "him", "her", "your", "his", "myself", "yourself", "himself", "herself"]
}

attributes = {
    Entity.Type.LOC: "type",
    Entity.Type.ORG: "type",
    Entity.Type.MISC: "type",
    Entity.Type.MALE: "gender",
    Entity.Type.FEMALE: "gender",
    Entity.Type.UNDECIDED: "gender",
    Entity.Type.PLURAL: "multiplicity"
}


def main(**kwargs):

    nlp = spacy.load('en_core_web_sm')

    s = Store()
    p = Parser()
    c = Checker()
    check_gold = []
    while True:
        text = str(input("Enter a sentence: "))
        if text == "quit":
            exit()
        elif "check" in text[:5]:
            print(c.calc_occ(check_gold,str(text[5])))

        entities = p.get_entities(text)
        for ent in entities:

            try:
                summ = wikipedia.summary(ent[0])
            except (wikipedia.exceptions.DisambiguationError, wikipedia.exceptions.WikipediaException):
                summ = ""

            if nltk.word_tokenize(ent[0])[-1] == nltk.word_tokenize(ent[0].lower().capitalize())[-1]:
                if ent[0] in open('all_surnames.txt', encoding="utf8").read():
                    ent = (ent[0], "PERSON",ent[2])

            if ent[1] == "PERSON":
                try:
                    gender = s.wolfram_alpha_query("What is the gender of {}?".format(ent[0]))[0]
                    if gender == "male":
                        gender = Entity.Type.MALE
                    elif gender == "female":
                        gender = Entity.Type.FEMALE
                except (AttributeError, IndexError) as e:
                    gender = Entity.Type.UNDECIDED
                s.add_entity(Entity(
                    name=ent[0],
                    type=Entity.Type.PER,
                    gender=gender,
                    summary=p.transform([summ]),
                    loc=(ent[2][1], ent[2][2])
                ))
            elif ent[1] in ["LOC", "GPE", "FAC"]:
                s.add_entity(Entity(
                    name=ent[0],
                    type=Entity.Type.LOC,
                    summary=p.transform([summ]),
                    loc=(ent[2][1], ent[2][2])
                ))
            elif ent[1] in ["ORG", "NORP"]:
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

                rel_dist = abs(an_index - entity.loc[0])
                prob = kwargs["wsim"] * p.sim(an_context, entity.summary) + kwargs["widist"] * 1 / rel_dist
                # prob = p.sim(an_context, entity.summary) + 1 / rel_dist

                if prob > h_prob:
                    h_prob = prob
                    most_likely = entity

            if most_likely:
                print("POSSIBLE MATCH: '{}' at word index {} -> '{}' at word index {} --- {}".format(anaphor, an_index, most_likely.name, most_likely.loc, h_prob))
                check_gold.append((anaphor,most_likely.name))


def restricted_float(x):
    x = float(x)
    if x < 0.0 or x > 1.0:
        raise argparse.ArgumentTypeError("%r not in range [0.0, 1.0]"%(x,))
    return x

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'QA with focus on anaphoric relations')
    parser.add_argument("--wsim", default=0.5, type=restricted_float)
    parser.add_argument("--widist", default=0.5, type=restricted_float)
    args = parser.parse_args()

    main(**vars(args))
