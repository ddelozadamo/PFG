#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:04:51 2023
Using the molecules info, we obtain the smiles, inchi and mol informations throug pubchempy and rdkit and store ir a metInfo_1
@author: diegodelozada
"""

import pandas as pd
import pubchempy as pcp
from rdkit import Chem
import ssl


df = pd.read_excel(r'/Users/diegodelozada/PycharmProjects/PFG/modelSEED_metInfo.xlsx')

iso_smiles = [0] * len(df)
can_smiles = [0] * len(df)
inchi = [0] * len(df)
mol = [0] * len(df)

ssl._create_default_https_context = ssl._create_unverified_context


for items in range(0, len(df)):
    names = str(df.NAME[items])
    if 'Extracellular' in names:
        parts = names.split()
        names = parts[0]

    c = pcp.get_compounds(names, 'name')

    # uso pubchempy para extraer smiles y inchi
    if c:
        iso_smiles[items] = c[0].isomeric_smiles
        can_smiles[items] = c[0].canonical_smiles
        inchi[items] = c[0].inchi

    # uso rdkit para extraer los mol
    # if can_smiles[items] != 0:
    #     mol[items] = Chem.MolFromSmiles(can_smiles[items])




df = df.assign(MOL=mol, INCHI=inchi, CANONICAL_SMILES=can_smiles, ISOMETRIC_SMILES=iso_smiles)
df.to_excel('modelSEED_metInfo_1.xlsx', index=True)
#
# import pandas as pd
# import pubchempy as pcp
# from rdkit import Chem
# import ssl
#
# ssl._create_default_https_context = ssl._create_unverified_context
#
# # Leer el archivo Excel
# df = pd.read_excel(r'/Users/diegodelozada/PycharmProjects/PFG/modelSEED_metInfo.xlsx')
#
# # Lista de columnas que queremos agregar al DataFrame
# new_columns = ['MOL', 'INCHI', 'CANONICAL_SMILES', 'ISOMETRIC_SMILES']
#
# # Inicializar listas para almacenar los datos
# mol, inchi, can_smiles, iso_smiles = [], [], [], []
#
# # Diccionario para almacenar en caché los resultados de las consultas a PubChemPy
# pcp_cache = {}
#
# # Iterar sobre el DataFrame
# for index, row in df.iterrows():
#     # Obtener el nombre del compuesto
#     name = str(row['NAME'])
#
#     # Obtener la información del compuesto de PubChemPy si no la hemos obtenido antes
#     if name not in pcp_cache:
#         compounds = pcp.get_compounds(name, 'name')
#         pcp_cache[name] = compounds[0] if compounds else None
#     else:
#         compounds = [pcp_cache[name]]
#
#     # Procesar la información si la encontramos
#     if compounds and compounds[0]:
#         compound = compounds[0]
#         iso_smiles.append(compound.isomeric_smiles)
#         can_smiles.append(compound.canonical_smiles)
#         inchi.append(compound.inchi)
#         mol.append(Chem.MolFromSmiles(compound.canonical_smiles))
#     else:
#         iso_smiles.append(None)
#         can_smiles.append(None)
#         inchi.append(None)
#         mol.append(None)
#
# # Agregar las listas al DataFrame
# df[new_columns[0]] = mol
# df[new_columns[1]] = inchi
# df[new_columns[2]] = can_smiles
# df[new_columns[3]] = iso_smiles
#
# # Guardar el DataFrame en un nuevo archivo Excel
# df.to_excel('modelSEED_metInfo_1.xlsx', index=True)
