#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:48:35 2024
Dividir la reaccion en sustratos y producto y operar desde ahi con dos bucles, creo que sera mas facil. inicilizar 
variables de orden y de ahi definir los pares. No perdas tiempo

@author: diegodelozada
"""
import pandas as pd
import os
from rdkit import Chem
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

df = pd.read_csv('ModelSEED_w_cofactor.csv')
ind = pd.read_excel('/Users/diegodelozada/PycharmProjects/PFG/BridgIT/Bridgit_index.xlsx')
directorio = '/Users/diegodelozada/PycharmProjects/PFG/BridgIT/molfiles'
count = 0

# chrome_driver_path = '/Users/diegodelozada/E-zyme/chromedriver'
# service = Service(chrome_driver_path)
# driver = webdriver.Chrome(service=service)


# # Abre E-zyme
# driver.get("https://www.genome.jp/tools/e-zyme2/")


for i in range(0,len(df)):
    elem = df.FORMULAS_ENCODED[i]
    elem = elem.split('<=>')
    reac = elem[0]
    prod = elem[1]

    if '+' in reac:
        reac = reac.split('+')
        reac = [elemento.strip() for elemento in reac]
    else:
        reac = reac.replace(' ','')

    if '+' in prod:
        prod = prod.split('+')
        prod = [elemento.strip() for elemento in prod]
    else:
        prod = prod.replace(' ','')
    print(reac)
    print(prod)

    total_C_reac = sum(elemento.count('C') for elemento in reac)
    print(total_C_reac)
    total_C_prod = sum(elemento.count('C') for elemento in prod)
    print(total_C_prod)

    
    if total_C_prod == 1 and total_C_reac ==1:
        count = count + 1
print(count)
#         identificador1 = reac
#         identificador2 = prod

#         nombre_archivo1 = identificador1 + '.mol'
#         ruta_completa1 = os.path.join(directorio, nombre_archivo1)
#         if nombre_archivo1 in os.listdir(directorio):
#             with open(ruta_completa1, 'r') as archivo:
#                 mol1 = archivo.read()
#         else:
#             continue

#         nombre_archivo2 = identificador2 + '.mol'
#         ruta_completa2 = os.path.join(directorio, nombre_archivo2)
#         if nombre_archivo2 in os.listdir(directorio):
#             with open(ruta_completa2, 'r') as archivo:
#                 mol2 = archivo.read()
#         else:
#             continue

#         textBox = driver.find_element(By.NAME, 'mol1')
#         textBox.send_keys(mol1)


#         textBox = driver.find_element(By.NAME, 'mol2')
#         textBox.send_keys(mol2)
          

#     elemento_submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="view structures"]')
#     elemento_submit.click()

#     elemento_submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="compute"]')
#     elemento_submit.click()

#     page_content = driver.page_source
#     search_text = "No enzyme was predicted."

#     # Verifica si el texto está presente
#     if search_text not in page_content:
#         table = driver.find_elements(By.CSS_SELECTOR, 'table.list')[3]

#         rows = table.find_elements(By.TAG_NAME, 'tr')

#         # Lista para guardar los datos
#         data = []

#         # Iterar sobre las filas y extraer las celdas
#         for row in rows:
#             cols = row.find_elements(By.TAG_NAME, 'td')
#             cols = [ele.text.strip() for ele in cols]
#             data.append([ele for ele in cols if ele])  # Añadir los datos si no están vacíos

#         # Convertir a DataFrame de pandas
#         df_results = pd.DataFrame(data)
#         df_results.to_csv(f'E-zyme2/{df.ID[i]}.csv', index=False)

#     driver.back()
#     time.sleep(3)

#     driver.back()
#     time.sleep(3)

#     elemento_clear = driver.find_element(By.CSS_SELECTOR, 'input[type="button"][value="clear"]')
#     elemento_clear.click()

#     time.sleep(3)

# driver.quit()