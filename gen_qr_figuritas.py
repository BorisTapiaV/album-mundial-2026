#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_qr_figuritas.py — genera el QR de "Importar album" de la app Figuritas
(com.majurfest.figuritas) desde registro_maestro.csv.

Formato del payload (reverse-engineered, ver FIGURITAS_APP_INVESTIGACION.md):
    '⋋^' + B64(gzip(bloque0)) ';' B64(gzip(bloque1)) ';' B64(gzip(bloque2))

Bloques: 123 bytes = 984 bits, LSB-first dentro de cada byte.
  bloque0 = bitmap tengo/falta  (bit 1 = falta, bit 0 = tengo)
  bloque1 = bitmap repetidas    (bit 1 = la lamina tiene repetida)   [v2]
  bloque2 = cantidades de repe  (semantica por confirmar)            [v2]

Mapeo bit <-> codigo (PROBADO byte-a-byte contra export real de Mexico):
  especiales (00, FWC1..FWC19): bits 0..19   (hipotesis: 00->0, FWCk->k)
  lamina de equipo: bit = 20 * orden_album + (slot - 1)
    (equipo 1 = Mexico -> bits 20..39 ; equipo 48 = Panama -> bits 960..979)
  padding: bits 980..983

v1: solo tengo/falta (bloque1 todo 0, bloque2 vacio) = formato identico a
    los QR sin repetidas exportados por la app.
"""
import csv, gzip, base64, sys

REG = "registro_maestro.csv"
NBYTES = 123
PREFIX = "⋋^"        # ⋋^
TENGO = {"tengo", "pegada"}   # HAVE; 'falta' y 'perdida' = NO tengo
PADDING_BITS = (980, 981, 982, 983)


def bit_of(r):
    oa = r["orden_album"].strip()
    if oa == "0":                       # especiales: 00->0, FWC1..19 -> 1..19
        b = int(r["slot"])              #             (bits 0-19, antes de Mexico)
    elif oa.isdigit():                  # lamina de equipo
        b = 20 * int(oa) + (int(r["slot"]) - 1)
    else:
        return None
    assert 0 <= b <= 979, f"bit fuera de rango para {r['codigo']}: {b}"
    return b


def clear_bit(buf, b):          # poner 0 (tengo) — LSB-first
    buf[b // 8] &= ~(1 << (b % 8))


def set_bit(buf, b):            # poner 1
    buf[b // 8] |= (1 << (b % 8))


def build_payload(rows, only_orden_album=None, with_repes=False):
    b0 = bytearray(b"\xff" * NBYTES)   # todo falta
    b1 = bytearray(b"\x00" * NBYTES)   # ninguna repe
    counts = []
    for r in rows:
        if only_orden_album is not None and r["orden_album"].strip() != str(only_orden_album):
            continue
        b = bit_of(r)
        if b is None:
            continue
        if r["estado"] in TENGO:
            clear_bit(b0, b)
        if with_repes:
            n = int(r["repetidas"] or 0)
            if n >= 1:
                set_bit(b1, b)
                counts.append(n)
    for b in PADDING_BITS:
        clear_bit(b0, b)
    blocks = [bytes(b0), bytes(b1), bytes(bytearray(counts)) if with_repes else b""]
    segs = [base64.b64encode(gzip.compress(blk, mtime=0)).decode() for blk in blocks]
    return PREFIX + ";".join(segs)


def render(payload, path):
    import qrcode
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=2)
    qr.add_data(payload)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(path)
    return path


def main():
    rows = list(csv.DictReader(open(REG, encoding="utf-8")))
    tengo = sum(1 for r in rows if r["estado"] in TENGO)

    # QR de prueba: solo Mexico (equipo 1) — replica el bitmap ya probado
    p_test = build_payload(rows, only_orden_album=1)
    render(p_test, "QR_FIGURITAS_test_mexico.png")
    print(f"OK -> QR_FIGURITAS_test_mexico.png (solo Mexico, {len(p_test)} chars)")

    # QR real completo: todas las tengo
    p_full = build_payload(rows)
    render(p_full, "QR_FIGURITAS_full.png")
    print(f"OK -> QR_FIGURITAS_full.png ({tengo} tengo, {len(p_full)} chars)")


if __name__ == "__main__":
    main()
