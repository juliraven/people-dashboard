import streamlit as st

page_bg_img_sidebar = """
<style>
[data-testid="stSidebar"] {
    background: radial-gradient(circle at 51% 40%, #b444fb, #2d035e, #202125); 
    background-blend-mode: multiply;
    background-size: cover;
    overflow: hidden; /* Prevent scrolling */
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

st.title("Tworzenie prostej aplikacji")

st.markdown(
    '''
    <p>
    W celu utworzenia prostej aplikacji zawierającej wizualizacje danych np. zawartych w pliku z rozszerzeniem <code>.csv</code>, należy ten plik umieścić w repozytorium wraz z innymi plikami. Repozytorium będzie miało wtedy następującą strukturę:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
app/
├── home.py
├── requirements.txt
├── data.csv
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Po dodaniu danych można zacząć tworzyć aplikację w pliku <code>home.py</code>. Na samym początku zwykle umieszcza się importy niezbędnych bibliotek, np.:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Następnie można nadać tytuł naszej aplikacji wykorzystując do tego polecenie <code>st.title()</code>, np.:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
st.title("🎬 Analiza filmów grozy")
'''

st.code(code, language='python')
