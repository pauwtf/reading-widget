import random


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
        "text": get_text(properties["Frase"]),
        "page": get_number(properties["Página"]),
        "favorite": get_checkbox(properties["<3"])
    }