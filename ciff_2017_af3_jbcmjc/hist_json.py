from flask import render_template
import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
from create_lagged_series2 import create_lagged_series2
import datetime
from datetime import datetime
import numpy as np
from matplotlib.pyplot import *
import json

def hist_json(ndias, symbol):

    lags = int(ndias)
    dict_valores = {"error":''}

    try:
        tsret = pd.DataFrame()
        tsret = create_lagged_series2(lags, symbol)

        hist, edges = np.histogram(tsret, bins=10, range=(-0.1,0.1))
        dict_valores = {}

        #total de muestras
        total_muestra = sum(hist)

        # crear histograma en diccionario
        for i, val in enumerate(hist):
            clave = str(edges[i]) + " to " + str(edges[i+1])
            dict_valores[clave] = float(val) / float(total_muestra)
    except:
        dict_valores = {}
        print 'error'

    return json.dumps(dict_valores)
