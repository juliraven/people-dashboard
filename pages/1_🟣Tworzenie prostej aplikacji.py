import streamlit as st
from streamlit_extras.app_logo import add_logo

add_logo('logo.png', height=350)

st.sidebar.markdown(
    """
    <style>
        }
        [data-testid="stSidebar"] {
            padding-top: 0px;
            padding: 10px;
            font-family: sans-serif;
            font-size: 18px;
            width: 150px !important; /* Wymuszenie */
            min-width: 150px !important;
            max-width: 150px !important;
        }

        [data-testid="stSidebarHeader"] {
            height: 30px;
            padding: 5px 10px; 
            margin: 0; 
            display: flex; 
            align-items: center;
            justify-content: center; 
        }
        .main {
            margin-left: 170px;
    </style>
    """,
    unsafe_allow_html=True,
)

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

    # Wczytanie danych z pliku csv:
    df = pd.read_csv("data.csv")

    # Ujednolicenie nazw kolumn (zamiana wszystkich liter na małe i usunięcie białych znaków):
    df.columns = [x.lower().strip() for x in df.columns]

    # Utworzenie kolumny z rokiem premiery filmu na podstawie kolumny release_date:
    df["release_year"] = pd.to_datetime(df["release_date"], errors="coerce").dt.year

    # Pozostawienie filmów, które mają przypisany plakat (poster_path nie jest pusty ani NaN):
    df = df[df["poster_path"].notna() & (df["poster_path"].str.strip() != "")]

    # Dodanie pełnego url do plakatu filmu na podstawie ścieżki poster_path:
    df["poster_url"] = "https://image.tmdb.org/t/p/w200" + df["poster_path"]

    # Usunięcie wierszy, w których brakuje tytułu, roku premiery lub oceny:
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
# Nagłówek filtrów:
st.sidebar.header("🎛️ Filtry")

# Pobranie minimalnego i maksymalnego roku z danych:
year_min, year_max = int(df["release_year"].min()), int(df["release_year"].max())

# Suwak do wyboru zakresu lat produkcji filmów:
years = st.sidebar.slider("Zakres lat:", year_min, year_max, (2000, 2020))

# Suwak do wyboru minimalnej oceny filmu:
min_rating = st.sidebar.slider("Minimalna ocena:", 0.0, 10.0, 5.0, 0.1)

# Lista rozwijana do wyboru języka oryginalnego (z opcją "wszystkie"):
lang = st.sidebar.selectbox("Język oryginalny:", options=["wszystkie"] + sorted(df["original_language"].dropna().unique().tolist()))

# Filtrowanie danych wg wybranych wartości (rok, ocena, język):
filtered_df = df[
    (df["release_year"] >= years[0]) & (df["release_year"] <= years[1]) &
    (df["vote_average"] >= min_rating)
]

# Dodatkowe filtrowanie po języku, jeśli użytkownik nie wybrał "wszystkie":
if lang != "wszystkie":
    filtered_df = filtered_df[filtered_df["original_language"] == lang]
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Następnym krokiem może być utworzenie prostego wykresu słupkowego. W przypadku naszej aplikacji będzie to wykres przedstawiający liczbę wyprodukowanych filmów grozy na przestrzeni lat. W tym celu można uprzednio pogrupować dane po roku i zliczyć liczbę filmów w każdym roku:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
movies_per_year = (
    filtered_df.groupby("release_year")["title"]
    .count()
    .reset_index(name="liczba_filmów")
)
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Następnie można narysować wykres z wykorzystaniem <code>plotly.express</code> i wyświetlić go w aplikacji:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
fig1 = px.bar(
    movies_per_year,
    x="release_year",
    y="liczba_filmów",
    title="Liczba wyprodukowanych filmów wg roku",
    labels={"release_year": "Rok", "liczba_filmów": "Liczba filmów"}
)

fig1.update_layout(title_x=0.4)

fig1.update_traces(
    marker_color="rgba(180, 68, 251, 0.2)", 
    marker_line_color="rgba(180, 68, 251, 1)",
    marker_line_width=2
)

st.plotly_chart(fig1, use_container_width=True)
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    W naszej aplikacji utworzyłyśmy dodatkowo ranking filmów według ocen użytkowników. Uzytkownik ma możliwość wyboru liczby wyświetlanych filmów dzięki wbudowanemu suwakowi. Oto kod pozwalający utworzyć taki ranking:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
# Nagłówek sekcji:
st.subheader("⭐ Top filmy wg oceny")

# Suwak do wyboru liczby filmów do pokazania:
top_n = st.slider("Ile filmów pokazać:", 5, 50, 10)

# Sortowanie filmów malejąco wg oceny i wybranie top N filmów:
top_movies = filtered_df.sort_values(by="vote_average", ascending=False).head(top_n)

# Wyświetlanie każdego filmu z listy top N:
for _, row in top_movies.iterrows():
    cols = st.columns([1, 4])
    with cols[0]:
        st.image(row["poster_url"], width=100)
    with cols[1]:
        st.markdown(f"**{row['title']}** ({int(row['release_year'])}) — {row['vote_average']}⭐")
        
        # Jeśli jest dostępny opis (overview), pokaż go:
        if pd.notna(row.get("overview", "")):
            st.caption(row["overview"])
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Utworzona w ten sposób aplikacja znajduje się w zakładce 🟣Prosta aplikacja.
    </p>
    ''',
    unsafe_allow_html=True
)

st.page_link("pages/2_🟣Prosta aplikacja.py", label="➡️ Przejdź do zakładki:  **Prosta aplikacja**")
