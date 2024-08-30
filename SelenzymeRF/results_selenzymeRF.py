import pandas as pd
import os

directorio = '/Users/diegodelozada/E-zyme/SelenzymeRF_results/'

archivos_csv = [f for f in os.listdir(directorio) if f.endswith('.csv')]
df_ec_numbers = pd.read_excel('/Users/diegodelozada/E-zyme/modelSEED_EC_Numbers.xlsx')
df_consolidado = pd.DataFrame()

for archivo in archivos_csv:
    ruta_completa = os.path.join(directorio, archivo)
    
    nombre_reaccion = archivo.replace('.csv', '')
    
    df = pd.read_csv(ruta_completa)
    df = df[['0','7']]
    df = df.dropna()
    df.columns = ['Score', 'EC Number']
    df = df.drop_duplicates(subset='EC Number', keep='first')

    if 'EC Number' in df.columns:
        # Crea un DataFrame temporal con el nombre de la reacción y los EC numbers
        df_temp = pd.DataFrame({
            'Reaction': nombre_reaccion,
            'EC': df['EC Number']
        })
        
        # Concatena este DataFrame con el consolidado
        df_consolidado = pd.concat([df_consolidado, df_temp], ignore_index=True)

# Agrupa por reacción y concatena los EC numbers separados por '|'
df_final = df_consolidado.groupby('Reaction')['EC'].agg('|'.join).reset_index()

df_merged = pd.merge(df_final, df_ec_numbers, on='Reaction', how='left')
df_merged['EC'] = df_merged['EC'].str.replace(';', '|')

# Guarda el DataFrame consolidado en un nuevo archivo CSV
ruta_final = '/Users/diegodelozada/E-zyme/Results_SelenzymeRF.xlsx'
df_merged.to_excel(ruta_final, index=False)
