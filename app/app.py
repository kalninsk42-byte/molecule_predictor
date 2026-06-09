import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.predict import predict

st.title("Molecule Solubility Predictor")

st.write("Enter 5 features:")

mw = st.number_input("Molecular Weight")
hbd = st.number_input("H-Bond Donors")
rings = st.number_input("Number of Rings")
rot = st.number_input("Rotatable Bonds")
psa = st.number_input("Polar Surface Area")

if st.button("Predict"):
    features = [mw, hbd, rings, rot, psa]
    result = predict(features)
    st.success(f"Predicted solubility: {result}")