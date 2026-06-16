# Formato del QR de Figuritas Mundial 2026 (reverse-engineered)

<!-- Decodificado empíricamente 2026-06-15 desde 4 QR controlados (vacío / 1 / 2 / repetida) exportados por Boris. App com.majurfest.figuritas. Decode con OpenCV QRCodeDetector. -->

## Veredicto
**SÍ — factible generar un QR importable desde el CSV.** El payload es `gzip + base64 + bitmaps`, sin cifrado ni firma detectada. Contra-hipótesis (server-token / cifrado) **refutada empíricamente**.

## Estructura
```
<prefijo> + B64(gzip(bloque0)) ; B64(gzip(bloque1)) ; B64(gzip(bloque2))
```
- **Prefijo:** `⋋^` (U+22CB + `^`), constante. Anteponer literal.
- **Separador:** `;` entre bloques base64.
- Cada bloque: gzip → base64. (`H4sI` = magic gzip 1f 8b 08 en base64.)

### Bloque 0 — bitmap "tengo" / faltantes
- 123 bytes = 984 bits ≈ 980 láminas (+4 padding).
- **Polaridad: bit `1` = falta, bit `0` = tengo.**
- Álbum vacío → casi todo `0xFF`. Marcar lámina tengo → su bit a `0`.
- Indexación observada: MSB-first dentro de cada byte; bit global = byte*8 + (posición desde MSB).

### Bloque 1 — bitmap "repetidas"
- Mismo tamaño e indexación que bloque 0.
- bit `1` = la lámina tiene ≥1 repetida. Misma posición de bit que en bloque0.
- Verificado: QR repetida prendió bit 928 en bloque0 (tengo) **y** bloque1 (repe).

### Bloque 2 — cantidad de repetidas (por confirmar)
- Aparece solo cuando hay repetidas. En el QR con 1 repetida = `0x03` (1 byte).
- Hipótesis: lista de cantidades para las láminas flaggeadas en bloque1, en orden. Confirmar con muestra de cantidad conocida.

### Bits estructurales constantes (en álbum vacío)
- byte 2 bit 3 (global 19) = 0
- byte 122 bits 0-3 (global 976-979) = 0
- Resto = `1` (bloque0) / `0` (bloque1). Replicar verbatim.

## Muestras controladas (2026-06-15)
| QR | láminas marcadas | bit(s) nuevos bloque0 | bloque1 | bloque2 |
|----|------------------|----------------------|---------|---------|
| vacío | 0 | — | 0 | vacío |
| solo 1 | 1 (código PENDIENTE) | 967 | 0 | vacío |
| solo 2 | 2 (códigos PENDIENTE) | 967, 956 | 0 | vacío |
| repetida | 2 tengo + 1 repe (PENDIENTE) | 967, 956, 928 | bit 928 | `0x03` |

## Pendiente para cerrar el generador
1. **Mapeo bit ↔ código:** conocer qué códigos marcó Boris en cada QR (3 anclajes) → deducir el orden del bitmap vs `registro_maestro.csv`.
2. Confirmar semántica de bloque 2 (cantidad de repetidas).
3. Verificar que el QR de "Exportar álbum" (device-to-device) usa este mismo formato que el QR de canje (probable, no confirmado).

## Plan generador (una vez mapeado)
`registro_maestro.csv` → bitmap tengo (bloque0) + bitmap repe (bloque1) + counts (bloque2) → gzip cada uno → base64 → unir con `;` → anteponer `⋋^` → renderizar QR (qrcode) → importar "Desde la galería".

## Decode (reproducible)
```python
import cv2, base64, gzip
det = cv2.QRCodeDetector()
ok, dec, _, _ = det.detectAndDecodeMulti(cv2.imread('qr.jpeg'))
s = next(x for x in dec if x)
body = s[s.find('H4sI'):]
blocks = [gzip.decompress(base64.b64decode(p+'='*(-len(p)%4))) for p in body.split(';') if p.strip()]
```
