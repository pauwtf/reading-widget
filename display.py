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
    Divide un título en dos líneas utilizando reglas editoriales.

    Prioridades:
    1. Nunca dejar una sola palabra abajo.
    2. Aprovechar al máximo la primera línea.
    3. Mantener un buen equilibrio visual.
    """

    words = title.split()

    if len(words) <= 2:
        return title

    MAX_TITLE_WIDTH = 24

    best_index = 1
    best_width = -1
    best_balance = float("inf")

    for i in range(1, len(words)):

        left_words = words[:i]
        right_words = words[i:]

        # Nunca dejar una palabra sola abajo
        if len(right_words) < 2:
            continue

        left = " ".join(left_words)
        right = " ".join(right_words)

        left_width = visual_width(left)

        # Si no cabe, descartamos
        if left_width > MAX_TITLE_WIDTH:
            continue

        balance = abs(
            left_width -
            visual_width(right)
        )

        # Preferimos la primera línea más larga.
        # Si hay empate, la más equilibrada.
        if (
            left_width > best_width
            or (
                left_width == best_width
                and balance < best_balance
            )
        ):
            best_width = left_width
            best_balance = balance
            best_index = i

    return (
        " ".join(words[:best_index])
        + "\n"
        + " ".join(words[best_index:])
    )


def get_title_font_size(title_display):
    """
    Calcula el tamaño recomendado según la línea
    más larga del título ya dividido.
    """

    lines = title_display.split("\n")

    longest_line = max(
        visual_width(line)
        for line in lines
    )

    if longest_line <= 14:
        return 50

    if longest_line <= 20:
        return 47

    if longest_line <= 23:
        return 44

    if longest_line <= 26:
        return 42

    return 40