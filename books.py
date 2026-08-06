from datetime import datetime, timezone

from presentation import build_book_display


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


def get_formula_boolean(prop):

    formula = prop["formula"]

    if formula["type"] == "boolean":

        return formula["boolean"]

    return False


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


def get_status(is_finished):

    if is_finished:
        return "Terminado"

    return "Leyendo"


def build_current_book(book, book_id):

    title = get_title(
        book["Titulo"]
    )

    author = get_formula_text(
        book["Autor Nombre"]
    )

    genre = get_formula_text(
        book["Genero Nombre"]
    )

    presentation = build_book_display(
        title,
        author,
        genre,
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

    pages_read = current_page

    pages_remaining = max(
        total_pages - current_page,
        0
    )

    is_finished = get_formula_boolean(
        book["Finalizado Check"]
    )

    return {

        "bookId": book_id,

        "title": title,

        "titleDisplay":
            presentation["titleDisplay"],

        "author": author,

        "displayAuthor":
            presentation["displayAuthor"],

        "genre": genre,

        "displayGenre":
            presentation["displayGenre"],

        "cover": get_cover(
            book["Portada"]
        ),

        "currentPage": current_page,

        "totalPages": total_pages,

        "pagesRead": pages_read,

        "pagesRemaining": pages_remaining,

        "progress": progress,

        "progressValue": round(
            progress / 100,
            2
        ),

        "isFinished": is_finished,

        "display": {

            "titleFontSize":
                presentation["titleFontSize"],

            "pageText":
                f"Página {current_page} de {total_pages}",

            "progressText":
                f"{progress}%",

            "progressBar":
                create_progress_bar(
                    progress
                ),

            "status":
                get_status(
                    is_finished
                )

        },

        "updatedAt":
            datetime.now(
                timezone.utc
            ).isoformat()

    }