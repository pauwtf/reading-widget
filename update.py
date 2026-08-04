import json
import requests

from notion import HEADERS, BOOK_LOG_DATABASE_URL
from books import build_current_book
from quotes import get_quotes_for_book, get_random_quote, get_quote_stats


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
    raise Exception("No hay ningún libro marcado como Actual")


book_page = data["results"][0]

book_id = book_page["id"]

book = book_page["properties"]


print("\n========== PROPIEDADES ENCONTRADAS ==========")

for key, value in book.items():
    print(f"{key:<20} -> {value['type']}")

print("=============================================\n")


current_book = build_current_book(book)


quotes = get_quotes_for_book(book_id)


current_book["quote"] = get_random_quote(quotes)

current_book["quoteStats"] = get_quote_stats(quotes)


print("\n========== LIBRO ACTUAL ==========")

print(
    json.dumps(
        current_book,
        indent=4,
        ensure_ascii=False
    )
)

print("=================================\n")


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


print("✅ currentBook.json generado correctamente")