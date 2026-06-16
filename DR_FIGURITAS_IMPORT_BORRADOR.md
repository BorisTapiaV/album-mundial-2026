# DR Borrador — Importar inventario propio a "Figuritas Mundial 2026 Album" vía QR

## ROLE
Eres un analista senior de **portabilidad de datos en apps móviles** y **reverse-engineering de formatos de import/export** (QR, deep links, archivos), especializado en apps de colección de cromos/figuritas. Tu principio rector: una afirmación sin fuente verificable no es un hallazgo, es ruido. Prefiero un mapa parcial trazable sobre un mapa completo inventado.

## CONTEXTO
- **App objetivo:** "Figuritas Mundial 2026 Album", Android. Desarrollador **Matias Jurfest**. Versión 4.5.2, actualizada 8-jun-2026, +1.000.000 descargas, requiere Android 8.1+. Compras in-app $1.100–$11.400 CLP.
- **Álbum dentro de la app:** "Usa Méx Can 26" (FIFA World Cup 2026).
- **Función "Importar álbum"** (texto literal en la app): *"Importa un álbum escaneando o adjuntando un código QR exportado de otro dispositivo."* Dos opciones: (a) "Escanear con la cámara", (b) "Desde la galería". Implica que la app **exporta** un QR que codifica el estado del álbum de un dispositivo para **importarlo** en otro.
- **Situación del usuario:** ya tiene su inventario completo en un CSV propio (980 láminas con estado `tengo`/`falta`/`repetida` por código, ej. POR15, NED10). Quiere cargar ese estado a la app SIN tipear las 980 láminas a mano.

## OBJETIVO
Determinar si es **factible cargar el inventario propio (desde un CSV) a la app Figuritas usando el QR de importación**, y de serlo, **cómo**. El núcleo técnico: ¿qué codifica el QR que la app exporta, y se puede generar uno compatible programáticamente desde datos externos?

## HIPÓTESIS (falsable)
El QR de exportación es un payload que codifica `album_id` + estado por lámina; podría reproducirse si la comunidad lo documentó o aplicó reverse-engineering. **Contra-hipótesis:** el formato es opaco/cifrado o solo lleva un token/ID que requiere el backend del desarrollador → los datos no viajan en el QR y no es replicable sin la app.

## ESTRATEGIA DE INVESTIGACIÓN
PASO 0 — PLAN: genera primero las queries concretas por paso, luego ejecuta.
1. Identificar el **package name exacto** (Play Store) + presencia oficial del dev Matias Jurfest (sitio, redes, soporte, otras apps suyas).
2. Buscar **documentación oficial** de export/import (ayuda in-app, FAQ, descripción Play Store, videos/posts del dev).
3. Buscar **reverse-engineering o discusiones de comunidad**: GitHub, Reddit (r/panini, comunidades de cromos LATAM), foros, YouTube que muestren el flujo export→QR→import o describan el contenido del QR.
4. Determinar la **naturaleza del payload**: ¿el QR contiene los datos completos (funciona offline) o solo un ID/token que requiere servidor? (es la variable que decide la factibilidad).
5. Verificar si existe **import por archivo/CSV** ("Desde la galería" probablemente acepta una imagen de QR, no un CSV — confirmar).
6. Buscar **herramientas de terceros** que generen QR compatibles con esta app.
7. Si no hay nada público: describir el **camino de reverse-engineering manual** (capturar un QR export real del dispositivo, decodificarlo, mapear el esquema, re-codificar el CSV) con esfuerzo y riesgo estimados.

## RESTRICCIONES
- Fecha de corte: junio 2026.
- NO inventar formato del QR, package name ni features. Distinguir **[NO EXISTE]** (verificado que no hay) de **[NO ENCONTRADO]** (no se halló pero podría existir).
- Toda afirmación crítica (ej. "el QR lleva los datos completos offline") requiere **≥2 fuentes independientes**; si hay 1, marcar [1 FUENTE].
- El **silencio es dato**: si no hay docs ni reverse-engineering público, reportarlo explícito (señal de formato cerrado).
- Separar lo **verificado con URL** de lo **inferido**.

## FORMATO DE SALIDA
1. **Veredicto de factibilidad:** Sí / Sí-con-trabajo / No / Indeterminado + 1 párrafo.
2. Tabla: Hallazgo | Fuente (URL) | Certeza (1-5) | Implicación.
3. Sección "Qué codifica el QR" (si se determinó).
4. Sección "Caminos para cargar el CSV": oficial / tercero / reverse-engineering manual — con esfuerzo + riesgo cada uno.
5. Gaps pendientes y próximos pasos.

## FUENTES PRIORITARIAS
- Play Store listing + sección "Acerca de" / "Asistencia de la aplicación".
- Sitio web / redes del dev Matias Jurfest.
- GitHub (buscar package name + "QR" + "export").
- Reddit, foros de coleccionistas, grupos Facebook/WhatsApp de canje LATAM.
- YouTube (tutoriales del flujo importar/exportar).
