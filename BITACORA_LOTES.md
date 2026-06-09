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

**Regla de perdidas re-obtenidas (Boris 2026-06-09):** si un código que está en `perdida` aparece
en un dictado, es porque **salió en un sobre nuevo** → se trata como **nueva** (`perdida→pegada`,
perdidas −1). NO es la copia extraviada que reaparece. Esta es la política por defecto **hasta que
Boris diga lo contrario** (ej. "encontré la que se me había perdido" → ahí sí es recuperación física).

---

## 🗓️ Log de lotes

| Fecha | Día | Lote | Inicio | Cierre | Estado lote | Δ neto | Pegado conf. | Notas |
|-------|-----|------|--------|--------|-------------|-------:|--------------|-------|
| 2026-06-05 o antes | — | inicial | — | — | cerrado | 126 | n/d | Inventario base 126/980 (commit `a9ee82c`) |
| 2026-06-06 | sáb | AM | n/d | n/d | cerrado | +55 | n/d | 126→181 (commit `2aebc85`) + fix imprimibles |
| 2026-06-06 | sáb | PM | n/d | n/d | cerrado | +44 | parcial | 181→225 (commit `31df639`). Verificación cruzada mazo-físico (rescató 6) |
| 2026-06-07 | **dom** | corrección | n/d | n/d | cerrado | **−39** | — | **39 sueltas del lote 06-06 PM marcadas `perdida`** (extraviadas en depto). HAVE 225→186 |
| 2026-06-07 | dom | **A (canje #1)** | 11:30 | 13:21 | ✅ cerrado | **+18** | sí (18 pegadas) | **Primer intercambio, 1:1 perfecto** (18×18, eficiencia 1,0). HAVE 186→204. Pool repetidas 27→9. FWC páginas mapeadas. Ahorro ~$2.830 |
| 2026-06-09 | **mar** | A (sobres) | 16:25 | 16:40 | ✅ cerrado | **+21** | sí (21 pegadas) | Dictado 28 códigos → 21 nuevas pegadas + 7 repetidas al pool. HAVE 204→225 (23,0%). Pool repetidas 9→16/15. 🇵🇹 Portugal estrena (POR12 Vitinha). Brillantes 12→13/68 (TUR1). Estrella ENG11 Bellingham |
| 2026-06-09 | mar | B (sobres) | 18:30 | 18:45 | ✅ cerrado | **+23** | sí (23 pegadas) | Dictado 28 → 22 nuevas + TUN10 re-obtenida en sobre (perdida→pegada, perdidas 39→38) + 5 repetidas. HAVE 225→248 (25,3%). Pool 16→21/20. Marruecos estrena (MAR1 escudo foil, brillantes 13→14). 🇵🇹 POR17 João Félix (Portugal 2/20). Estrellas FRA15 Dembélé, ENG10 Rice |
| 2026-06-09 | mar | C (sobres) | 19:20 | 19:35 | ✅ cerrado | **+22** | sí (22 pegadas) | Dictado 28 → 21 nuevas + BEL2 re-obtenida en sobre (perdida→pegada, perdidas 38→37) + 6 repetidas. HAVE 248→270 (27,6%). Pool 21→27/25. ARG1 escudo Argentina foil (brillantes 14→15). Estrellas BEL2 Courtois, CRO10 Kovačić, ENG15 Gordon |

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

## 🔄 Lote A — 2026-06-07 (dom) · Canje #1 (primer intercambio) · inicio 11:30

Marcadas `pegada` con `fecha_estado=2026-06-07`. Todas eran `falta` → avance directo (18 casillas
nuevas, ninguna repetida). **HAVE 186→204 (19,0%→20,8%)**.

**Recibidas (18, todas pegadas):**
UZB19 (Igor Sergeev) · AUS1 (Escudo Australia ⭐T2) · USA17 (Brenden Aaronson) · IRQ4 (Hussein Ali) ·
AUT15 (Nicolas Seiwald) · KSA13 (Foto equipo Arabia Saudita) · RSA3 (Sipho Chaine) · GER2 (ter Stegen) ·
CRO12 (Lovro Majer) · IRN6 (Khalilzadeh) · NZL7 (Tyler Bindon) · NZL8 (Francis de Vries) ·
NZL10 (Joe Bell) · QAT13 (Foto equipo Catar) · BEL16 (Doku) · BEL13 (Foto equipo Bélgica) ·
SWE2 (Victor Johansson) · SWE6 (Nilsson Lindelöf).

**Match pendiente — número de aporte del canje** (calcular al cierre):
- **X** = repetidas en el pool ANTES del canje (registradas: 20 — confirmar si era el pool real).
- **Y** = repetidas que QUEDAN tras el canje (Boris dicta).
- Repetidas entregadas = **X − Y**. Eficiencia = 18 ÷ (X−Y) nuevas/repetida (ideal 1:1).
- Ahorro ≈ 18 × ~$157/lámina (no compradas en sobre) → pesos que el canje evitó.

**Match cerrado (2026-06-07 13:21):** se reconcilió el registro de repetidas a la **pila física real
de Boris = 9 cartas / 8 códigos** (`AUS10, AUS20, BIH9, BIH14×2, EGY5, FWC10, NED9, RSA11`). El
registro estaba inflado/incompleto (listaba 25 tras añadir 4 no registradas): se pusieron a 0 las 13
que ya no tiene y se revirtieron 5 de `estado=repetida`→`tengo` (BEL6, BEL7, JOR14, JOR18, RSA7).
Hallazgo: tenía duplicados sin registrar (NED9, FWC10, BIH9, BIH14) — 2 fueron **regalados**. HAVE sin
cambio (204).

**🎯 Número del canje (cerrado):** entregadas = **18** → **canje 1:1 perfecto, eficiencia 1,0**
(18 recibidas ÷ 18 entregadas). Pool de repetidas **27 → 9** (27 = 18 entregadas + 9 restantes;
confirma que el registro de 25 estaba corto por los duplicados sin anotar). Costo $0; ahorro estimado
~18 × $157 ≈ **$2.830** en sobres no comprados. Aporte = 18 casillas reales gratis sin perder ninguna.

**FWC páginas mapeadas** (dato físico Boris, ver `ALBUM_ORDEN.md`): 1→FWC1-4, 2→FWC5-6, 3→FWC7-8,
106→FWC9-10, 107→FWC11-13, 108→FWC14-15, 109→FWC16-18. Pendiente: `00`, FWC19, inserto 56-57.

**Tarjeta para compartir** (`dashboard_share.png` + `gen_dashboard.py`): réplica de la tarjeta azul
de la app Figuritas con data real — Completado 21% · Total 980 · Me faltan 776 · Tengo 204 ·
Repetidas 9 · Brillantes 12/68. Regenerable con `py gen_dashboard.py`.

---

## 📦 Lote A — 2026-06-09 (mar) · Sobres · inicio 16:25 · cierre 16:40

Dictado de **28 códigos** → resueltos contra registro ANTES de pegar. **21 nuevas pegadas**
(`falta→pegada`, `fecha_estado=2026-06-09`) + **7 repetidas** al pool de canje (`repetidas +1`,
estado sin cambio). **HAVE 204→225 (20,8%→23,0%)**.

**Nuevas pegadas (21):** MEX17 (Raúl Jiménez) · CPV7 (Wagner Pina) · CZE15 (Matej Vydra) ·
KSA17 (Abdulrahman Al-Aboud) · CPV6 (Steven Moreira) · SEN8 (Kalidou Koulibaly) · PAR10 (Diego Gómez) ·
ARG2 (Emiliano Martínez) · HAI2 (Johny Placide) · RSA20 (Oswin Appollis) · NED15 (Xavi Simons) ·
COL12 (Richard Ríos) · EGY11 (Zizo) · **ENG11 (Jude Bellingham ⭐T3)** · BEL11 (Nicolas Raskin) ·
🇵🇹 **POR12 (Vitinha — primera de Portugal, 0→1/20)** · AUT16 (Romano Schmid) ·
**TUR1 (Escudo Turquía ⭐ foil)** · AUS4 (Harry Souttar) · PAN12 (Adalberto Carrasquilla) · KOR5 (Cho Yu-min).

**Repetidas al pool (7):** FWC18 (Alemania 2014 FIFA Museum, foil) · RSA19 (Mohau Nkota) ·
BIH10 (Armin Gigović) · RSA16 (Sipho Mbule) · EGY9 (Ahmed Fatouh) · CUW6 (Joshua Brenet) ·
**AUT15 (Nicolas Seiwald — recibida en el canje #1 de antier)**. Pool repetidas **9→16 cartas / 15 códigos**.

**Hitos:** Portugal estrena casillero (POR12) — Cristiano POR15 sigue pendiente. Brillantes **12→13/68**
(TUR1 escudo foil). Primera estrella T3 del lote: Bellingham (ENG11).

---

## 📦 Lote B — 2026-06-09 (mar) · Sobres · inicio 18:30 · cierre 18:45

Dictado de **28 códigos** → **22 nuevas pegadas** + **TUN10 re-obtenida en sobre** + **5 repetidas**.
**HAVE 225→248 (23,0%→25,3%)** — cruza el 25%.

**Nuevas pegadas (22):** CIV2 (Yahia Fofana) · COD6 (Chancel Mbemba) · **MAR1 (Escudo Marruecos ✨ foil — Marruecos estrena)** ·
**FRA15 (Ousmane Dembélé ⭐)** · EGY12 (Hamdy Fathy) · ESP8 (Marc Cucurella) · CRO2 (Dominik Livaković) ·
UZB6 (Husniddin Aliqulov) · CPV16 (Jovane Cabral) · CIV6 (Evan Ndicka) · QAT2 (Meshaal Barsham) ·
UZB15 (Khojimat Erkinov) · CPV20 (Bebé) · PAN17 (José Fajardo) · CPV19 (Willy Semedo) ·
🇵🇹 **POR17 (João Félix — Portugal 2/20)** · CZE12 (Tomas Soucek) · ARG11 (Exequiel Palacios) ·
FRA19 (Hugo Ekitike) · NOR19 (Antonio Nusa) · **ENG10 (Declan Rice)** · BRA8 (Wesley).

**Re-obtenida en sobre (1):** **TUN10 (Aïssa Laïdouni)** — estaba `perdida` (lote 06-06). NO es la copia
extraviada que reaparece: es una **copia nueva salida de un sobre**. `perdida→pegada`, perdidas **39→38**.
La copia perdida sigue extraviada pero ya es irrelevante (el casillero queda cubierto).

**Repetidas al pool (5):** CRO1 (Escudo Croacia foil) · CPV15 (Garry Rodrigues) · CUW10 (Godfried Roemeratoe) ·
CUW19 (Gervane Kastaneer) · ENG2 (Jordan Pickford). Pool repetidas **16→21 cartas / 20 códigos**.

**Hitos:** 🇲🇦 Marruecos estrena con su escudo foil (brillantes 12→**14/68** sumando MAR1 + el TUR1 del Lote A) ·
🇵🇹 Portugal sube a 2/20 (POR12 Vitinha + POR17 João Félix; Cristiano POR15 sigue pendiente) ·
estrellas FRA15 Dembélé + ENG10 Rice.

---

## 📦 Lote C — 2026-06-09 (mar) · Sobres · inicio 19:20 · cierre 19:35

Dictado de **28 códigos** → **21 nuevas pegadas** + **BEL2 re-obtenida en sobre** + **6 repetidas**.
**HAVE 248→270 (25,3%→27,6%)**.

**Nuevas pegadas (21):** **ARG1 (Escudo Argentina ✨ foil)** · ESP4 (Aymeric Laporte) · ESP13 (foto equipo) ·
CRO10 (Mateo Kovačić) · CRO6 (Luka Vušković) · GER8 (Ridle Baku) · GER4 (David Raum) · CIV11 (Seko Fofana) ·
CIV16 (Sébastien Haller) · NZL12 (Ryan Thomas) · NZL4 (Michael Boxall) · CUW12 (Leandro Bacuna) ·
CAN18 (Liam Millar) · BIH3 (Amer Dedić) · CPV2 (Vozinha) · CPV3 (Logan Costa) · PAR2 (Roberto Fernández) ·
ARG6 (Nicolás Tagliafico) · ALG17 (Anis Hadj Moussa) · UZB10 (Odiljon Hamrobekov) · ENG15 (Anthony Gordon).

**Re-obtenida en sobre (1):** **BEL2 (Thibaut Courtois ⭐)** — estaba `perdida` (lote 06-06). Salió en
sobre nuevo → `perdida→pegada`, perdidas **38→37**. (Regla de perdidas re-obtenidas, ver protocolo arriba.)

**Repetidas al pool (6):** FWC12 (Brasil 1962 FIFA Museum foil) · AUS15 (Connor Metcalfe) · AUS19 (Nestory Irankunda) ·
BEL10 (Amadou Onana) · NZL8 (Francis de Vries) · **RSA19 (Mohau Nkota — 2ª repetida)**. Pool **21→27 cartas / 25 códigos**.

**Hitos:** 🇦🇷 escudo Argentina foil (ARG1, brillantes 14→**15/68**) · re-obtenido el arquero estrella Courtois (BEL2) ·
estrellas Kovačić (CRO10) + Gordon (ENG15).

---

*Cross-ref: `registro_maestro.csv` (estado autoritativo) · `DASHBOARD.md` (KPIs) ·
`INVESTIGACION_Y_SISTEMA.md` (arquitectura).*
