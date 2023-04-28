import csv
from random import randint

def get_grammar_for_table():
    sentences = []
    with open("./data/grammar.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')
        for cnt, (sentence, word, source) in enumerate(reader, start=1):
            sentences.append([cnt, sentence, word])
    return sentences


def get_grammar_to_play():
    sentences = get_grammar_for_table()
    index = randint(0, len(sentences) - 1)
    num, sentence, word = sentences[index]
    with open("./data/tmp", "w", encoding="utf-8") as f:
        f.write(word)
    return sentence

def get_grammar_to_check():
    with open("./data/tmp", "r", encoding="utf-8") as f:
        for line in f.readlines():
            word = line
    return word