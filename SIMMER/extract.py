import os
import csv
import re
import pandas as pd

# Ruta de la carpeta que contiene los archivos TSV
carpeta = "SIMMER_EC_PREDS"
reac = pd.read_excel(r'../ModelSEED_Filtered_rxnInfo.xlsx')
reac['EC_SIMMER'] = ''


def clases_distintas_de_cero(ec_number):
    clases = ec_number.split(".")[:3]  # Obtener las primeras tres clases
    if '0' in clases:
        return True


EC = []
ec_preds = []
patron_numero = re.compile(r'\d+')

for archivo in os.listdir(carpeta):
    if archivo.endswith(".tsv"):  # Verificar si el archivo es un archivo TSV
        ruta_archivo = os.path.join(carpeta, archivo)
        ec_preds = []

        # Abrir el archivo TSV y leerlo utilizando el módulo csv
        with open(ruta_archivo, "r", newline="", encoding="utf-8") as f:
            lector_tsv = csv.reader(f, delimiter="\t")
            next(lector_tsv)  # Saltar la primera fila que contiene los encabezados
            numero = patron_numero.search(archivo).group()
            for fila in lector_tsv:
                ec_number = fila[0]  # Obtener el EC number de la fila
                if not clases_distintas_de_cero(ec_number):
                    ec_preds.append(ec_number)
        ec_preds = "|".join(ec_preds)
        reac.EC_SIMMER[int(numero) - 1] = ec_preds


reac.to_excel('ModelSEED_simmer_EC_rxnInfo.xlsx', index=True)
