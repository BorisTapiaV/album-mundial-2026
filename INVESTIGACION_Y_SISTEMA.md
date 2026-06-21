# Álbum Mundial 2026 — Investigación y Sistema

<!-- Documentación canónica del proyecto. Última actualización: 2026-06-03 -->

Bitácora completa de la investigación realizada y del sistema de seguimiento del
álbum **Panini FIFA World Cup 2026** (ala personal de Boris — el último Mundial de
Cristiano Ronaldo). Este documento existe porque la investigación fue extensa
(numeración + 864 jugadores + bio) y conviene tenerla trazada.

---

## 1. Objetivo

Completar el álbum de **980 láminas** de forma óptima en costo, tratándolo como un
sistema con telemetría (medir, cuantificar, seguir) sin perder el carácter de
pasatiempo de regulación. El álbum físico es **tapa dura**.

---

## 2. Investigación realizada (2026-06-01 → 2026-06-03)

### 2.1 Ficha base (DR, 2026-06-01)
- 980 láminas · 112 páginas · sobre = 7 láminas a $1.100 · caja 50 = $55.000 · álbum tapa blanda $3.900.
- Servicio de faltantes oficial: tiendapanini.cl, hasta 30 láminas exactas por pedido.
- Modelo coupon-collector: sobres hasta ~80-85% → luego faltantes + canje de repetidas.

### 2.2 Numeración del álbum (verificada 2026-06-03)
**Hallazgo clave:** el álbum NO se numera 1→980 corrido. Cada lámina trae un **CÓDIGO impreso**:
- `00` — logo Panini (foil)
- `FWC1`–`FWC19` — 19 especiales foil (emblema 1/2 y 2/2, mascota, eslogan, balón, 3 anfitriones, 11 FIFA Museum 1934-2022)
- **48 selecciones × 20** con código de país: `ALG1-20`, `ARG1-20`, … `POR1-20`, … `UZB1-20`
  - Dentro de cada equipo: **slot 1 = escudo (foil)** · **slot 13 = foto equipo** · resto = 18 jugadores
- **Cristiano Ronaldo = `POR15`** (confirmado por 3 fuentes)
- **Total** = 1 + 19 + 960 = **980**. Todas salen en sobres.
- **Set Coca-Cola (~12)** = promo APARTE, fuera de las 980.

**Consecuencia práctica:** como cada cromo se autoidentifica por su código, el mazo
puede estar revuelto. No importa el orden — se lee el código impreso.

### 2.3 Falsos positivos atrapados (transparencia)
- ⚠️ El "checklist oficial" de paninistore.com (`004911---checklist_INT_EN.pdf`) era el
  **FIFA 365 Adrenalyn XL 2025** (cartas de CLUBES — River, Bayern, Liverpool…),
  producto equivocado. Descartado. Por eso nunca se inventa numeración.
- ⚠️ La "ficha verificada" inicial decía "26 exclusivas dentro del álbum". Impreciso:
  las 980 son todas obtenibles en sobres (incluidos los 19 foil `FWC`); solo el set
  Coca-Cola queda fuera.

### 2.4 Nombres de jugador (8 agentes, 2026-06-03)
8 agentes en paralelo (6 equipos cada uno) extrajeron los **864 jugadores** (18 × 48)
+ 20 especiales. Dos fuentes de coleccionistas coincidieron slot-por-slot en la mayoría.
Resultado en `names.csv`.

### 2.5 Ficha por jugador (8 agentes, 2026-06-03)
8 agentes más reunieron la bio que imprime cada lámina + posición: **posición, club,
nacimiento, altura, peso**. Verificado contra la foto física de `COL6` (Daniel Muñoz):
coincide 100% (26-05-1996 · 1,81 m · 73 kg · Crystal Palace FC). Resultado en `bio.csv`.
- 864/864 con posición · 418 con peso (peso casi nunca publicado → vacío honesto, nunca inventado).

### 2.6 Fuentes
- diamondcardsonline.com/blog/2026-panini-fifa-world-cup-sticker-collection-checklist
- checklistinsider.com/2026-panini-fifa-world-cup-sticker
- cartophilic-info-exch.blogspot.com (estructura + endpoints)
- worldtradingcards.com (spot-checks)
- Bio: Transfermarkt, Wikipedia, ESPN, FBref, FotMob, sitios de clubes/ligas + squad pages WC2026.

---

## 3. Caveats de fiabilidad (importante)
1. **Rosters preliminares:** el álbum se imprimió antes del sorteo/convocatorias finales;
   algunos jugadores pueden no estar en la nómina final del Mundial. **El código impreso
   en la lámina manda** sobre cualquier nombre.
2. **Catar y Arabia Saudita** aparecen en el álbum aunque su clasificación deportiva sea
   dudosa (Panini los incluyó).
3. **Confianza `med`** en transliteraciones (UZB, JOR, KOR, nombres árabes): el slot es
   firme, la grafía exacta puede variar.
4. Lista de 48 equipos = según fuentes de coleccionistas; validar contra los códigos
   impresos de las láminas reales a medida que entren.

---

## 4. Arquitectura de archivos

