import datetime
import pandas as pd


def procesar_datos_time():
    """
    Devuelve los datos del archivo de precios en un DataFrame.
    El archivo tiene que ser.json
    Los índices son datetime y las columnas son timedelta
    """

    # Funcion para sacar la hora del string de la fecha del json
    def sacarhora(fecha):
        fecha = fecha[11:16]
        return fecha

    # Funcion para sacar el dia del string de la fecha del json
    def sacardia(fecha):
        fecha = fecha[8:10]
        return fecha

    # Funcion para sacar el mes del string de la fecha del json
    def sacarmes(fecha):
        fecha = fecha[5:7]
        return fecha

    # Funcion para sacar el anyo del string de la fecha del json
    def sacaranyo(fecha):
        fecha = fecha[0:4]
        return fecha

    # Diccionario donde vamos guardando los datos que luego pasaremos a un DataFrame
    diccionario = {}

    # Variable donde guardamos los datos del json a procesar
    values = pd.read_json(input("Archivo donde están los datos del precio (sin extensión): ") + ".json")

    # Bucle para rellenar el diccionario con los valores del json
    # Iteramos sobre los valores de la clave "values" ya que es donde estan los datos del precio
    for dic in values["values"]:

        # Sacamos la fecha del valor usando la clave "datetime"
        fecha = dic["datetime"]
        fecha_real = sacaranyo(fecha) + sacarmes(fecha) + sacardia(fecha)

        # Pasamos la fecha a datetime
        fecha_real = datetime.datetime.strptime(fecha_real, "%Y%m%d")
        hora = sacarhora(fecha)

        # Si es la primera hora de un dia, inicializamos su diccionario de valores
        if hora == "00:00":
            diccionario.update({fecha_real: {}})
            # Si no, lo inicializamos con lo que tenia antes
        else:
            diccionario.update({fecha_real: diccionario[fecha_anterior]})

        # Actualizamos el diccionario, metiendo la hora con su valor de precio
        diccionario[fecha_real].update({hora: dic["value"]})

        # Fecha que usaremos para inicializar el diccionario si no es la primera hora
        fecha_anterior = fecha_real

    # Generamos el DataFrame con los datos
    # Hay que hacer la transpuesta de la tabla para que salga como queremos
    datos = pd.DataFrame(diccionario).transpose()

    # Lista para no perder los indices de las columnas
    lista = list(datos.columns)

    # Lista en la que guardaremos los indices de columnas como TimeDelta
    lista2 = []

    # Bucle para formatear como TimeDelta los indices de columnas
    for i in lista:
        h, m = map(int, i.split(':'))
        lista2.append(datetime.timedelta(hours=h, minutes=m))

    # Actualizamos los indices de columnas del DataFrame columna
    datos.columns = lista2

    # Para arreglar el problema de los dias a los que le faltan horas
    for col in datos.columns:
        datos[col] = datos[col].fillna(datos[col].mean())

    # Retornamos el DataFrame final
    return datos.round(2)


if __name__ == "__main__":
    procesar_datos_time()
