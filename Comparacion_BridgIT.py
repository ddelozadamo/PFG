import pandas as pd
import os
import csv


def best_result(nombre_archivo):
    valores = []
    with open(nombre_archivo, 'r') as archivo:
        lector_csv = csv.reader(archivo)
        for fila in lector_csv:
            if fila and len(fila) >= 2 and fila[0] and fila[1]:
                valores.append((fila[0], fila[1]))
    return valores


def clean_result_name(filename):
    partes = filename.split('_')
    filename = partes[-1]
    filename = filename.replace('.csv','')
    return filename


directorio = '/Users/diegodelozada/PycharmProjects/PFG/BridgIT/ModelSEED_results_filtered'
archivos = os.listdir(directorio)

resultados = []
for archivo in archivos:
    if archivo.endswith('.csv'):
        ruta_archivo = os.path.join(directorio, archivo)
        resultado = best_result(ruta_archivo)
        try:
            resultado = resultado[1]
            reac_name = clean_result_name(archivo)
            resultado_final = resultado + (reac_name,)
            resultados.append(resultado_final)
        except IndexError:
            pass

df = pd.DataFrame(resultados, columns=['EC', 'Tanimoto_Score', 'ID'])
df['Real_EC'] = 0

df1 = pd.read_excel(r'../Data/modelSEED_Filtered_rxnInfo.xlsx')
for i in range(0, len(df)):
    ind = df.ID[i]
    ind = ind.replace('r', '')
    df.ID[i] = df1.ID[int(ind) - 1]

reac = pd.read_excel(r'../Data/modelSEED_rxnInfo.xlsx')
reac = reac[['ID', 'EC']]
df['Real_EC'] = 0


for i in range(0, len(df)):
    try:
        indice_fila_reac = reac[reac['ID'] == df.ID[i]].index[0]
        df.Real_EC[i] = reac.EC[indice_fila_reac]
    except IndexError:
        pass

df.to_excel('BridgIT_RESULTS.xlsx', index=False)


