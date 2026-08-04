from datetime import datetime, timezone


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


def build_current_book(book):

    return {
        "title": get_title(book["Titulo"]),
        "author": get_formula_text(book["Autor Nombre"]),
        "genre": get_formula_text(book["Genero Nombre"]),
        "currentPage": get_number(book["Página Actual"]),
        "totalPages": get_number(book["Total Páginas"]),
        "progress": get_progress(book["Progreso"]),
        "updatedAt": datetime.now(timezone.utc).isoformat()
    }