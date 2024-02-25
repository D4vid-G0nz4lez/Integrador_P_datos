import numpy as np
from datasets import load_dataset

# Cargar el conjunto de datos
dataset = load_dataset("mstz/heart_failure")

# Acceder a la partición de entrenamiento
data = dataset["train"]

# Obtener la lista de edades
edades = data["age"]

# Convertir la lista de edades a un arreglo de NumPy
edades_np = np.array(edades)

# Calcular el promedio de edad y redondearlo a 2 decimales
promedio_edad = round(np.mean(edades_np), 2)

print("El promedio de edad de las personas participantes en el estudio es:", promedio_edad)
