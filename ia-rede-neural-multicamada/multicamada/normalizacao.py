import numpy as np
from sklearn import preprocessing

e= np.array([[5.90, 3.63, 59, 3.00, 670],
                     [6.00, 7.12, 58, 2.40, 395],
                     [5.70, 5.49, 58, 3.19, 520],
                     [6.30, 9.91, 73, 2.90, 520],
                     [5.50, 8.12, 67, 2.20, 670]])

s = np.array([[3120],
                   [4000],
                   [3900],
                   [4200],
                   [4300]])

entradas_minmax = preprocessing.MinMaxScaler().fit(e)
entradas = entradas_minmax.transform(e)

saidas_minmax = preprocessing.MinMaxScaler().fit(s)
saidas = saidas_minmax.transform(s)



