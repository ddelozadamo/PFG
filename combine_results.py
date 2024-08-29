import os
import shutil

source_folders = [
    '/Users/diegodelozada/Downloads/ModelSEED1',
    '/Users/diegodelozada/Downloads/ModelSEED2',
    '/Users/diegodelozada/Downloads/ModelSEED3',
    '/Users/diegodelozada/Downloads/ModelSEED4',
    '/Users/diegodelozada/Downloads/ModelSEED5',
    '/Users/diegodelozada/Downloads/ModelSEED6',
    '/Users/diegodelozada/Downloads/ModelSEED7',
    '/Users/diegodelozada/Downloads/ModelSEED8',
    '/Users/diegodelozada/Downloads/ModelSEED9',
    '/Users/diegodelozada/Downloads/ModelSEED10',
    '/Users/diegodelozada/Downloads/ModelSEED11'
]
destination_folder = '/Users/diegodelozada/PycharmProjects/PFG/BridgIT/BridgIT_results'

for folder in source_folders:
    for filename in os.listdir(folder):
        source_file = os.path.join(folder, filename)
        destination_file = os.path.join(destination_folder, filename)
        if os.path.isfile(source_file):  # Asegura que es un archivo y no una carpeta
            shutil.copy(source_file, destination_file)
            # Use shutil.move(source_file, destination_file) para mover en lugar de copiar

