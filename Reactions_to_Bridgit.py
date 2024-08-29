# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 11:47:22 2024
Este codigo genera una tabla con las reacciones en el formato original y con el formato para enviar a BrigIT
@author: ddelozadamo
"""

import pandas as pd

reac = pd.read_excel(r'../Data/modelSEED_Filtered_rxnInfo.xlsx')
comp = pd.read_excel(r'Bridgit_index.xlsx')
reacciones = []


for i in range(0, len(reac)):
    # Cadena de reacción
    cadena_reaccion = reac.FORMULAS[i]

    # Dividir la cadena por espacios y eliminar los símbolos "<=>", "+", "[" y "]"
    componentes = cadena_reaccion.split(" ")
    print(i)
    i = 0
    componentes_new = []
    for c in componentes:
        if c[0] != '+' and c[0] != '<':
            componentes_new.append(c)
            i = i + 1
    j = 0
    for c in componentes_new:
        # Obtener el índice correspondiente al componente
        indice = comp.loc[comp['ABBREVIATION'] == c, 'index'].iloc[0]

        # Reemplazar el componente por su índice
        componentes_new[j] = componentes_new[j].replace(c, str(indice))
        j = j + 1
    k = 0
    for i in range(0, len(componentes)):
        if componentes[i] != '+' and componentes[i] != '<=>':
            componentes[i] = componentes_new[k]
            k = k + 1

    cadena_reaccion = ' '.join(componentes)
    reacciones.append(cadena_reaccion)


data = {'REACTIONS': reacciones , 'FORMULAS': reac.FORMULAS}
df1 = pd.DataFrame(data)
df1.to_excel('Reactions_to_BridgIT.xlsx', index=False)
