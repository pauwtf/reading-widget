import os
import json
import requests
from datetime import datetime, timezone

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

NOTION_VERSION = "2022-06-28"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": NOTION_VERSION
}

url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

payload = {
    "filter": {
        "property": "Estado",
        "select": {
            "equals": "Leyendo"
        }
    },
    "page_size": 1
}

response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()

data = response.json()

if not data["results"]:
    raise Exception("No hay ningún libro con Estado = Leyendo")

book = data["results"][0]["properties"]


def get_title(prop):
    if not prop["title"]:
        return ""
    return "".join(t["plain_text"] for t in prop["title"])


def get_formula_text(prop):
    value = prop["formula"]

    if value["type"] == "string":
        return value["string"] or ""

    return ""


def get_number(prop):
    return prop["number"] or 0


def get_progress(prop):
    value = prop["formula"]

    if value["type"] == "number" and value["number"] is not None:
        return round(value["number"] * 100)

    return 0


current_book = {
    "title": get_title(book["Titulo"]),
    "author": get_formula_text(book["Autor Nombre"]),
    "currentPage": get_number(book["Página Actual"]),
    "totalPages": get_number(book["Total Páginas"]),
    "progress": get_progress(book["Progreso"]),
    "updatedAt": datetime.now(timezone.utc).isoformat()
}

with open("currentBook.json", "w", encoding="utf-8") as f:
    json.dump(current_book, f, ensure_ascii=False, indent=4)

print("✅ currentBook.json generado correctamente")
    return "".join([t["plain_text"] for t in prop["title"]])


def get_rich_text(prop):
    if not prop["rich_text"]:
        return ""
    return "".join([t["plain_text"] for t in prop["rich_text"]])


def get_number(prop):
    return prop["number"]


def get_formula_percent(prop):
    value = prop["formula"]

    if value["type"] == "number":
        return round(value["number"] * 100)

    return 0


current_book = {
    "title": get_title(book["Titulo"]),
    "author": get_rich_text(book["Autor"]),
    "currentPage": get_number(book["Página Actual"]),
    "totalPages": get_number(book["Total páginas"]),
    "progress": get_formula_percent(book["Progreso"])
}

with open("currentBook.json", "w", encoding="utf8") as f:
    json.dump(current_book, f, ensure_ascii=False, indent=4)

print("currentBook.json generado correctamente")
