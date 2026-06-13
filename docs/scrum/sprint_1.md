# Sprint 1 — Persistencia de Contexto y API

## Información general

| Aspecto | Detalle |
|---------|---------|
| **Duración** | 1 semana |
| **Objetivo del Sprint** | Implementar el almacenamiento y recuperación de contexto de usuario a través de la API REST. |
| **Sprint Goal** | Habilitar los endpoints `POST /api/context` y `GET /api/context` para que usuarios puedan guardar y consultar sus preferencias. |

---

## Sprint Backlog

| Tarea | Descripción | HU asociada | SP | Estado |
|-------|-------------|-------------|----|--------|
| S1-T1 | Implementar `ContextStore.save(user_id, key, value)` en `backend/context_store.py` | HU-01 | 2 | Pendiente |
| S1-T2 | Implementar `ContextStore.list_for_user(user_id)` en `backend/context_store.py` | HU-02 | 1 | Pendiente |
| S1-T3 | Implementar handler `POST /api/context` en `backend/server.py` (crea contexto, responde 201) | HU-01 | 2 | Pendiente |
| S1-T4 | Implementar handler `GET /api/context` en `backend/server.py` (lista contexto por usuario) | HU-02 | 1 | Pendiente |
| S1-T5 | Ejecutar pruebas base y validación para verificar HU-01 y HU-02 | HU-01, HU-02 | 1 | Pendiente |

**Total SP comprometidos:** 7

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
| **Lecciones aprendidas** | (A completar) |

---

## Sprint Retrospective

| ¿Qué funcionó bien? | ¿Qué mejorar? | Acciones |
|---------------------|---------------|----------|
| (A completar) | (A completar) | (A completar) |
