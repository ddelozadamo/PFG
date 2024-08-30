import os
import shutil
import pandas as pd

# Este código es para reducir el tamaño de la carpeta de molfiles para BridgIT. Se guardan solo los molfiles necesarios para las reacciones que se estan analizando
directorio = 'molfiles'
carpeta_destino = 'molfiles_reduced'

archivos = os.listdir(directorio)


mol_sin_extension = [archivo.replace('.mol', '') for archivo in archivos]

formulas = pd.read_excel(r'Reactions_to_BridgIT.xlsx')

formula = formulas.REACTIONS


def comp_in_reac(reaction):
    reaction_split = reaction.split(" ")
    i = 0
    componentes_new = []
    for c in reaction_split:
        if c[0] != '+' and c[0] != '<':
            componentes_new.append(c)
            i = i + 1
    return componentes_new


check_list = []

for i in range(0, 10):
    cadena_reaccion = formula[i]
    componentes_new = comp_in_reac(cadena_reaccion)
    for comp in componentes_new:
        if comp not in check_list:
            try:
                print(comp)
                indice = mol_sin_extension.index(comp)
                file = os.path.join('molfiles', f'{mol_sin_extension[indice]}.mol')
                check_list.append(mol_sin_extension[indice])
                print(file)
                shutil.move(file, carpeta_destino)
            except ValueError:
                continue

