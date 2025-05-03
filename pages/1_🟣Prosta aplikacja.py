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

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Tytuł aplikacji
st.title("🎬 Analiza Filmów Grozy")

# Wczytanie danych
@st.cache_data
def load_data():
    return pd.read_csv("horror_movies.csv")

df = load_data()

# Wstępne czyszczenie danych
df = df.dropna(subset=["Title", "Year", "Rating"])
df["Year"] = df["Year"].astype(int)

# Panel boczny z filtrami
st.sidebar.header("🎛️ Filtry")
years = st.sidebar.slider("Zakres lat", int(df["Year"].min()), int(df["Year"].max()), (1990, 2020))
min_rating = st.sidebar.slider("Minimalna ocena", 0.0, 10.0, 5.0, 0.1)
country = st.sidebar.selectbox("Kraj produkcji", options=["Wszystkie"] + sorted(df["Country"].dropna().unique().tolist()))

filtered_df = df[
    (df["Year"] >= years[0]) & (df["Year"] <= years[1]) &
    (df["Rating"] >= min_rating)
]
if country != "Wszystkie":
    filtered_df = filtered_df[filtered_df["Country"] == country]

# Sekcja: Statystyki ogólne
st.subheader("📊 Statystyki")

col1, col2 = st.columns(2)

with col1:
    movies_per_year = filtered_df.groupby("Year")["Title"].count()
    st.markdown("**Liczba filmów rocznie**")
    fig, ax = plt.subplots()
    sns.barplot(x=movies_per_year.index, y=movies_per_year.values, ax=ax)
    ax.set_xlabel("Rok")
    ax.set_ylabel("Liczba filmów")
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    avg_rating_per_year = filtered_df.groupby("Year")["Rating"].mean()
    st.markdown("**Średnia ocena wg roku**")
    fig, ax = plt.subplots()
    sns.lineplot(x=avg_rating_per_year.index, y=avg_rating_per_year.values, ax=ax, marker="o")
    ax.set_xlabel("Rok")
    ax.set_ylabel("Średnia ocena")
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Sekcja: Top filmy
st.subheader("⭐ Top filmy wg oceny")

top_n = st.slider("Ile filmów pokazać?", 5, 50, 10)
top_movies = filtered_df.sort_values(by="Rating", ascending=False).head(top_n)

# Wyświetlanie tabeli z plakatami i tytułami
for i, row in top_movies.iterrows():
    cols = st.columns([1, 4])
    with cols[0]:
        if pd.notna(row.get("Poster_Link", None)):
            st.image(row["Poster_Link"], width=100)
        else:
            st.image("https://via.placeholder.com/100x150.png?text=Brak+plakatu", width=100)
    with cols[1]:
        st.markdown(f"**{row['Title']}** ({row['Year']}) — {row['Rating']}⭐")
        if "Description" in row and pd.notna(row["Description"]):
            st.caption(row["Description"])



