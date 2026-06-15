# Repetidas por país — mazo de canje

**Generado 2026-06-14.** Estado álbum 564/980. Lista de repetidas (`repetidas>0` en el
registro) **agrupada por país en orden del álbum**, para armar el mazo de canje en el mismo
orden en que se abren las páginas — así no hay que revisar las 200+ cada vez que se busca una.

- Fuente: `registro_maestro.csv` → generador `gen_print.py` → `repetidas_por_pais.html` (con buscador).
- **Excluye 14 reservadas a canje** (no van en el mazo libre): las 13 de Andrés Acosta
  (CZE18, HAI5, HAI9, HAI14, GER1, TUN6, BEL8, JOR6, JOR17, COD1, COL1, CRO1, GHA18) + **AUT15**
  (dada a Jorge Vásquez). Definidas en `RESERVADAS` dentro de `gen_print.py` — **punto-en-el-tiempo:**
  vaciar/editar cuando se cierren los canjes.
- `xN` = copias de ese código. Sin `xN` = 1 copia repetida.

**Total tras exclusiones: 175 códigos / 208 cartas.**

| País | Códigos |
|------|---------|
| Especiales | `00`, FWC10, FWC12, FWC13, FWC15, FWC18, FWC19 |
| México | MEX3 |
| Sudáfrica | RSA4, RSA5 x2, RSA6, RSA10, RSA11, RSA16 x2, RSA19 x2, RSA20 x2 |
| Corea del Sur | KOR16, KOR20 |
| Chequia | CZE5 x2, CZE7, CZE9 x3, CZE14 |
| Bosnia | BIH5, BIH8, BIH9 x4, BIH12, BIH14 x4 |
| Catar | QAT6, QAT8, QAT13 |
| Suiza | SUI3, SUI5, SUI7, SUI8 x2, SUI12 x2, SUI13, SUI16, SUI17 |
| Brasil | BRA8 |
| Haití | HAI3, HAI7, HAI11, HAI16 x2, HAI18 x2 |
| Escocia | SCO2, SCO13 x2, SCO14 |
| Estados Unidos | USA16, USA17, USA18 |
| Paraguay | PAR1, PAR6, PAR13 |
| Australia | AUS1, AUS6, AUS10 x3, AUS12, AUS15 x2, AUS19 x2, AUS20 |
| Turquía | TUR1, TUR5, TUR14, TUR15, TUR18, TUR19 |
| Alemania | GER5, GER14, GER20 |
| Curazao | CUW5, CUW6, CUW7, CUW9, CUW10, CUW16, CUW18, CUW19 |
| Costa de Marfil | CIV6 |
| Ecuador | ECU3, ECU16 |
| Países Bajos | NED2, NED5, NED6, NED9 x2, NED10, NED11, NED14, NED15 x2 |
| Suecia | SWE3, SWE4, SWE5, SWE7, SWE17 |
| Túnez | TUN2, TUN10 x2, TUN15, TUN18 |
| Bélgica | BEL9, BEL10, BEL15, BEL16, BEL19 |
| Egipto | EGY5 x2, EGY9, EGY11, EGY18, EGY20 x2 |
| Irán | IRN3, IRN7, IRN11, IRN14, IRN16, IRN18, IRN19 x2, IRN20 |
| Nueva Zelanda | NZL4, NZL8 x2, NZL12, NZL17 |
| España | ESP4, ESP8 |
| Cabo Verde | CPV10, CPV15 |
| Arabia Saudita | KSA5, KSA9, KSA13 x2 |
| Uruguay | URU5, URU8 x2, URU14, URU16, URU17, URU20 |
| Francia | FRA19 |
| Senegal | SEN11, SEN18 |
| Irak | IRQ4, IRQ9, IRQ15, IRQ19, IRQ20 |
| Noruega | NOR19 |
| Argentina | ARG2, ARG6, ARG13 |
| Argelia | ALG1 x2, ALG12, ALG17 |
| Austria | AUT2, AUT4 |
| Jordania | JOR5, JOR9, JOR11, JOR14, JOR18 |
| RD Congo | COD3, COD7, COD13, COD16 |
| Uzbekistán | UZB1 x2, UZB2, UZB6, UZB10, UZB13, UZB15 |
| Inglaterra | ENG2, ENG20 |
| Croacia | CRO2, CRO6 |
| Ghana | GHA1, GHA5, GHA9, GHA13, GHA14, GHA20 |
| Panamá | PAN13 |

---

## Buscador en las hojas HTML

Todas las hojas imprimibles (`gen_print.py`) llevan ahora un **buscador en vivo** arriba:
se escribe un código (`URU8`) o un nombre (`Messi`) y la lista se filtra al instante —
ignora acentos y mayúsculas, oculta los países sin coincidencias, y muestra el conteo de
resultados. Es solo para pantalla (teléfono/navegador): **no se imprime**. Funciona offline
(JavaScript embebido). Botón "limpiar" para resetear.

Hojas con buscador: `checklist_por_equipo`, `lista_intercambio`, `indice_alfabetico`,
`repetidas_por_pais`, `faltantes`, `repetidas`, `perdidas`.

*Regenerar todo: `python gen_print.py --todo`.*
