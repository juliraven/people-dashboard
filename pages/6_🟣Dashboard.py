import streamlit as st

page_bg_img_sidebar = """
<style>
[data-testid="stSidebar"] {
    background: radial-gradient(circle at 51% 50%, #202125, #2d035e, #b444fb); 
    background-blend-mode: multiply;
    background-size: cover;
    overflow: hidden; 
}

header[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

body {
    background-color: #202125; 
}

</style>
"""

st.markdown(page_bg_img_sidebar, unsafe_allow_html=True)

import numpy as np
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard ludności Europy (2015–2024)")

df = pd.read_excel('plik.xlsx')

# Transspozycja danych do wykresów:
df1 = df.melt(id_vars=["Country"], var_name="Year", value_name="Population")
df1["Year"] = df1["Year"].astype(int)

# Filtr wyboru kraju/krajów:
countries = df["Country"].unique()
selected = st.sidebar.multiselect("Wybierz kraj(e)", countries, default=["Poland"])

# Filtrowanie danych:
df2 = df1[df1["Country"].isin(selected)]






