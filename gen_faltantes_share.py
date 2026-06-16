#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_faltantes_share.py — afiche(s) PARA COMPARTIR (WhatsApp) con las laminas que faltan,
agrupadas por pais. Mismo estilo que dashboard_share (azul + naranjo).

Genera:
  faltantes_share.html        -> afiche unico (4 columnas, compacto)
  faltantes_share_1.html / _2 -> partido en 2 (3 columnas, mas grande), balanceado por codigos.
Tomar captura o renderizar a PNG con Edge headless.

Me faltan = estado 'falta' o 'perdida'. Orden = orden del album (orden_album, luego slot).
"""
import csv

REG = "registro_maestro.csv"
FECHA = "2026-06-16"

FLAGS = {
 "FWC Especiales":"🌎","Mexico":"🇲🇽","Sudafrica":"🇿🇦","Corea del Sur":"🇰🇷","Chequia":"🇨🇿",
 "Canada":"🇨🇦","Bosnia y Herzegovina":"🇧🇦","Catar":"🇶🇦","Suiza":"🇨🇭","Brasil":"🇧🇷",
 "Marruecos":"🇲🇦","Haiti":"🇭🇹","Escocia":"🏴","Estados Unidos":"🇺🇸","Paraguay":"🇵🇾",
 "Australia":"🇦🇺","Turquia":"🇹🇷","Alemania":"🇩🇪","Curazao":"🇨🇼","Costa de Marfil":"🇨🇮",
 "Ecuador":"🇪🇨","Paises Bajos":"🇳🇱","Japon":"🇯🇵","Suecia":"🇸🇪","Tunez":"🇹🇳",
 "Belgica":"🇧🇪","Egipto":"🇪🇬","Iran":"🇮🇷","Nueva Zelanda":"🇳🇿","Espana":"🇪🇸",
 "Cabo Verde":"🇨🇻","Arabia Saudita":"🇸🇦","Uruguay":"🇺🇾","Francia":"🇫🇷","Senegal":"🇸🇳",
 "Irak":"🇮🇶","Noruega":"🇳🇴","Argentina":"🇦🇷","Argelia":"🇩🇿","Austria":"🇦🇹",
 "Jordania":"🇯🇴","Portugal":"🇵🇹","RD Congo":"🇨🇩","Uzbekistan":"🇺🇿","Colombia":"🇨🇴",
 "Inglaterra":"🏴","Croacia":"🇭🇷","Ghana":"🇬🇭","Panama":"🇵🇦",
}
NICE = {
 "FWC Especiales":"Especiales","Mexico":"México","Sudafrica":"Sudáfrica","Canada":"Canadá",
 "Bosnia y Herzegovina":"Bosnia","Haiti":"Haití","Turquia":"Turquía","Japon":"Japón",
 "Tunez":"Túnez","Belgica":"Bélgica","Iran":"Irán","Espana":"España","Francia":"Francia",
 "Paises Bajos":"Países Bajos","Panama":"Panamá",
}


def card_html(eq, codes):
    chips = "".join(f'<span class="chip">{c}</span>' for c in codes)
    name = NICE.get(eq, eq)
    return (f'<div class="card"><div class="hd">'
            f'<span class="fl">{FLAGS.get(eq,"")}</span>'
            f'<span class="nm">{name}</span><span class="ct">{len(codes)}</span></div>'
            f'<div class="chips">{chips}</div></div>')


def page(cards_html, total, cols, big, subtitle):
    f = 1.25 if big else 1.0
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Me faltan — Mundial 2026</title>
<style>
 *{{box-sizing:border-box;margin:0;padding:0}}
 html,body{{background:#2f54d9}}
 body{{font-family:'Segoe UI',Arial,Helvetica,sans-serif;-webkit-print-color-adjust:exact;print-color-adjust:exact}}
 .wrap{{width:1080px;margin:0 auto;padding:34px 28px 30px}}
 .head{{display:flex;align-items:center;justify-content:center;gap:14px;margin-bottom:6px}}
 .logo{{width:44px;height:44px;border-radius:11px;background:linear-gradient(135deg,#5b78ec 60%,#f4922e 60%);box-shadow:0 2px 6px rgba(0,0,0,.2)}}
 .title{{color:#fff;font-size:30px;font-weight:800;letter-spacing:.4px}}
 .sub{{text-align:center;color:#fff;font-size:18px;font-weight:700;margin:8px 0 22px}}
 .sub b{{background:#f6ad3c;color:#22305f;padding:3px 12px;border-radius:14px}}
 .grid{{column-count:{cols};column-gap:16px}}
 .card{{break-inside:avoid;background:#fff;border-radius:16px;border:2px solid #f6ad3c;
        padding:{int(11*f)}px {int(13*f)}px {int(13*f)}px;margin:0 0 16px;box-shadow:0 4px 12px rgba(0,0,0,.14)}}
 .hd{{display:flex;align-items:center;gap:8px;border-bottom:1.5px solid #eee;padding-bottom:7px;margin-bottom:9px}}
 .fl{{font-size:{int(21*f)}px;line-height:1}}
 .nm{{font-size:{int(16*f)}px;font-weight:800;color:#1c1c1c;flex:1;line-height:1.05}}
 .ct{{font-size:{int(14*f)}px;font-weight:800;color:#fff;background:#2f6fe6;border-radius:11px;padding:1px 10px}}
 .chips{{display:flex;flex-wrap:wrap;gap:6px}}
 .chip{{font-size:{int(14*f)}px;font-weight:700;color:#22305f;background:#eef2ff;border:1px solid #d6def9;
        border-radius:8px;padding:{int(3*f)}px {int(8*f)}px;letter-spacing:.2px}}
 .foot{{text-align:center;color:rgba(255,255,255,.9);font-size:13px;margin-top:14px}}
 .foot b{{color:#fff}}
</style></head><body>
<div class="wrap">
 <div class="head"><span class="logo"></span><span class="title">MUNDIAL 2026 — ME FALTAN</span></div>
 <div class="sub"><b>{total} láminas</b> &nbsp;·&nbsp; {subtitle}</div>
 <div class="grid">{cards_html}</div>
 <div class="foot">Para canje o compra · actualizado {FECHA} · <b>Boris</b></div>
</div></body></html>"""


