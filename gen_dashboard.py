#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_dashboard.py — tarjeta de progreso PARA COMPARTIR (estilo app Figuritas),
generada desde registro_maestro.csv. Abrir dashboard_share.html en el navegador
y tomar captura (o Ctrl+P -> PDF) para compartir por WhatsApp.

Campos (mismo set que la tarjeta azul de Figuritas):
  Completado %  ·  Total  ·  Me faltan  ·  Tengo  ·  Repetidas  ·  Brillantes X/68

Brillantes = laminas foil: 48 escudos (slot 1) + logo 00 + 19 especiales FWC = 68.
Me faltan = Total - Tengo (incluye las 'perdida', porque fisicamente no las tienes).
"""
import csv

REG = "registro_maestro.csv"
OUT = "dashboard_share.html"
HAVE = {"tengo", "pegada", "repetida"}
COLECCION = "USA MÉX CAN 26"
FECHA = "2026-06-17"


def is_brillante(r):
    return r["slot"] == "1" or r["codigo"] == "00" or r["codigo"].startswith("FWC")


def compute():
    with open(REG, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    total = len(rows)
    tengo = sum(1 for r in rows if r["estado"] in HAVE)
    faltan = total - tengo
    repetidas = sum(int(r["repetidas"]) for r in rows if r["repetidas"] not in ("", "0"))
    brt = sum(1 for r in rows if is_brillante(r))
    brh = sum(1 for r in rows if is_brillante(r) and r["estado"] in HAVE)
    pct = round(tengo / total * 100)
    return dict(total=total, tengo=tengo, faltan=faltan, repetidas=repetidas,
                brillantes=f"{brh}/{brt}", pct=pct)


# Iconos SVG (trazo blanco) dentro del circulo azul
IC_CARDS = '<rect x="7" y="7" width="11" height="14" rx="2"/><path d="M11 3h9a1 1 0 0 1 1 1v13"/>'
IC_CHECK = '<rect x="6" y="6" width="13" height="16" rx="2"/><path d="M9 14l2.5 2.5L16 11"/>'
IC_X = '<rect x="6" y="6" width="13" height="16" rx="2"/><path d="M10 11l5 5M15 11l-5 5"/>'
IC_SWAP = '<rect x="6" y="6" width="13" height="16" rx="2"/><path d="M9.5 12.5l2-2 2 2M14.5 15.5l-2 2-2-2"/>'
IC_STAR = '<circle cx="13" cy="13" r="8"/><path d="M9.5 13l2.5 2.5L17 10"/>'

TILES_ORDER = [
    ("Completado", "{pct}%", IC_CHECK),
    ("Total", "{total}", IC_CARDS),
    ("Me faltan", "{faltan}", IC_X),
    ("Tengo", "{tengo}", IC_CHECK),
    ("Repetidas", "{repetidas}", IC_SWAP),
    ("Brillantes", "{brillantes}", IC_STAR),
]


def render(d):
    def circle(svg):
        return (f'<span class="circ"><svg viewBox="0 0 26 28" fill="none" stroke="#fff" '
                f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round">{svg}</svg></span>')
    tiles = []
    for label, valfmt, svg in TILES_ORDER:
        val = valfmt.format(**d)
        tiles.append(
            f'<div class="tile">{circle(svg)}'
            f'<div class="txt"><div class="lbl">{label}</div><div class="val">{val}</div></div></div>')
    grid = "".join(tiles)
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Mi album — {COLECCION}</title>
<style>
  * {{ box-sizing:border-box; margin:0; padding:0; }}
  html,body {{ background:#2f54d9; overflow:hidden; }}
  body {{ font-family:'Segoe UI',Arial,Helvetica,sans-serif; -webkit-print-color-adjust:exact; print-color-adjust:exact; }}
  .card-wrap {{ width:440px; margin:0 auto; padding:34px 26px 26px; background:#2f54d9; }}
  .brand {{ display:flex; align-items:center; justify-content:center; gap:12px; margin-bottom:18px; }}
  .brand .logo {{ width:46px; height:46px; border-radius:11px; background:linear-gradient(135deg,#5b78ec 60%,#f4922e 60%); box-shadow:0 2px 6px rgba(0,0,0,.18); }}
  .brand .word {{ color:#fff; font-size:30px; font-weight:800; letter-spacing:.5px; }}
  .pill {{ display:block; width:max-content; margin:0 auto 26px; padding:9px 26px; background:rgba(255,255,255,.16); color:#fff; font-weight:700; font-size:18px; letter-spacing:1px; border-radius:22px; }}
  .panel {{ background:#fff; border:3px solid #f6ad3c; border-radius:26px; padding:30px 26px; box-shadow:0 8px 22px rgba(0,0,0,.18); }}
  .grid {{ display:grid; grid-template-columns:1fr 1fr; row-gap:34px; column-gap:14px; }}
  .tile {{ display:flex; align-items:center; gap:14px; }}
  .circ {{ flex:0 0 auto; width:54px; height:54px; border-radius:50%; background:#2f6fe6; display:flex; align-items:center; justify-content:center; }}
  .circ svg {{ width:26px; height:28px; }}
  .txt .lbl {{ font-size:18px; font-weight:700; color:#1c1c1c; line-height:1.1; }}
  .txt .val {{ font-size:30px; font-weight:800; color:#111; line-height:1.15; }}
  .foot {{ text-align:center; color:rgba(255,255,255,.85); font-size:12.5px; margin-top:22px; white-space:nowrap; }}
  .foot b {{ color:#fff; }}
  @media print {{ .card-wrap {{ padding-top:20px; }} }}
</style></head><body>
<div class="card-wrap">
  <div class="brand"><span class="logo"></span><span class="word">MUNDIAL 2026</span></div>
  <span class="pill">{COLECCION}</span>
  <div class="panel"><div class="grid">{grid}</div></div>
</div></body></html>"""


def main():
    d = compute()
    with open(OUT, "w", encoding="utf-8") as f:
        f.write(render(d))
    print(f"OK -> {OUT}")
    for k in ("pct", "total", "faltan", "tengo", "repetidas", "brillantes"):
        print(f"  {k:11}: {d[k]}")


if __name__ == "__main__":
    main()
