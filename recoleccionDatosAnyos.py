import json
import requests


def recolecta_datos_anyos():
    """
    :return: Dos archivos json, uno para los datos de la demanda y otro para los datos del precio.

    Los nombres proporcionados para los archivos tienen que ser sin .json
    """

    # Cadenas de nombres para los archivos
    archivo_demanda = input("Nombre del archivo para demanda: ")
    archivo_precio = input("Nombre del archivo para precio: ")
    print("")

    # Listas para los meses y anyos que vamos a descargar
    lista_dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    anios = [2017, 2018, 2019]

    # Diccionarios para los valores de demanda y precio
    valores_demanda = {"values": []}
    valores_precio = {"values": []}

    # Hacemos un try except por si pasase algo durante la descarga
    try:

        # Para cada anyo
        for anio in anios:

            # Para cada mes
            for j in range(1, 13):
                print("Descargando año " + str(anio) + " mes " + str(j))

                # Si el mes es menor de 10
                if j < 10:

                    # URL a descargar
                    url = "https://apidatos.ree.es/es/datos/demanda/demanda-tiempo-real?start_date=" + str(
                        anio) + "-0" + str(
                        j) + "-01T00:00&end_date=" + str(anio) + "-0" + str(j) + "-" + str(
                        lista_dias_meses[j - 1]) + "T23:50&time_trunc=hour"

                    # Lista donde guardamos el json recibido de la URL
                    lista = list(requests.get(url).json()["included"][0]["attributes"]["values"])

                    # Actualizamos los valores de la demanda con los nuevos descargados
                    valores_demanda["values"].extend(lista)

                    # Hacemos lo mismo para precio
                    url = "https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?start_date=" + str(
                        anio) + "-0" + str(j) + "-01T00:00&end_date=" + str(anio) + "-0" + str(j) + "-" + str(
                        lista_dias_meses[j - 1]) + "T23:00&time_trunc=hour"
                    lista = list(requests.get(url).json()["included"][0]["attributes"]["values"])
                    valores_precio["values"].extend(lista)

                # Si no, hacemos lo mismo pero con otro formato de URL
                else:
                    url = "https://apidatos.ree.es/es/datos/demanda/demanda-tiempo-real?start_date=" + str(
                        anio) + "-" + str(
                        j) + "-01T00:00&end_date=" + str(anio) + "-" + str(j) + "-" + str(
                        lista_dias_meses[j - 1]) + "T23:50&time_trunc=hour"
                    lista = list(requests.get(url).json()["included"][0]["attributes"]["values"])
                    valores_demanda["values"].extend(lista)

                    url = "https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?start_date=" + str(
                        anio) + "-" + str(j) + "-01T00:00&end_date=" + str(anio) + "-" + str(j) + "-" + str(
                        lista_dias_meses[j - 1]) + "T23:00&time_trunc=hour"
                    lista = list(requests.get(url).json()["included"][0]["attributes"]["values"])
                    valores_precio["values"].extend(lista)

        # Generamos los archivos json
        print("")
        print("Generando " + str(archivo_demanda) + ".json")
        with open(archivo_demanda + ".json", "a+", encoding='utf-8') as f:
            json.dump(valores_demanda, f, ensure_ascii=False, indent=4)

        print("")
        print("Generando " + str(archivo_precio) + ".json")
        with open(archivo_precio + ".json", "a+", encoding='utf-8') as f:
            json.dump(valores_precio, f, ensure_ascii=False, indent=4)

    except:
        print("")
        print("Ha ocurrido un error")

    else:
        print("")
        print("Datos correctamente descargados y generados")


if __name__ == "__main__":
    recolecta_datos_anyos()
