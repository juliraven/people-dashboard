
import streamlit as st

st.title("Czym jest Streamlit?")

st.markdown(
    '''
    <p>
    <a href="https://streamlit.io" style="color:red; font-weight:bold;">Streamlit</a> umożliwia tworzenie interaktywnych aplikacji internetowych opartych na danych.
    Aplikacje można tworzyć wyłącznie z użyciem Pythona i bez konieczności używania innych technologii, takich jak JavaScript, HTML, CSS.
    Dokumentacja dostępna jest na stronie: 
    <a href="https://docs.streamlit.io" target="_blank">dokumentacja</a>.
    Utworzoną aplikację można w łatwy sposób wdrożyć dzięki chmurze za pomocą kilku kliknięć.
    </p>
    ''',
    unsafe_allow_html=True
)
