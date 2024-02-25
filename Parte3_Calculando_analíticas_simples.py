from datasets import load_dataset
import pandas as pd 

#Cargando conjunto de datos 
conjunto_datos = load_dataset("mstz/heart_failure")

datos = conjunto_datos['train']

#Convirtiendo datos a DataFrame
df = pd.DataFrame(datos)

#Verificando los datos de la colunna  
print("Tipos de datos en el Dataframe")
print(df.dtypes)

# Calculando hombres y mujeres fumadores
hombres_fumadores = df[(df['is_male'] == 1) & (df['is_smoker'] == 1)].shape[0]
mujeres_fumadores = df[(df['is_male'] == 1) & (df['is_smoker'] == 1)].shape[0]

#Imprimir resutados 
print("Promediode hombres fumadores: ", hombres_fumadores )
print("Promedio de mujeres fumadores: ", mujeres_fumadores )