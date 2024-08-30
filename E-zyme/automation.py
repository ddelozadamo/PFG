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
similarity = pd.read_csv('similarity_matrix.csv')
similarity.set_index('x', inplace=True)
ind = pd.read_excel('/Users/diegodelozada/PycharmProjects/PFG/BridgIT/Bridgit_index.xlsx')
directorio = '/Users/diegodelozada/PycharmProjects/PFG/BridgIT/molfiles'
count = 8632

chrome_driver_path = '/Users/diegodelozada/E-zyme/chromedriver'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)


# Abre E-zyme
driver.get("https://www.genome.jp/tools-bin/predict_reaction")


for i in range(8632,len(df)):
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

    if total_C_prod > 2 or total_C_reac > 2:
        continue

    if total_C_prod == 1 and total_C_reac ==1:
        identificador1 = reac
        identificador2 = prod

        nombre_archivo1 = identificador1 + '.mol'
        ruta_completa1 = os.path.join(directorio, nombre_archivo1)
        if nombre_archivo1 in os.listdir(directorio):
            with open(ruta_completa1, 'r') as archivo:
                mol1 = archivo.read()
        else:
            continue

        nombre_archivo2 = identificador2 + '.mol'
        ruta_completa2 = os.path.join(directorio, nombre_archivo2)
        if nombre_archivo2 in os.listdir(directorio):
            with open(ruta_completa2, 'r') as archivo:
                mol2 = archivo.read()
        else:
            continue

        # Elegimos multiple pairs
        select_element = driver.find_element(By.NAME, "QUERY_MODE")
        select = Select(select_element)
        select.select_by_value("MULTI")


        textBox = driver.find_element(By.NAME, 'S_MOLTEXT')
        textBox.send_keys(mol1)


        textBox = driver.find_element(By.NAME, 'P_MOLTEXT')
        textBox.send_keys(mol2)


    if total_C_prod == 1 and total_C_reac == 2:
        identificador1 = reac[0]
        identificador2 = reac[1]
        identificador3 = prod
        molecule1 = ind.loc[ind['index'] == identificador1, 'NAME'].values[0]
        molecule2 = ind.loc[ind['index'] == identificador2, 'NAME'].values[0]
        molecule3 = ind.loc[ind['index'] == identificador3, 'NAME'].values[0]

        nombre_archivo1 = identificador1 + '.mol'
        ruta_completa1 = os.path.join(directorio, nombre_archivo1)
        if nombre_archivo1 in os.listdir(directorio):
            with open(ruta_completa1, 'r') as archivo:
                mol1 = archivo.read()
        else:
            continue
        nombre_archivo2 = identificador2 + '.mol'
        ruta_completa2 = os.path.join(directorio, nombre_archivo2)

        if nombre_archivo2 in os.listdir(directorio):
            with open(ruta_completa2, 'r') as archivo:
                mol2 = archivo.read()
        else:
            continue

        nombre_archivo3 = identificador3 + '.mol'
        ruta_completa3 = os.path.join(directorio, nombre_archivo3)
        if nombre_archivo3 in os.listdir(directorio):
            with open(ruta_completa3, 'r') as archivo:
                mol3 = archivo.read()
        else:
            continue

        try:
            sim_1_2 = similarity.loc[molecule1, molecule2]
            sim_1_3 = similarity.loc[molecule1, molecule3]
        except:
            sim_1_2 = 2
            sim_1_3 = 1

        if sim_1_2 > sim_1_3:

            # Elegimos multiple pairs
            select_element = driver.find_element(By.NAME, "QUERY_MODE")
            select = Select(select_element)
            select.select_by_value("MULTI")


            textBox = driver.find_elements(By.NAME, 'S_MOLTEXT')[0]
            textBox.send_keys(mol1)


            textBox = driver.find_elements(By.NAME, 'P_MOLTEXT')[0]
            textBox.send_keys(mol2)

            textBox = driver.find_elements(By.NAME, 'S_MOLTEXT')[1]
            textBox.send_keys(mol3)

        else:
             # Elegimos multiple pairs
            select_element = driver.find_element(By.NAME, "QUERY_MODE")
            select = Select(select_element)
            select.select_by_value("MULTI")

            textBox = driver.find_elements(By.NAME, 'S_MOLTEXT')[0]
            textBox.send_keys(mol1)


            textBox = driver.find_elements(By.NAME, 'P_MOLTEXT')[0]
            textBox.send_keys(mol3)


            textBox = driver.find_elements(By.NAME, 'S_MOLTEXT')[1]
            textBox.send_keys(mol2)


    if total_C_prod == 2 and total_C_reac == 1:
        identificador1 = reac
        identificador2 = prod[0]
        identificador3 = prod[1]
        molecule1 = ind.loc[ind['index'] == identificador1, 'NAME'].values[0]
        molecule2 = ind.loc[ind['index'] == identificador2, 'NAME'].values[0]
        molecule3 = ind.loc[ind['index'] == identificador3, 'NAME'].values[0]

        nombre_archivo1 = identificador1 + '.mol'
        ruta_completa1 = os.path.join(directorio, nombre_archivo1)
        if nombre_archivo1 in os.listdir(directorio):
            with open(ruta_completa1, 'r') as archivo:
                mol1 = archivo.read()
        else:
            continue

        nombre_archivo2 = identificador2 + '.mol'
        ruta_completa2 = os.path.join(directorio, nombre_archivo2)

        if nombre_archivo2 in os.listdir(directorio):
            with open(ruta_completa2, 'r') as archivo:
                mol2 = archivo.read()
        else:
            continue

        nombre_archivo3 = identificador3 + '.mol'
        ruta_completa3 = os.path.join(directorio, nombre_archivo3)
        if nombre_archivo3 in os.listdir(directorio):
            with open(ruta_completa3, 'r') as archivo:
                mol3 = archivo.read()
        else:
            continue

        try:
            sim_1_2 = similarity.loc[molecule1, molecule2]
            sim_1_3 = similarity.loc[molecule1, molecule3]
        except:
            sim_1_2 = 2
            sim_1_3 = 1

        if sim_1_2 > sim_1_3:

            # Elegimos multiple pairs
            select_element = driver.find_element(By.NAME, "QUERY_MODE")
            select = Select(select_element)
            select.select_by_value("MULTI")


            textBox = driver.find_elements(By.NAME, 'S_MOLTEXT')[0]
            textBox.send_keys(mol1)


            textBox = driver.find_elements(By.NAME, 'P_MOLTEXT')[0]
            textBox.send_keys(mol2)

            textBox = driver.find_elements(By.NAME, 'P_MOLTEXT')[1]
            textBox.send_keys(mol3)

        else:
             # Elegimos multiple pairs
            select_element = driver.find_element(By.NAME, "QUERY_MODE")
            select = Select(select_element)
            select.select_by_value("MULTI")

            textBox = driver.find_elements(By.NAME, 'S_MOLTEXT')[0]
            textBox.send_keys(mol1)


            textBox = driver.find_elements(By.NAME, 'P_MOLTEXT')[0]
            textBox.send_keys(mol3)


            textBox = driver.find_elements(By.NAME, 'P_MOLTEXT')[1]
            textBox.send_keys(mol2)


    if total_C_prod == 2 and total_C_reac == 2:
        identificador1 = reac[0]
        identificador2 = reac[1]
        identificador3 = prod[0]
        identificador4 = prod[1]
        molecule1 = ind.loc[ind['index'] == identificador1, 'NAME'].values[0]
        molecule2 = ind.loc[ind['index'] == identificador2, 'NAME'].values[0]
        molecule3 = ind.loc[ind['index'] == identificador3, 'NAME'].values[0]
        molecule4 = ind.loc[ind['index'] == identificador4, 'NAME'].values[0]

        nombre_archivo1 = identificador1 + '.mol'
        ruta_completa1 = os.path.join(directorio, nombre_archivo1)
        if nombre_archivo1 in os.listdir(directorio):
            with open(ruta_completa1, 'r') as archivo:
                mol1 = archivo.read()
        else:
            continue

        nombre_archivo2 = identificador2 + '.mol'
        ruta_completa2 = os.path.join(directorio, nombre_archivo2)
        if nombre_archivo2 in os.listdir(directorio):
            with open(ruta_completa2, 'r') as archivo:
                mol2 = archivo.read()
        else:
            continue

        nombre_archivo3 = identificador3 + '.mol'
        ruta_completa3 = os.path.join(directorio, nombre_archivo3)
        if nombre_archivo3 in os.listdir(directorio):
            with open(ruta_completa3, 'r') as archivo:
                mol3 = archivo.read()
        else:
            continue

        nombre_archivo4 = identificador4 + '.mol'
        ruta_completa4 = os.path.join(directorio, nombre_archivo4)
        if nombre_archivo4 in os.listdir(directorio):
            with open(ruta_completa4, 'r') as archivo:
                mol4 = archivo.read()
        else:
            continue

        try:
            sim_1_3 = similarity.loc[molecule1, molecule3]
            sim_1_4 = similarity.loc[molecule1, molecule4]
            sim_2_3 = similarity.loc[molecule2, molecule3]
            sim_2_4 = similarity.loc[molecule2, molecule4]
        except:
            sim_1_3 = 3
            sim_1_4 = 1
            sim_2_3 = 2

        # Elegimos multiple pairs
        select_element = driver.find_element(By.NAME, "QUERY_MODE")
        select = Select(select_element)
        select.select_by_value("MULTI")

        if sim_1_3 > sim_1_4:
            if sim_1_3 > sim_2_3:
                textBox = driver.find_elements(By.NAME, 'S_MOLTEXT')[0]
                textBox.send_keys(mol1)

                textBox = driver.find_elements(By.NAME, 'P_MOLTEXT')[0]
                textBox.send_keys(mol3)

                textBox = driver.find_elements(By.NAME, 'S_MOLTEXT')[1]
                textBox.send_keys(mol2)

                textBox = driver.find_elements(By.NAME, 'P_MOLTEXT')[1]
                textBox.send_keys(mol4)
            else: 
                textBox = driver.find_elements(By.NAME, 'S_MOLTEXT')[0]
                textBox.send_keys(mol1)

                textBox = driver.find_elements(By.NAME, 'P_MOLTEXT')[0]
                textBox.send_keys(mol4)

                textBox = driver.find_elements(By.NAME, 'S_MOLTEXT')[1]
                textBox.send_keys(mol2)

                textBox = driver.find_elements(By.NAME, 'P_MOLTEXT')[1]
                textBox.send_keys(mol3)
        else:
            textBox = driver.find_elements(By.NAME, 'S_MOLTEXT')[0]
            textBox.send_keys(mol1)

            textBox = driver.find_elements(By.NAME, 'P_MOLTEXT')[0]
            textBox.send_keys(mol4)

            textBox = driver.find_elements(By.NAME, 'S_MOLTEXT')[1]
            textBox.send_keys(mol2)

            textBox = driver.find_elements(By.NAME, 'P_MOLTEXT')[1]
            textBox.send_keys(mol3)            

    elemento_submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="View structures"]')
    elemento_submit.click()

    elemento_submit = driver.find_element(By.CSS_SELECTOR, 'input[type="submit"][value="Compute"]')
    elemento_submit.click()

    elemento_tabla = driver.find_element(By.CSS_SELECTOR, 'table[border="0"][cellspacing="3"][cellpadding="1"]')

    filas = elemento_tabla.find_elements(By.TAG_NAME, 'tr')

    datos_tabla = []

    for fila in filas:
        celdas = fila.find_elements(By.TAG_NAME, 'td')
        datos_fila = [celda.text for celda in celdas]
        datos_tabla.append(datos_fila)

    df1 = pd.DataFrame(datos_tabla)
    df1.to_csv(f'{df.ID[i]}.csv', index=False)
    count = count + 1
    print(count)
    time.sleep(3)

    driver.back()
    time.sleep(3)

    driver.back()
    time.sleep(3)

    elemento_clear = driver.find_element(By.CSS_SELECTOR, 'input[type="button"][value="Clear"]')
    elemento_clear.click()

    time.sleep(3)

driver.quit()