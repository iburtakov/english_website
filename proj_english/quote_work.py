import csv
from random import randint
from typing import Tuple

def get_quotes_for_table():
    with open("./data/quotes.csv", "r", encoding="utf-8") as f:
        quotes = [[cnt, quote, person] for cnt, (quote, person) in enumerate(csv.reader(f, delimiter=";"), start=1)]
    return quotes


def get_quote_to_use() -> Tuple[str, str]:
    with open("./data/quotes.csv", "r", encoding="utf-8") as f:
        quotes = list(csv.reader(f, delimiter=";"))
    index = randint(0, len(quotes) - 1)
    return quotes[index][0], quotes[index][1]