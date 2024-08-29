library(RxnSim)
library(readxl)

met_info <- read_excel("/Users/diegodelozada/PycharmProjects/PFG/Data/modelSEED_metInfo_1.xlsx")
met_info$CANONICAL_SMILES[met_info$CANONICAL_SMILES == 0] <- NA
met_info_clean <- met_info[!is.na(met_info$CANONICAL_SMILES), ]
smiles <- met_info_clean$CANONICAL_SMILES

similarity <- read.csv('/Users/diegodelozada/E-zyme/similarity_matrix.csv')
index <- read_excel('/Users/diegodelozada/PycharmProjects/PFG/BridgIT/Bridgit_index.xlsx')

similarity <- similarity[,-1]

indices <- match(met_info_clean$NAME, index$NAME)
# Filtrar las filas de 'index' que coinciden
matched_rows <- index[indices, , drop = FALSE]  # drop = FALSE para mantener como DataFrame

df <- data.frame(
  x = matched_rows$NAME,  # Nueva columna con algunos datos
  similarity  # DataFrame original
)

# similarity_matrix = ms.compute.sim.matrix(
#   molA = smiles,
#   format = 'smiles',              # Formato de las moléculas
#   standardize = TRUE,             # Estándar para simplificar las moléculas
#   explicitH = FALSE,              # No convertir hidrógenos implícitos en explícitos
#   sim.method = 'tanimoto',        # Método de similaridad
#   fp.type = 'extended',           # Tipo de huella digital extendida
#   fp.mode = 'bit',                # Modo de huella digital en bits
#   fp.depth = 6,                   # Profundidad de la búsqueda para la huella digital
#   fp.size = 1024,                 # Tamaño del string de bits de la huella digital
#   clearCache = TRUE               # Limpiar caché antes de calcular
# )
# matriz <- similarity_matrix
similarity <- similarity[,-1]
rownames(similarity) <- matched_rows$NAME
colnames(similarity) <- matched_rows$NAME
# 
# 
write.csv(df, "/Users/diegodelozada/E-zyme/similarity_matrix.csv", row.names = TRUE)
