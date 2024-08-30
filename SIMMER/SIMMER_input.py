import pandas as pd

reac = pd.read_excel(r'../ModelSEED_Filtered_rxnInfo.xlsx')

reaction = []
left_comp = []
right_comp = []
left_smiles = []
right_smiles = []

for items in range(0, len(reac.ID)):
    reaction.append(f'DM{items + 1}')
    left_comp.append('a')
    right_comp.append('b')
    a = reac.REACTION_SMILE[items]
    s1 = ''
    s2 = ''
    var = 0
    for i in range(0, len(reac.REACTION_SMILE[items])):
        if a[i] != '>' and var == 0:
            s1 += a[i]
        else:
            var = 1
        if var == 1:
            s2 += a[i]
    s2 = s2.replace('>>', '')
    left_smiles.append(s1)
    right_smiles.append(s2)

data = {'reaction': reaction, 'left_comp': left_comp, 'right_comp': right_comp, 'left_smiles': left_smiles, 'right_smiles': right_smiles}
df1 = pd.DataFrame(data)
df1.to_csv('SIMMER.tsv', sep='\t', index=False)

