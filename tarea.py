# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:15:05 2018

@author: kevin
"""

import pandas as pd
from datetime import date

    
def create_df(file_name):
    quotes = []
    list1=[]
    if file_name=="u.data":
        list1 = ['id_usuario','id_elemento','calificacion','date']
        quotes=pd.read_table (file_name, sep = '\t', names = list1)
    elif file_name=="u.user":
        list1 = ['id_usuario','edad','genero','ocupacion','codigo postal']
        quotes=pd.read_table (file_name, sep = '|', names = list1)
    elif file_name=="u.item":
        list1 = ['identificación de la película', 'título de la película', 'fecha de lanzamiento', 'fecha de lanzamiento del video', 'IMDb URL', 'desconocido ', 'Acción', 'Aventura', 'Animación', 'Niños','Comedia', 'Crimen', 'Documental', 'Drama', 'Fantasía','Película-Noir' , 'Horror' , 'Musical Misterio' , 'Romance' , 'Ciencia ficción' , 'Novela de suspense', ' Guerra ', 'Western ']
        quotes=pd.read_table (file_name, sep = '|', names = list1)
    #pd.pivot_table (data, values ​​= None, columns = None, aggfunc = 'mean')
    #pd.merge (left, right, cómo = 'interior')
    dataFrame = pd.DataFrame(quotes,columns=list1)
    list2 = []
    for i in range(len(dataFrame)):
        x = date.fromtimestamp(dataFrame[i]['date'])
        y = date.strftime(x,'%Y-%m-%d')
        list2.append(y)
    quotesdf_ori = pd.DataFrame(dataFrame, index = list2)
    quotesdf = quotesdf_ori.drop(['date'], axis = 1)
    return dataFrame


print(create_df("u.data"))
#print(create_df("u.user"))
#print(create_df("u.item"))
