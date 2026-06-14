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
| 2026-06-09 | mar | D (sobres) | 20:05 | 20:20 | ✅ cerrado | **+20** | sí (20 pegadas) | Dictado 28 → 17 nuevas + 3 re-obtenidas de sobre (AUT12/AUT17/COL10, perdidas 37→34) + 8 repetidas. HAVE 270→290 (29,6%). Pool 27→35/32. GER1 + FWC16 foil (brillantes 15→17). Estrellas SWE17 Kulusevski, KOR12 Lee Kang-in, COL15 Quintero |
| 2026-06-09 | mar | E (sobres) | 21:10 | 21:25 | ✅ cerrado | **+30** | sí (30 pegadas) | Dictado 35 → 28 nuevas + 2 re-obtenidas de sobre (AUT4/PAR13, perdidas 34→32) + 5 repetidas. HAVE 290→320 (32,7%, cruza 30%). Pool 35→40/37. GHA1 escudo foil (brillantes 17→18). 🇵🇹 Portugal 3/20 (POR9 Bernardo Silva). Estrellas BRA19 Raphinha, NED3 van Dijk, AUT4 Alaba |
| 2026-06-09 | mar | F (sobres) | 22:55 | 23:10 | ✅ cerrado | **+12** | sí (11 pegadas) | Dictado 14 → 10 nuevas + TUR14 re-obtenida de sobre (perdidas 32→31) + GHA20 (ya pegada en álbum, registro lo tenía `falta` → corregido a pegada + 1 repetida) + IRN3/CZE14 repetidas. HAVE 320→332 (33,9%). Pool 40→43/40. SWE1 escudo foil (brillantes 18→19). Estrellas BRA14 Vinicius Jr, TUR14 Arda Güler |
| 2026-06-10 | mié | A (sobres) | 12:30 | — | ✅ cerrado | **+25** | sí (pegadas) | +25 nuevas (3 escudos COD1/IRN1/URU1 + Marmoush EGY20, Kim Min-jae KOR4, Trent ENG6, Kramarić CRO19, Nico González ARG16) + 12 repetidas. HAVE 332→357 (36,4%). Brillantes 19→22/68 |
| 2026-06-10 | mié | B (sobres) | 17:00 | — | ✅ cerrado | **+12** | sí (pegadas) | +12 nuevas (PAR1 escudo; TUN13+UZB13 = primeras 2 fotos de equipo; Dumfries/Reijnders/Sabitzer) + 1 repetida (USA17). HAVE 357→369 (37,7%). Brillantes 22→23/68 (PAR1) |
| 2026-06-10 | mié | C (sobres) | 20:24 | 20:45 | ✅ cerrado | **+23** | ⚠️ no (sueltas en caja) | +22 nuevas sueltas (JOR1 escudo, Rodrygo BRA15 ⭐, Bardghji SWE16 ⭐) + TUN20 re-obtenida (perdida→tengo, perdidas 31→30) + 11 repetidas. HAVE 369→392 (40,0%, cruza 40%). Pool 56→67. Brillantes 23→24/68 (JOR1). ⚠️ pendiente pegar |
| 2026-06-12 | vie | A (sobres) | n/d | — | ✅ cerrado | **+25** | sí (pegadas) | 25 nuevas. HAVE 392→417 (42,6%). +10 repetidas al pool |
| 2026-06-12 | vie | B (sobres) | 18:50 | — | ✅ cerrado | **+27** | sí (pegadas) | 26 nuevas + **ALG16 recuperada** (perdida→pegada, perdidas 30→29) + 7 repetidas. HAVE 417→444 (45,3%) |
| 2026-06-12 | vie | C (sobres) | 20:05 | — | ✅ cerrado | **+24** | sí (pegadas) | 24 nuevas incl. **`00` logo Panini + KSA1 escudo + foils FWC11 (Alemania Occ. 1954) y FWC19 (Argentina 2022)** + 11 repetidas. HAVE 444→468 (47,8%) |
| 2026-06-12 | vie | D (sobres) | 22:30 | — | ✅ cerrado | **+6** | sí (pegadas) | 5 nuevas + ⭐ **Mbappé (FRA20) recuperado** (perdida→pegada, perdidas 29→28) + 8 repetidas; corrección `00`→repetida (ya estaba pegado). HAVE 468→474 (48,4%) |
| 2026-06-13 | sáb | A (sobres) | 10:59 | — | ✅ cerrado | **+7** | sí (pegadas) | 7 nuevas (⭐ URU4 Araújo, ⭐ NED17 Depay, MAR8, TUN19, TUR15, GHA19, URU12) + 21 repetidas (incl. 2ª TUR15). HAVE 474→481 (49,1%). Pool 110→131 |
| 2026-06-13 | sáb | B (sobres) | 16:02 | — | ✅ cerrado | **+11** | sí (pegadas) | 🎉 **cruza 50%**. 11 nuevas (⭐ MAR4 Hakimi, ⭐ JPN2, ✨ FWC9/CIV1/IRQ1 foils, RSA15, AUS3, KSA15/19, SWE8/12) + 17 repetidas (incl. IRN19→2). IRN19 era repetida, no nueva. HAVE 481→492 (50,2%). Pool 131→148 |
| 2026-06-13 | sáb | C (sobres) | 17:25 | — | ✅ cerrado | **+11** | sí (pegadas) | 10 nuevas (🇵🇹 POR7 Nuno Mendes, ✨ USA1 escudo, GER13, UZB16, AUS14, ALG14, TUR6, ECU11, CZE19, MAR18) + **ARG13 recuperada** (perdida→pegada) + 17 repetidas (incl. SEN11→1). HAVE 492→504 (51,4%). Perdidas 28→27. Pool 148→165 |
| 2026-06-13 | sáb | D (sobres) | 18:22 | — | ✅ cerrado | **+16** | sí (pegadas) | 16 nuevas (✨ AUT1/ECU1/BEL1 escudos, BRA16, COL5, SEN5, CIV20, ALG5/9, CPV13, ECU13, UZB7/11, AUS9, TUR2, JPN3) + 12 repetidas (incl. SEN18→1). HAVE 504→521 (53,2%). Pool 165→177 |
| 2026-06-13 | sáb | E (sobres) | 20:10 | — | ✅ cerrado | **+12** | sí (pegadas) | 11 nuevas (⭐ COL14 James, BRA20 Estêvão, BRA4 Marquinhos, CAN5/9/14, COL9/18, SEN9/14, TUN14) + **UZB18 recuperada** + 16 repetidas (incl. ARG13). HAVE 521→533 (54,4%). Perdidas 27→26. Pool 177→193 |
| 2026-06-13 | sáb | F (sobres) | — | — | ⚠️ SOLO IDENTIF. | **+11** | 🔴 **SUELTAS** | 11 nuevas SIN PEGAR (estado `tengo`: ⭐ SWE20 Gyökeres, GER19, ENG5, MEX20, CUW11, IRQ14/18, TUR9, EGY16, CZE2, SCO9) + 16 repetidas. HAVE 533→544 (55,5%). Pool 193→209. **Pendiente: pegarlas.** |

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

