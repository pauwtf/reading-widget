from datetime import datetime, timezone

from display import (
    build_title_display,
    get_title_font_size,
    build_author_display,
    build_display_text,
)

def get_title(prop):

    if not prop["title"]:
        return ""

    return "".join(
        item["plain_text"]
        for item in prop["title"]
    )


def get_formula_text(prop):

    formula = prop["formula"]

    if formula["type"] == "string":

        return formula["string"] or ""

    return ""


def get_number(prop):

    return (
        prop["number"]
        if prop["number"] is not None
        else 0
    )


def get_progress(prop):

    formula = prop["formula"]

    if (
        formula["type"] == "number"
        and formula["number"] is not None
    ):

        return round(
            formula["number"] * 100
        )

    return 0


def get_cover(prop):

    files = prop["files"]

    if not files:
        return ""

    file = files[0]

    if file["type"] == "external":
        return file["external"]["url"]

    if file["type"] == "file":
        return file["file"]["url"]

    return ""


def create_progress_bar(progress, length=10):

    filled = round(progress / 100 * length)
    empty = length - filled

    return "█" * filled + "░" * empty


def get_status(progress):

    if progress >= 100:
        return "Terminado"

    return "Leyendo"


def build_current_book(book, book_id):

    title = get_title(
        book["Titulo"]
    )

    title_display = build_title_display(
        title
    )

    author = get_formula_text(
        book["Autor Nombre"]
    )

    current_page = get_number(
        book["Página Actual"]
    )

    total_pages = get_number(
        book["Total Páginas"]
    )

    progress = get_progress(
        book["Progreso"]
    )

    return {

        "bookId": book_id,

        "title": title,

        "titleDisplay": title_display,

        "author": author,

        "displayAuthor":
            build_author_display(author),

        "genre": get_formula_text(
            book["Genero Nombre"]
        ),

        "cover": get_cover(
            book["Portada"]
        ),

        "currentPage": current_page,

        "totalPages": total_pages,

        "progress": progress,

        "progressValue": round(progress / 100, 2),

        "display": {

            "titleFontSize":
                get_title_font_size(
                    title_display
                ),

            "pageText":
                f"Página {current_page} de {total_pages}",

            "progressText":
                f"{progress}%",

            "progressBar":
                create_progress_bar(progress),

            "status":
                get_status(progress)

        },

        "updatedAt":
            datetime.now(
                timezone.utc
            ).isoformat()

    }