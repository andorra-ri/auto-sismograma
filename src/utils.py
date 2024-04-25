from datetime import datetime


def put_copyright(station, time=str(datetime.now().year)):
    """dfdd"""
    if station == 'PAND':
        text_station = "Pic de Padern (PAND). Dades: OMP."

    elif station == 'SCOL':
        text_station = "Santa Coloma (SCOL). Dades: ICGC."

    else:
        text_station = "La Rabassa (ARBS). Dades: ICGC."

    text =  "{} Autor: AR+I©. Tots els drets reservats. ".format(text_station) + time
    return text
