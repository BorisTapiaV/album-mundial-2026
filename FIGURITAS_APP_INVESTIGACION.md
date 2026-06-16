# Figuritas App — Investigación completa: importar mi álbum vía QR

<!-- Documento maestro. Consolida: motivación, DR (Leonor→Claude), y el reverse-engineering empírico del formato del QR. Creado 2026-06-15. -->

**Estado:** ✅ **RESUELTO, COMPLETO Y FUNCIONANDO (2026-06-16).** Mapeo bit↔código descifrado, generador `CSV → QR` escrito (`gen_qr_figuritas.py`) e **import real confirmado en la app**: tengo + faltantes + **repetidas con contadores**. Cargó las **595 tengo + 196 repetidas** exactas. v1 (tengo/falta) y **v2 (repetidas)** ambas cerradas.
**Veredicto:** **SÍ — confirmado en producción.** El inventario del CSV se carga a la app vía QR sin tipear nada.

---

## ✅ Resolución del mapeo (2026-06-16)

**El truco era el orden de bits: LSB-first dentro de cada byte** (no MSB-first). Con eso México (equipo 1) = bits 20-39 contiguos, y todo el esquema queda lineal:

| Tramo de bits | Contenido |
|---|---|
| 0-19 | 20 especiales: `00` → bit 0 · FWC1-19 → bits 1-19 (`bit = slot`) |
| 20-39 | México (equipo 1) |
| `20·T` … `20·T+19` | equipo T (T = `orden_album`, 1-48) |
| 960-979 | Panamá (equipo 48) |
| 980-983 | padding |

**Fórmula:** lámina de equipo → `bit = 20·orden_album + (slot−1)` · especial → `bit = slot`.
**Polaridad:** bit `0` = tengo · `1` = falta (bloque 0). Bloque 1 = repetidas (bitmap, mismo esquema de bits). **Bloque 2 = cantidades** (un byte por bit prendido en bloque 1, en orden ascendente de bit) → **byte = copias totales = `repetidas` + 1**. Confirmado con test controlado (contadores 1/2/3 → bytes 2/3/4).

**Validación:**
1. Generé "México todo tengo" desde el CSV → **idéntico byte a byte** al export real de la app.
2. Con inventario real, las diferencias fueron *exactamente* las láminas que faltaban → cero error.
3. **Import real en la app:** test México calzó + QR full marcó **595** exactas.

**Generador:** `gen_qr_figuritas.py` → produce `QR_FIGURITAS_test_mexico.png` (prueba) + `QR_FIGURITAS_full.png` (inventario completo). Regenerar tras cada cambio de inventario.

---

## 1. Objetivo

La app **Figuritas Mundial 2026 Album** (Android) ofrece "Importar álbum" mediante un **código QR exportado de otro dispositivo**. Boris ya tiene su inventario de 980 láminas en `registro_maestro.csv` (estado `tengo`/`falta`/`repetida` por código). **Pregunta:** ¿se puede generar un QR desde ese CSV y cargarlo en la app, sin tipear 980 láminas a mano?

**Para qué:** la app hace **matching automático de canjes** (cruza tus faltantes vs repetidas de otro coleccionista). Es la única función que el sistema CSV propio no tiene. Migrar/duplicar el inventario a la app daría acceso a ese matching con la comunidad.

---

## 2. Identidad de la app (verificado por DR)

| Dato | Valor | Fuente |
|------|-------|--------|
| Nombre | "Figuritas Mundial 2026 Album" (es) / "World Cup 2026 Album" (en) | Play Store |
| **Package** | **`com.majurfest.figuritas`** | Play Store (`?id=`) |
| Desarrollador | **Matias Jurfest** (ingeniero uruguayo, Founder @ Figuritas App) | LinkedIn dev + prensa |
| Contacto dev | appfiguritas@gmail.com | Play Store |
| Versión analizada | 4.5.2 (actualizada 8-jun-2026) | Play Store / APKPure |
| SO requerido | Android 8.1+ | Play Store |
| Descargas | +1.000.000 | Play Store |
| Compras in-app | $1.100–$11.400 CLP | Play Store |
| Sitio | figuritas.app/world-cup-2026 | — |
| Lineage | App continua 2018 → 2022 (Mundial) → 2026, mismo package, mismo autor | prensa + stores |

