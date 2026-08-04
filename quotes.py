
import random
import requests
import json
import os

from notion import HEADERS, QUOTES_DATABASE_URL


HISTORY_FILE = "quote_history.json"


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


def load_history():

    if not os.path.exists(HISTORY_FILE):
        return []

    with open(
        HISTORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        data = json.load(f)

    return data.get("shown", [])


def save_history(history):

    print("\n========== GUARDANDO HISTORIAL ==========")
    print(history)
    print("ARCHIVO:", HISTORY_FILE)
    print("=========================================\n")


    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            {
                "shown": history
            },
            f,
            ensure_ascii=False,
            indent=4
        )


def choose_quote(quotes):

    history = load_history()


    available_quotes = [
        q for q in quotes
        if q["id"] not in history
    ]


    if not available_quotes:

        history = []

        available_quotes = quotes


    favorites = [
        q for q in available_quotes
        if get_checkbox(q["properties"]["  "])
    ]


    if favorites and random.random() < 0.7:

        selected = random.choice(favorites)

    else:

        selected = random.choice(available_quotes)


    history.append(selected["id"])

    save_history(history)


    return selected


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