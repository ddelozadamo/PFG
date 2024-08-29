#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 09:49:48 2023
Here we obtain the molfiles for each molecule using rdkit. (creo que esto es para meterlo a bridgIT)
También se genra una tabla con el indice de los identificadores para las reacciones
@author: diegodelozada
"""

import pandas as pd
from rdkit import Chem
import os
df = pd.read_excel(r'../Data/modelSEED_metInfo_1.xlsx')
can_smiles = df.CANONICAL_SMILES.astype(str)

BridgIT_index = []
abbreviation = df.ABBREVIATION
names = df.NAME
id = df.ID
for i in range(0, len(df)):
    mol = 0

    if can_smiles[i] != '0':
        mol = Chem.MolFromSmiles(can_smiles[i])

    if mol != 0:
        output_file = os.path.join('molfiles', f'C{i}.mol')
        Chem.MolToMolFile(mol, output_file)
    BridgIT_index.append(f'C{i}')
print(i)
data = {'index': BridgIT_index, 'ABBREVIATION': abbreviation, 'NAME': names}
df1 = pd.DataFrame(data)
df1.to_excel('Bridgit_index.xlsx', index=False)
