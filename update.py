import json
import requests
from datetime import datetime, timezone

from notion import HEADERS, DATABASE_URL

payload = {
    "filter": {
        "property": "Actual",
        "checkbox": {
            "equals": True
        }
    },
    "page_size": 1
}

response = requests.post(DATABASE_URL, headers=HEADERS, json=payload)
response.raise_for_status()

data = response.json()

if not data["results"]:
    raise Exception("No hay ningún libro marcado como Actual")

book = data["results"][0]["properties"]

print("\n========== PROPIEDADES ENCONTRADAS ==========")
for key, value in book.items():
    print(f"{key:<20} -> {value['type']}")
print("=============================================\n")


def get_title(prop):
    if not prop["title"]:
        return ""
    return "".join(item["plain_text"] for item in prop["title"])


def get_formula_text(prop):
    formula = prop["formula"]

    if formula["type"] == "string":
        return formula["string"] or ""

    return ""


def get_number(prop):
    return prop["number"] if prop["number"] is not None else 0


def get_progress(prop):
    formula = prop["formula"]

    if formula["type"] == "number" and formula["number"] is not None:
        return round(formula["number"] * 100)

    return 0


current_book = {
    "title": get_title(book["Titulo"]),
    "author": get_formula_text(book["Autor Nombre"]),
    "genre": get_formula_text(book["Genero Nombre"]),
    "currentPage": get_number(book["Página Actual"]),
    "totalPages": get_number(book["Total Páginas"]),
    "progress": get_progress(book["Progreso"]),
    "updatedAt": datetime.now(timezone.utc).isoformat()
}

print("\n========== LIBRO ACTUAL ==========")
print(json.dumps(current_book, indent=4, ensure_ascii=False))
print("=================================\n")

with open("currentBook.json", "w", encoding="utf-8") as f:
    json.dump(current_book, f, ensure_ascii=False, indent=4)

print("✅ currentBook.json generado correctamente")