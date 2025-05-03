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

st.markdown(
    '''
    <p>
    Kolejnym krokiem może być wczytanie i przekształcenie danych do dalszej analizy. W naszej apliakcji używamy w tym celu poniższej funkcji:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
def load_data():

    # wczytanie danych z pliku csv:
    df = pd.read_csv("data.csv")

    # ujednolicenie nazw kolumn (zamiana wszystkich liter na małe i usunięcie białych znaków):
    df.columns = [x.lower().strip() for x in df.columns]

    # utworzenie kolumny z rokiem premiery filmu na podstawie kolumny release_date:
    df["release_year"] = pd.to_datetime(df["release_date"], errors="coerce").dt.year

    # pozostawienie filmów, które mają przypisany plakat (poster_path nie jest pusty ani NaN):
    df = df[df["poster_path"].notna() & (df["poster_path"].str.strip() != "")]

    # dodanie pełnego url do plakatu filmu na podstawie ścieżki poster_path:
    df["poster_url"] = "https://image.tmdb.org/t/p/w200" + df["poster_path"]

    # usunięcie wierszy, w których brakuje tytułu, roku premiery lub oceny:
    df = df.dropna(subset=["title", "release_year", "vote_average"])

    return df

df = load_data()
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    W celu dodania interakcji do aplikacji można utworzyć filtry, które pozwolą użytkownikowi zmieniać opcje w wyświetlanych wizualizacjach. Oto przykładowy kod tworzący takie filtry na pasku bocznym aplikacji:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
# nagłówek filtrów:
st.sidebar.header("🎛️ Filtry")

# pobranie minimalnego i maksymalnego roku z danych:
year_min, year_max = int(df["release_year"].min()), int(df["release_year"].max())

# suwak do wyboru zakresu lat produkcji filmów:
years = st.sidebar.slider("Zakres lat:", year_min, year_max, (2000, 2020))

# suwak do wyboru minimalnej oceny filmu:
min_rating = st.sidebar.slider("Minimalna ocena:", 0.0, 10.0, 5.0, 0.1)

# lista rozwijana do wyboru języka oryginalnego (z opcją "wszystkie"):
lang = st.sidebar.selectbox("Język oryginalny:", options=["wszystkie"] + sorted(df["original_language"].dropna().unique().tolist()))

# filtrowanie danych wg wybranych wartości (rok, ocena, język):
filtered_df = df[
    (df["release_year"] >= years[0]) & (df["release_year"] <= years[1]) &
    (df["vote_average"] >= min_rating)
]

# dodatkowe filtrowanie po języku, jeśli użytkownik nie wybrał "wszystkie":
if lang != "wszystkie":
    filtered_df = filtered_df[filtered_df["original_language"] == lang]
'''

st.code(code, language='python')
