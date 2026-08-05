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

    En lugar de buscar el centro matemático, evalúa todos los
    los posibles saltos y elige el que mejor se vea.
    """

    words = title.split()

    if len(words) <= 2:
        return title

    weak_words = {
        "de", "del", "la", "las",
        "el", "los",
        "y", "e", "o", "u",
        "a", "en", "con", "por"
    }

    best_score = float("-inf")
    best_index = 1

    for i in range(1, len(words)):

        left_words = words[:i]
        right_words = words[i:]

        left = " ".join(left_words)
        right = " ".join(right_words)

        left_width = visual_width(left)
        right_width = visual_width(right)

        score = 0

        # ----------------------------------
        # 1. Queremos líneas equilibradas
        # ----------------------------------
        score -= abs(left_width - right_width) * 3

        # ----------------------------------
        # 2. Preferimos que la primera línea
        # sea ligeramente más larga.
        # ----------------------------------
        if left_width >= right_width:
            score += 12

        # ----------------------------------
        # 3. Evitar una palabra sola arriba.
        # ----------------------------------
        if len(left_words) == 1:
            score -= 100

        # ----------------------------------
        # 4. Evitar una palabra sola abajo.
        # ----------------------------------
        if len(right_words) == 1:
            score -= 100

        # ----------------------------------
        # 5. Evitar dejar artículos solos
        # al final de la primera línea.
        # ----------------------------------
        if left_words[-1].lower() in weak_words:
            score -= 60

        # ----------------------------------
        # 6. Evitar empezar la segunda línea
        # con artículos.
        # ----------------------------------
        if right_words[0].lower() in weak_words:
            score -= 20

        # ----------------------------------
        # 7. Bonus si ambas líneas tienen
        # al menos dos palabras.
        # ----------------------------------
        if len(left_words) >= 2:
            score += 10

        if len(right_words) >= 2:
            score += 10

        if score > best_score:
            best_score = score
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