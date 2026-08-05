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

print("\n========== SANDBOX ==========\n")

for title in titles:

    title_display = build_title_display(title)
    font_size = get_title_font_size(title_display)

    print(f"Título: {title}")
    print(f"Display:\n{title_display}")
    print(f"Font Size: {font_size}")
    print("-" * 40)

print("\n=============================\n")