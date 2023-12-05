import pyodbc
import numpy as np
import pandas as pd

def selectData():
    conn = pyodbc.connect('Driver={SQL Server};'
    'Server=aps-sad.database.windows.net;'
    'Database=Homolog;'
    'UID=sad;'
    'PWD=#Aps2023')

    sql = 'SELECT SUM(Valor) as ValorTotalDia FROM Vendas GROUP BY Data_Venda ORDER BY Data_Venda;'
    data = pd.read_sql(sql, conn)
    nova_entrada = data.to_numpy()[-60:]

    conn.close() 
    return nova_entrada