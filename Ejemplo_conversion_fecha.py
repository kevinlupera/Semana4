#import time
import pandas as pd
from datetime import date 

datos = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
     "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "PretoriaDDDD"],
     "date": [1464010200, 1464010201, 1464010202, 1464010203, 1464010204] }
df = pd.DataFrame(datos)
#print(df['date'][0])
#x = date.fromtimestamp(df['date'][0]).strftime('%Y-%m-%d %H:%M')
#print(x)
list1=[]
#Cambiar formato de fechas
#list1= pd.to_datetime(df['date'], format='%Y-%m-%d')
for i in range(len(ldate)):
    x = date.fromtimestamp(df['date'][i]).strftime('%Y-%m-%d')
    list1.append(x)
#df['date']=df['date'].apply(lambda x: dt.datetime.strptime(x,'%d%b%Y:%H:%M:%S.%f'))
print(list1)
"""
#df['date']=ldate
#1 Agregar la fecha como indice
dfOri=pd.DataFrame(datos,index=ldate)
#Eliminar la columna date
dfOri=pd.DataFrame(dfOri.drop(['date'],axis=1))
print(dfOri)
#2 Reemplazar el campo date con la fecha en un nuevo formato
dfOri=pd.DataFrame(datos)
dfOri.date=ldate
#Imprimir resultados
print(dfOri)
"""