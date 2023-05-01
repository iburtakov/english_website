import csv
import random

# get terms from the table 
def get_terms_for_table():
    with open("./data/terms.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        return [[cnt, term, translation] for cnt, (term, translation, source) in enumerate(reader, start=1)]


# write new terms to terms.csv
def write_term(new_term: str, new_translation: str, term_src: str):
    terms_file = "./data/terms.csv"
    with open(terms_file, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow([new_term, new_translation, term_src])



def get_term_to_use():
    terms = get_terms_for_table()
    term = random.choice(terms)
    with open("./data/tmp", "w", encoding="utf-8") as f:
        f.write(term[1])
    return term[2]



def get_term_to_check():
    with open("./data/tmp", "r", encoding="utf-8") as f:
        term = f.read().strip()
    return term