| Archivo | Qué es | Generado por |
|---------|--------|--------------|
| `registro_maestro.csv` | **Fuente de verdad.** 980 láminas: código, equipo, slot, jugador, tier, **estado**, repetidas, notas + posición/club/nacimiento/altura/peso/conf_bio | `gen_registro.py` |
| `names.csv` | Datos: código → nombre jugador (+ especiales) | manual (agentes) |
| `bio.csv` | Datos: código → posición, club, nacimiento, altura, peso, confianza | manual (agentes) |
| `gen_registro.py` | Une names + bio, **preserva estado**, escribe el registro maestro | — |
| `gen_print.py` | Genera hojas imprimibles HTML desde el registro | — |
| `checklist_por_equipo.html` | Hoja primaria para marcar a mano | `gen_print.py` |
| `indice_alfabetico.html` | Búsqueda por nombre → código (canje) | `gen_print.py` |
| `faltantes.html` / `repetidas.html` | Listas dinámicas (con `--todo`) | `gen_print.py` |
| `DASHBOARD.md` | KPIs + estrategia + numeración + sistema | — |
| `fotos/`, `crops/` | Fotos fuente iniciales | — |

**Reproducir todo:** `python gen_registro.py` (regenera el CSV preservando estado) →
`python gen_print.py --todo` (regenera las hojas).

---

## 5. Sistema de seguimiento (híbrido)

**Principio:** el álbum tapa dura es **"solo escritura"** — se abre solo para pegar,
nunca para consultar. La fuente de verdad es el registro digital.

**Tres superficies, una sola fuente (`registro_maestro.csv`):**

| Superficie | Para qué | Cómo |
|-----------|----------|------|
| **Google Sheets** (importar el CSV) | Edición en vivo desde el teléfono, KPIs automáticos | `=CONTAR.SI(F:F;"pegada")` etc. (estado=col F) |
| **Hojas impresas** (HTML → PDF) | Marcar a mano, llevar a ferias/canjes sin el álbum | abrir HTML → Ctrl+P |
| **Dictado a Claude** | "tengo COL6" → Claude marca estado en el CSV | conversacional |

**Estados:** `falta` (default) · `tengo` (lo tienes, sin pegar) · `pegada` (en el álbum) ·
`repetida` (+ contador en columna repetidas = moneda de canje). `tengo` y `pegada` cuentan
ambos como "lo tengo" para el % completado.

---

## 6. Formatos impresos — cuál usar cuándo

Diseñados para resolver dos ejes: **marcar a mano** + **código vs nombre** (al canjear,
muchos aficionados dicen "¿tienes a Messi?" en vez de "¿tienes ARG17?").

| Hoja | Cuándo | Por qué |
|------|--------|---------|
| **checklist_por_equipo** | Día a día: pegar y trackear | Ordenada como el álbum. Cada línea trae **código Y nombre** → sirve a quien piensa en código y a quien piensa en nombre. Casilla para marcar; lo ya registrado sale relleno. ⭐ marca estrellas |
| **indice_alfabetico** | En canje/feria | Ordenado por apellido → "¿tienes a Mbappé?" → lo encuentras y lees `FRA20`. Resuelve el eje nombre |
| **faltantes** | Cerca del cierre (80%+) | Solo lo que falta = lista de caza compacta. Regenerar cuando haya avance |
| **repetidas** | Al canjear | Tu inventario de duplicados = moneda 1:1 |

**Recomendación:** imprimir **checklist_por_equipo** (hoja madre) + **indice_alfabetico**
(compañera de canje). Las otras dos se regeneran cuando tengan datos útiles.

---

## 7. Estrategia de cierre (canje)

**Regla de oro:** canje **1:1 de commons primero (gratis)**, faltante pagado después
(tiendapanini.cl cobra por unidad).
- El 1:1 solo aplica dentro del mismo tier. Una estrella/foil no se cambia 1:1 por una common.
- Orden óptimo: (a) agotar canje 1:1 de commons → (b) pedir a tiendapanini.cl lo que no se
  consiga → (c) estrellas/exclusivas, estrategia aparte.
- **12 estrellas T3** (mejor moneda): Cristiano POR15, Messi ARG17, Mbappé FRA20,
  Haaland NOR15, Bellingham ENG11, Kane ENG18, Vinicius BRA14, Lamine Yamal ESP15,
  Salah EGY17, Son KOR18, van Dijk NED3, Musiala GER15.

---

## 8. Estado actual (2026-06-21)

- **Pegadas:** **825/980 (84,2%)** · **Faltan:** 145 · **Perdidas:** 10 · **Por conseguir:** 155 · **Repetidas:** 168 cartas / 130 códigos · **Brillantes:** 51/68.
- **Endgame:** sobres cerrados (>80%). Cierre por canje 1:1 + faltantes oficiales (tiendapanini.cl, tope 30/pedido, abre ~fin jun).
- **Pendientes clave:** ⭐ POR15 Cristiano y ARG17 Messi (compra suelta) · 4 "scomar" sin mapear · precio unitario faltante por confirmar.
- **Fuente de verdad:** `registro_maestro.csv`; estado vivo en `DASHBOARD.md` (este doc es la bitácora de investigación/arquitectura, no el tracker diario).

---

*Proyecto: `C:\Users\boris\PROJECTS\Mundial-2026\album\`*
