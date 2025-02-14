import requests #para llamar a la api de google
from dotenv import load_dotenv #libreria para interactuar con .env
import os

#cargamos las variables .env en el entorno
load_dotenv()

# Constantes para configurar la API de búsqueda personalizada de Google
#estas variables se encuantran en el entorno .env
# se usa os para llamar a las variables de .env
API_KEY_GOOGLE = os.getenv("API_KEY_GOOGLE")
ID_SEARCH_GOOGLE = os.getenv("SEARCH_ENGINE_ID")



# Configuración de la consulta y parámetros de búsqueda
query = 'filetype:sql "MySQL dump" (pass|password|passwd|pwd)' # lo que queremos buscar
page = 1 # pagina por la que queremos empezar
lang = "lang_es" # idioma en que queremos los resultados

# Construcción de la URL para la API de Google Custom Search
url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY_GOOGLE}&cx={ID_SEARCH_GOOGLE}&q={query}&start={page}&lr={lang}"

# Realizar la solicitud HTTP GET y convertir la respuesta en JSON
response = requests.get(url)
data = response.json()

# Recuperar la lista de resultados de la respuesta
results = data.get("items", [])  # Uso de get para evitar KeyError si 'items' no existe

# Iterar sobre cada resultado e imprimir los detalles relevantes
for result in results:
    print("------- Nuevo resultado -------")
    print(f"Título: {result.get('title')}")
    print(f"Descripción: {result.get('snippet')}")
    print(f"Enlace: {result.get('link')}")
    print("-------------------------------")
