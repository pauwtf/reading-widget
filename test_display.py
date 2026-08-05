from display import (
    build_title_display,
    get_title_font_size,
)

titles = [
    "Holly",
    "Nos Acompañan Los Muertos",
    "La Insoportable Levedad Del Ser",
    "Cien años de soledad",
    "Crónica de una muerte anunciada",
    "El problema de los tres cuerpos",
    "Los detectives salvajes",
    "El amor en los tiempos del cólera",
]

for title in titles:

    display = build_title_display(title)

    size = get_title_font_size(display)

    print("--------------------------------")

    print(title)

    print(display)

    print(size)