**Apps que NO son esta (descartadas para no contaminar):** "Figuri App" de Octavio Berruti (Rosario, IA+geo, Infobae 2026-04-30); lookalikes `mobi.todoapp.mialbum`, `com.figurinhas.figurinhas_light`, `com.picatecla.album`; app análoga "Sticker Collector 26" (otro dev, usada solo como referencia de categoría).

### Pantalla "Importar álbum" (texto literal, screenshot)
> "Importa un álbum escaneando o adjuntando un código QR exportado de otro dispositivo."
> Opciones: **[Escanear con la cámara]** · **[Desde la galería]**

"Desde la galería" = adjuntar una **imagen de QR** (no un CSV). No hay import de CSV oficial.

---

## 3. Proceso de investigación

1. **Borrador DR** escrito por Claude (`DR_FIGURITAS_IMPORT_BORRADOR.md`).
2. **Optimización Leonor** (regla obligatoria pre-DR): agente que adoptó `leonor-optimizer.md` en modo Quirúrgico, IA destino Claude. Subió 6/10 dimensiones (Adaptación al modelo 3→5, Ejemplos 2→4, Verificabilidad 4→5), conservó 100% de fuentes/restricciones. Resultado: `DR_FIGURITAS_IMPORT_LEONOR.md`.
3. **Deep Research** (workflow Claude): 101 agentes, 6 ángulos, 18 fuentes, 51 claims → 21 confirmados / 4 refutados. Resultado: `DR_FIGURITAS_IMPORT_RESULTADO_2026-06-15.md`.
4. **Reverse-engineering empírico** del QR con 5 muestras reales (sección 5). Resultado: `DR_FIGURITAS_QR_FORMATO.md` + este doc.

---

## 4. Hallazgos del DR

**Veredicto DR (antes del decode):** SÍ-CON-TRABAJO. El decode empírico posterior lo subió a **SÍ**.

| Hallazgo | Certeza | Implicación |
|----------|:------:|-------------|
| Package `com.majurfest.figuritas`, dev Matias Jurfest | 5 | App correcta; APK accesible |
| App **100% offline**: solo internet la 1ª vez (baja estructura del álbum); **sin login, sin nube** | 4-5 | El inventario vive en el dispositivo |
| "Cada usuario tiene un QR con su colección"; el cruce de canje es **local, sin servidor** | 4 | **El QR transporta los datos** (no es token server-bound) → refuta contra-hipótesis |
| Feature "Import and Export an album" existe (changelog v4.5.x) | 5 | El flujo export→QR→import es real |
| **No** hay import CSV oficial ni herramienta de terceros | 3-4 | El único camino es generar el QR nosotros |
| Formato exacto del payload | — | Era [DATA GAP] en el DR → **resuelto por decode (sección 5)** |

**Caveats del DR:** "el QR lleva los datos" fue, en el DR, inferencia arquitectónica (no teardown). Las fuentes de prensa (La Nación, La Nueva, La Gaceta, El Observador) son secundarias con tono algo promocional. La landing oficial documenta casi cero features. "No herramienta de terceros" = [NO ENCONTRADO], no prueba de inexistencia. → **El decode empírico (sección 5) eliminó estos caveats: confirmó directamente que el QR lleva los datos en gzip+base64, sin cifrado.**

**Open questions que quedaban del DR:**
- ¿El QR de "Importar álbum" (device-to-device) usa el mismo formato que el QR de canje? (probable, no confirmado al 100%).
- ¿La app valida/firma el QR? → decode sugiere **que no** (no hay espacio para firma en el payload).

---

## 5. Reverse-engineering del QR (decode empírico)

### 5.1 Método
- Decode con **OpenCV `QRCodeDetector`** (Python). pyzbar no estaba; OpenCV bastó.
- 5 muestras exportadas por Boris desde la app (copiadas a `qr_muestras/`):
  1. `QR_original.jpeg` — álbum con ~3 láminas marcadas (primera muestra).
  2. `QR_0_vacio.jpeg` — **álbum vacío** (baseline).
  3. `QR_1_una.jpeg` — **1 lámina** marcada tengo.
  4. `QR_2_dos.jpeg` — **2 láminas** marcadas tengo.
  5. `QR_3_repe.jpeg` — 2 tengo **+ 1 repetida**.
