# Sprint 2 — Aumento Contextual de Respuestas e Integración

## Información general

| Aspecto | Detalle |
|---------|---------|
| **Duración** | 1 semana |
| **Objetivo del Sprint** | Implementar la lógica CAG para que las respuestas se adapten al contexto del usuario, integrando frontend con backend. |
| **Sprint Goal** | El asistente responde considerando las preferencias del usuario, el frontend muestra el contexto activo, y todas las pruebas de validación pasan. |

---

## Sprint Backlog

| Tarea | Descripción | HU asociada | SP | Estado |
|-------|-------------|-------------|----|--------|
| S2-T1 | Implementar `apply_context()` en `backend/cag.py` para modificar respuesta según contexto del usuario | HU-03 | 3 | Pendiente |
| S2-T2 | Modificar `assistant.answer_question()` en `backend/assistant.py` para cargar contexto y aplicarlo; poblar `context_used` | HU-03 | 2 | Pendiente |
| S2-T3 | Asegurar que frontend (JS) consuma `GET /api/context` y actualice el panel lateral "CAG Panel" | HU-04 | 2 | Pendiente |
| S2-T4 | Ejecutar pruebas de validación completes (`./test.sh`) y corregir errores | HU-03, HU-04 | 1 | Pendiente |
| S2-T5 | Capturar evidencias (capturas de pantalla, ejecución de pruebas) en `docs/evidencias/` | HU-05 | 1 | Pendiente |

**Total SP comprometidos:** 9

---

## Daily Scrum

| Día | Avances | Bloqueos | Plan siguiente |
|-----|---------|----------|----------------|
| (A completar durante el sprint) | | | |

---

## Sprint Review

| Aspecto | Resultado |
|---------|-----------|
| **HU completadas** | (A completar al final del sprint) |
| **Pruebas pasan** | (A completar) |
| **Evidencias capturadas** | (A completar) |

---

## Sprint Retrospective

| ¿Qué funcionó bien? | ¿Qué mejorar? | Acciones |
|---------------------|---------------|----------|
| (A completar) | (A completar) | (A completar) |
