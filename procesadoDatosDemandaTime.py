import json
import datetime
import pandas as pd


def procesar_datos_time():
    """
    Devuelve los datos del archivo de demandas en un DataFrame.
    El archivo tiene que ser.json
    Los índices son datetime y las columnas son timedelta
    """

    def cambiafecha(fecha):
        fecha = fecha[:16]
        fecha = fecha.replace("-", " ")
        fecha = fecha.replace("T", " ")
        fecha_final = datetime.datetime.strptime(fecha, "%Y %m %d %H:%M")
        return fecha_final

    def sacarhora(fecha):
        fecha = fecha[11:16]
        fecha_final = datetime.datetime.strptime(fecha, "%H:%M")
        return fecha

    def sacardia(fecha):
        fecha = fecha[8:10]
        fecha_final = datetime.datetime.strptime(fecha, "%d")
        return fecha

    def sacarmes(fecha):
        fecha = fecha[5:7]
        fecha_final = datetime.datetime.strptime(fecha, "%m")
        return fecha

    def sacaranyo(fecha):
        fecha = fecha[0:4]
        fecha_final = datetime.datetime.strptime(fecha, "%Y")
        return fecha

    lista_value = []
    lista_datetime = []
    lista_hora = []
    lista_dia = []
    lista_mes = []
    lista_anyo = []
    diccionario = {}

    values = pd.read_json(str(input("Archivo donde están los datos de la demanda (sin extensión): ")) + ".json")
    datos = pd.DataFrame({})

    for dic in values["values"]:
        fecha = dic["datetime"]
        fecha_real = sacaranyo(fecha) + sacarmes(fecha) + sacardia(fecha)
        fecha_real = datetime.datetime.strptime(fecha_real, "%Y%m%d")
        hora = sacarhora(fecha)
        if hora == "00:00":
            diccionario.update({fecha_real: {}})
        else:
            diccionario.update({fecha_real: diccionario[fecha_anterior]})
        h, m = map(int, hora.split(':'))
        # hora = datetime.timedelta(hours=h, minutes=m)
        diccionario[fecha_real].update({hora: dic["value"]})
        fecha_anterior = fecha_real

    datos = pd.DataFrame(diccionario).transpose()

    lista = list(datos.columns)
    horas = [x for x in range(0, 24)]
    lista_indices = [x for x in range(0, 139, 6)]
    n = 0
    columna = pd.DataFrame()

    for i in lista_indices:
        columna = pd.concat([columna, pd.DataFrame(datos.iloc[:, i:i + 6].mean(axis=1))], axis=1)

    for i in horas:
        for j in range(10, 60, 10):
            lista.remove(str(i).zfill(2) + ":" + str(j))

    lista2 = []

    for i in lista:
        h, m = map(int, i.split(':'))
        lista2.append(datetime.timedelta(hours=h, minutes=m))

    columna.columns = lista2

    # To eliminate days that lacks hours:
    m = columna.mean(axis=1)
    for i, col in enumerate(columna):
        # using i allows for duplicate columns
        # inplace *may* not always work here, so IMO the next line is preferred
        # df.iloc[:, i].fillna(m, inplace=True)
        columna.iloc[:, i] = columna.iloc[:, i].fillna(m)

    return columna


if __name__ == "__main__":
    procesar_datos_time()