- Raw completo de las 5 en `qr_muestras_raw.json` (payload + base64 + hex de cada bloque).

### 5.2 Estructura del payload
```
⋋^  +  B64(gzip(bloque0))  ;  B64(gzip(bloque1))  ;  B64(gzip(bloque2))
```

| Elemento | Detalle |
|----------|---------|
| **Prefijo** | `⋋^` = `U+22CB` (⋋) + `U+005E` (^). **Constante** en las 5 muestras. Anteponer literal. |
| **Separador** | `;` entre segmentos base64 |
| **Codificación de c/bloque** | bytes crudos → **gzip** → **base64**. (`H4sI` al inicio de cada segmento = magic gzip `1f 8b 08` en base64) |
| **Cifrado / firma** | **Ninguno detectado.** El payload (100–116 chars) se explica entero con prefijo + 3 blobs gzip; no sobra espacio para HMAC/firma |

### 5.3 Bloque 0 — bitmap "tengo / falta"
- **123 bytes = 984 bits ≈ 980 láminas** (+4 bits de padding).
- **Polaridad: bit `1` = falta · bit `0` = tengo.**
- Álbum vacío → casi todo `0xFF`. Marcar lámina como tengo → su bit pasa a `0`.
- **Indexación observada:** MSB-first dentro de cada byte. Bit global = `byte*8 + (posición desde el MSB)`.

### 5.4 Bloque 1 — bitmap "repetidas"
- Mismo tamaño (123 B) e **misma indexación** que bloque 0.
- bit `1` = la lámina tiene repetida.
- **Verificado:** en `QR_3_repe`, la lámina de la repetida prendió el bit **928** tanto en bloque0 (tengo=0) como en bloque1 (repe=1). Misma posición → mismo esquema de bits.

### 5.5 Bloque 2 — cantidad de repetidas (por confirmar)
- Aparece **solo cuando hay repetidas**. En `QR_3_repe` = **1 byte = `0x03`**. En las otras 4 muestras: vacío (0 bytes).
- Hipótesis: lista de cantidades para las láminas flaggeadas en bloque1 (en orden). Valor `0x03` con 1 repetida → confirmar semántica con una muestra de cantidad conocida.

### 5.6 Bits estructurales constantes (en álbum vacío)
En `QR_0_vacio`, bloque0 NO es 100% `0xFF`:
- byte **2** = `11101111` → bit en 0 global **19**
- byte **122** = `00001111` → bits en 0 globales **976, 977, 978, 979**

Estos 5 bits están en `0` incluso en álbum vacío → **estructurales** (padding/reservados, no láminas marcadas). Se replican verbatim. Bloque1 vacío = todo `0x00`.

### 5.7 Análisis de las marcas controladas (diffs de bloque0 vs vacío)

| QR | láminas marcadas | byte cambiado | binario vacío→nuevo | bit global nuevo |
|----|:----------------:|:-------------:|---------------------|:----------------:|
| `QR_1_una` | 1 (código **PENDIENTE**) | 120 | `11111111`→`11111110` | **967** |
| `QR_2_dos` | 2 (códigos **PENDIENTE**) | 119, 120 | `…→11110111`, `…→11111110` | **956**, 967 |
| `QR_3_repe` | 2 tengo + 1 repe (**PENDIENTE**) | 116, 119, 120 | `…→01111111`, … | **928**, 956, 967 |

Bloque1 cambió solo en `QR_3_repe`: byte 116 = `10000000` (bit **928**). Bloque2 = `0x03`.

**Observación clave:** los bits marcados (967, 956, 928) están cerca del final del rango y NO son consecutivos → el orden del bitmap no es trivialmente el orden que Claude asume. Por eso falta el ground truth (sección 7).

### 5.8 Datos crudos de referencia (de `qr_muestras_raw.json`)

