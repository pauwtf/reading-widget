from display import (
    build_title_display,
    get_title_font_size,
    build_author_display,
    build_display_text,
    build_quote_display,
    get_quote_font_size,
    build_page_display,
)


def build_book_display(
    title,
    author,
    genre,
):
    """
    Construye todos los campos de presentación
    relacionados con un libro.
    """

    title_display = build_title_display(
        title
    )

    return {

        "titleDisplay":
            title_display,

        "displayAuthor":
            build_author_display(
                author
            ),

        "displayGenre":
            build_display_text(
                genre
            ),

        "titleFontSize":
            get_title_font_size(
                title_display
            )

    }


def build_quote_presentation(
    quote,
):
    """
    Construye toda la representación visual
    de una cita.
    """

    quote_display = build_quote_display(
        quote["text"]
    )

    return {

        "id":
            quote["id"],

        "text":
            quote["text"],

        "display":
            quote_display,

        "fontSize":
            get_quote_font_size(
                quote_display
            ),

        "page":
            quote["page"],

        "pageDisplay":
            build_page_display(
                quote["page"]
            ),

        "favorite":
            quote["favorite"],

        "favoriteIcon":
            "♥"
            if quote["favorite"]
            else ""

    }