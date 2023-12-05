import numpy as np

def zscore(X, mean=None, std=None):
    """
        Calculo da normalização zscore\n
        X    = conjunto de características\n
        mean = média das colunas\n
        std  = desvio padrão das colunas
    """    
    if mean is None:
        mean = np.mean(X, axis=0)
    if std is None:
        std = np.std(X, axis=0) + 0.00000000000001
    X = (X - mean) / (std)
    return (X, mean, std)


# convert into dataset matrix
def convertToMatrix(data, step):
    X, Y = [], []

    for i in range(len(data) - step):
        d = i + step
        X.append(data[i:d])
        Y.append(data[d])
    return np.array(X), np.array(Y)

# Convert for result predict
def convertToMatrixForPredict(data, step):
    X = []
    for i in range(len(data) - step+1):
        d = i + step
        X.append(data[i:d])
    return np.array(X)