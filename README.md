# Proyecto Examen Final - Módulo 3: CAG Lab

Context-Augmented Generation (CAG): integración de memoria contextual persistente en un asistente que recupera conocimiento del curso.

## Estructura del proyecto

| Ruta | Contenido |
|------|-----------|
| `backend/` | Servidor HTTP (API REST) + lógica del asistente |
| `frontend/` | Interfaz web estática (HTML + CSS + JS) |
| `data/` | Base de conocimiento en JSON |
| `tests/base/` | Pruebas base (3) — verifican funcionamiento inicial |
| `tests/validation/` | Pruebas de validación (3) — definen el contrato CAG |
| `tests/custom/` | **Pruebas propias (25)** — unitarias y de integración |
| `docs/scrum/` | Planificación Scrum (2 sprints) |
| `docs/evidencias/` | Capturas y resultados de pruebas |

## Implementación CAG

### Backend

- **`backend/context_store.py`** — `ContextStore` con almacenamiento en memoria. Métodos: `save(user_id, key, value)` y `list_for_user(user_id)`. Singleton compartido entre server y assistant.
- **`backend/cag.py`** — `apply_context()` modifica respuestas según claves de contexto:
  - `audience`: principiante / avanzado — ajusta el nivel de la explicación
  - `tone`: formal / casual — agrega recomendaciones o mensajes amigables
  - `format`: breve / detallado — acorta o extiende la respuesta
- **`backend/assistant.py`** — Orquestador: recupera snippets, aplica contexto, retorna `context_used` con las claves aplicadas.
- **`backend/server.py`** — Endpoints REST:
  - `GET /health` — estado del servidor
  - `POST /api/ask` — pregunta al asistente (soporta CAG)
  - `POST /api/context` — guarda contexto de usuario
  - `GET /api/context?user_id=X` — lista contexto de usuario

### Frontend

Panel CAG con formulario para guardar contexto (clave/valor) y visualización del contexto activo. La respuesta del asistente se actualiza automáticamente reflejando las preferencias.

## Ejecutar pruebas

### Pruebas base (3)
```bash
python -m unittest discover -s tests/base -p "test_*.py" -v
```

### Pruebas de validación (3)
```bash
python -m unittest discover -s tests/validation -p "test_*.py" -v
```

### Pruebas propias (25)
```bash
python -m unittest discover -s tests/custom -p "test_*.py" -v
```

### Todas las pruebas (31)
```bash
python -m unittest discover -s tests/base -p "test_*.py" -v && ^
python -m unittest discover -s tests/validation -p "test_*.py" -v && ^
python -m unittest discover -s tests/custom -p "test_*.py" -v
```

## Ejecutar backend

```bash
python -m backend.server
```

El backend queda disponible en `http://127.0.0.1:8000`.

## Abrir frontend

Abra `frontend/index.html` en un navegador.

## Planificación Scrum

Ver `docs/scrum/`:
- `product_backlog.md` — 5 historias de usuario priorizadas (13 SP)
- `sprint_1.md` — Sprint 1: persistencia de contexto y API (7 SP)
- `sprint_2.md` — Sprint 2: aumento contextual e integración (9 SP)
- `artefactos_scrum.md` — DoD, burndown charts, ceremonias, calendario