Payload completo del QR vacío (baseline):
```
⋋^H4sIAAAAAAAAA/v/Hw...   (3 segmentos gzip — ver qr_muestras_raw.json para el string exacto y el hex de cada bloque)
```
Longitudes de payload: original=116 · vacío=100 · una=104 · dos=108 · repe=116 chars.
Tamaños de bloques: `[123, 123, 0]` (sin repe) / `[123, 123, 1]` (con repe).

---

## 6. Decode reproducible (Python)
```python
import cv2, base64, gzip
det = cv2.QRCodeDetector()
ok, dec, _, _ = det.detectAndDecodeMulti(cv2.imread('qr.jpeg'))
s = next(x for x in dec if x)                 # payload string completo
prefix = s[:s.find('H4sI')]                   # '⋋^'
body = s[s.find('H4sI'):]
blocks = [gzip.decompress(base64.b64decode(p+'='*(-len(p)%4)))
          for p in body.split(';') if p.strip()]
# blocks[0] = bitmap tengo (1=falta,0=tengo) | blocks[1] = bitmap repetidas | blocks[2] = counts repe
```

---

## 7. Lo que falta para cerrar el generador

> ✅ **Puntos 1 y 4 RESUELTOS 2026-06-16** (ver sección "Resolución del mapeo" arriba): mapeo descifrado vía export de México completo (no hicieron falta los 3 códigos) + import real verificado (595). **Pendiente solo:** punto 2 (semántica bloque 2 = repetidas, para v2) y punto 3 (confirmar especiales 1-a-1, opcional — el conteo ya calza).

1. **Mapeo bit ↔ código (bloqueante).** Necesito los **3 códigos** que Boris marcó:
   - `QR_1_una` → ¿qué lámina? · `QR_2_dos` → ¿cuál fue la 2ª? · `QR_3_repe` → ¿cuál marcó como repe?
   Con esos 3 anclajes + el orden de `registro_maestro.csv` se deduce la función bit↔código. Si no alcanza, marcar 1-2 láminas puntuales que Claude indique.
2. **Confirmar semántica de bloque 2** (cantidad de repetidas) con una muestra de cantidad conocida (ej. marcar 2 repes de una lámina).
3. **Confirmar** que el QR de "Exportar álbum" (device-to-device) = mismo formato que el de canje (probable).
4. **Verificar import real:** generar un QR de prueba con 2-3 láminas y cargarlo con "Desde la galería" para confirmar que la app lo acepta (descarta validación oculta).

### Plan del generador (una vez mapeado)
`registro_maestro.csv` → construir bitmap tengo (bloque0, 1=falta/0=tengo) + bitmap repetidas (bloque1) + counts (bloque2) → gzip cada bloque → base64 → unir con `;` → anteponer `⋋^` → renderizar QR (lib `qrcode`) → importar "Desde la galería".

---

## 8. Inventario de archivos de esta investigación

| Archivo | Contenido |
|---------|-----------|
| `FIGURITAS_APP_INVESTIGACION.md` | **Este doc** — maestro, entry point |
| `DR_FIGURITAS_IMPORT_BORRADOR.md` | Borrador del prompt DR (pre-Leonor) |
| `DR_FIGURITAS_IMPORT_LEONOR.md` | Prompt optimizado por Leonor (lanzado) |
| `DR_FIGURITAS_IMPORT_RESULTADO_2026-06-15.md` | Reporte del Deep Research |
| `DR_FIGURITAS_QR_FORMATO.md` | Spec técnica del formato del QR |
| `qr_muestras_raw.json` | Raw completo de los 5 QR (payload + base64 + hex bloques) |
| `qr_muestras/` | Las 5 imágenes QR fuente + 3 screenshots (pantalla importar, ficha Play Store) |

---

## 9. Riesgo / decisión

- **Riesgo técnico bajo:** formato abierto (gzip+base64+bitmap), sin cifrado/firma. El único riesgo residual es una validación oculta al importar (se descarta con la prueba 7.4).
- **Decisión de fondo (Boris):** el sistema CSV propio ya es superior para *medir y optimizar*. Migrar a Figuritas tiene sentido **solo** por su matching automático de canjes con la comunidad. Si eso aporta, el generador lo hace en 1 export.

*Última actualización: 2026-06-15.*
