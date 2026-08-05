# ============================================================
# Library OS
# display.py
#
# Funciones encargadas de preparar la representación visual
# de los datos antes de enviarlos a KWGT.
# ============================================================

CHAR_WIDTHS = {

    # Muy estrechas
    "i": 0.5,
    "l": 0.5,
    "I": 0.6,
    "j": 0.6,

    # Estrechas
    "f": 0.8,
    "r": 0.8,
    "t": 0.8,

    # Muy anchas
    "m": 1.5,
    "w": 1.5,
    "M": 1.7,
    "W": 1.7,

    # Espacio
    " ": 0.6,
}


def visual_width(text):
    """
    Calcula un ancho visual aproximado de un texto.
    """

    return sum(
        CHAR_WIDTHS.get(char, 1)
        for char in text
    )


def build_title_display(title):
    """
    Divide un título utilizando un ancho máximo visual.

    Busca la primera línea más larga posible sin superar
    el ancho permitido.
    """

    words = title.split()

    if len(words) <= 2:
        return title

    MAX_TITLE_WIDTH = 24

    best_index = 1
    best_width = 0

    for i in range(1, len(words)):

        left = " ".join(words[:i])
        width = visual_width(left)

        if width <= MAX_TITLE_WIDTH and width > best_width:
            best_width = width
            best_index = i

    return (
        " ".join(words[:best_index])
        + "\n"
        + " ".join(words[best_index:])
    )


def get_title_font_size(title):

    width = visual_width(title)

    if width <= 14:
        return 50

    if width <= 22:
        return 47

    if width <= 30:
        return 44

    if width <= 38:
        return 42

    return 40