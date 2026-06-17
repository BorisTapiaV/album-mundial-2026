#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_faltantes_txt.py — listas de faltantes en TEXTO desde registro_maestro.csv.

Genera:
  FALTANTES_<FECHA>.txt   detalle por equipo (orden del album), codigo + nombre.
  FALTANTES_WHATSAPP.txt  formato compacto para pegar en WhatsApp (bandera + codigos).

Me faltan = estado 'falta' o 'perdida'. Orden detalle = orden del album.
"""
import csv

REG = "registro_maestro.csv"
FECHA = "2026-06-17"

FLAGS = {
 "FWC Especiales":"\U0001F30E","Mexico":"\U0001F1F2\U0001F1FD","Sudafrica":"\U0001F1FF\U0001F1E6",
 "Corea del Sur":"\U0001F1F0\U0001F1F7","Chequia":"\U0001F1E8\U0001F1FF","Canada":"\U0001F1E8\U0001F1E6",
 "Bosnia y Herzegovina":"\U0001F1E7\U0001F1E6","Catar":"\U0001F1F6\U0001F1E6","Suiza":"\U0001F1E8\U0001F1ED",
 "Brasil":"\U0001F1E7\U0001F1F7","Marruecos":"\U0001F1F2\U0001F1E6","Haiti":"\U0001F1ED\U0001F1F9",
 "Escocia":"\U0001F3F4","Estados Unidos":"\U0001F1FA\U0001F1F8","Paraguay":"\U0001F1F5\U0001F1FE",
 "Australia":"\U0001F1E6\U0001F1FA","Turquia":"\U0001F1F9\U0001F1F7","Alemania":"\U0001F1E9\U0001F1EA",
 "Curazao":"\U0001F1E8\U0001F1FC","Costa de Marfil":"\U0001F1E8\U0001F1EE","Ecuador":"\U0001F1EA\U0001F1E8",
 "Paises Bajos":"\U0001F1F3\U0001F1F1","Japon":"\U0001F1EF\U0001F1F5","Suecia":"\U0001F1F8\U0001F1EA",
 "Tunez":"\U0001F1F9\U0001F1F3","Belgica":"\U0001F1E7\U0001F1EA","Egipto":"\U0001F1EA\U0001F1EC",
 "Iran":"\U0001F1EE\U0001F1F7","Nueva Zelanda":"\U0001F1F3\U0001F1FF","Espana":"\U0001F1EA\U0001F1F8",
 "Cabo Verde":"\U0001F1E8\U0001F1FB","Arabia Saudita":"\U0001F1F8\U0001F1E6","Uruguay":"\U0001F1FA\U0001F1FE",
 "Francia":"\U0001F1EB\U0001F1F7","Senegal":"\U0001F1F8\U0001F1F3","Irak":"\U0001F1EE\U0001F1F6",
 "Noruega":"\U0001F1F3\U0001F1F4","Argentina":"\U0001F1E6\U0001F1F7","Argelia":"\U0001F1E9\U0001F1FF",
 "Austria":"\U0001F1E6\U0001F1F9","Jordania":"\U0001F1EF\U0001F1F4","Portugal":"\U0001F1F5\U0001F1F9",
 "RD Congo":"\U0001F1E8\U0001F1E9","Uzbekistan":"\U0001F1FA\U0001F1FF","Colombia":"\U0001F1E8\U0001F1F4",
 "Inglaterra":"\U0001F3F4","Croacia":"\U0001F1ED\U0001F1F7","Ghana":"\U0001F1EC\U0001F1ED",
 "Panama":"\U0001F1F5\U0001F1E6",
}
NICE = {
 "FWC Especiales":"Especiales","Mexico":"México","Sudafrica":"Sudáfrica","Canada":"Canadá",
 "Bosnia y Herzegovina":"Bosnia","Haiti":"Haití","Turquia":"Turquía","Japon":"Japón",
 "Tunez":"Túnez","Belgica":"Bélgica","Iran":"Irán","Espana":"España",
 "Paises Bajos":"Países Bajos","Panama":"Panamá",
}


def load():
    with open(REG, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def team_order_groups(miss):
    miss.sort(key=lambda r: (int(r["orden_album"] or 999), int(r["slot"] or 0)))
    order = []
    for r in miss:
        if r["equipo"] not in order:
            order.append(r["equipo"])
    return [(eq, [r for r in miss if r["equipo"] == eq]) for eq in order]


def page_label(rows_all, equipo):
    pags = sorted({int(r["pagina"]) for r in rows_all
                   if r["equipo"] == equipo and (r.get("pagina") or "").strip().lstrip("-").isdigit()})
    if not pags:
        return ""
    if equipo == "FWC Especiales":
        return "especiales"
    return f"{pags[0]}-{pags[-1]}" if pags[0] != pags[-1] else str(pags[0])


def main():
    rows = load()
    miss = [r for r in rows if r["estado"] in ("falta", "perdida")]
    n_falta = sum(1 for r in miss if r["estado"] == "falta")
    n_perd = sum(1 for r in miss if r["estado"] == "perdida")
    total = len(miss)
    groups = team_order_groups(list(miss))

    # ---- detalle ----
    out = []
    out.append("FALTANTES — Álbum Panini FIFA World Cup 2026 (edición Chile)")
    out.append(f"Generado: {FECHA} · Boris Tapia")
    out.append(f"Total faltan: {total}/980  (falta={n_falta} · perdida={n_perd})")
    out.append("=" * 60)
    out.append("")
    for eq, rs in groups:
        pag = page_label(rows, eq)
        nice = NICE.get(eq, eq)
        out.append(f"## {nice}  (pág {pag}) — faltan {len(rs)}")
        for r in rs:
            tag = "  [PERDIDA]" if r["estado"] == "perdida" else ""
            out.append(f"  {r['codigo']:<7} {r['jugador_tipo'] or '—'}{tag}")
        out.append("")
    open(f"FALTANTES_{FECHA}.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
    print(f"OK -> FALTANTES_{FECHA}.txt  ({total} faltantes)")

    # ---- whatsapp (alfabetico por nombre nice, Especiales primero) ----
    wa = [f"FIGURITAS QUE ME FALTAN ⚽ Mundial 2026 ({total})", ""]
    gmap = {eq: [r["codigo"] for r in rs] for eq, rs in groups}
    def sortkey(eq):
        return ("" if eq == "FWC Especiales" else NICE.get(eq, eq).lower())
    for eq in sorted(gmap, key=sortkey):
        nice = NICE.get(eq, eq)
        codes = ", ".join(gmap[eq])
        wa.append(f"{FLAGS.get(eq,'')} {nice} ({len(gmap[eq])}): {codes}")
    open("FALTANTES_WHATSAPP.txt", "w", encoding="utf-8").write("\n".join(wa) + "\n")
    print(f"OK -> FALTANTES_WHATSAPP.txt  ({total} faltantes)")


if __name__ == "__main__":
    main()
