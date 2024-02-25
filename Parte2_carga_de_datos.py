import pandas as pd
from datasets import load_dataset


# Convertir Dataset en DataFrame de Pandas

dataset = load_dataset("mstz/heart_failure")

# Acceder a la partición de entrenamiento
data = dataset["train"]

df = pd.DataFrame(data)

# Separar el DataFrame en dos según el valor de la columna "is_dead"
df_perecidos = df[df['is_dead'] == 1]
df_sobrevivientes = df[df['is_dead'] == 0]

# Calcular los promedios de las edades de cada dataset
promedio_edad_perecidos = df_perecidos['age'].mean()
promedio_edad_sobrevivientes = df_sobrevivientes['age'].mean()


#redondeando los valores
promedio_edad_perecidos_redondeado = round(promedio_edad_perecidos)
promedio_edad_sobrevivientes_redondeado = round(promedio_edad_sobrevivientes)


# Imprimir los resultados
print("Promedio de edad de personas que perecieron:", promedio_edad_perecidos)
print("Promedio de edad de personas que sobrevivieron:", promedio_edad_sobrevivientes)
