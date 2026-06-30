#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
reservadas.py — fuente canonica de RESERVADAS ENTRANTES.

Una reservada entrante = lamina comprometida en un canje/compra PENDIENTE,
todavia NO en mano. El registro_maestro.csv sigue marcandola 'falta'/'perdida'
(regla: no se escribe 'pegada' hasta tenerla fisicamente, por si el trato cae).

PERO para CUALQUIER cruce o lista de faltantes que se use con OTRA persona, se
trata como "ya la tengo" -> asi no se vuelve a pedir/comprar la misma lamina a
un tercero mientras el trato pendiente esta abierto.

USO:
  from reservadas import load_reservadas_entrantes
  reserv = load_reservadas_entrantes()          # set de codigos, p.ej. {"ARG10", ...}
  faltan = [r for r in rows
            if r["estado"] in ("falta","perdida") and r["codigo"] not in reserv]

AL CERRAR el trato (laminas en mano):
  1) registro: falta/perdida -> pegada (gen normal de ingreso de lote)
  2) borrar esas filas de RESERVADAS_ENTRANTES.csv
  3) regenerar artefactos + QR
"""
import csv
import os

ARCH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "RESERVADAS_ENTRANTES.csv")


def load_reservadas_entrantes():
    """Set de codigos reservados entrantes (vacio si no existe el archivo)."""
    if not os.path.exists(ARCH):
        return set()
    with open(ARCH, newline="", encoding="utf-8") as f:
        return {r["codigo"].strip() for r in csv.DictReader(f) if r.get("codigo", "").strip()}


def load_reservadas_detalle():
    """Lista de dicts (codigo, persona, fecha, nota) para inspeccion/reportes."""
    if not os.path.exists(ARCH):
        return []
    with open(ARCH, newline="", encoding="utf-8") as f:
        return [r for r in csv.DictReader(f) if r.get("codigo", "").strip()]


if __name__ == "__main__":
    det = load_reservadas_detalle()
    print(f"RESERVADAS ENTRANTES: {len(det)} codigos")
    for r in det:
        print(f"  {r['codigo']:<7} {r.get('persona',''):<12} {r.get('nota','')}")
