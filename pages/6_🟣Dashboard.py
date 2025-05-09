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

from pandasdmx import Request

# Tworzymy obiekt zapytania do Eurostat
estat = Request('ESTAT')

# Pobieramy dane (może to chwilę potrwać)
response = estat.data(resource_id='tps00001')

# Konwertujemy dane do DataFrame
data = response.to_pandas()

st.dataframe(data.head())



