# Bitácora de lotes — Álbum Mundial 2026

Registro temporal exacto de cada ingreso de láminas. El **registro maestro** (estado por
lámina) vive en `registro_maestro.csv`; esta bitácora mapea **cuándo** y **cómo** entró cada lote.

---

## 📋 Protocolo de ingreso (obligatorio, de ahora en adelante)

Cada vez que Boris ingresa un lote, Claude debe:

1. **Confirmar la fecha exacta y el día de la semana** que tiene, y pedir validación.
   > NO asumir días ("mañana lunes" en sábado). Decir p. ej. *"Tengo domingo 2026-06-07,
   > ¿correcto?"* y esperar que Boris confirme o corrija.
2. **Pedir la hora de inicio** del lote (Boris la confirma).
3. Por cada código dictado, **resolver equipo + nombre ANTES de que Boris pegue**
   (caza códigos ambiguos tipo "scomar"). Devolver: `CÓDIGO = Nombre, Equipo`.
4. **Preguntar si las láminas del lote están pegadas o sueltas.**
   - Si Boris **no lo confirma**, las láminas quedan como `tengo` (suelta) con flag
     **⏳ pegado sin confirmar**, y Claude **insiste/pregunta hasta obtener la confirmación**.
     No asumir `pegada` jamás.
   - `pegada` = en la página (segura). `tengo` = suelta (riesgo de extravío → lección 2026-06-06).
5. Al cerrar, registrar **hora de cierre**, si el lote quedó **TERMINADO o EN PROGRESO**,
   y numerar si hubo **más de un ingreso en el día** (Lote A, Lote B…).
6. Escribir la fila en esta bitácora + setear `fecha_estado` en el registro maestro.

**Estados del registro:** `falta` · `tengo` (suelta) · `pegada` (en álbum) · `repetida` (moneda
de canje) · `perdida` (adquirida pero extraviada — NO cuenta como tener, sí aparece en faltantes).

---

## 🗓️ Log de lotes

| Fecha | Día | Lote | Inicio | Cierre | Estado lote | Δ neto | Pegado conf. | Notas |
|-------|-----|------|--------|--------|-------------|-------:|--------------|-------|
| 2026-06-05 o antes | — | inicial | — | — | cerrado | 126 | n/d | Inventario base 126/980 (commit `a9ee82c`) |
| 2026-06-06 | sáb | AM | n/d | n/d | cerrado | +55 | n/d | 126→181 (commit `2aebc85`) + fix imprimibles |
| 2026-06-06 | sáb | PM | n/d | n/d | cerrado | +44 | parcial | 181→225 (commit `31df639`). Verificación cruzada mazo-físico (rescató 6) |
| 2026-06-07 | **dom** | corrección | n/d | n/d | cerrado | **−39** | — | **39 sueltas del lote 06-06 PM marcadas `perdida`** (extraviadas en depto). HAVE 225→186 |

---

## 🔴 Lote perdido — 2026-06-06 (39 láminas sueltas extraviadas)

Marcadas `perdida` con `fecha_estado=2026-06-06` el 2026-06-07. Eran `falta→tengo` (sueltas,
nunca pegadas) de la sesión PM; físicamente extraviadas en el depto, baja probabilidad de
recuperación. Las 5 que en esa sesión se **pegaron** al álbum (AUS20, IRQ19, PAN2, SEN2, RSA2)
**NO** se pierden — están en la página.

**Códigos (39):**
ALG2, ALG16, ALG19, ARG8, ARG13, **ARG17 (Messi ⭐)**, AUT4, AUT5, AUT12, AUT17, BEL2, BRA12,
BRA17, COL2, COL10, COD10, COD11, COD12, COD15, CUW4, **FRA20 (Mbappé ⭐)**, GHA10, CIV4, JPN13,
PAN6, PAN10, PAR13, POR13, POR19 (Pedro Neto), QAT14, KSA6, KSA10, TUN4, TUN10, TUN20, TUR14,
USA2, UZB17, UZB18.

> Si alguna reaparece físicamente: cambiar `perdida → tengo` (o `pegada` si se pega) y anotar
> la fecha de recuperación. Cuentan como costo hundido hasta entonces.

---

*Cross-ref: `registro_maestro.csv` (estado autoritativo) · `DASHBOARD.md` (KPIs) ·
`INVESTIGACION_Y_SISTEMA.md` (arquitectura).*
