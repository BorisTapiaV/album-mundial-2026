# DR Resultado — ¿Cargar mi CSV a Figuritas vía QR? (2026-06-15)

<!-- DR Claude (101 agentes, 18 fuentes, 51 claims → 21 confirmados / 4 refutados). Prompt: DR_FIGURITAS_IMPORT_LEONOR.md (optimizado Leonor). -->

## 🎯 VEREDICTO: SÍ-CON-TRABAJO (reverse-engineering manual)

Factibilidad **muy probable pero no demostrada empíricamente**. La app NO depende de servidor para el cruce → el QR **lleva los datos de inventario** (no un token de backend). Eso significa que, en principio, un QR generado externamente desde tu CSV debería poder importarse. PERO nadie ha decodificado el payload públicamente, y hay un riesgo real de validación/firma que podría bloquearlo. No hay ruta oficial ni herramienta de terceros: el único camino es decodificar un QR real tú mismo.

---

## Hallazgos clave

| Hallazgo | Fuente | Certeza | Implicación |
|---|---|:--:|---|
| Package = `com.majurfest.figuritas`, dev Matias Jurfest (uruguayo) | Play Store + LinkedIn dev + prensa | 5 | App correcta identificada; APK accesible para RE |
| App **100% offline**: solo internet la 1ª vez (baja estructura del álbum); **sin login, sin nube** | La Nación + La Nueva + Play Store | 4-5 | El inventario vive en el dispositivo → el QR transporta datos |
| "Cada usuario tiene un QR con su colección"; el match faltantes-vs-repetidas es **local, sin servidor** | La Nación + La Gaceta + App Store | 4 | **Refuta la contra-hipótesis** (no es token server-bound) → el QR codifica estado por lámina |
| Existe feature "Import and Export an album" (changelog v4.5.x, may-2026) | App Store changelog | 5 | El flujo export→QR→import es real, device-to-device |
| "Desde la galería" = subir **imagen de QR**, NO un CSV. **No hay import CSV oficial** | App Store + figuritas.app | 4 | Camino oficial directo desde CSV = **[NO ENCONTRADO]** |
| **NO** existe herramienta de terceros ni RE público que genere un QR compatible | GitHub/Reddit/foros sin resultados | 3 | Hay que decodificar el QR uno mismo |
| Formato exacto del payload (serialización/compresión/firma) | — | — | **[DATA GAP]** — requiere exportar y decodificar un QR real |

## Qué codifica el QR
**Inferencia arquitectónica triangulada (no teardown byte-a-byte):** como la app es offline, sin nube y sin login, y el cruce de canje ocurre localmente al escanear el QR de otro, el QR **debe** transportar el estado de inventario por lámina (faltantes/repetidas, posiblemente las 980). NO es un token que apunte a un servidor. **Lo que NO se sabe:** la serialización (JSON / protobuf / binario), si está comprimido (gzip), si lleva firma/HMAC anti-manipulación, y si codifica las 980 láminas o solo el subconjunto repetidas/faltantes.

## ⚠️ 2 incógnitas que deciden todo (open questions)
1. **¿El QR de "Importar álbum" (device-to-device) usa el mismo formato que el QR de canje (peer matching)?** Podrían ser esquemas distintos.
2. **¿La app valida criptográficamente el QR importado (firma/checksum)?** Si sí → un QR generado externamente sería rechazado y el camino queda **bloqueado**. Si acepta cualquier QR bien formado → viable.

## Caminos para cargar el CSV

| Camino | Viable | Esfuerzo | Riesgo |
|--------|:------:|:--------:|--------|
| **Oficial (import CSV)** | ❌ No existe | — | — |
| **Tercero (herramienta lista)** | ❌ No existe | — | — |
| **Reverse-engineering manual** | ✅ Único viable | Medio-alto | La app valide/firme el payload → bloqueo |

### RE manual — pasos
1. Marcar unas láminas en la app y **exportar un QR real** desde tu dispositivo.
2. **Decodificar el QR** (lector QR / Python `pyzbar`) → ver el payload crudo.
3. **Mapear el esquema** (qué campo = qué lámina/estado) — idealmente exportando 2 QR con distinto inventario y comparando el diff.
4. Re-codificar tu CSV (980 láminas) en ese formato → generar un QR.
5. Importarlo "Desde la galería".

## 🟢 Próximo paso barato (spike de ~15 min, decide la inversión)
Antes de meterse al RE completo: **exportar 1 QR de la app y decodificarlo**. En minutos sabes si el payload es:
- **Texto legible / Base64 / JSON** → muy buena señal, RE factible.
- **Binario opaco o claramente cifrado/firmado** → probable bloqueo, no vale la pena.

Aún mejor: exportar **dos** QR (uno con X láminas marcadas, otro con X+2) y comparar — el diff revela el esquema directo.

---
*Fuentes principales: Play Store (com.majurfest.figuritas), figuritas.app, La Nación (2026-05-05), La Nueva, La Gaceta, App Store changelog. Caveat: la naturaleza "el QR lleva los datos" es inferencia desde arquitectura offline, no decodificación directa.*
