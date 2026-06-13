# Product Backlog — CAG Lab: Context-Augmented Generation

## Rol del equipo

| Rol | Responsable |
|-----|-------------|
| **Product Owner (PO)** | Instructor del curso |
| **Scrum Master** | Estudiante |
| **Development Team** | Estudiante (equipo de 1) |

---

## Épicas

1. **Persistencia de contexto** — Almacenar y recuperar preferencias de usuario.
2. **Aumento contextual de respuestas** — Modificar respuestas según el contexto almacenado.
3. **Integración frontend-backend** — Exponer contexto en API y mostrarlo en la UI.

---

## Historias de Usuario (HU)

### HU-01: Guardar contexto de usuario
**Como** usuario del sistema,  
**Quiero** enviar pares clave-valor con mis preferencias,  
**Para que** el asistente recuerde cómo quiero que me responda.

**Criterios de aceptación:**
- `POST /api/context` acepta `{user_id, key, value}` y responde `201 {"saved": true}`.
- El valor persiste al menos durante la sesión del servidor.

**Prioridad:** Alta | **Estimación:** 3 SP

---

### HU-02: Listar contexto de usuario
**Como** usuario del sistema,  
**Quiero** consultar las preferencias que tengo guardadas,  
**Para que** pueda verificar qué contexto tiene el asistente sobre mí.

**Criterios de aceptación:**
- `GET /api/context?user_id=X` devuelve `200 {"user_id": X, "context": [...]}`.
- Cada item de contexto tiene formato `{"key": ..., "value": ...}`.

**Prioridad:** Alta | **Estimación:** 2 SP

---

### HU-03: Adaptar respuestas según contexto
**Como** usuario del sistema,  
**Quiero** que el asistente ajuste sus respuestas según mis preferencias guardadas,  
**Para que** reciba información adaptada a mi nivel o estilo solicitado.

**Criterios de aceptación:**
- Si el usuario tiene contexto `audience: "explicar como principiante"`, la respuesta debe incluir la palabra "principiante".
- El campo `context_used` en la respuesta de `/api/ask` lista las claves de contexto aplicadas.

**Prioridad:** Alta | **Estimación:** 5 SP

---

### HU-04: Visualizar contexto en interfaz web
**Como** usuario del sistema,  
**Quiero** ver en la interfaz web el contexto activo que tengo almacenado,  
**Para que** pueda saber qué preferencias está usando el asistente.

**Criterios de aceptación:**
- El panel lateral "CAG Panel" se actualiza automáticamente tras cada pregunta.
- Muestra cada par clave-valor almacenado.

**Prioridad:** Media | **Estimación:** 2 SP

---

### HU-05: Documentar evidencias del proyecto
**Como** estudiante,  
**Quiero** capturar evidencias del funcionamiento del sistema,  
**Para que** el instructor pueda verificar la implementación.

**Criterios de aceptación:**
- Capturas de pantalla del servidor corriendo y pruebas pasando.
- Videos o reporte breve del comportamiento esperado.

**Prioridad:** Media | **Estimación:** 1 SP

---

## Resumen de estimaciones

| HU | Descripción | SP |
|----|-------------|----|
| HU-01 | Guardar contexto de usuario | 3 |
| HU-02 | Listar contexto de usuario | 2 |
| HU-03 | Adaptar respuestas según contexto | 5 |
| HU-04 | Visualizar contexto en interfaz web | 2 |
| HU-05 | Documentar evidencias del proyecto | 1 |
| **Total** | | **13 SP** |

> **SP = Story Points** (usando escala Fibonacci: 1, 2, 3, 5, 8, 13)
