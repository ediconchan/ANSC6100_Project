#importing necessary libraries
import numpy as np
import pandas as pd
from rdkit.Chem import AllChem
from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.ML.Descriptors import MoleculeDescriptors

def morgan_fpts(data):
    Morgan_fpts = []
    for i in data:
        mol = Chem.MolFromSmiles(i) 
        fpts =  AllChem.GetMorganFingerprintAsBitVect(mol,2,4096)
        mfpts = np.array(fpts)
        Morgan_fpts.append(mfpts)  
    return np.array(Morgan_fpts)

erbb1_df = pd.read_csv("erbb1_singleprotein_neglog10_ic50.csv")
Morgan_fpts = morgan_fpts(erbb1_df['canonical_smiles'])
print(Morgan_fpts.shape)

Morgan_fingerprints = pd.DataFrame(Morgan_fpts,columns=['Col_{}'.format(i) for i in range(Morgan_fpts.shape[1])])
print(Morgan_fingerprints)

# result = pd.concat([Morgan_fingerprints, erbb1_df.loc[['standard_value']]], axis=1, ignore_index=True)
response = erbb1_df[['-log(M)']]

result = Morgan_fingerprints.join(response)

print(result.shape)
print(result)

counts = result.nunique()
print('counts = \n', counts, type(counts), '\n')

to_del = [i for i, v in enumerate(counts) if v ==1]
print('columns to delete: ', to_del)

result.drop(result.columns[to_del], axis = 1, inplace=True)
print("Data frame size: ", result.shape)
print(result)

dups = result.duplicated()
dups2 = result.T.duplicated()

print("Duplicated rows: ", dups)
print("Duplicated columns: ", dups2)

print(result[dups])
print(result.T[dups2])
print(result.dtypes)

result.to_csv("erbb1_singleprotein_neglog10_ic50_fingerprint.csv")
