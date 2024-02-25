import requests

def descargar_datos_csv_desde_url(url_datos, nombre_archivo):
    try:
        # Realizar el GET request
        response = requests.get(url_datos)
        
        # Verificar si la solicitud fue exitosa (código de estado 200)
        if response.status_code == 200:
            # Escribir la respuesta en un archivo CSV
            with open(nombre_archivo, 'wb') as archivo_csv:
                archivo_csv.write(response.content)
            print("Datos descargados correctamente como", nombre_archivo)
        else:
            print("Error al descargar los datos. Código de estado:", response.status_code)
    except Exception as e:
        print("Ocurrió un error:", str(e))

# URL de los datos
url_datos = "https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv"

# Nombre del archivo en el que se guardarán los datos
nombre_archivo = "datos_integrador.csv"

# Llamar a la función para descargar los datos
descargar_datos_csv_desde_url(url_datos, nombre_archivo)
