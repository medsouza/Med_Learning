import streamlit as st
import pandas as pd
from sklearn.datasets import load_wine

st.title("Med Learning Dashboard")

st.markdown(
    """
    This simple Streamlit app demonstrates how to run an interactive dashboard
    within this repository. It loads the classic wine dataset from
    `scikit-learn` and displays the first few rows.
    """
)

# Load sample data
wine = load_wine(as_frame=True)
df = wine.frame

st.subheader("Wine Dataset Preview")
st.dataframe(df.head())
