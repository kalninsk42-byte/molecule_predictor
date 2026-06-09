import pandas as pd
from rdkit import Chem

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    df = df.dropna()

    def valid(smiles):
        return Chem.MolFromSmiles(smiles) is not None

    df = df[df["smiles"].apply(valid)]
    return df