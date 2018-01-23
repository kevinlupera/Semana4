import time
import pandas as pd
from datetime import date

datos = {"country": ["Brazil", "Russia", "India", "China", "South Africa"],
     "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "PretoriaDDDD"],
     "date": [1464010200, 1464010201, 1464010202, 1464010203, 1464010204] }
df = pd.DataFrame(datos)
ldate=[]
# Cambiar formato de fechas
ldate= pd.to_datetime(df['date'], format='%Y-%m-%d')
for i in range(len(ldate)):
    ldate[i]=ldate[i].strftime('%Y-%m-%d')
df['date']=ldate
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