## 📦 Lote D — 2026-06-09 (mar) · Sobres · inicio 20:05 · cierre 20:20

Dictado de **28 códigos** → **17 nuevas pegadas** + **3 re-obtenidas de sobre** + **8 repetidas**.
**HAVE 270→290 (27,6%→29,6%)**.

**Nuevas pegadas (17):** **GER1 (Escudo Alemania ✨ foil)** · **FWC16 (Brasil 2002 FIFA Museum ✨ foil)** ·
SWE17 (Dejan Kulusevski ⭐) · KOR12 (Lee Kang-in ⭐) · COL15 (Juan Fernando Quintero) · NZL17 (Chris Wood) ·
SUI8 (Silvan Widmer) · AUS5 (Alessandro Circati) · CIV3 (Ghislain Konan) · CIV7 (Willy Boly) ·
CIV17 (Simon Adingra) · COD13 (foto equipo) · TUR19 (Kerem Aktürkoğlu) · KOR8 (Lee Tae-seok) ·
PAN13 (foto equipo) · CPV17 (Ryan Mendes) · ARG7 (Leonardo Balerdi).

**Re-obtenidas de sobre (3):** AUT12 (Konrad Laimer) · AUT17 (Patrick Wimmer) · COL10 (Jefferson Lerma).
`perdida→pegada`. Perdidas **37→34**.

