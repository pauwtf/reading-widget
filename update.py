import json
import requests

from notion import HEADERS, DATABASE_URL
from books import build_current_book

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
    DATABASE_URL,
    headers=HEADERS,
    json=payload
)

response.raise_for_status()

data = response.json()

if not data["results"]:
    raise Exception("No hay ningún libro marcado como Actual")

book = data["results"][0]["properties"]

print("\n========== PROPIEDADES ENCONTRADAS ==========")
for key, value in book.items():
    print(f"{key:<20} -> {value['type']}")
print("=============================================\n")

current_book = build_current_book(book)

print("\n========== LIBRO ACTUAL ==========")
print(json.dumps(current_book, indent=4, ensure_ascii=False))
print("=================================\n")

with open("currentBook.json", "w", encoding="utf-8") as f:
    json.dump(current_book, f, ensure_ascii=False, indent=4)

print("✅ currentBook.json generado correctamente")