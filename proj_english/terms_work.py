import csv
from random import randint

# get terms from the table 
def get_terms_for_table():
    terms = []
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')
        for cnt, (term, translation, source) in enumerate(reader, start=1):
            terms.append([cnt, term, translation])
    return terms


# write new terms to terms.csv
def write_term(new_term, new_translation, term_src):
    new_term_line = f"{new_term};{new_translation};{term_src}"
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        existing_terms = [l.strip("\n") for l in f.readlines()]
        title = existing_terms[0]
        old_terms = existing_terms[1:]
    terms_sorted = old_terms + [new_term_line]
    terms_sorted.sort()
    new_terms = [title] + terms_sorted
    with open("./data/terms.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_terms))



def get_term_to_play():
    terms = get_terms_for_table()
    index = randint(0, len(terms)-1)
    num, term, trans = terms[index]
    with open("./data/tmp", "w", encoding="utf-8") as f:
        f.write(term)
    return trans



def get_term_to_check():
    with open("./data/tmp", "r", encoding="utf-8") as f:
        for line in f.readlines():
            term = line
    return term

