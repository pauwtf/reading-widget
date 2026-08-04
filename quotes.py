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


def get_checkbox(prop):

    return prop["checkbox"]


def get_quote_stats(quotes):

    total = len(quotes)

    favorites = 0

    for quote in quotes:

        properties = quote["properties"]

        if get_checkbox(properties["  "]):
            favorites += 1

    return {
        "total": total,
        "favorites": favorites
    }


def choose_quote(quotes):

    favorites = []

    for quote in quotes:

        properties = quote["properties"]

        if get_checkbox(properties["  "]):
            favorites.append(quote)


    # 70% favoritas ❤️ si existen
    if favorites and random.random() < 0.7:
        return random.choice(favorites)


    # 30% cualquier frase
    return random.choice(quotes)


def get_random_quote(quotes):

    if not quotes:
        return None


    quote = choose_quote(quotes)

    properties = quote["properties"]


    return {
        "id": quote["id"],
        "text": get_text(properties["Frase"]),
        "page": get_number(properties["Página"]),
        "favorite": get_checkbox(properties["  "])
    }