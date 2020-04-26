import pandas as pd
import numpy as np

def demanda_a_3_horas(precio, demanda):
    '''
    Los parametros son dos DataFrame, el precio y la demanda.
    Devuelve un DataFrame con 4 columnas:
        la demanda 1,2 y 3 horas antes y el precio.
    '''
    
    lista_precio = precio.values.tolist()
    lista_precio = [x for y in lista_precio for x in y]
    columna_precio = pd.DataFrame(lista_precio[3:])

    lista_demanda1 = demanda.values.tolist()
    lista_demanda1 = [x for y in lista_demanda1 for x in y][:26277]
    columna_demanda1 = pd.DataFrame(lista_demanda1)

    lista_demanda2 = demanda.values.tolist()
    lista_demanda2 = [x for y in lista_demanda2 for x in y][1:26278]
    columna_demanda2 = pd.DataFrame(lista_demanda2)

    lista_demanda3 = demanda.values.tolist()
    lista_demanda3 = [x for y in lista_demanda3 for x in y][2:26279]
    columna_demanda3 = pd.DataFrame(lista_demanda3)

    demanda_a_3_horas = pd.concat([columna_demanda1, columna_demanda2, columna_demanda3, columna_precio], axis = 1)
    demanda_a_3_horas.columns = ['3 horas antes', '2 horas antes', '1 hora antes', 'precio']
    
    return demanda_a_3_horas

def correlacion_hasta_n_horas_antes(precio, demanda, n):
    '''
    Recibe dos dataframes, uno para demanda y otro para precio, y las horas para las que queremos
    ver las correlaciones.
    
    Devuelve una lista con las horas y su respectiva correlacion entre esa demanda y el precio.
    '''
    
    lista_precio = precio.values.tolist()
    lista_precio = [x for y in lista_precio for x in y][n:]
    columna_precio = pd.DataFrame(lista_precio)
    correlaciones = []
    for i in range(n):
        lista_demanda = demanda.values.tolist()

        lista_demanda = [x for y in lista_demanda for x in y][i:26256+i]

        columna_demanda = pd.DataFrame(lista_demanda)
        corr = float(pd.DataFrame(lista_demanda).corrwith(columna_precio))
        correlaciones.append((n-i, corr))
        
    return correlaciones

def comprueba_correlacion_n_horas_antes(precio, demanda, n):
    '''
    Recibe dataframes de precio y demanda y el numero de horas antes para la que
    queremos calcular la correlacion (tiene que ser entre 1 y 24).
    
    Devuelve la correlacion entre precio y demanda n horas antes.
    '''
    lista_precio = precio.values.tolist()
    lista_precio = [x for y in lista_precio for x in y][24:]
    columna_precio = pd.DataFrame(lista_precio)
    for i in range(24):
        lista_demanda = demanda.values.tolist()

        lista_demanda = [x for y in lista_demanda for x in y][i:26256+i]
        #print(len(lista_demanda))

        columna_demanda = pd.DataFrame(lista_demanda)

        if i == 24-n:
            return "Correlacion {} horas antes".format(24-i), float(pd.DataFrame(lista_demanda).corrwith(columna_precio))