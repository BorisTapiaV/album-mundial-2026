#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gen_print.py — genera hojas de seguimiento IMPRIMIBLES (HTML) del album
Panini FIFA World Cup 2026, desde registro_maestro.csv.

Uso:  python gen_print.py            -> genera las 2 hojas principales
      python gen_print.py --todo     -> ademas faltantes.html + repetidas.html

Abrir el .html en el navegador -> Ctrl+P -> imprimir o "Guardar como PDF".

Hojas:
  1) checklist_por_equipo.html  HOJA PRIMARIA para marcar a mano. Ordenada como el
     album (00, FWC, 48 selecciones). Cada linea: [casilla] CODIGO  Nombre (estrellas ⭐).
     Las laminas que ya tienes (estado tengo/pegada) salen con la casilla rellena.
  2) lista_intercambio.html     Lista plana (formato faltantes) de TODAS las laminas,
     SIN paginas. Las que ya tengo salen atenuadas; las que faltan resaltan; xN = repetidas.
     Para el intercambio de laminas: de un vistazo ves que te falta y que te sobra.
  3) indice_alfabetico.html     Busqueda por NOMBRE -> codigo. Para canje: muchos
     aficionados dicen "tienes a Messi?" en vez de "tienes ARG17?".
  3) faltantes.html (--todo)    Solo lo que falta (lista de caza; util cerca del cierre).
  4) repetidas.html (--todo)    Repetidas>0 (moneda de canje 1:1).

