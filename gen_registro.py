#!/usr/bin/env python3
"""
gen_registro.py — genera el registro maestro de las 980 laminas del album
Panini FIFA World Cup 2026 como CSV listo para importar a Google Sheets.

NUMERACION (verificada 2026-06-03, fuentes: diamondcardsonline + checklistinsider
+ cartophilic-info-exch + laststicker; varias coinciden slot-por-slot):
  Cada lamina trae impreso un CODIGO:
    - 00            : logo Panini (foil)
    - FWC1..FWC19   : 19 especiales foil (emblema 1/2 y 2/2, mascota, eslogan, balon,
                      3 anfitriones, 11 FIFA Museum 1934-2022)
    - <PAIS>1..20   : 48 selecciones x 20 (slot 1 = escudo foil, slot 13 = foto
                      equipo, el resto = 18 jugadores)
  Total = 1 + 19 + 960 = 980.  Cristiano Ronaldo = POR15.
  Set Coca-Cola (~12) = promo APARTE, fuera de las 980.

DATOS: los nombres viven en names.csv (codigo,jugador_tipo). Este script los lee,
calcula tier, y PRESERVA estado/repetidas del registro_maestro.csv existente (para
no borrar lo ya inventariado). El codigo IMPRESO en las laminas reales manda.

Confianza: nombres con 'med'/transliteracion incierta (UZB, JOR, KOR, arabes) ->
el slot es firme, la grafia puede variar. Rosters preliminares (album impreso
antes del sorteo/convocatorias finales).

Uso:  python gen_registro.py
Salida: registro_maestro.csv
"""
import csv
import os

OUT = "registro_maestro.csv"
NAMES = "names.csv"
BIO = "bio.csv"
# estado=col F, repetidas=col G (sin cambios); bio appended al final.
# orden_album/pagina/fecha_estado se agregaron despues y se PRESERVAN (no los genera
# este script) para no perderlos al regenerar.
HEADER = ["codigo", "equipo", "slot", "jugador_tipo", "tier", "estado", "repetidas",
          "notas", "posicion", "club", "nacimiento", "altura", "peso", "conf_bio",
          "orden_album", "pagina", "fecha_estado"]
# columnas preservadas desde el registro existente (ademas de estado/repetidas).
PRESERVE = ["orden_album", "pagina", "fecha_estado"]

# 48 selecciones — (codigo, nombre). Orden alfabetico por nombre ES (verificar vs album).
TEAMS = [
    ("ALG", "Argelia"), ("ARG", "Argentina"), ("AUS", "Australia"), ("AUT", "Austria"),
    ("BEL", "Belgica"), ("BIH", "Bosnia y Herzegovina"), ("BRA", "Brasil"), ("CAN", "Canada"),
    ("CPV", "Cabo Verde"), ("COL", "Colombia"), ("COD", "RD Congo"), ("CRO", "Croacia"),
    ("CUW", "Curazao"), ("CZE", "Chequia"), ("ECU", "Ecuador"), ("EGY", "Egipto"),
    ("ENG", "Inglaterra"), ("FRA", "Francia"), ("GER", "Alemania"), ("GHA", "Ghana"),
    ("HAI", "Haiti"), ("IRN", "Iran"), ("IRQ", "Irak"), ("CIV", "Costa de Marfil"),
    ("JPN", "Japon"), ("JOR", "Jordania"), ("MEX", "Mexico"), ("MAR", "Marruecos"),
    ("NED", "Paises Bajos"), ("NZL", "Nueva Zelanda"), ("NOR", "Noruega"), ("PAN", "Panama"),
    ("PAR", "Paraguay"), ("POR", "Portugal"), ("QAT", "Catar"), ("KSA", "Arabia Saudita"),
    ("SCO", "Escocia"), ("SEN", "Senegal"), ("RSA", "Sudafrica"), ("KOR", "Corea del Sur"),
    ("ESP", "Espana"), ("SWE", "Suecia"), ("SUI", "Suiza"), ("TUN", "Tunez"),
    ("TUR", "Turquia"), ("URU", "Uruguay"), ("USA", "Estados Unidos"), ("UZB", "Uzbekistan"),
]

# Estrellas de alta demanda -> tier T3 (mejor moneda de canje / valor).
STARS = {
    "POR15",  # Cristiano Ronaldo (objetivo)
    "ARG17",  # Messi
    "FRA20",  # Mbappe
    "NOR15",  # Haaland
    "ENG11",  # Bellingham
    "ENG18",  # Kane
    "BRA14",  # Vinicius Jr
    "ESP15",  # Lamine Yamal
    "EGY17",  # Salah
    "KOR18",  # Son Heung-min
    "NED3",   # van Dijk
    "GER15",  # Musiala
}


def load_names():
    d = {}
    if os.path.exists(NAMES):
        with open(NAMES, newline="", encoding="utf-8") as f:
            for row in csv.reader(f):
                if not row or row[0] == "codigo":
                    continue
                d[row[0]] = row[1] if len(row) > 1 else ""
    return d


def load_bio():
    """code -> (posicion, club, nacimiento, altura, peso, confianza)."""
    d = {}
    if os.path.exists(BIO):
        with open(BIO, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                d[r["codigo"]] = (r.get("posicion", ""), r.get("club", ""),
                                  r.get("nacimiento", ""), r.get("altura", ""),
                                  r.get("peso", ""), r.get("confianza", ""))
    return d


def load_state():
    """Preserva estado/repetidas + columnas PRESERVE (orden_album/pagina/fecha_estado)."""
    d = {}
    if os.path.exists(OUT):
        with open(OUT, newline="", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                d[row["codigo"]] = (row.get("estado", "falta"), row.get("repetidas", "0"),
                                    {k: row.get(k, "") for k in PRESERVE})
    return d


def tier_for(code, slot):
    if code in STARS:
        return "T3"
    if slot == 1:
        return "T2"  # escudo foil
    if code == "00" or code.startswith("FWC"):
        return "T2"  # especial foil
    return "base"


def notas_for(code, slot):
    if code == "POR15":
        return "objetivo del album"
    if code == "00" or code.startswith("FWC"):
        return "foil"
    if slot == 1:
        return "escudo foil"
    return ""


def main():
    names = load_names()
    state = load_state()
    bio = load_bio()

    def row(code, equipo, slot, default_jt):
        jt = names.get(code, default_jt)
        est, rep, extra = state.get(code, ("falta", "0", {k: "" for k in PRESERVE}))
        pos, club, nac, alt, peso, conf = bio.get(code, ("", "", "", "", "", ""))
        return [code, equipo, slot, jt, tier_for(code, slot), est, rep,
                notas_for(code, slot), pos, club, nac, alt, peso, conf,
                *(extra.get(k, "") for k in PRESERVE)]

    rows = [row("00", "Panini", 0, "Logo Panini (foil)")]
    for n in range(1, 20):
        rows.append(row(f"FWC{n}", "FWC Especiales", n, ""))
    for code, name in TEAMS:
        for slot in range(1, 21):
            if slot == 1:
                default = "Escudo (foil)"
            elif slot == 13:
                default = "Foto equipo"
            else:
                default = ""
            rows.append(row(f"{code}{slot}", name, slot, default))

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(HEADER)
        w.writerows(rows)

    tengo = sum(1 for r in rows if r[5] == "tengo")
    named = sum(1 for r in rows if r[3])
    print(f"OK -> {OUT} ({len(rows)} laminas, {named} con nombre, {tengo} en 'tengo')")


if __name__ == "__main__":
    main()
