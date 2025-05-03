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

st.set_page_config(page_title="Analiza Filmów Grozy", layout="wide")
st.title("🎬 Analiza Filmów Grozy")

# Wczytywanie danych z internetu (zamień URL na własny!)
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/nazwouzytkownika/projekt/main/horror_movies.csv"
    df = pd.read_csv(url)
    df.columns = [col.lower().strip().replace(" ", "_") for col in df.columns]  # snake_case
    return df

df = load_data()

# Czyszczenie danych
df = df.dropna(subset=["title", "year", "rating"])
df["year"] = df["year"].astype(int)

# Panel boczny z filtrami
st.sidebar.header("🎛️ Filtry")
years = st.sidebar.slider("Zakres lat", int(df["year"].min()), int(df["year"].max()), (1990, 2020))
min_rating = st.sidebar.slider("Minimalna ocena", 0.0, 10.0, 5.0, 0.1)
country = st.sidebar.selectbox("Kraj produkcji", options=["Wszystkie"] + sorted(df["country"].dropna().unique().tolist()))

filtered_df = df[
    (df["year"] >= years[0]) & (df["year"] <= years[1]) &
    (df["rating"] >= min_rating)
]
if country != "Wszystkie":
    filtered_df = filtered_df[filtered_df["country"] == country]

# Statystyki
st.subheader("📊 Statystyki")

col1, col2 = st.columns(2)

with col1:
    movies_per_year = filtered_df.groupby("year")["title"].count()
    st.markdown("**Liczba filmów rocznie**")
    fig, ax = plt.subplots()
    sns.barplot(x=movies_per_year.index, y=movies_per_year.values, ax=ax)
    ax.set_xlabel("Rok")
    ax.set_ylabel("Liczba filmów")
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    avg_rating_per_year = filtered_df.groupby("year")["rating"].mean()
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
top_movies = filtered_df.sort_values(by="rating", ascending=False).head(top_n)

# Wyświetlanie tabeli z plakatami i tytułami
for _, row in top_movies.iterrows():
    cols = st.columns([1, 4])
    with cols[0]:
        if pd.notna(row.get("poster_link", None)):
            st.image(row["poster_link"], width=100)
        else:
            st.image("https://via.placeholder.com/100x150.png?text=Brak+plakatu", width=100)
    with cols[1]:
        st.markdown(f"**{row['title']}** ({row['year']}) — {row['rating']}⭐")
        if "description" in row and pd.notna(row["description"]):
            st.caption(row["description"])




