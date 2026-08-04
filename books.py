from datetime import datetime, timezone
from utils import get_title, get_formula_text, get_number, get_progress


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