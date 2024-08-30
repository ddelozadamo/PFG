import pandas as pd
import os

directorio = '/Users/diegodelozada/E-zyme/E-zyme2_results/'

try:
    archivos_csv = [f for f in os.listdir(directorio) if f.endswith('.csv')]
    df_ec_numbers = pd.read_excel('/Users/diegodelozada/E-zyme/modelSEED_EC_Numbers.xlsx')
    df_consolidado = pd.DataFrame()

    for archivo in archivos_csv:
        ruta_completa = os.path.join(directorio, archivo)
        nombre_reaccion = archivo.replace('.csv', '')
        df = pd.read_csv(ruta_completa)
        df.columns = ['RPAIR', 'score', 'EC', 'KO']

        # Asegurarse que la columna 'EC' contiene solo strings y no es NaN
        df['EC'] = df['EC'].astype(str)
        df['EC'] = df['EC'].replace('nan', '')  # Reemplazar 'nan' por cadena vacía

        # Expandir las entradas de EC separadas por '\n' y apilar los resultados
        df_expanded = df['EC'].str.split('\n').explode().reset_index(drop=True)

        # Filtrar para mantener solo entradas que coinciden con el patrón de números EC
        df_filtered = df_expanded[df_expanded.str.match(r'^\d+\.\d+\.\d+\.\d+$')].drop_duplicates()

        # Concatenar todos los EC numbers únicos con '|'
        ec_numbers_concatenated = '|'.join(df_filtered.tolist())

        # Crea un DataFrame temporal con el nombre de la reacción y los EC numbers         
        df_temp = pd.DataFrame({
            'Reaction': [nombre_reaccion],
            'EC': [ec_numbers_concatenated] if not df_filtered.empty else ['']
        })
        
        # Concatena este DataFrame con el consolidado
        df_consolidado = pd.concat([df_consolidado, df_temp], ignore_index=True)

    df_merged = pd.merge(df_consolidado, df_ec_numbers, on='Reaction', how='left')
    ruta_final = '/Users/diegodelozada/E-zyme/Results_E-zyme2.xlsx'
    df_merged.to_excel(ruta_final, index=False)

except Exception as e:
    print(f"Se produjo un error: {e}")