**Repetidas al pool (8):** UZB1 (escudo foil) · BIH8 (Hadžiahmetović) · BIH12 (Bašić) · SUI12 (Rieder) ·
RSA5 (Kabini) · IRQ15 (Aymar Sher) · KSA13 (foto equipo, canje #1) · **AUS10 (Degenek — 2ª repetida)**.
Pool **27→35 cartas / 32 códigos**.

**Hitos:** 🇩🇪 escudo Alemania foil + FWC Brasil 2002 (brillantes 15→**17/68**) · estrellas Kulusevski (SWE17) +
Lee Kang-in (KOR12) + Quintero (COL15). Perdidas ya en 34 (de 39 originales).

---

## 📦 Lote E — 2026-06-09 (mar) · Sobres · inicio 21:10 · cierre 21:25

Dictado de **35 códigos** (2 venían pegados en el dictado: "par 15mex 18"→PAR15+MEX18,
"kor 20ger 3"→KOR20+GER3) → **28 nuevas pegadas** + **2 re-obtenidas de sobre** + **5 repetidas**.
**HAVE 290→320 (29,6%→32,7%)** — cruza el 30%.

**Nuevas pegadas (28):** 🇵🇹 **POR9 (Bernardo Silva)** · BRA19 (Raphinha ⭐) · NED3 (van Dijk ⭐) ·
NED11 (Gravenberch) · **GHA1 (Escudo Ghana ✨ foil)** · GER3 (Tah) · GER7 (Anton) · GER12 (Nmecha) ·
BIH15 (Bajraktarević) · IRQ9 (Iqbal) · IRQ8 (Younis) · PAR15 (Enciso) · MEX18 (Vega) ·
KSA14 (Abu Alshamat) · KSA18 (Akbrikan) · KSA5 (Bouwashl) · KOR20 (Oh Hyeon-gyu) · KOR17 (Cho Gue-sung) ·
NOR13 (foto equipo) · USA18 (Pepi) · URU20 (Pellistri) · URU8 (Varela) · RSA14 (Aubaas) ·
ESP3 (Le Normand) · TUR5 (Bardakcı) · CPV12 (Monteiro) · HAI6 (Adé) · JOR6 (Nasib).

**Re-obtenidas de sobre (2):** **AUT4 (David Alaba ⭐)** · PAR13 (foto equipo). `perdida→pegada`. Perdidas **34→32**.

**Repetidas al pool (5):** IRN18 (Taremi) · **NED15 (Xavi Simons — pegada en Lote A de hoy)** ·
PAN13 (foto equipo, Lote D) · SCO13 (foto equipo) · COD7 (Joris Kayembe). Pool **35→40 cartas / 37 códigos**.

**Hitos:** 🇵🇹 Portugal sube a **3/20** (POR9 Bernardo Silva + POR12 Vitinha + POR17 João Félix; Cristiano POR15
sigue pendiente) · 🇬🇭 escudo Ghana foil (brillantes 17→**18/68**) · estrellas Raphinha (BRA19), van Dijk (NED3),
Alaba re-obtenido (AUT4).

---

## 📦 Lote F — 2026-06-09 (mar) · Sobres · inicio 22:55 · cierre 23:10 · **último del día**

Dictado de **14 códigos** → **10 nuevas pegadas** + **TUR14 re-obtenida de sobre** +
**GHA20 (corrección de registro)** + **2 repetidas**. **HAVE 320→332 (32,7%→33,9%)**.

**Nuevas pegadas (10):** **BRA14 (Vinicius Júnior ⭐)** · **SWE1 (Escudo Suecia ✨ foil)** · FRA7 (Dayot Upamecano) ·
NED18 (Donyell Malen) · GHA18 (Joseph Paintsil) · ALG18 (Amine Gouiri) · NOR2 (Ørjan Nyland) ·
CZE7 (Tomas Holes) · CZE10 (Lukas Provod) · HAI3 (Carlens Arcus).

**Re-obtenida de sobre (1):** **TUR14 (Arda Güler ⭐)** — `perdida→pegada`. Perdidas **32→31**.

**Corrección de registro (1):** **GHA20 (Antoine Semenyo)** — Boris confirmó que ya estaba **pegada en el álbum**
pero el registro la tenía `falta` (caso verificación cruzada). Corregido a `pegada` + la copia dictada va al pool
(`repetidas=1`). Suma 1 a HAVE (estaba subcontada) y 1 al pool.

**Repetidas al pool (2):** IRN3 (Pouraliganji) · CZE14 (Pavel Sulc). Pool total con GHA20 **40→43 cartas / 40 códigos**.

**Hitos:** ⭐⭐ Vinicius Júnior (BRA14) · 🇸🇪 escudo Suecia foil (brillantes 18→**19/68**) · Arda Güler re-obtenido.

---

## 🏁 Resumen del día 2026-06-09 (martes) — 6 lotes

| Lote | Hora | Δ HAVE | Cierre % |
|------|------|-------:|---------:|
| A | 16:25 | +21 | 23,0% |
| B | 18:30 | +23 | 25,3% |
| C | 19:20 | +22 | 27,6% |
| D | 20:05 | +20 | 29,6% |
| E | 21:10 | +30 | 32,7% |
| F | 22:55 | +12 | **33,9%** |
| **Total** | | **+128** | **204→332** |

**Movimientos del día:** HAVE 204→**332** (+128, todo sobres). Perdidas 39→**31** (8 re-obtenidas en sobres
nuevos: TUN10, BEL2, AUT12, AUT17, COL10, AUT4, PAR13, TUR14). Pool repetidas 9→**43 cartas / 40 códigos**.
Brillantes 12→**19/68** (TUR1, MAR1, ARG1, GER1, FWC16, GHA1, SWE1). 🇵🇹 Portugal **3/20** (Vitinha, João Félix,
Bernardo Silva) — Cristiano POR15 sigue pendiente. 1 rotura (BIH10 repetida).

---

## 📦 Lote A — 2026-06-10 (mié) · Sobres · inicio 12:30 · **PEGADAS**

Dictado de **35 códigos** (+2 consultas posteriores) → **25 nuevas pegadas** + **12 repetidas**.
**HAVE 332→357 (33,9%→36,4%)**.

**Nuevas pegadas (25):** **COD1, IRN1, URU1 (3 escudos ✨ foil)** · **EGY20 (Omar Marmoush ⭐)** ·
**KOR4 (Kim Min-jae ⭐)** · **ENG6 (Trent Alexander-Arnold ⭐)** · **CRO19 (Kramarić ⭐)** ·
**ARG16 (Nico González ⭐)** · HAI16 · BIH2 · BIH6 · NOR11 · EGY10 · EGY15 · EGY8 · QAT6 ·
KSA12 · COD8 · ALG12 · SEN12 · CRO15 · TUN15 · SWE4 · RSA6 · ARG20.

**Repetidas al pool (12):** HAI14 · BEL16 · ENG20 · EGY10 (2ª copia) · BEL8 · BEL9 · IRN19 · ARG6 ·
CIV6 · IRN16 · EGY18 · IRN6. Pool **43→55 cartas**.

**Hitos:** brillantes 19→**22/68** (3 escudos) · Egipto avanza fuerte (EGY8/10/15/20).

---

## 📦 Lote B — 2026-06-10 (mié) · Sobres · inicio 17:00 · **PEGADAS**

Dictado de **13 códigos** (+consultas) → **12 nuevas pegadas** + **1 repetida**.
**HAVE 357→369 (36,4%→37,7%)**.

**Nuevas pegadas (12):** **PAR1 (Escudo Paraguay ✨ foil)** · **TUN13 + UZB13 (📷 primeras 2 fotos de equipo)** ·
NED6 (Dumfries) · NED10 (Reijnders) · AUT10 (X. Schlager) · AUT11 (Sabitzer) · CAN8 (Bombito) ·
CAN12 (Osorio) · UZB2 (Yusupov) · SWE10 (Karlström) · SWE11 (Ayari).

**Repetidas al pool (1):** USA17 (Aaronson). Pool **55→56 cartas**.

**Hitos:** brillantes 22→**23/68** (PAR1) · primeras fotos de equipo del proyecto (TUN13, UZB13).

---

## 📦 Lote C — 2026-06-10 (mié) · Sobres · inicio 20:24 · cierre 20:45 · **último del día** · ⚠️ **SUELTAS (en caja)**

Dictado de **34 códigos** → **22 nuevas sueltas** + **TUN20 re-obtenida** + **11 repetidas**.
**HAVE 369→392 (37,7%→40,0%)**. 🎉 cruza el 40%.

> ⚠️ **Las 22 nuevas + TUN20 quedaron SUELTAS en una caja** (estado `tengo`, no `pegada`) — riesgo de
> extravío (lección 2026-06-06: 39 sueltas perdidas). Pendiente pegarlas. Entre ellas: BRA15 (Rodrygo ⭐),
> SWE16 (Bardghji ⭐), JOR1 (escudo ✨).

**Nuevas sueltas (22):** **JOR1 (Escudo Jordania ✨ foil)** · **BRA15 (Rodrygo ⭐)** · **SWE16 (Bardghji ⭐)** ·
BRA9 (Paquetá) · SWE5 · SWE15 · URU9 (Nández) · JPN16 (Minamino) · JPN11 (Kamada) · JPN20 (Ueda) ·
CZE11 · CRO3 · CRO7 · HAI20 (Pierrot) · MAR10 (Amrabat) · MAR2 (Bounou) · BIH5 · PAR6 · NED2 (Verbruggen) ·
ALG8 (Bennacer) · CPV11 · SEN4 (Niakhaté).

**Re-obtenida de sobre (1):** **TUN20 (Naïm Sliti)** — `perdida→tengo`. Perdidas **31→30**.

**Repetidas al pool (11):** PAR1 (¡pegada en Lote B de hoy!) · IRQ20 · CZE5 · FWC15 (foil Brasil 94) · CZE7 ·
IRN20 · HAI18 · AUS12 · SCO2 · CPV10 · USA17 (2ª copia → rep=2). Pool **56→67 cartas**.

**Hitos:** brillantes 23→**24/68** (JOR1) · 40% alcanzado · Naím Sliti recuperado.

---

## 🏁 Resumen del día 2026-06-10 (miércoles) — 3 lotes

| Lote | Inicio | Cierre | Pegado | Δ HAVE | Cierre % |
|------|--------|--------|--------|-------:|---------:|
| A | 12:30 | — | pegadas | +25 | 36,4% |
| B | 17:00 | — | pegadas | +12 | 37,7% |
| C | 20:24 | 20:45 | ⚠️ sueltas (caja) | +23 | **40,0%** |
| **Total** | | | | **+60** | **332→392** |

**Movimientos del día:** HAVE 332→**392** (+60, todo sobres). Perdidas 31→**30** (TUN20 re-obtenida).
Pool repetidas 43→**67 cartas** (+24). Brillantes 19→**24/68** (COD1, IRN1, URU1, PAR1, JOR1 — 5 escudos).
Primeras **2 fotos de equipo** (TUN13, UZB13). 🇵🇹 Portugal sigue **3/20**, Cristiano POR15 pendiente.
⚠️ **Lote C (23 láminas) quedó suelto en caja** — pendiente pegar (riesgo extravío).

---

## 📦 Día 2026-06-12 (vie) — 4 lotes de sobres (A–D) · **PEGADAS**

> ⚠️ **Reconstruido el 2026-06-13** a partir del `registro_maestro.csv` (estado autoritativo) +
> resumen por lote que quedó en el `DASHBOARD.md`. El registro timestampa el **día**
> (`fecha_estado=2026-06-12`), no el lote individual → el detalle **código-por-código de abajo es el
> agregado del día**; los conteos y destacados **por lote** (L1–L4) vienen del DASHBOARD.

**HAVE 392→474 (40,0%→48,4%)** = **+82** (80 nuevas + 2 recuperadas). Cruza el **48%**.
Perdidas **30→28** · Pool repetidas **67→110 cartas / 98 códigos** (+43) · Brillantes **24→32/68**.
**Además: 173 láminas que estaban sueltas se pegaron al álbum** (`tengo→pegada`) — cierra el riesgo
de extravío del Lote C del 10-jun y el backlog suelto acumulado. 🇵🇹 Portugal sigue **3/20**,
**Cristiano POR15 pendiente**.

**Resumen por lote (del DASHBOARD):**

| Lote | Inicio | Nuevas | Recuperada | Rep. | Δ HAVE | Cierre % | Destacados |
|------|--------|-------:|------------|-----:|-------:|---------:|------------|
| A | n/d | 25 | — | +10 | +25 | 42,6% | — |
| B | 18:50 | 26 | ALG16 (perdida→pegada) | +7 | +27 | 45,3% | ALG16 recuperada |
| C | 20:05 | 24 | — | +11 | +24 | 47,8% | `00` logo Panini · KSA1 escudo · foils FWC11 (Alemania Occ. 1954) + FWC19 (Argentina 2022) |
| D | 22:30 | 5 | FRA20 (perdida→pegada) | +8 | +6 | **48,4%** | ⭐ **Mbappé (FRA20) recuperado** · corrección `00`→repetida (ya estaba pegado) |
| **Total** | | **80** | **2** | **+43** | **+82** | **392→474** | brillantes 24→32 |

**Recuperadas de sobre (2):** ALG16 (Argelia) · **FRA20 (Mbappé ⭐, Francia)** — ambas `perdida→pegada`.
Perdidas 30→28.

**Nuevas del día (80, agregado por equipo):**
Alemania GER11/16/20 · Arabia Saudita KSA1(escudo)/9 · Argelia ALG11 · Austria AUT2/18 ·
Bélgica BEL3/20 · Brasil BRA5 · Catar QAT7/8/12/17 · Colombia COL17 · Corea del Sur KOR1(escudo)/7/11/16 ·
Croacia CRO11/16/20 · Curazao CUW16 · Ecuador ECU5/18 · España ESP9/11 · Estados Unidos USA20 ·
**FWC FWC11(foil)/FWC19(foil)** · Francia FRA18 · Ghana GHA5/9/14 · Haití HAI7/11/19 ·
Inglaterra ENG4/7/8/9/14/18 · Irán IRN9 · Japón JPN1(escudo)/7 · Jordania JOR3/7/11/16/20 ·
Marruecos MAR3/7/11 · México MEX13 · Noruega NOR3/7/16 · Países Bajos NED7/16 · Panamá PAN1(escudo) ·
**Panini `00`(logo foil)** · Paraguay PAR3 · Senegal SEN20 · Sudáfrica RSA13 · Suecia SWE3/7 ·
Suiza SUI9/11/13/14/17 · Túnez TUN1(escudo)/2/6/18 · Uruguay URU6/18 · Uzbekistán UZB3.

**Brillantes nuevos (8 → 24→32/68):** `00` · FWC11 · FWC19 · KSA1 · KOR1 · PAN1 · TUN1 · JPN1.

**Repetidas al pool (41 códigos, pool 67→110 cartas):**
00 · ALG1 · BIH9 (rep=3) · BIH14 · COD3 · COL1 · CUW5 · CUW9 · CUW18 · CZE9 · ECU3 · EGY5 · FRA19 ·
GER5 · GER14 · GHA13 · HAI3 · HAI5 · HAI7 · HAI9 · HAI11 · HAI16 · HAI18 · IRN7 (rep=2) · IRN11 ·
IRN14 · IRN20 · JOR11 · KSA13 · NED11 · QAT13 · RSA20 · SUI5 · SUI8 · SUI16 · URU5 · URU14 · URU16 ·
URU20 · USA16 · USA18.

**Housekeeping del día:** 173 láminas `tengo→pegada` (sueltas acumuladas finalmente pegadas, incl. el
Lote C del 10-jun) + RSA11 `repetida→pegada` (reconciliación). Tras esto, **0 láminas en estado
`tengo`** — todo lo adquirido está `pegada` o en el pool de `repetida`.

---

## 📦 Lote — 2026-06-13 (sáb) · Sobres · 10:59 · **PEGADAS**

Dictado de **28 láminas** (sobres frescos; TUR15 dictado 2 veces = **1 pegada + 1 repetida**) →
**7 nuevas pegadas** + **21 repetidas**. **HAVE 474→481 (48,4%→49,1%)**. Perdidas 28 (sin cambios).

**Nuevas pegadas (7):** ⭐ **URU4 (Ronald Araújo)** · ⭐ **NED17 (Memphis Depay)** · MAR8 (Jawad El Yamiq) ·
TUN19 (Sayfallah Ltaief) · TUR15 (İrfan Can Kahveci) · GHA19 (Osman Bukari) · URU12 (Rodrigo Bentancur).

**Repetidas al pool (21):** COD13 · SWE4 · NZL4 · TUN6 · BIH5 · ESP8 · URU17 · NZL12 · SUI12 (→2) ·
URU8 · BIH14 (→4) · TUR19 · IRQ19 · NZL8 (→2) · SUI8 (→2) · BIH9 (→4) · ESP4 · NZL17 · TUN10 ·
RSA16 (→2) · **TUR15 (2ª copia)**. Pool **110→131 cartas / 98→113 códigos**.

**Hitos:** brillantes 32/68 (ninguna foil nueva) · Uruguay suma 2 estrellas (Araújo + Bentancur) ·
🇵🇹 Portugal sigue 3/20 (Cristiano POR15 aún falta) · **a 9 láminas del 50%**.

**Nota de calendario:** se corrigió el error de día arrastrado del DASHBOARD — el **12-jun fue viernes**, no jueves
(el 9-jun fue martes). Filas del log y encabezados del 12-jun ya corregidos.

---

## 📦 Lote — 2026-06-13 (sáb) · Sobres · 16:02 · **PEGADAS** · 🎉 CRUZA EL 50%

Dictado de **28 láminas (4 sobres)** → **11 nuevas pegadas** + **17 repetidas**.
**HAVE 481→492 (49,1%→50,2%)** — **cruza el 50%**. Perdidas 28 (sin cambios).

**Nuevas pegadas (11):** ⭐ **MAR4 (Achraf Hakimi)** · ⭐ **JPN2 (Zion Suzuki)** ·
✨ **FWC9 (Italia 1934 — FIFA Museum, foil)** · ✨ **CIV1 (Costa de Marfil, escudo)** · ✨ **IRQ1 (Irak, escudo)** ·
RSA15 (Yaya Sithole) · AUS3 (Joe Gauci) · KSA15 (Marwan Alsahafi) ·
KSA19 (Saleh Alshehri) · SWE12 (Mattias Svanberg) · SWE8 (Lucas Bergvall).

**Repetidas al pool (17):** JOR12 · URU8 (→2) · JOR17 · UZB1 (→2) · TUN10 (→2) · QAT8 · RSA10 ·
RSA20 (→2) · TUN15 · SUI17 · GER1 · SUI13 · NOR19 · TUN2 · RSA6 · UZB13 · **IRN19 (→2)**. Pool **131→148 cartas / 113→125 códigos**.

**Hitos:** brillantes 32→**35/68** (FWC9 + CIV1 + IRQ1) · 🇵🇹 Portugal sigue 3/20 (Cristiano POR15 aún falta).

**⚠️ Enredo Iran (resuelto):** al dictar, "IRN20" fue un desliz por **IRN19**. **IRN20** no venía en este lote (Boris
la tiene pegada; no se tocó). **IRN19 sí venía y resultó repetida** — Boris la tenía bien pegada con 1 repetida desde
el 10-jun, así que la de este sobre la subió a **rep=2** (el registro estaba correcto; no había fantasma). HAVE no se
movió por IRN19 (ya estaba pegada); solo sumó al pool.

---

## 📦 Lote — 2026-06-13 (sáb) · Sobres · 17:25 · **PEGADAS**

Dictado de **28 láminas (4 sobres)** → **10 nuevas pegadas** + **1 recuperada** + **17 repetidas**.
**HAVE 492→504 (50,2%→51,4%)**. Perdidas 28→**27**.

**Nuevas pegadas (10):** 🇵🇹 **POR7 (Nuno Mendes)** → Portugal 3→4/20 · ✨ **USA1 (EE.UU., escudo)** ·
GER13 (foto equipo Alemania) · UZB16 (Eldor Shomurodov) · AUS14 (Aiden O'Neill) · ALG14 (Farès Chaïbi) ·
TUR6 (Çağlar Söyüncü) · ECU11 (Kendry Páez) · CZE19 (Adam Hložek) · MAR18 (Soufiane Rahimi).

**Recuperada (1):** **ARG13** (Argentina, foto equipo) `perdida→pegada`. Perdidas 28→27.

**Repetidas al pool (17):** FWC13 · COD1 · CZE9 (→2) · PAR13 · MEX3 · SWE5 · CZE18 · ECU16 · SCO13 (→2) ·
IRQ4 · **FWC19** · UZB6 · AUT2 · AUS1 · AUS6 · COD16 · **SEN11 (→1)**. Pool **148→165 cartas / 125→140 códigos**.

**⚠️ Corrección SEN11:** el registro traía SEN11 como `falta` (atrasado), pero Boris ya la tenía pegada → la de este
sobre es repetida. Se dejó `pegada` con rep=1. HAVE no cambió (ya contaba como pegada en el total).

**Hitos:** brillantes 35→**36/68** (USA1 escudo) · 🇵🇹 **Portugal 3→4/20** (POR15 Cristiano aún falta).

---

## 📦 Lote — 2026-06-13 (sáb) · Sobres · 18:22 · **PEGADAS**

Dictado de **28 láminas (4 sobres)** → **16 nuevas pegadas** + **12 repetidas**.
**HAVE 504→521 (51,4%→53,2%)**. Perdidas 27 (sin cambios). ("al 9" = ALG9.)

**Nuevas pegadas (16):** ✨ **AUT1 (Austria, escudo)** · ✨ **ECU1 (Ecuador, escudo)** · ✨ **BEL1 (Bélgica, escudo)** ·
BRA16 (João Pedro) · COL5 (Yerry Mina) · SEN5 (Abdoulaye Seck) · CIV20 (Oumar Diakité) · ALG5 (Rayan Aït-Nouri) ·
ALG9 (Houssem Aouar) · CPV13 (foto eq. Cabo Verde) · ECU13 (foto eq. Ecuador) · UZB7 (Rustamjon Ashurmatov) ·
UZB11 (Otabek Shukurov) · AUS9 (Lewis Miller) · TUR2 (Uğurcan Çakır) · JPN3 (Henry Mochizuki).

**Repetidas al pool (12):** GHA9 · RSA5 (→2) · JOR14 · GHA14 · SWE17 · JOR18 · GHA18 · ALG1 (→2) · GHA5 ·
BRA8 · JOR9 · **SEN18 (→1)**. Pool **165→177 cartas / 140→150 códigos**.

**Hitos:** brillantes 36→**39/68** (AUT1 + ECU1 + BEL1) · 🇵🇹 Portugal sigue 4/20 (POR15 Cristiano aún falta).

**⚠️ Corrección SEN18:** igual que SEN11 — registro `falta` (atrasado) pero Boris ya la tenía pegada → la del sobre
es repetida. Se dejó `pegada` con rep=1.

---

## 📦 Lote — 2026-06-13 (sáb) · Sobres · 20:10 · **PEGADAS**

Dictado de **28 láminas (4 sobres)** → **11 nuevas pegadas** + **1 recuperada** + **16 repetidas**.
**HAVE 521→533 (53,2%→54,4%)**. Perdidas 27→**26**.

**Nuevas pegadas (11):** ⭐ **COL14 (James Rodríguez)** · BRA20 (Estêvão) · BRA4 (Marquinhos) ·
CAN14 (Jacob Shaffelburg) · CAN9 (Kamal Miller) · CAN5 (Samuel Adekugbe) · COL18 (Jhon Córdoba) ·
COL9 (Santiago Arias) · SEN14 (Lamine Camara) · SEN9 (Idrissa Gana Gueye) · TUN14 (Hannibal Mejbri).

**Recuperada (1):** **UZB18** (Jaloliddin Masharipov) `perdida→pegada`. Perdidas 27→26.

**Repetidas al pool (16):** TUR14 · SWE3 · EGY11 · KSA9 · GHA1 · NED14 · TUR18 · SWE7 · GER20 · BEL15 ·
JOR5 · SUI7 · TUN18 · BEL19 · **ARG13** (recuperada 17:25, ahora repe) · SUI3. Pool **177→193 cartas / 150→166 códigos**.

**Hitos:** brillantes 39/68 (sin foils nuevos) · 🇵🇹 Portugal sigue 4/20 (POR15 Cristiano aún falta).

---

## 📦 Lote — 2026-06-13 (sáb) · Sobres · lote F · ⚠️ **SOLO IDENTIFICADO — NO PEGADO**

Dictado de **27 láminas** → **11 nuevas** + **16 repetidas**. **Boris solo las identificó; no pegó nada.**
Las 11 nuevas quedan en estado **`tengo` (SUELTAS, sin pegar)** — NO `pegada`. **HAVE 533→544 (54,4%→55,5%)**
(el estado `tengo` cuenta en HAVE igual que `pegada`, pero marca el riesgo de extravío — lección 06-06). Perdidas 26.

**🔴 Nuevas SUELTAS (11) — pendiente pegarlas:** ⭐ **SWE20 (Viktor Gyökeres)** · GER19 (Karim Adeyemi) ·
ENG5 (Ezri Konsa) · MEX20 (César Huerta) · CUW11 (Juninho Bacuna) · IRQ14 (Youssef Amyn) · IRQ18 (Ali Al-Hamadi) ·
TUR9 (Kaan Ayhan) · EGY16 (Osama Faisal) · CZE2 (Matěj Kovář) · SCO9 (Anthony Ralston).

**Repetidas al pool (16):** CRO2 · IRQ9 · KOR16 · CUW16 · CRO6 · KOR20 · **EGY20** ("egv 20") · TUR5 · NED5 ·
KSA5 · BEL10 (→2) · NED9 (→2) · JOR6 · PAR6 · RSA4 · AUT4. Pool **193→209 cartas / 166→180 códigos**.

**Notas:** (1) el lote salió de **27 láminas**, no 28 — si fueron 4 sobres falta un código por dictar. (2) "egv 20"
se interpretó como **EGY20** (Egipto). (3) **Se rompe la racha de 0 sueltas** que venía desde el 12-jun; quedan 11
en estado `tengo` pendientes de pegar.

---

## 📦 Lote — 2026-06-14 (dom) · Sobres · 14:40 · **PEGADAS**

Dictado de **28 láminas (4 sobres)** → **8 nuevas pegadas** + **1 recuperada** + **19 repetidas**.
**HAVE 544→553 (55,5%→56,4%)**. Perdidas 26→**25**. Suerte dura: 9/28 nuevas (~32%, normal pasado el 40%).

**Nuevas pegadas (8):** SCO19 (Che Adams) · KOR19 (Hwang Hee-chan) · KOR15 (Jens Castrop) ·
KSA4 (Saud Abdulhamid) · KSA8 (Hassan Altambakti) · COD17 (Brian Cipenga) · COD20 (Nathanaël Mbuku) ·
AUT6 (Philipp Lienhart).

**Recuperada (1):** **COD12** (Noah Sadiki) `perdida→pegada`. Perdidas 26→25.

**Repetidas al pool (19):** NED6 · UZB15 · ALG12 · **AUS10 (→3)** · CZE5 (→2) · NED10 · **USA17 (→3)** ·
ALG17 · AUS15 (→2) · **CZE9 (→3)** · NED15 (→2) · UZB2 · ARG2 (Dibu Martínez) · AUS19 (→2) · SCO14 · NED2 ·
UZB10 · ALG8 · COL1 escudo foil (→2). Pool **209→228 cartas / 180→191 códigos**.

**Hitos:** brillantes 39/68 (sin foils nuevos) · 🇵🇹 Portugal sigue (POR15 Cristiano aún falta).

**Notas:** (1) Ninguna repetida cruzó con la wantlist de 20 del otro coleccionista; ojo códigos trampa
AUS≠AUT, NED2≠NOR2, UZB2≠UZB8. (2) Siguen pendientes de pegar las **11 sueltas del lote F (13-jun)** en estado `tengo`.

---

*Cross-ref: `registro_maestro.csv` (estado autoritativo) · `DASHBOARD.md` (KPIs) ·
`INVESTIGACION_Y_SISTEMA.md` (arquitectura).*
