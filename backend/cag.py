"""Base placeholder for student implementation."""


def apply_context(user_id, question, base_answer, context_items):
    if not context_items:
        return base_answer

    for item in context_items:
        key = item.get("key", "")
        value = item.get("value", "")

        if key == "audience" and "principiante" in value.lower():
            base_answer = base_answer.replace(
                "Segun la base de conocimiento del curso:",
                "Segun la base de conocimiento del curso (explicado para principiantes):",
            )
            base_answer += (
                " Ademas, recuerda que estamos explicando estos conceptos como si fuera"
                " la primera vez que los escuchas, pensando en un principiante."
            )

    return base_answer
