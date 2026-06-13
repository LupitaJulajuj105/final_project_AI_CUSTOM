"""Context-Augmented Generation logic.

Applies user context preferences to modify the assistant's answer.
Supported context keys:
  - audience: adjusts explanation level (principiante, avanzado, etc.)
  - tone: adjusts response tone (formal, casual, etc.)
  - language: adjusts response language (es, en, etc.)
  - format: adjusts response format (breve, detallado, etc.)
"""


def _apply_audience(answer, value):
    value_lower = value.lower()
    if "principiante" in value_lower:
        answer = answer.replace(
            "Segun la base de conocimiento del curso:",
            "Segun la base de conocimiento del curso (explicado para principiantes):",
        )
        answer += (
            " Ademas, recuerda que estamos explicando estos conceptos como si fuera"
            " la primera vez que los escuchas, pensando en un principiante."
        )
    elif "avanzado" in value_lower or "experto" in value_lower:
        answer = answer.replace(
            "Segun la base de conocimiento del curso:",
            "Segun la base de conocimiento del curso (nivel avanzado):",
        )
    return answer


def _apply_tone(answer, value):
    value_lower = value.lower()
    if "formal" in value_lower:
        answer += (
            " Se recomienda consultar fuentes adicionales para una comprension"
            " mas profunda de los temas tratados."
        )
    elif "casual" in value_lower or "relajado" in value_lower:
        answer += " Espero que te haya quedado claro. Si tienes dudas, aqui estoy."
    return answer


def _apply_format(answer, value):
    value_lower = value.lower()
    if "breve" in value_lower or "corto" in value_lower:
        sentences = answer.split(". ")
        if len(sentences) > 2:
            answer = ". ".join(sentences[:2]) + "."
    elif "detallado" in value_lower or "extenso" in value_lower:
        answer += " Este tema puede explorarse con mayor profundidad en el curso."
    return answer


_CONTEXT_HANDLERS = {
    "audience": _apply_audience,
    "tone": _apply_tone,
    "format": _apply_format,
}


def apply_context(user_id, question, base_answer, context_items, language="es"):
    if not context_items:
        return base_answer

    for item in context_items:
        key = item.get("key", "")
        value = item.get("value", "")
        handler = _CONTEXT_HANDLERS.get(key)
        if handler:
            base_answer = handler(base_answer, value)

    return base_answer
