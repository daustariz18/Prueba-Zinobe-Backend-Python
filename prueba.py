import requests
import pandas as pd
from time import time
from hashlib import sha1

url = "https://restcountries.com/v3.1/all"
data = requests.get(url)
paises = data.json()
lenguaje = []
country = []
region = []
encriptar = []
tiempo = []
cont = False


def countries():

    tiempo_inicial = time()
    cont = False
    for pais in paises:

        try:
            # Region
            region.append(pais['region'])
            # Pais
            country.append(pais['name']['common'])
            # Idiomas
            idiomas = pais['languages']
 
            for idioma in idiomas:
                if cont is False:
                    idioma_select = idiomas[idioma]
                    psw = sha1(idioma_select.encode('utf-8')).hexdigest()
                    lenguaje.append(idiomas[idioma])
                    encriptar.append(psw)
                    tiempo_final = time()
                    tiempo_ejecucion = tiempo_final - tiempo_inicial
                    tiempo.append(tiempo_ejecucion)
                    cont = True
                else:
                    break
        except KeyError:
            country.append('')
        cont = False
    return True


countries()

# TABLA EN PANDA
user_list = list(zip(region, country, encriptar, tiempo))
tabla = pd.DataFrame(user_list, columns=['Region', 'Pais', 'Idioma', 'Tiempo'])
print(tabla)

# JSON GENERADO
js = tabla.to_json(orient='records')
