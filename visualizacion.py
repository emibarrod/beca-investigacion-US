import pandas as pd
pd.plotting.register_matplotlib_converters()
import matplotlib.pyplot as plt
import seaborn as sns
from procesadoDatosDemandaString import procesar_datos_string

def pinta_datos():
    plt.rcParams['xtick.major.pad']='100'
    plt.rcParams['xtick.minor.pad']='8'
    plt.figure(figsize=(1000,6))
    datos = procesar_datos_string()
    lista_filas = [i for i in datos.index]
    ax = plt.gca()
    ax.tick_params(axis='x', which='major', pad=150)
    figura = sns.lineplot(data=datos, dashes=False)
    #figura = sns.lineplot(data=datos, dashes=False)
    figura.set(xlabel='Dias', ylabel='Demanda')
    plt.show()

if __name__ == "__main__":
    pinta_datos()