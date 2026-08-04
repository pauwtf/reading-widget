import random
import requests

from notion import HEADERS, QUOTES_DATABASE_URL


def get_quotes_for_book(book_id):

    payload = {
        "filter": {
            "property": "Libro",
            "relation": {
                "contains": book_id
            }
        }
    }

    response = requests.post(
        QUOTES_DATABASE_URL,
        headers=HEADERS,
        json=payload
    )

    response.raise_for_status()

    return response.json()["results"]


def get_text(prop):

    title = prop["title"]

    if not title:
        return ""

    return "".join(
        item["plain_text"]
        for item in title
    )


def get_number(prop):

    return prop["number"] if prop["number"] is not None else 0


def get_random_quote(quotes):

    if not quotes:
        return None

    quote = random.choice(quotes)

    properties = quote["properties"]

    print("\n========== PROPIEDADES FRASE ==========")

    for key, value in properties.items():
        print(f"{key:<20} -> {value['type']}")

    print("=======================================\n")


    return {
        "id": quote["id"],
        "text": get_text(properties["Frase"]),
        "page": get_number(properties["Página"]),
        "favorite": False
    }