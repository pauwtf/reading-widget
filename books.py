from datetime import datetime, timezone


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

    filled = round(
        progress / 100 * length
    )

    empty = length - filled

    return (
        "█" * filled
        +
        "░" * empty
    )


def get_status(progress):

    if progress >= 100:

        return "Terminado"

    return "Leyendo"


def build_current_book(book):

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

        "title": get_title(
            book["Titulo"]
        ),

        "author": get_formula_text(
            book["Autor Nombre"]
        ),

        "genre": get_formula_text(
            book["Genero Nombre"]
        ),

        "cover": get_cover(
            book["Portada"]
        ),

        "currentPage": current_page,

        "totalPages": total_pages,

        "progress": progress,


        "display": {

            "pageText":
                f"Página {current_page} de {total_pages}",

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