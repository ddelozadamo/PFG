#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 13:04:51 2023
Using the molecules info, we obtain the smiles, inchi and mol informations through pubchempy and rdkit and store ir a metInfo_complete
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
