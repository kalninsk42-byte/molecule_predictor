def build_features(df):
    feature_cols = [
        "Molecular Weight",
        "Number of H-Bond Donors",
        "Number of Rings",
        "Number of Rotatable Bonds",
        "Polar Surface Area"
    ]

    X = df[feature_cols]
    y = df["measured log solubility in mols per litre"]

    return X, y