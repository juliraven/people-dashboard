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

add_logo('logo.svg', height=350)


