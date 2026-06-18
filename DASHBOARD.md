# Álbum Mundial 2026 — Dashboard

<!-- Ala personal Boris. Sistema tipo Profiler: medir, cuantificar, seguir.
     Objetivo: completar el álbum Panini FIFA World Cup 2026 (último Mundial de Cristiano Ronaldo)
     de forma óptima en costo, usando el modelo del coleccionista de cupones. -->

**Colección:** Panini — FIFA World Cup 2026 (edición Chile)
**Última actualización:** 2026-06-18 (jue) — **687/980 (70,1%)** 🎉 cruza el 70% — **+20 láminas nuevas de Andrés** (detectadas decodificando el QR exportado de la app Figuritas): KOR2/9/14, CZE16, BIH7/11/20, MAR9, PAR16, ESP6/7/14/19, URU13, ARG3, AUT7/20, POR4, COD5/9 → todas `falta→tengo` (sueltas ⏳ pegar). **Canje 2 Andrés recalculado:** total real **54 láminas por $9.000 CLP** (34 de la lista de 37 + 20 extra). ⚠️ **PENDIENTE:** de las 37 originales, Andrés **no tenía 3** (entregó 34) — Boris revisa la lista para identificarlas y revertir a `falta` (CRO13 ya está fuera; probablemente es una de las 3). *Anterior: CRO13 sacada del Canje 2 (HAVE 668→667).* Pool repetidas 245→**243**. Brillantes **45/68**. 🇵🇹 **POR15 Cristiano sigue faltando**. · *Anterior: 2026-06-16 (mar) — **595/980 (60,7%)** 🎉 cruza el 60% — **2 canjes CERRADOS:** **Carlos** (recibió 16: 14 canje + POR6/URU3 extra) + **Andrés Acosta** (das 13 / recibes 15: GER15⭐, FRA5/9/14, URU15, SEN16, NED19, CIV10, KSA16, POR14/18/13 🇵🇹, PAN6, UZB20⭐, ALG3). **31 recibidas SUELTAS** (`falta→tengo`, ⏳ pendiente pegar). POR13+PAN6 eran perdidas → recuperadas (perdidas 25→23). Pool repetidas 209→**196/164** (Andrés -13). 🇵🇹 Portugal +4 hoy (POR6/13/14/18) — **POR15 Cristiano sigue faltando**. Brillantes 40/68. · *Anterior: 14-jun (dom, 21:10) — **564/980 (57,6%)** — **canje recibido de Jorge Vásquez:** +10 nuevas PEGADAS (CUW20, USA14/15/19, ECU8/17, TUR12, ⭐TUR20 Kenan Yıldız, ⭐SCO11 McTominay, HAI15) + 2º CUW7 (pega 1 → repe=1). Pool 222→**223 cartas / 189 códigos**. · *Antes mismo día — **554/980 (56,5%)** — **CROSS-CHECK FÍSICO COMPLETO de la pila de repetidas** (5 paquetes, 223 cartas dictadas) tras detectar repetidas mal registradas al canjear con Jorge Vásquez. **Corrección:** registro inflaba 9 cartas en 8 códigos (USA17, ALG8, EGY10, IRN6, JOR12, BEL10, IRN7, IRN20 — todas con slot **pegado**, no se perdió ningún slot del álbum) + 3 cartas extra en mano (EGY20, HAI16, QAT6) + **CUW7** rescatada (estaba `falta` pero la tenías en la pila → `tengo`, apartada para pegar). Pool **222 cartas / 188 códigos** (= pila física real). Wantlist de Jorge guardada en `JORGE_VASQUEZ_WANTLIST.md` (17 códigos; JOR12+AUT15 ya entregadas). Perdidas 25. Brillantes 39/68. 🇵🇹 Portugal (POR15 Cristiano aún falta). · *Anterior: 14-jun 14:40 lote sobres 553 (+9 pegadas) · 13-jun lote F 544 · 12-jun 392→474.*

**Artefactos clave:** `BITACORA_LOTES.md` (protocolo de ingreso + log temporal de lotes) · `dashboard_share.png` + `gen_dashboard.py` (tarjeta para compartir estilo Figuritas) · `perdidas.html` · `ALBUM_ORDEN.md` (orden + páginas FWC).
**Pendientes abiertos:** resolver "scomar" cuando aparezca · precio unitario faltantes tiendapanini.cl · v2 dashboard radar de habilidades. *(Mapeo de especiales `00`/FWC19/inserto ✅ cerrado 14-jun — ver ALBUM_ORDEN.md.)* *(Las 11 sueltas del lote F figuran ya como `pegada` en el registro.)*

