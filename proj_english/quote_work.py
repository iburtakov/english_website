import csv
from random import randint
from typing import Tuple

def get_quotes_for_table():
    quotes = []
    with open("./data/quotes.csv", "r", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=';')
        for cnt, (quote, person) in enumerate(reader, start=1):
            quotes.append([cnt, quote, person])
    return quotes


def get_quote_to_play() -> Tuple[str, str]:
    quotes = get_quotes_for_table()
    index = randint(0, len(quotes)-1)
    num, quote, person = quotes[index]
    return quote, person