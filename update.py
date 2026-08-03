import os
import json
import requests

NOTION_TOKEN = os.environ["NOTION_TOKEN"]
DATABASE_ID = os.environ["NOTION_DATABASE_ID"]

url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

payload = {
    "filter": {
        "property": "Estado",
        "status": {
            "equals": "Leyendo"
        }
    }
}

response = requests.post(url, headers=headers, json=payload)
response.raise_for_status()

results = response.json()["results"]

if len(results) == 0:
    raise Exception("No hay ningún libro con Estado = Leyendo")

book = results[0]["properties"]


def get_title(prop):
    if not prop["title"]:
        return ""
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
    "title": get_title(book["Título"]),
    "author": get_rich_text(book["Autor"]),
    "currentPage": get_number(book["Página Actual"]),
    "totalPages": get_number(book["Total páginas"]),
    "progress": get_formula_percent(book["Progreso"])
}

with open("currentBook.json", "w", encoding="utf8") as f:
    json.dump(current_book, f, ensure_ascii=False, indent=4)

print("currentBook.json generado correctamente")
