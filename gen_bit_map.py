#!/usr/bin/env python
"""Genera la tabla código <-> bit de Figuritas (com.majurfest.figuritas).

El "número" de una lámina en la app NO es su código impreso, sino su posición
de bit en el bitmap del QR:
  - especial  -> bit = slot         (00 = bit 0, FWC1..FWC19 = bits 1..19)
  - de equipo -> bit = 20*orden_album + (slot-1)   (orden_album 1..48, slot 1..20)

Lee registro_maestro.csv y escribe figuritas_bit_map.csv (ordenado por bit) +
figuritas_bit_map.md (referencia legible). Valida: 980 bits únicos, 0..979 sin
huecos ni colisiones.
"""
import csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass


def bit_de(codigo, slot, orden_album):
    if codigo == '00':
        return 0
    if codigo.startswith('FWC'):
        return int(codigo[3:])
    return 20 * int(orden_album) + (int(slot) - 1)


def main():
    rows = []
    with open(os.path.join(HERE, 'registro_maestro.csv'), encoding='utf-8') as f:
        for r in csv.DictReader(f):
            bit = bit_de(r['codigo'], r['slot'], r['orden_album'])
            rows.append({
                'bit': bit,
                'codigo': r['codigo'],
                'equipo': r['equipo'],
                'orden_album': r['orden_album'],
                'slot': r['slot'],
                'jugador_tipo': r['jugador_tipo'],
                'tier': r['tier'],
                'pagina': r['pagina'],
            })

    rows.sort(key=lambda x: x['bit'])

    # --- validación de integridad ---
    bits = [r['bit'] for r in rows]
    assert len(rows) == 980, f'esperaba 980 láminas, hay {len(rows)}'
    dups = {b for b in bits if bits.count(b) > 1}
    assert not dups, f'COLISIÓN de bits: {sorted(dups)}'
    rango = set(range(0, 980))
    usados = set(bits)
    faltan = sorted(rango - usados)
    extra = sorted(usados - rango)
    assert not faltan, f'bits 0-979 sin asignar: {faltan}'
    assert not extra, f'bits fuera de 0-979: {extra}'

    # --- CSV ---
    cols = ['bit', 'codigo', 'equipo', 'orden_album', 'slot', 'jugador_tipo', 'tier', 'pagina']
    with open(os.path.join(HERE, 'figuritas_bit_map.csv'), 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)

    # --- MD legible (agrupado por equipo) ---
    md = ['# Tabla código ↔ bit — Figuritas Mundial 2026',
          '',
          '> Posición de bit en el bitmap del QR de `com.majurfest.figuritas`.',
          '> `bit = 20·orden_album + (slot−1)` (equipo) · `bit = slot` (especial, 00 = bit 0).',
          '> Bloque 0: bit 0 = tengo, 1 = falta (LSB-first). 980 láminas → bits 0–979.',
          '',
          '| bit | código | equipo | slot | tipo | pág |',
          '|----:|--------|--------|:----:|------|-----|']
    for r in rows:
        md.append(f"| {r['bit']} | {r['codigo']} | {r['equipo']} | {r['slot']} | {r['jugador_tipo']} | {r['pagina']} |")
    with open(os.path.join(HERE, 'figuritas_bit_map.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(md) + '\n')

    print(f'OK -> figuritas_bit_map.csv ({len(rows)} filas)')
    print(f'OK -> figuritas_bit_map.md')
    print(f'Validación: 980 bits únicos, rango 0–979 completo, sin colisiones. ✓')
    print(f'  bit 0   = {rows[0]["codigo"]}')
    print(f'  bit 979 = {rows[-1]["codigo"]}')


if __name__ == '__main__':
    main()