**🆕 Figuritas App (import vía QR) — 2026-06-15:** investigación completa en **`FIGURITAS_APP_INVESTIGACION.md`** (entry point). Veredicto **SÍ factible**: el QR de la app (`com.majurfest.figuritas`, dev Matias Jurfest) es `⋋^ + gzip+base64` de 3 bitmaps (tengo / repetidas / counts), 123 bytes ≈ 980 láminas, **sin cifrado**. Formato crackeado con 5 QR de muestra. **Pendiente:** 3 códigos que Boris marcó para fijar mapeo bit↔código → luego se escribe generador `registro_maestro.csv → QR`. DR optimizado por Leonor. Muestras en `qr_muestras/` + raw en `qr_muestras_raw.json`.

---

## 📊 KPIs

| Métrica | Valor | Fuente |
|---------|------:|--------|
| Total de láminas del álbum (N) | **980** | DR ✅ |
| Tengo/pegadas (HAVE) | **687** (595 pegadas + 92 sueltas ⏳ pegar) | registro 2026-06-18 (+20 nuevas Andrés) |
| **% completado** (HAVE/N) | **70,1%** | calculado |
| Perdidas (extraviadas en casa) | **22** | calculado |
| Faltan (`falta`) | **271** | calculado |
| **Por conseguir** (falta + perdida) | **385** | falta 362 + perdida 23 |
| Repetidas (n°) | **196 cartas / 164 códigos** | registro 2026-06-16 (post-canjes Carlos +Andrés: dio 14+13) |
| Tasa de novedad (nuevas÷compradas) | `—` | registro compras |
| Costo hundido (gastado) | `$— CLP` | registro compras |
| **Costo real sobre (Boris)** | **$1.700 online c/despacho** (evita fila) vs $1.100 mostrador | Boris 14-jun |
| **Costo/lámina NUEVA hoy (sobres $1.700 @60,7%)** | **~$618** = 1700÷(7×0,393) | modelo |
| Costo cerrar TODO solo con sobres $1.700 | **~$1,57M** (≈925 sobres, coupon-collector) | modelo |
| Costo cerrar — mixto (canje+faltantes) | **$158.000–$330.000** | DR |
| **Punto de cruce (sobres→faltantes)** | **~31-39% completado** (recalc con sobre $1.700 vs faltante $350-400) — **YA cruzado, voy 60,7%** | modelo 14-jun |
| Precio faltante estimado (servicio aún no abre) | **~$350–420 CLP/lámina** (tiendapanini.cl FIFA 365 $350 · MX 8 MXN≈$420); tope 30/pedido; abre ~fin jun | web 14-jun ⏳ |
| Valor reventa estrellas | ver abajo | DR ✅ |

---

## 🔢 Datos del DR (ficha verificada — edición Chile)

| Dato | Valor | Estado |
|------|------:|--------|
| Marca / colección | Panini FIFA World Cup 2026 | ✅ |
| Total láminas | **980** (112 páginas) | ✅ |
| Estructura por equipo | 48 selecciones × 20 (18 jugadores + foto + escudo) | ✅ |
| Especiales | 68 especiales + 12 exclusivas Coca-Cola + **14 fuera de sobres** | ✅ |
| Láminas por sobre | **7** (subió de 5) | ✅ |
| Precio sobre suelto | **$1.100** mostrador · **$1.700 online (Boris paga este, evita fila)** | ✅ |
| Caja 50 sobres | **$55.000** (~$1.100 c/u) | ✅ |
| Álbum tapa blanda | **$3.900** (o pack + 50 sobres $58.900) | ✅ |
| Servicio faltantes oficial | tiendapanini.cl — hasta **30 láminas exactas/pedido** | ✅ |
| Precio por lámina faltante (unitario) | **~$350–420 CLP est.** (CL FIFA 365 $350 · MX 8 MXN≈$420) | ⏳ servicio WC2026 abre ~fin jun; reconfirmar |
| Reventa Cristiano (normal) | ~$40 USD tope / especiales >$700 USD | ✅ |

---

## 🔡 Numeración del álbum (verificada 2026-06-03)

> Fuentes: diamondcardsonline + checklistinsider (coinciden). El **código impreso en cada lámina manda** — verificar la lista de equipos al leer las fotos reales.

**El álbum NO se numera 1→980 corrido. Cada lámina trae un código:**
- **`00`** — logo Panini (foil)
- **`FWC1`–`FWC19`** — 19 especiales foil (emblema, mascota, historia de Mundiales)
- **48 selecciones × 20** con código de país: `ALG1-20`, `ARG1-20`, … `POR1-20`, … `UZB1-20`
  - Dentro de cada equipo: **slot 1 = escudo (foil)** · **slot 13 = foto equipo** · resto = 18 jugadores
