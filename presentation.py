from display import (
    build_title_display,
    get_title_font_size,
    build_author_display,
    build_display_text,
)


def build_book_display(
    title,
    author,
    genre,
):

    title_display = build_title_display(
        title
    )

    return {

        "titleDisplay":
            title_display,

        "displayAuthor":
            build_author_display(author),

        "displayGenre":
            build_display_text(genre),

        "titleFontSize":
            get_title_font_size(
                title_display
            )

    }