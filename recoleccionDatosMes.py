import requests
import json
import os


def recolecta_datos_meses():
    """
    Funciona igual que recolecta_datos_anyos, pero de mes en mes
    :return: Una carpeta para demanda y otra para precio, con las demandas y precios por meses
    """
    path1 = input("Nombre de la carpeta a crear para demanda: ")
    path2 = input("Nombre de la carpeta a crear para precio: ")
    print("")

    lista_dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    anios = [2017, 2018, 2019]

    try:
        os.mkdir(path1)
    except OSError:
        print("No se puede crear la carpeta" % 1)
    else:
        print("Se ha creado la carpeta %s " % path1)

    try:
        os.mkdir(path2)
    except OSError:
        print("No se puede crear la carpeta" % 1)
    else:
        print("Se ha creado la carpeta %s " % path2)

    print("")
    print("Descargando los datos...")

    try:
        for anio in anios:

            for j in range(1, 13):

                if j < 10:
                    url = "https://apidatos.ree.es/es/datos/demanda/demanda-tiempo-real?start_date=" + str(
                        anio) + "-0" + str(j) + "-01T00:00&end_date=" + str(anio) + "-0" + str(j) + "-" + str(
                        lista_dias_meses[j - 1]) + "T23:50&time_trunc=hour"
                    datos = requests.get(url).json()
                    with open(path1 + "/dataset_demanda_anyo_" + str(anio) + "_mes_" + str(j) + ".json", "a+",
                              encoding='utf-8') as f:
                        json.dump(datos, f, ensure_ascii=False, indent=4)

                    url = "https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?start_date=" + str(
                        anio) + "-0" + str(j) + "-01T00:00&end_date=" + str(anio) + "-0" + str(j) + "-" + str(
                        lista_dias_meses[j - 1]) + "T23:00&time_trunc=hour"
                    datos = requests.get(url).json()
                    with open(path2 + "/dataset_precio_anyo_" + str(anio) + "_mes_" + str(j) + ".json", "a+",
                              encoding='utf-8') as f:
                        json.dump(datos, f, ensure_ascii=False, indent=4)

                else:
                    url = "https://apidatos.ree.es/es/datos/demanda/demanda-tiempo-real?start_date=" + str(
                        anio) + "-" + str(j) + "-01T00:00&end_date=" + str(anio) + "-" + str(j) + "-" + str(
                        lista_dias_meses[j - 1]) + "T23:50&time_trunc=hour"
                    datos = requests.get(url).json()
                    with open(path1 + "/dataset_demanda_anyo_" + str(anio) + "_mes_" + str(j) + ".json", "a+",
                              encoding='utf-8') as f:
                        json.dump(datos, f, ensure_ascii=False, indent=4)

                    url = "https://apidatos.ree.es/es/datos/mercados/precios-mercados-tiempo-real?start_date=" + str(
                        anio) + "-" + str(j) + "-01T00:00&end_date=" + str(anio) + "-" + str(j) + "-" + str(
                        lista_dias_meses[j - 1]) + "T23:00&time_trunc=hour"
                    datos = requests.get(url).json()
                    with open(path2 + "/dataset_precio_anyo_" + str(anio) + "_mes_" + str(j) + ".json", "a+",
                              encoding='utf-8') as f:
                        json.dump(datos, f, ensure_ascii=False, indent=4)
    except:
        print("Ha ocurrido un error")

    else:
        print("Datos descargados")


if __name__ == "__main__":
    recolecta_datos_meses()