- **Cristiano Ronaldo = `POR15`** ✅ (confirmado por 2 fuentes)
- **Total 980** = 1 (`00`) + 19 (`FWC`) + 960 (48×20). Todas salen en sobres.
- **Set Coca-Cola (~12)** = promo APARTE, **fuera de las 980** (canal Coca-Cola).

⚠️ **Corrección:** la "ficha verificada" inicial decía "26 exclusivas dentro del álbum (14 fuera de sobres + 12 Coca-Cola)" — impreciso. El modelo correcto: las 980 son todas obtenibles en sobres (incluidos los 19 foil `FWC`); solo el set Coca-Cola queda fuera. ⚠️ También: el PDF del Panini Store oficial estaba mal etiquetado (era FIFA 365 Adrenalyn XL 2025, cartas de clubes — descartado).

---

## 📖 Orden y páginas del álbum (VERIFICADO 2026-06-05)

> Detalle completo en `ALBUM_ORDEN.md`. Columnas `orden_album` (1-48) + `pagina` ya en `registro_maestro.csv`.

- El álbum **NO es alfabético** → va por **grupo del Mundial** (12 grupos × 4), anfitriones primero. Fuente: checklistinsider + dato físico de Boris.
- **2 páginas por equipo.** México (#1) arranca en **pág 8**.
  - Equipos #1-24 (México→Túnez): página inicio = `8 + (n−1)×2`
  - **Inserto de especiales en págs 56-57** (entre Túnez #24 y Bélgica #25)
  - Equipos #25-48 (Bélgica→Panamá): página inicio = `58 + (n−25)×2`. Panamá (#48) = págs 104-105.
- **Especiales FWC NO van todas juntas:** bloque inicio (págs 1-7, `00`+`FWC1-8` emblema+anfitriones) + inserto (56-57) + cierre (págs 106-112, `FWC9-19` FIFA Museum). **Mapear páginas exactas de FWC pendiente.**
- 🇵🇹 **Portugal (Cristiano, POR15) = págs 90-91** (equipo #41, grupo K). Aún 0/20.

---

## ⚠️ Pendiente abierto — "scomar" (4 cartas huérfanas)

En una sesión previa Boris dictó **"scomar 4, 6, 9, 20"** y **las pegó** antes de mapearlas. "scomar" no es código válido. **NO es Marruecos ni Costa de Marfil** (ambos confirmados en 0 láminas pegadas). → 4 cartas pegadas en un equipo desconocido, fuera del registro (el conteo real es +4 sobre los 126).
**Resolución esperada:** cuando Boris llegue a un equipo y encuentre los slots 4/6/9/20 ya pegados → ese es. Mapear ahí. (O si recuerda confederación/camiseta, búsqueda dirigida.)

---

## 🧮 Modelo de decisión (coupon collector)

**Regla dura:** sobres hasta ~**80-85%**, luego **faltantes exactos** + **canje de repetidas**.

- 980 únicas. Sin canje, completar solo con sobres ≈ **inviable** (esperanza matemática ~1.000+ sobres).
- Con canje activo, el promedio real es **~400 sobres ≈ $440.000**.
- Las **26 láminas exclusivas** (14 fuera de sobres + 12 Coca-Cola) **NO salen en sobres** → canal aparte (botellas Coca-Cola, promos retail). Planificar desde ya.
- **Punto de cruce:** cuando el costo marginal de una lámina nueva vía sobre supera el precio del faltante unitario → ahí se corta y se pide a tiendapanini.cl (tope 30/pedido, se repite).

---

## 🤝 Estrategia de cierre (canje)

**Regla de oro:** en la recta final, **canje 1:1 de commons primero, faltante pagado después.** El canje 1:1 es gratis; tiendapanini.cl cobra por unidad.

1. **Commons (base):** se canjean **1 repetida por 1 faltante**. Funciona porque las base valen casi lo mismo y la oferta es pareja → es pura matemática de "yo tengo lo que tú no". Las repetidas apartadas = la moneda de canje. Agotar este canal **antes** de pagar nada.
2. **El 1:1 SOLO aplica dentro del mismo tier.** Una estrella o escudo foil NO se cambia 1:1 por una common → piden 2-3 commons u otra estrella. Las exclusivas (Coca-Cola / chase) casi no entran al circuito de canje → se compran o se pagan caras.
3. **Dos tipos de hueco en el endgame:**
   - **Commons que faltan** → cerrar con canje 1:1 (barato, tranquilo).
   - **Estrellas/foil/exclusivas que faltan** → no cierran 1:1; faltante oficial, varias commons, o compra suelta.
4. **Orden óptimo de cierre:** (a) agotar canje 1:1 de commons → (b) pedir a tiendapanini.cl solo lo que no se consiga canjeando (tope 30/pedido) → (c) estrellas/exclusivas, estrategia aparte desde ya.

---

## ⭐ Valoración por tiers (DR Gemini 2026-06-01)

> ⚠️ Separar **valor verificado en Chile** vs **especulativo/internacional** (el DR infla la prosa).

### 🔴 TIER 1 — Exclusivas (NO salen en sobres)
- **Set Coca-Cola "Team Believers" = C1–C14** (14 láminas, no 26). Se obtienen comprando Coca-Cola Zero (2 + $500 copago) o six-pack en micoca-cola.cl. Floor reventa **~$2.600–5.000 c/u**.
  - Conocidas: **C1 Lamine Yamal** (España) · **C2 Lautaro Martínez** (Arg) · **C3 Fede Valverde** (Uru). C4–C14 por confirmar.
- **Extra Stickers** (Bronce/Plata/Oro) — chase cards NO numeradas, fuera del álbum, ratio ~1/50–100 sobres. Cristiano tiene. Valor alto y volátil.

### 🟠 TIER 2 — Especiales / foil (~68)
- Escudos foil de 48 federaciones + institucionales INT-1 a INT-20 (trofeo, logos, mascota).
- Escudos potencias (BRA/ARG/CHI/FRA): **$2.000–5.000** c/u. Periféricos, menos.
- Outlier: **Fede Valverde dorada $35.000** (1 listing ML — tomar con pinzas).

### 🟡 TIER 3 — Estrellas estándar
- **🇵🇹 Cristiano Ronaldo = Portugal #15** ✅ CONFIRMADO (ML MLC69731494). Base normal pero retención ~100% → escaso en la calle, se vende en toploader.
- Messi (ARG), Mbappé (FRA), Haaland (NOR), Bellingham (ING), Vinícius (BRA): base, alta demanda, sin precio fijo (data gap real).

### 💎 Las más caras (mayormente ESPECULATIVAS / importadas — NO líquidas en Chile)
- CR **Gold Crumple Foil** (parallel importado): ~$400 USD ≈ **$360.000 CLP** — NO viene en sobres Latam.
- Messi **case hits**: proyectado $180–200K. CR **Extra Sticker** bronce: premium variable.

---

## 📷 Registro de compras (para tasa de novedad)

| Fecha | Sobres comprados | Láminas nuevas | Repetidas | $ gastado |
|-------|-----------------:|---------------:|----------:|----------:|
| | | | | |

---

## 🛰️ Sistema de seguimiento (híbrido Sheets + MD)

**Principio:** el álbum (tapa dura) es **"solo escritura"** → se abre solo para pegar, nunca para consultar. La fuente de verdad es el **registro digital**. Así el álbum se manipula un puñado de veces en toda la colección = cero desgaste.

- **Registro maestro vivo:** Google Sheets, importado desde `registro_maestro.csv` (980 láminas **con nombre de jugador**, columnas `codigo / equipo / slot / jugador_tipo / tier / estado / repetidas / notas`). Boris lo edita desde el teléfono. Estados: `falta` / `tengo` / `repetida`. Los nombres viven en `names.csv` y los inyecta `gen_registro.py` (que preserva el estado ya inventariado).
- **Telemetría:** Claude extrae los KPIs del Sheets a este DASHBOARD cada sesión (% completado, faltan, repetidas).
- **2 artefactos portátiles (teléfono, nunca el álbum):**
  - **Lista de FALTANTES** (códigos en `falta`) → qué buscar en quiosco/feria/canje.
  - **Lista de REPETIDAS** (`repetidas` > 0) → moneda de canje 1:1.

**Flujo de registro (sin hojear):** Boris dicta los códigos impresos (`COL6`, `POR15`…) → Claude marca `tengo` (1ª copia) o `repetida +1` (duplicado) → al pegar, lote de una pasada por página/equipo → álbum al cajón. El código impreso autoidentifica cada lámina, así que el mazo puede estar revuelto.

**Fórmulas Sheets sugeridas:** `=CONTAR.SI(F:F;"tengo")` (tengo) · `=CONTAR.SI(F:F;"falta")` (faltan) · `=CONTAR.SI(F:F;"tengo")/980` (% completado) · `=SUMA(G:G)` (total repetidas).

---

## 📁 Archivos

- `INVESTIGACION_Y_SISTEMA.md` — **documentación canónica**: bitácora de investigación + arquitectura + formatos impresos + fuentes + caveats
- `ALBUM_ORDEN.md` — **orden + páginas del álbum** (48 equipos por grupo, página por equipo, progreso) — VERIFICADO 2026-06-05
- `registro_maestro.csv` — **registro maestro 980 láminas con nombres + ficha** (importar a Google Sheets = fuente de verdad). Columnas bio: `posicion / club / nacimiento / altura / peso / conf_bio`. Nuevas: `orden_album` (1-48) + `pagina` (rango por equipo)
- `names.csv` — nombres jugador↔código (verificados 2026-06-03 por 8 agentes)
- `bio.csv` — ficha por jugador (posición, club, nacimiento, altura, peso) — 864 con posición, 418 con peso; huecos en selecciones chicas (vacío > inventado)
- `gen_registro.py` — generador del CSV (lee names.csv + bio.csv, preserva estado)
- `gen_print.py` — genera **hojas imprimibles** desde el registro (`--todo` = las 4). **Fix 2026-06-05:** las marcadas usan **✓ impreso** (no fondo negro, que el navegador omitía al imprimir → se veían vacías en PDF) + `print-color-adjust: exact`. Encabezado de equipo y listas muestran la **página del álbum** (azul).
- `checklist_por_equipo.html` — **hoja primaria** marcar a mano (código + nombre + casilla con ✓ las que tienes, ⭐ estrellas, **página por equipo**)
- `lista_intercambio.html` — **hoja de intercambio/canje** (2026-06-06 PM). Formato plano del faltantes (código · nombre · equipo · **página como columna**), pero con **TODAS** las láminas: las que ya tengo salen **atenuadas (opacity 0.32) + check**; las que faltan se ven **idénticas a faltantes** (texto normal); `xN` = repetidas. De un vistazo: qué me falta + qué me sobra. ⚠️ Las que faltan NO se reestilizan (no negrita/no caja negra) — fue el bug que Boris rechazó 2 veces.
- `indice_alfabetico.html` — búsqueda **por nombre → código** (para canje)
- `faltantes.html` / `repetidas.html` — listas dinámicas (lista de caza / moneda de canje), cada línea con su **página**
- `CHECKLIST.md` — inventario por equipo (✅ tengo / ❌ falta / 🔁 repetida)
- `fotos/` — fotos fuente
- `crops/` — recortes de trabajo

## 🔎 Lección S 2026-06-06 PM — verificación cruzada mazo-físico-vs-registro

Boris maneja **2 mazos físicos**: el de pegar y el de repetidas (moneda de canje). Riesgo detectado: cartas de **primera copia** mal pasadas al mazo de repetidas → al mirar la página del álbum (vacía) se cree que "faltan", cuando en realidad están sueltas en el mazo equivocado (caso IRN15/IRN17). La verificación cruzada (leer el mazo físico de repetidas y compararlo contra el registro) rescató **6 falsos-faltantes**: AUS20 (pegada +2), IRN15, IRN17, SEN2, RSA2, PAN2.

- **Regla anti-confusión:** una carta solo va al mazo de repetidas **si su slot ya está pegado en el álbum**. Slot vacío en álbum = primera copia → mazo de pegar.
- **Bug corregido:** `gen_print.py` tenía `HAVE = {"tengo","pegada"}` sin `"repetida"` → subcontaba 6. Ahora incluye `repetida`.

**Hoja nueva `lista_intercambio.html` (mismo PM):** pedido de Boris para el canje. Iteró 3 veces hasta el formato correcto. **Lección de diseño imprimible:** Boris quería el **formato plano del faltantes** (NO el agrupado por equipo con encabezados densos tipo checklist) + agregar las que ya tiene (atenuadas + check) + **columna de página SÍ**. El error repetido fue **reestilizar también las que faltan** (negrita + caja negra vía `.dim .row:not(.have)`) — Boris las quiere **idénticas a faltantes**, solo las que TIENE deben diferenciarse. Regla: en vistas "todas las láminas", atenuar solo el estado `have`, nunca tocar el render de las `falta`.

*Próximo paso: (1) Resolver "scomar" cuando aparezca (4 huérfanas). (2) Mapear páginas exactas de los especiales FWC (no van juntas). (3) Repetir verificación cruzada mazo-vs-registro por equipo. (4) Seguir dictando lotes. (5) Confirmar precio unitario faltante en tiendapanini.cl. (6) Importar `registro_maestro.csv` actualizado a Google Sheets.*
