# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:15:05 2018

@author: kevin lupera
"""

import pandas as pd
from datetime import date
import numpy as np
#crear dataFrame de archivos    
def create_df(file_name):
    quotes = []
    list1=[]
    if file_name=="u.data":
        list1 = ['id_usu','id_mov','calificacion','fecha']
        quotes=pd.read_table (file_name, sep = '\t', names = list1)
    elif file_name=="u.user":
        list1 = ['id_usu','edad','genero','ocupacion','cod_postal']
        quotes=pd.read_table (file_name, sep = '|', names = list1)
    elif file_name=="item.txt":
        list1 = ['id_mov','título_película', 'fecha_lanz', 'fecha_lanz_video', 'IMDb URL', 'desconocido ', 'Acción', 'Aventura', 'Animación', 'Niños','Comedia', 'Crimen', 'Documental', 'Drama', 'Fantasía','Humor_negro' , 'Horror' , 'Musical' ,'Misterio', 'Romance' , 'Ciencia_ficción' , 'Suspenso', ' Guerra ', 'Western ']
        quotes=pd.read_table (file_name, sep = '|', names = list1)
    dataFrame = pd.DataFrame(quotes,columns=list1)
    return dataFrame
#convertir formato de fecha
def fecha_df(df):
    list1=[]
    # Cambiar formato de fechas
    for i in range(len(df)):
        x = date.fromtimestamp(df['fecha'][i]).strftime('%Y-%m-%d')
        list1.append(x)
    df['fecha']=list1
    #Reemplazar el campo date con la fecha en un nuevo formato
    dfOri=pd.DataFrame(df)
    dfOri.date=list1
    return dfOri
#obtener informacion de los archivos y crear los DataFrames
data=fecha_df(create_df("u.data"))
user=create_df("u.user")
item=create_df("item.txt")
#Agrupar la informacion por genero
table = pd.pivot_table (user, columns = 'genero', aggfunc = np.mean)
#calcular la desviacion estandar de la calificacion
desv_est=np.std(user['edad'])
#print(desv_est)
#Fusionar las columnas 
a=data.merge(user,on='id_usu' , how='inner')
b=a.merge(item, on='id_mov', how='inner')
#agrupar
resultado = pd.pivot_table (b, values='calificacion',columns = 'genero', aggfunc = np.mean)
print(resultado)