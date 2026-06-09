from src.data_loader import load_data, clean_data
from src.features import build_features
from src.train import train_model
from src.evaluate import evaluate
import joblib

# Load data
df = load_data("data/esol.csv")

# Clean data
df = clean_data(df)

# Features + target
X, y = build_features(df)

# Train
model, X_test, y_test = train_model(X, y)

# Evaluate
evaluate(model, X_test, y_test)

# Save model
joblib.dump(model, "models/model.pkl")

print("\nDONE")