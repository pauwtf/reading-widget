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
    Divide un título en dos líneas buscando el punto
    más equilibrado visualmente.
    """

    words = title.split()

    if len(words) <= 2:
        return title

    best_index = 1
    best_difference = float("inf")

    for i in range(1, len(words)):

        left = " ".join(words[:i])
        right = " ".join(words[i:])

        difference = abs(
            visual_width(left)
            - visual_width(right)
        )

        if difference < best_difference:
            best_difference = difference
            best_index = i

    return (
        " ".join(words[:best_index])
        + "\n"
        + " ".join(words[best_index:])
    )


def get_title_font_size(title):
    """
    Recomienda un tamaño de fuente según
    la longitud visual del título.
    """

    width = visual_width(title)

    if width <= 15:
        return 50

    if width <= 24:
        return 47

    if width <= 34:
        return 44

    if width <= 42:
        return 42

    return 40