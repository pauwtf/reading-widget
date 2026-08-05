from display import (
    build_title_display,
    get_title_font_size,
)

titles = [
    "Holly",
    "Dune",
    "It",
    "Carrie",
    "Misery",
    "La Insoportable Levedad Del Ser",
    "Nos Acompañan Los Muertos",
    "Cien años de soledad",
    "Crónica de una muerte anunciada",
    "El amor en los tiempos del cólera",
    "El problema de los tres cuerpos",
    "Los detectives salvajes",
    "La sombra del viento",
    "El nombre de la rosa",
    "El retrato de Dorian Gray",
]

print("\n========== SANDBOX ==========\n")

for title in titles:

    title_display = build_title_display(title)
    font_size = get_title_font_size(title_display)

    print(f"Título: {title}")
    print(f"Display:\n{title_display}")
    print(f"Font Size: {font_size}")
    print("-" * 40)

print("\n=============================\n")