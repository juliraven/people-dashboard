import streamlit as st

st.title("Czym jest Streamlit?")

st.markdown(
    '''
    <p>
    <span style="color:red; font-weight:bold;">Streamlit</span> umożliwia tworzenie interaktywnych aplikacji internetowych opartych na danych.
    Aplikacje można tworzyć wyłącznie z użyciem Pythona i bez konieczności używania innych technologii, takich jak JavaScript, HTML, CSS.
    Dokumentacja dostępna jest na stronie: 
    <a href="https://docs.streamlit.io" style="color:purple; font-weight:bold;">dokumentacja</a>.
    Utworzoną aplikację można w łatwy sposób wdrożyć dzięki <a href="https://docs.streamlit.io/" style="color:purple; font-weight:bold;">chmurze</a> za pomocą kilku kliknięć.
    </p>
    ''',
    unsafe_allow_html=True
)

from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Analiza sentymentu", page_icon="🎥", layout="wide")

add_logo('logo.png', height=350)

st.sidebar.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            padding-top: 0px;
            padding: 10px;
            font-family: sans-serif;
            font-size: 18px;
        }

        [data-testid="stSidebarHeader"] {
            height: 30px;
            padding: 5px 10px; 
            margin: 0; 
            display: flex; 
            align-items: center;
            justify-content: center; 
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {
        width: 350px;  /* Ustaw stałą szerokość */
        min-width: 350px;  /* Minimalna szerokość */
        max-width: 350px;  /* Maksymalna szerokość */
    }
    </style>
    """,
    unsafe_allow_html=True
)
