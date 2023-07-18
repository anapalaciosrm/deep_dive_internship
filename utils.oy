"""This program creates the urls needed to run seccionE.py
"""
degrees = {
    "ACTUARÍA": "000031",
    "ADMINISTRACIÓN": "000032",
    "ADMINISTRACIÓN DE EMPRESAS": "000070",
    "ADMINISTRACIÓN DE NEGOCIOS": "000440",
    "CIENCIA DE DATOS": "001352",
    "CIENCIA POLÍTICA": "000055",
    "CIENCIAS SOCIALES": "000035",
    "CONTADOR PUBLICO Y AUDITOR": "000395",
    "CONTADOR PÚBLICO": "001113",
    "CONTADURÍA PÚBLICA": "000170",
    "CONTADURÍA PÚBLICA Y ESTRATEGIA FINANCIERA": "000626",
    "DERECHO": "000036",
    "DIRECCIÓN FINANCIERA": "001053",
    "ECONOMÍA": "000038",
    "INGENIERÍA EN COMPUTACIÓN": "000009",
    "INGENIERÍA EN MECATRÓNICA": "000935",
    "INGENIERÍA EN NEGOCIOS": "000890",
    "INGENIERÍA EN TELEMÁTICA": "000314",
    "INGENIERÍA INDUSTRIAL": "000011",
    "MATEMÁTICAS APLICADAS": "000169",
    "RELACIONES INTERNACIONALES": "000047",
}
prog_url = "titulacion/titulados.asp?prog="
main_url = "http://escolar1.rhon.itam.mx/"
main_page = f"{main_url}titulacion/programas.asp"


def get_url(degree: str = None, prog: int = None):
    return f"{main_url}{prog_url}{str(prog) if prog else degrees[degree]}"

