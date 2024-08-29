import pandas as pd
import os

carpeta = '/Users/diegodelozada/PycharmProjects/PFG/BridgIT/BridgIT_results'
files = os.listdir(carpeta)

for file in files:
    # Verifica que el archivo tenga una extensión .txt
    if file.endswith('.txt'):
        ruta_completa = os.path.join(carpeta, file)
        archivo_txt = ruta_completa

        resultados = os.path.splitext(os.path.basename(ruta_completa))[0]

        data = pd.read_csv(archivo_txt, sep='\t', header=0)

        data = data[['reactionsA/ECA', 'Tanimoto_FBI_Scores']]
        data = data[data['Tanimoto_FBI_Scores'] > 0.1]

        if len(data['Tanimoto_FBI_Scores']):

            filtered_data = pd.DataFrame(columns=['EC_Number', "Tanimoto_score"])
            tanimoto = []

            EC = []
            for i in range(len(data['reactionsA/ECA'])):
                a = data['reactionsA/ECA'][i].split('/')
                scores = a[-1]
                scores = scores.replace(';', '')
                if len(scores) >= 2:
                    scores = scores.split(',')
                    for j in range(len(scores)):
                        tanimoto.append(data['Tanimoto_FBI_Scores'][i])
                        EC.append(scores[j])
                else:
                    EC.append(scores)
                    tanimoto.append(data['Tanimoto_FBI_Scores'][i])

            filtered_data = pd.DataFrame({
                'EC_Number': EC,
                'Tanimoto_score': tanimoto,
            })
            filtered_data = filtered_data.groupby('EC_Number')['Tanimoto_score'].max().reset_index()

            filtered_data.to_csv(f'ModelSEED_results_filtered/{resultados}.csv', index=False)
