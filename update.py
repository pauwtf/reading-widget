import os
import json
import requests
from datetime import datetime, timezone

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

all_books = []
has_more = True
next_cursor = None

while has_more:

    payload = {}

    if next_cursor:
        payload["start_cursor"] = next_cursor

    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()

    data = response.json()

    for page in data["results"]:

        p = page["properties"]

        def title(name):
            return "".join(x["plain_text"] for x in p[name]["title"])

        def formula_text(name):
            f = p[name]["formula"]
            return f["string"] if f["type"] == "string" else ""

        def number(name):
            return p[name]["number"] or 0

        def formula_number(name):
            f = p[name]["formula"]
            return f["number"] if f["type"] == "number" else 0

        estado = p["Estado"]["select"]["name"] if p["Estado"]["select"] else ""

        book = {
            "title": title("Titulo"),
            "author": formula_text("Autor Nombre"),
            "genre": formula_text("Genero Nombre"),
            "month": formula_text("Mes Nombre"),
            "year": formula_text("Año Nombre"),
            "status": estado,
            "currentPage": number("Página Actual"),
            "totalPages": number("Total Páginas"),
            "progress": round(formula_number("Progreso") * 100),
            "updatedAt": datetime.now(timezone.utc).isoformat()
        }

        all_books.append(book)

    has_more = data["has_more"]
    next_cursor = data["next_cursor"]

print(f"{len(all_books)} libros encontrados.")

with open("library.json", "w", encoding="utf-8") as f:
    json.dump(all_books, f, ensure_ascii=False, indent=4)

current = next((b for b in all_books if b["status"] == "Leyendo"), None)

with open("currentBook.json", "w", encoding="utf-8") as f:
    json.dump(current, f, ensure_ascii=False, indent=4)

finished = [b for b in all_books if b["status"] == "Leído"]

stats = {
    "booksRead": len(finished),
    "pagesRead": sum(b["totalPages"] for b in finished),
    "currentlyReading": len([b for b in all_books if b["status"] == "Leyendo"]),
    "updatedAt": datetime.now(timezone.utc).isoformat()
}

with open("readingStats.json", "w", encoding="utf-8") as f:
    json.dump(stats, f, ensure_ascii=False, indent=4)

streak = {
    "currentStreak": 0,
    "longestStreak": 0,
    "updatedAt": datetime.now(timezone.utc).isoformat()
}

with open("streak.json", "w", encoding="utf-8") as f:
    json.dump(streak, f, ensure_ascii=False, indent=4)

print("✅ library.json generado")
print("✅ currentBook.json generado")
print("✅ readingStats.json generado")
print("✅ streak.json generado")