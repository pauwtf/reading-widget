# ============================================================
# COUNTDOWN OS — KWGT COORDINATE ADAPTER
# Version: 1.2 Elegance
# ============================================================


# ============================================================
# ZERO NORMALIZATION
# ============================================================

def clean_zero(value):
    """
    Normaliza cualquier representación de cero.

    Evita que el JSON produzca -0.0.
    """

    value = float(value)

    if value == 0:
        return 0.0

    return value


# ============================================================
# DIRECTIONAL POSITION
# ============================================================

def adapt_directional_position(x, y):
    """
    Convierte coordenadas firmadas de Countdown OS
    en los cuatro campos direccionales de KWGT.

    Countdown OS:
        +X = derecha
        -X = izquierda
        +Y = abajo
        -Y = arriba

    KWGT:
        x_right
        x_left
        y_down
        y_up
    """

    x = clean_zero(x or 0)
    y = clean_zero(y or 0)

    return {
        "x_right": clean_zero(max(x, 0)),
        "x_left": clean_zero(max(-x, 0)),
        "y_down": clean_zero(max(y, 0)),
        "y_up": clean_zero(max(-y, 0)),
    }


# ============================================================
# DUAL-X POSITION
# ============================================================

def adapt_dual_x_position(x_left, x_right, y):
    """
    Convierte una posición KWGT que utiliza
    simultáneamente X izquierda y X derecha.

    Usado por componentes como Plane.
    """

    x_left = clean_zero(x_left or 0)
    x_right = clean_zero(x_right or 0)
    y = clean_zero(y or 0)

    if x_left < 0:
        raise ValueError(
            f"x_left cannot be negative: {x_left}"
        )

    if x_right < 0:
        raise ValueError(
            f"x_right cannot be negative: {x_right}"
        )

    return {
        "x_left": x_left,
        "x_right": x_right,
        "y": y,
    }