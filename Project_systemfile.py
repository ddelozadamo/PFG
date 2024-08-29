"""
Created on Wed Jun  7 09:49:48 2023
Creamos el archivo systemfile para usar en la base de datos de BridgIT en la que anotamos la informacion de las reacciones filtradas
@author: diegodelozada
"""
import pandas as pd

reac = pd.read_excel(r'../Data/modelSEED_Filtered_rxnInfo.xlsx')
formulas = pd.read_excel(r'Reactions_to_BridgIT.xlsx')


ID = reac.ID
print(ID[0])
formula = formulas.REACTIONS
count = 0
# 1/6 2/6 1/2 4/6 5/6 6/6

archivo = open("Project_systemfile.txt", "w")
archivo.write("COMPOUNDS\n")
archivo.write("ENTRY\n")
archivo.write("reactionsS\n")
archivo.write("ENTRY;KEGG;EQUATION;OPERATORS\n")

for item in range(0, 10):
    a = str(formula[item])
    a = a.replace(' ', '')
    archivo.write(f'r{item + 1};;{a};\n')
    count = count + 1

print(count)
archivo.close()
