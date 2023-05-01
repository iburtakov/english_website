import csv
import random

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
    new_row = [new_term, new_translation, term_src]
    terms_file = "./data/terms.csv"

    # read existing terms from file and append the new row
    with open(terms_file, "r", encoding="utf-8", newline="") as f:
        reader = csv.reader(f, delimiter=";")
        existing_rows = list(reader)
    existing_rows.append(new_row)

    # sort the rows and write them back to the file
    sorted_rows = sorted(existing_rows, key=lambda row: row[0])
    with open(terms_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerows(sorted_rows)



def get_term_to_play():
    terms = get_terms_for_table()
    index = random.randint(0, len(terms) - 1)
    num, term, trans = terms[index]
    tmp_file = "./data/tmp"

    # write the term to a temporary file
    with open(tmp_file, "w", encoding="utf-8") as f:
        f.write(term)

    return trans



def get_term_to_check():
    with open("./data/tmp", "r", encoding="utf-8") as f:
        term = f.read().strip()
    return term

