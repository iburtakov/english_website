import csv
import random

def get_grammar_from_table():
    with open("./data/grammar.csv", "r", encoding="utf-8") as f:
        sentences = [[cnt, sentence, word] for cnt, (sentence, word, source)
                     in enumerate(csv.reader(f, delimiter=';'), start=1)]
    return sentences


def get_grammar_to_use():
    _, sentence, word = random.choice(get_grammar_from_table())
    with open("./data/tmp", "w", encoding="utf-8") as f:
        f.write(word)
    return sentence

def get_grammar_to_check():
    with open("./data/tmp", "r", encoding="utf-8") as f:
        word = f.read().strip()
    return word