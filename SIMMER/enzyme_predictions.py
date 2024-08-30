import os
import pandas as pd

# Especifica la ruta de tu carpeta
carpeta = '/Users/diegodelozada/Desktop/output_SIMMER/'

# Obtén la lista de archivos en la carpeta
archivos_en_carpeta = os.listdir(carpeta)

# Filtra los archivos que contienen la palabra "EC" en su nombre
archivos_ec = [archivo for archivo in archivos_en_carpeta if 'enzyme' in archivo]

for file in archivos_ec:
    if os.path.getsize(carpeta + file) > 2:
        data = pd.read_csv(carpeta + file, sep='\t')

        data = data[['hit_id', 'Lineage']]

        for i in range(len(data['Lineage'])):
            lineage = str(data['Lineage'][i])
            lineage = lineage.split(';')
            lineage = lineage[-1]
            data['Lineage'][i] = lineage

        ruta_archivo_tsv = f'/Users/diegodelozada/Desktop/SIMMER_enzyme_PREDS/result_{file}'

        data.to_csv(ruta_archivo_tsv, sep='\t', index=False)
