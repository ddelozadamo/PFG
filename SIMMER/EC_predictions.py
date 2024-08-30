import os
import pandas as pd

# Especifica la ruta de tu carpeta
carpeta = '../SIMMER_out/'

# Obtén la lista de archivos en la carpeta
archivos_en_carpeta = os.listdir(carpeta)

# Filtra los archivos que contienen la palabra "EC" en su nombre
archivos_ec = [archivo for archivo in archivos_en_carpeta if 'EC' in archivo]

for file in archivos_ec:
    data = pd.read_csv(carpeta + file, sep='\t')

    data = data[['EC', 'p_val']]

    for i in range(len(data['EC'])):
        ec = str(data['EC'][i])
        ec = ec.split('.')
        if len(ec) == 1:
            ec = ec + ['0', '0', '0']

        if len(ec) == 2:
            ec = ec + ['0', '0']

        if len(ec) == 3:
            ec = ec + ['0']

        ec = '.'.join(ec)
        data['EC'][i] = ec

    ruta_archivo_tsv = f'SIMMER_EC_PREDS/result_{file}'

    data.to_csv(ruta_archivo_tsv, sep='\t', index=False)




