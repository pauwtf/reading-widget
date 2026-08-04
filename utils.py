def get_title(prop):
    if not prop["title"]:
        return ""

    return "".join(
        item["plain_text"]
        for item in prop["title"]
    )


def get_formula_text(prop):
    formula = prop["formula"]

    if formula["type"] == "string":
        return formula["string"] or ""

    return ""


def get_number(prop):
    return prop["number"] if prop["number"] is not None else 0


def get_progress(prop):
    formula = prop["formula"]

    if formula["type"] == "number" and formula["number"] is not None:
        return round(formula["number"] * 100)

    return 0