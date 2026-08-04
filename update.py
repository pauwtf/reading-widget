import json
import requests

from notion import HEADERS, BOOK_LOG_DATABASE_URL
from books import build_current_book
from quotes import (
    get_quotes_for_book,
    get_random_quote,
    get_quote_stats
)


payload = {
    "filter": {
        "property": "Actual",
        "checkbox": {
            "equals": True
        }
    },
    "page_size": 1
}


response = requests.post(
    BOOK_LOG_DATABASE_URL,
    headers=HEADERS,
    json=payload
)

response.raise_for_status()

data = response.json()

if not data["results"]:

    raise Exception(
        "No hay ningún libro marcado como Actual"
    )


book_page = data["results"][0]

book_id = book_page["id"]

book = book_page["properties"]


current_book = build_current_book(
    book,
    book_id
)


quotes = get_quotes_for_book(book_id)


current_book["quote"] = get_random_quote(
    quotes,
    book_id
)


if current_book["quote"]:

    current_book["quote"]["favoriteIcon"] = (
        "♥"
        if current_book["quote"]["favorite"]
        else ""
    )


current_book["quoteStats"] = get_quote_stats(
    quotes
)


print("\n========== READING WIDGET ==========\n")

print(current_book["title"])
print(current_book["author"])
print(current_book["display"]["pageText"])
print(current_book["display"]["progressBar"])
print(current_book["display"]["progressText"])

if current_book.get("quote"):

    print()

    print(
        f'"{current_book["quote"]["text"]}"'
    )

    print(
        f'Página {current_book["quote"]["page"]}'
    )

    print(
        current_book["quote"]["favoriteIcon"]
    )

print("\n====================================\n")


with open(
    "currentBook.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        current_book,
        f,
        ensure_ascii=False,
        indent=4
    )


print(
    "✅ currentBook.json generado correctamente"
)