El codigo IMPRESO en cada lamina manda; los nombres son guia (rosters preliminares).
"""
import csv
import os
import sys

REG = "registro_maestro.csv"
HAVE = {"tengo", "pegada", "repetida"}
# 'perdida' = la adquiri pero esta fisicamente extraviada -> NO cuenta como tener,
# pero SI aparece en faltantes (la necesito para cerrar). Se etiqueta aparte.
LOST = {"perdida"}

CSS = """
@page { size: A4; margin: 9mm; }
* { box-sizing: border-box; }
html { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
body { font-family: Arial, Helvetica, sans-serif; font-size: 8.4pt; color:#111; margin:0; }
h1 { font-size: 15pt; margin: 0 0 1mm; }
.sub { font-size: 8pt; color:#555; margin:0 0 3mm; }
.legend { font-size: 7.5pt; color:#444; margin:0 0 4mm; }
.cols3 { column-count: 3; column-gap: 6mm; }
.cols4 { column-count: 4; column-gap: 5mm; }
.team { break-inside: avoid; margin-bottom: 2.5mm; }
.team h2 { font-size: 9.5pt; margin: 0 0 0.8mm; padding:0 0 0.6mm; border-bottom:1.3px solid #111; }
.team h2 .cnt { float:right; font-size:7.5pt; font-weight:normal; color:#777; }
.team h2 .pag { font-size:7.5pt; font-weight:normal; color:#1565c0; margin-left:1.5mm; }
.pg { font-size:6.8pt; color:#1565c0; flex:0 0 auto; }
.row { display:flex; align-items:center; gap:1.4mm; padding:0.25mm 0; line-height:1.2; }
.box { display:inline-block; width:3.1mm; height:3.1mm; border:1px solid #333; flex:0 0 auto; border-radius:0.5mm; text-align:center; line-height:2.9mm; font-size:2.9mm; font-weight:bold; color:#111; }
.box.on { border:1.3px solid #111; }
.box.on::after { content:"\\2713"; }
.code { font-weight:bold; width:13mm; flex:0 0 auto; }
.nm { flex:1 1 auto; overflow:hidden; text-overflow:ellipsis; white-space:nowrap; }
.team2 { font-size:7pt; color:#888; flex:0 0 auto; }
.star { color:#b8860b; font-weight:bold; }
.lost { color:#b00020; font-size:6.8pt; font-weight:bold; border:1px solid #b00020; border-radius:1mm; padding:0 0.6mm; }
.have .nm { color:#666; }
/* Intercambio: las que faltan se ven IGUAL que en faltantes; solo las que tengo se atenuan */
.dim .row.have { opacity:0.32; }
@media print { .noprint { display:none; } }
.noprint { background:#fffbe6; border:1px solid #e8d97a; padding:2mm 3mm; font-size:8pt; margin-bottom:4mm; }
/* Buscador (solo pantalla): filtra .row por codigo o nombre en vivo */
.search { position:sticky; top:0; z-index:5; display:flex; gap:2mm; align-items:center;
          background:#eef6ff; border:1px solid #b3d4fc; border-radius:1.5mm; padding:2mm 3mm; margin-bottom:3mm; }
.search input { flex:1 1 auto; font-size:12pt; padding:1.6mm 2.2mm; border:1px solid #888; border-radius:1mm; }
.search button { font-size:9pt; padding:1.6mm 3mm; cursor:pointer; border:1px solid #888; border-radius:1mm; background:#fff; }
#cnt { font-size:8.5pt; color:#1565c0; white-space:nowrap; min-width:18mm; }
@media print { .search { display:none; } }
"""

LEGEND = ('<div class="legend">Casilla &#9744; = marca a mano lo que pegas. '
          'Casilla con &#10003; = ya registrado (lo tienes). '
          '&#11088; = estrella (mejor moneda de canje). '
          'El <b>codigo impreso en la lamina manda</b>.</div>')

PRINT_HINT = ('<div class="noprint">Abre este archivo en el navegador y pulsa '
              '<b>Ctrl+P</b> para imprimir o guardar como PDF. Esta caja no se imprime.</div>')

SEARCH_BAR = ('<div class="search noprint">'
              '<input id="q" type="search" autocomplete="off" '
              'placeholder="Buscar codigo o nombre (ej: URU8, Messi)...">'
              '<button id="clr" type="button">limpiar</button>'
              '<span id="cnt"></span></div>')

# Filtra .row por texto (codigo o nombre), ignora acentos/mayusculas, y oculta los
# encabezados .team que queden sin filas visibles. Funciona offline.
SEARCH_JS = """<script>
(function(){
  var q=document.getElementById('q'),clr=document.getElementById('clr'),cnt=document.getElementById('cnt');
  if(!q)return;
  function norm(s){return s.normalize('NFD').replace(/[\\u0300-\\u036f]/g,'').toLowerCase();}
  var data=[].slice.call(document.querySelectorAll('.row')).map(function(r){return {el:r,t:norm(r.textContent)};});
  var teams=[].slice.call(document.querySelectorAll('.team'));
  function apply(){
    var v=norm(q.value.trim()),shown=0;
    data.forEach(function(d){var ok=!v||d.t.indexOf(v)>=0;d.el.style.display=ok?'':'none';if(ok)shown++;});
    teams.forEach(function(t){
      var any=[].slice.call(t.querySelectorAll('.row')).some(function(r){return r.style.display!=='none';});
      t.style.display=any?'':'none';});
    cnt.textContent=v?(shown+' resultado'+(shown===1?'':'s')):'';
  }
  q.addEventListener('input',apply);
  clr.addEventListener('click',function(){q.value='';apply();q.focus();});
})();
</script>"""


def load():
    with open(REG, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def box(have):
    return '<span class="box on"></span>' if have else '<span class="box"></span>'


def page(title, sub, body, cols_class):
    return f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><style>{CSS}</style></head><body>
<h1>{esc(title)}</h1><div class="sub">{esc(sub)}</div>{PRINT_HINT}{SEARCH_BAR}{LEGEND}
<div class="{cols_class}">{body}</div>{SEARCH_JS}</body></html>"""


def code_abbr(codigo):
    # prefijo de pais (letras antes del primer digito); "00"/"FWC" -> tal cual
    i = 0
    while i < len(codigo) and not codigo[i].isdigit():
        i += 1
    return codigo[:i] or codigo


def checklist_por_equipo(rows, title="Album Mundial 2026 — Checklist por equipo",
                         sub="980 laminas. Marca lo que pegas. Sin marcar = te falta.",
                         cols_class="cols3"):
    blocks, cur, cur_team = [], [], None
    for r in rows:
        if r["equipo"] != cur_team:
            if cur:
                blocks.append((cur_team, cur))
            cur, cur_team = [], r["equipo"]
        cur.append(r)
    if cur:
        blocks.append((cur_team, cur))

    html = []
    for team, rs in blocks:
        have = sum(1 for r in rs if r["estado"] in HAVE)
        pag = (rs[0].get("pagina") or "").strip()
        pag_html = f'<span class="pag">pag {esc(pag)}</span>' if pag else ""
        lines = [f'<div class="team"><h2>{esc(team)}{pag_html}<span class="cnt">{have}/{len(rs)}</span></h2>']
        for r in rs:
            h = r["estado"] in HAVE
            star = ' <span class="star">&#11088;</span>' if r["tier"] == "T3" else ""
            cls = "row have" if h else "row"
            lines.append(
                f'<div class="{cls}">{box(h)}'
                f'<span class="code">{esc(r["codigo"])}</span>'
                f'<span class="nm">{esc(r["jugador_tipo"]) or "&mdash;"}{star}</span></div>'
            )
        lines.append("</div>")
        html.append("".join(lines))
    return page(title, sub, "".join(html), cols_class)


def is_player(r):
    return (r["codigo"] != "00" and not r["codigo"].startswith("FWC")
            and r["slot"] not in ("1", "13") and r["jugador_tipo"])


def surname_key(name):
    return name.split()[-1].lower() if name else "zzz"


def indice_alfabetico(rows):
    players = [r for r in rows if is_player(r)]
    players.sort(key=lambda r: (surname_key(r["jugador_tipo"]), r["jugador_tipo"].lower()))
    lines = []
    for r in players:
        h = r["estado"] in HAVE
        star = ' <span class="star">&#11088;</span>' if r["tier"] == "T3" else ""
        cls = "row have" if h else "row"
        lines.append(
            f'<div class="{cls}">{box(h)}'
            f'<span class="nm">{esc(r["jugador_tipo"])}{star}</span>'
            f'<span class="team2">{esc(code_abbr(r["codigo"]))}</span>'
            f'<span class="code">{esc(r["codigo"])}</span></div>'
        )
    return page(
        "Album Mundial 2026 — Indice alfabetico (nombre -> codigo)",
        "Para canje: busca al jugador por apellido y obten su codigo de album.",
        "".join(lines), "cols4",
    )


def filtered_por_equipo(rows, keep, title, sub, fname):
    sub_rows = [r for r in rows if keep(r)]
    # reusar el layout por equipo
    return checklist_por_equipo(sub_rows) if False else _simple_list(sub_rows, title, sub)


def _simple_list(rows, title, sub):
    lines = []
    for r in rows:
        rep = r.get("repetidas", "0")
        extra = f' <span class="team2">x{rep}</span>' if rep not in ("0", "") else ""
        star = ' <span class="star">&#11088;</span>' if r["tier"] == "T3" else ""
        pag = (r.get("pagina") or "").strip()
        pag_html = f'<span class="pg">pag {esc(pag)}</span>' if pag else ""
        lost = ""
        if r["estado"] in LOST:
            fch = (r.get("fecha_estado") or "").strip()
            lost = f' <span class="lost">perdida{(" " + esc(fch)) if fch else ""}</span>'
        lines.append(
            f'<div class="row">{box(False)}'
            f'<span class="code">{esc(r["codigo"])}</span>'
            f'<span class="nm">{esc(r["jugador_tipo"]) or "&mdash;"}{star}{extra}{lost}</span>'
            f'<span class="team2">{esc(r["equipo"])}</span>{pag_html}</div>'
        )
    return page(title, sub, "".join(lines), "cols3")


def lista_intercambio(rows):
    """Lista plana (formato faltantes) de TODAS las laminas, CON columna de pagina.
    Las que ya tengo salen atenuadas y con check; las que faltan resaltan. Para canje."""
    lines = []
    for r in rows:
        h = r["estado"] in HAVE
        rep = r.get("repetidas", "0")
        extra = f' <span class="team2">x{rep}</span>' if rep not in ("0", "") else ""
        star = ' <span class="star">&#11088;</span>' if r["tier"] == "T3" else ""
        pag = (r.get("pagina") or "").strip()
        pag_html = f'<span class="pg">pag {esc(pag)}</span>' if pag else ""
        cls = "row have" if h else "row"
        lines.append(
            f'<div class="{cls}">{box(h)}'
            f'<span class="code">{esc(r["codigo"])}</span>'
            f'<span class="nm">{esc(r["jugador_tipo"]) or "&mdash;"}{star}{extra}</span>'
            f'<span class="team2">{esc(r["equipo"])}</span>{pag_html}</div>'
        )
    return page(
        "Album Mundial 2026 — Lista de intercambio",
        "Todas las laminas (orden alfabetico por equipo). Atenuadas con check = ya las tengo. "
        "Resaltadas = me faltan. xN = repetidas (moneda de canje). pag = pagina del album.",
        "".join(lines), "cols3 dim")


# Codigos YA comprometidos a canje (no van en el mazo de canje libre).
# Punto-en-el-tiempo: vaciar/editar cuando se cierren los canjes.
#   2026-06-16: canjes Andres (13) + Jorge (AUT15) CERRADOS -> sin reservas activas.
#   2026-06-18: 12 apartadas para Sobrina Catalina (canje abierto) -> vaciar al cerrar.
RESERVADAS = {"USA18","AUS12","IRN16","IRN17","IRN18","IRN20","CPV12","FRA19","ARG2","AUT2","UZB1","UZB6"}


def _oa(r):
    try:
        return int(r.get("orden_album") or 999)
    except ValueError:
        return 999


def repetidas_por_pais(rows):
    """Repetidas (repetidas>0) agrupadas POR PAIS en orden del album, para ordenar
    el mazo de canje en el mismo orden en que se abren las paginas. Excluye RESERVADAS."""
    rep = [r for r in rows
           if r.get("repetidas", "0") not in ("0", "") and r["codigo"] not in RESERVADAS]
    rep.sort(key=lambda r: (_oa(r), int(r["slot"]) if r["slot"].isdigit() else 0))
    # agrupar por equipo preservando el orden ya aplicado
    blocks, cur, cur_team = [], [], None
    for r in rep:
        if r["equipo"] != cur_team:
            if cur:
                blocks.append((cur_team, cur))
            cur, cur_team = [], r["equipo"]
        cur.append(r)
    if cur:
        blocks.append((cur_team, cur))

    n_codes = len(rep)
    n_cards = sum(int(r["repetidas"]) for r in rep)
    html = []
    for team, rs in blocks:
        cards = sum(int(r["repetidas"]) for r in rs)
        pag = (rs[0].get("pagina") or "").strip()
        pag_html = f'<span class="pag">pag {esc(pag)}</span>' if pag else ""
        lines = [f'<div class="team"><h2>{esc(team)}{pag_html}'
                 f'<span class="cnt">{len(rs)} cod / {cards} cartas</span></h2>']
        for r in rs:
            n = int(r["repetidas"])
            extra = f' <span class="team2">x{n}</span>' if n > 1 else ""
            star = ' <span class="star">&#11088;</span>' if r["tier"] == "T3" else ""
            lines.append(
                f'<div class="row">'
                f'<span class="code">{esc(r["codigo"])}</span>'
                f'<span class="nm">{esc(r["jugador_tipo"]) or "&mdash;"}{star}{extra}</span></div>'
            )
        lines.append("</div>")
        html.append("".join(lines))
    return page(
        "Album Mundial 2026 — Repetidas por pais (mazo de canje)",
        f"{n_codes} codigos / {n_cards} cartas, en orden del album. "
        f"Excluye {len(RESERVADAS)} reservadas a canje (Andres + Jorge). "
        "xN = copias de ese codigo. Usa el buscador para hallar un codigo al toque.",
        "".join(html), "cols4")


def write(fname, html):
    with open(fname, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"OK -> {fname}")


def main():
    rows = load()
    write("checklist_por_equipo.html", checklist_por_equipo(rows))
    write("lista_intercambio.html", lista_intercambio(rows))
    write("indice_alfabetico.html", indice_alfabetico(rows))
    write("repetidas_por_pais.html", repetidas_por_pais(rows))
    if "--todo" in sys.argv:
        # faltantes = lo que falta + lo perdido (ambos hay que conseguirlos para cerrar)
        falt = [r for r in rows if r["estado"] in ("falta",) or r["estado"] in LOST]
        rep = [r for r in rows if r.get("repetidas", "0") not in ("0", "")]
        lost = [r for r in rows if r["estado"] in LOST]
        n_falt = sum(1 for r in falt if r["estado"] == "falta")
        write("faltantes.html", _simple_list(
            falt, "Album Mundial 2026 — Faltantes",
            f"{n_falt} faltan + {len(lost)} perdidas = {len(falt)} por conseguir. "
            "Las perdidas (rojo) ya las tuviste pero estan extraviadas."))
        write("repetidas.html", _simple_list(
            rep, "Album Mundial 2026 — Repetidas (canje)",
            f"{len(rep)} codigos con repetidas. Moneda de canje 1:1."))
        write("perdidas.html", _simple_list(
            lost, "Album Mundial 2026 — Perdidas (extraviadas en casa)",
            f"{len(lost)} laminas adquiridas pero fisicamente extraviadas. "
            "Costo hundido; reaparecen o se recompran. NO cuentan como tener."))
    have = sum(1 for r in rows if r["estado"] in HAVE)
    lost = sum(1 for r in rows if r["estado"] in LOST)
    print(f"Estado: {have}/{len(rows)} en HAVE (tengo/pegada/repetida) | perdidas: {lost}")


if __name__ == "__main__":
    main()