def main():
    with open(REG, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    miss = [r for r in rows if r["estado"] in ("falta", "perdida")]
    miss.sort(key=lambda r: (int(r["orden_album"] or 999), int(r["slot"] or 0)))
    order = []
    for r in miss:
        if r["equipo"] not in order:
            order.append(r["equipo"])
    groups = [(eq, [r["codigo"] for r in miss if r["equipo"] == eq]) for eq in order]
    total = len(miss)

    # afiche unico (4 col)
    full = "".join(card_html(eq, cs) for eq, cs in groups)
    open("faltantes_share.html", "w", encoding="utf-8").write(
        page(full, total, 4, False, "USA · MÉX · CAN 26"))

    # partido en 2, balanceado por nº de codigos
    half = total / 2
    acc, cut = 0, len(groups)
    for i, (_, cs) in enumerate(groups):
        acc += len(cs)
        if acc >= half:
            cut = i + 1
            break
    parts = [groups[:cut], groups[cut:]]
    for n, part in enumerate(parts, 1):
        ph = "".join(card_html(eq, cs) for eq, cs in part)
        t = sum(len(cs) for _, cs in part)
        names = f"{NICE.get(part[0][0], part[0][0])} a {NICE.get(part[-1][0], part[-1][0])}"
        open(f"faltantes_share_{n}.html", "w", encoding="utf-8").write(
            page(ph, t, 3, True, f"Parte {n}/2 · {names}"))
        print(f"OK -> faltantes_share_{n}.html  ({t} faltantes, {len(part)} equipos: {names})")
    print(f"OK -> faltantes_share.html  ({total} faltantes, {len(groups)} equipos)")


if __name__ == "__main__":
    main()
