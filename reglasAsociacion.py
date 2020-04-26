from sklearn import preprocessing
import pandas as pd

def discretiza_con_kmeans(dataframe, n):
    '''
    Recibe un dataframe y un numero de intervalos en el que queramos dividir
    dicho dataframe.
    
    Devuelve el dataframe dividido en n intervalos por la tecnica de kmeans.
    '''
    
    discretizado = preprocessing.KBinsDiscretizer(n_bins=n, encode='ordinal',
                               strategy = "uniform").fit_transform(dataframe)
    datas = pd.DataFrame(discretizado)
    datas.index = dataframe.index
    datas.columns = dataframe.columns
    return datas