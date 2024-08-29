# Create a filter that checks if the components on the reactions from rxnInfo has an identified SMILE from the metInfo data
import math

import numpy
import pandas as pd

comp = pd.read_excel(r'ModelSEED_metInfo_1.xlsx')
reac = pd.read_excel(r'ModelSEED_rxnInfo.xlsx')

Smiles = comp.ISOMETRIC_SMILES
Formulas = reac.FORMULA
ID = reac.ID
EC_number = reac.EC

# Primero voy a crear una lista que guarde los smiles conocidos con sus abrevieciones
Abbreviation = []
can_smile = []
names = []

for items in range(0, len(comp)):
    if Smiles[items] != 0:
        Abbreviation.append(comp.ABBREVIATION[items])
        can_smile.append(comp.ISOMETRIC_SMILES[items])
        names.append(comp.NAME[items])

data = {'NAME': names, 'ABBREVIATION': Abbreviation, 'ISOMETRIC_SMILES': can_smile}
df = pd.DataFrame(data)

filtered_formulas = []
Reaction_smile = []
reaction_ID = []
name = []
EC = []

for items in range(0, len(Formulas)):
    formula_spliced = Formulas[items].split()
    formula_elements = [item for item in formula_spliced if item != '+' and item != '==>']
    if all(elem in list(df.ABBREVIATION) for elem in formula_elements) and len(formula_elements) > 1:
        filtered_formulas.append(str(Formulas[items]))
        reaction_ID.append(ID[items])
        EC.append(EC_number[items])

formula_spliced = []
for i in range(0, len(filtered_formulas)):
    n = filtered_formulas[i].replace('==>', '<=>')
    filtered_formulas[i] = n
    formula_spliced = filtered_formulas[i].split()
    reac_smile = ''
    for x in range(0, len(formula_spliced)):
        if formula_spliced[x] != '+' and formula_spliced[x] != '<=>':
            index = Abbreviation.index(formula_spliced[x])
            a = df.ISOMETRIC_SMILES[index]
            reac_smile += str(a)
        if formula_spliced[x] == '+':
            reac_smile += '.'
        if formula_spliced[x] == '<=>':
            reac_smile = reac_smile + '>>'

    Reaction_smile.append(reac_smile)
data1 = {'ID': reaction_ID, 'FORMULAS': filtered_formulas, 'REACTION_SMILE_ISOMETRIC': Reaction_smile, 'EC': EC}
df1 = pd.DataFrame(data1)
df1.to_excel('ModelSEED_complete_rxnInfo.xlsx', index=True)
