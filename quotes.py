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


# -------------------------
# MEMORIA POR LIBRO
# -------------------------

def load_history():

    if not os.path.exists(HISTORY_FILE):

        return {
            "books": {}
        }


    with open(
        HISTORY_FILE,
        "r",
        encoding="utf-8"
    ) as f:

        history = json.load(f)


    # Crear estructura nueva si no existe
    if "books" not in history:

        history["books"] = {}


    # Eliminar memoria antigua global
    if "shown" in history:

        del history["shown"]


    return history



def save_history(history):

    with open(
        HISTORY_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            history,
            f,
            ensure_ascii=False,
            indent=4
        )



def get_book_history(history, book_title):

    if book_title not in history["books"]:

        history["books"][book_title] = []


    return history["books"][book_title]



def choose_quote(quotes, book_title):

    history = load_history()


    shown = get_book_history(
        history,
        book_title
    )


    available_quotes = [
        q for q in quotes
        if q["id"] not in shown
    ]


    # Si ya mostramos todas las frases
    # de este libro, reiniciamos
    if not available_quotes:

        shown.clear()

        available_quotes = quotes



    favorites = [
        q for q in available_quotes
        if get_checkbox(q["properties"]["  "])
    ]


    # 70% favoritas ❤️
    if favorites and random.random() < 0.7:

        selected = random.choice(favorites)

    else:

        selected = random.choice(available_quotes)



    shown.append(selected["id"])


    save_history(history)


    return selected



def get_random_quote(quotes, book_title):

    if not quotes:

        return None


    quote = choose_quote(
        quotes,
        book_title
    )


    properties = quote["properties"]


    return {
        "id": quote["id"],
        "text": get_text(properties["Frase"]),
        "page": get_number(properties["Página"]),
        "favorite": get_checkbox(properties["  "])
    }