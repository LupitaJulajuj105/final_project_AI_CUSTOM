# Artefactos Complementarios Scrum

## 1. Definition of Done (DoD)

Una historia de usuario se considera **completada** cuando cumple **todos** los siguientes criterios:

- [ ] **Código implementado** — La funcionalidad está codificada según los criterios de aceptación.
- [ ] **Pruebas unitarias pasan** — Todas las pruebas existentes (base y validación) relacionadas con la HU se ejecutan sin error.
- [ ] **Sin errores de sintaxis** — El servidor se inicia sin errores de importación o ejecución.
- [ ] **Integración API verificada** — Los endpoints responden con los códigos HTTP y cuerpos JSON esperados.
- [ ] **Frontend funcional** — Si aplica, la UI refleja correctamente los cambios.
- [ ] **Evidencia capturada** — Se guarda captura de pantalla o registro de prueba en `docs/evidencias/`.

---

## 2. Plantilla de Burndown Chart (Sprint 1)

| Día | SP pendientes inicio | SP completados | SP pendientes fin |
|-----|---------------------|----------------|-------------------|
| 1   | 7                   | 0              | 7                 |
| 2   | 7                   |                |                   |
| 3   |                     |                |                   |
| 4   |                     |                |                   |
| 5   |                     | 0              |                   |
| **Total** | 7               |                | 0                 |

*Nota: Actualizar diariamente con los SP realmente completados.*

### Curva ideal (referencia)

```
SP
7 | ●
6 |  \
5 |   \
4 |    \
3 |     \
2 |      \
1 |       \
0 |________●
   1 2 3 4 5  Día
```

---

## 3. Plantilla de Burndown Chart (Sprint 2)

| Día | SP pendientes inicio | SP completados | SP pendientes fin |
|-----|---------------------|----------------|-------------------|
| 1   | 9                   | 0              | 9                 |
| 2   | 9                   |                |                   |
| 3   |                     |                |                   |
| 4   |                     |                |                   |
| 5   |                     | 0              |                   |
| **Total** | 9               |                | 0                 |

---

## 4. Ceremonias Scrum

| Ceremonia | Frecuencia | Duración | Participantes |
|-----------|-----------|----------|---------------|
| **Sprint Planning** | Al inicio de cada sprint | 1 hora | Scrum Master, Dev Team |
| **Daily Scrum** | Diaria | 15 min | Scrum Master, Dev Team |
| **Sprint Review** | Fin de cada sprint | 30 min | Todos los roles |
| **Sprint Retrospective** | Fin de cada sprint | 30 min | Scrum Master, Dev Team |

---

## 5. Calendario general

```
Sprint 1 (Semana 1)
├── Día 1: Sprint Planning → Implementar ContextStore
├── Día 2: Implementar POST /api/context
├── Día 3: Implementar GET /api/context
├── Día 4: Pruebas y correcciones
└── Día 5: Sprint Review + Retrospective

Sprint 2 (Semana 2)
├── Día 1: Sprint Planning → Implementar apply_context()
├── Día 2: Integrar contexto en assistant.py (context_used)
├── Día 3: Frontend — actualizar CAG Panel
├── Día 4: Pruebas de validación completas + evidencias
└── Día 5: Sprint Review + Retrospective + Entrega final
```
