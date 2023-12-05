import os
from keras.models import load_model
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from utils import *
from selectVendas import *

#model = load_model('C:\\Users\\denis\\Desktop\\Python\\APS\\Modelo_APS_GastronomIA.h5')

diretorio_script = os.path.dirname(os.path.abspath(__file__))
nome_arquivo_modelo = "Modelo_APS_GastronomIA.h5"
caminho_modelo = os.path.join(diretorio_script, nome_arquivo_modelo)
model = load_model(caminho_modelo)

def predictDays(resultDays):
    nova_entrada = selectData()

    scaler = MinMaxScaler()
    scaler.fit(nova_entrada)
    nova_entrada = scaler.transform(nova_entrada)
    x = nova_entrada
    nova_entrada.shape

    nova_entrada  = nova_entrada.reshape(nova_entrada.shape[0])

    step = 60
    datax = convertToMatrixForPredict(nova_entrada, step)
    datax = np.reshape(datax, (datax.shape[0], 1, datax.shape[1]))

    aux = np.array(datax)
    for i in range(resultDays):
        resultado = model.predict(aux[-60:].reshape(1, 1, 60))

        aux = np.append(aux, resultado[0, 0])
        print(f'aux.shape: {aux.shape}')

    resultList = aux[60:].copy()

    resultado_inverse = scaler.inverse_transform(resultList.reshape((resultList.shape[0], 1)))
    datax_inverse = scaler.inverse_transform(x)
    resultado_inverse = resultado_inverse.reshape(resultado_inverse.shape[0])
    return resultado_inverse