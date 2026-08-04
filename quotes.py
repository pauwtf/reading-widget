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

    return prop["number"] or 0


def get_checkbox(prop):

    return prop["checkbox"]


def get_random_quote(quotes):

    if not quotes:
        return None

    quote = random.choice(quotes)

    properties = quote["properties"]

    return {
        "text": get_text(properties["Frase"]),
        "page": get_number(properties["Página"]),
        "favorite": get_checkbox(properties["<3"])
    }