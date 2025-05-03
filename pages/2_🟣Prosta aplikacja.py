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

st.markdown(page_bg_img_sidebar, unsafe_allow_html=True, layout="wide")

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🎬 Analiza filmów grozy")

def load_data():
    df = pd.read_csv("horror_movies.csv")
    df.columns = [c.lower().strip() for c in df.columns]
    df["release_year"] = pd.to_datetime(df["release_date"], errors="coerce").dt.year

    # wybranie filmów, które mają plakat:
    df = df[df["poster_path"].notna() & (df["poster_path"].str.strip() != "")]
    df["poster_url"] = "https://image.tmdb.org/t/p/w200" + df["poster_path"]
    df = df.dropna(subset=["title", "release_year", "vote_average"])
    return df

df = load_data()

# filtry:
st.sidebar.header("🎛️ Filtry")
year_min, year_max = int(df["release_year"].min()), int(df["release_year"].max())
years = st.sidebar.slider("Zakres lat:", year_min, year_max, (2000, 2020))
min_rating = st.sidebar.slider("Minimalna ocena:", 0.0, 10.0, 5.0, 0.1)
lang = st.sidebar.selectbox("Język oryginalny:", options=["wszystkie"] + sorted(df["original_language"].dropna().unique().tolist()))

filtered_df = df[
    (df["release_year"] >= years[0]) & (df["release_year"] <= years[1]) &
    (df["vote_average"] >= min_rating)
]
if lang != "wszystkie":
    filtered_df = filtered_df[filtered_df["original_language"] == lang]


col1, col2 = st.columns(2)

with col1:
    movies_per_year = (
        filtered_df.groupby("release_year")["title"]
        .count()
        .reset_index(name="liczba_filmów")
    )
    fig1 = px.bar(movies_per_year, x="release_year", y="liczba_filmów",
                  title="Liczba filmów rocznie", labels={"release_year": "Rok", "liczba_filmów": "Liczba filmów"})
    st.plotly_chart(fig1, use_container_width=True)

with col2:
    avg_rating = (
        filtered_df.groupby("release_year")["vote_average"]
        .mean()
        .reset_index(name="średnia_ocena")
    )
    fig2 = px.line(avg_rating, x="release_year", y="średnia_ocena",
                   markers=True, title="Średnia ocena wg roku",
                   labels={"release_year": "Rok", "średnia_ocena": "Średnia ocena"})
    fig2.update_layout(title_x=0.5)
    fig2.update_traces(line_color="#b444fb")
    st.plotly_chart(fig2, use_container_width=True)

st.subheader("⭐ Top filmy wg oceny")
top_n = st.slider("Ile filmów pokazać:", 5, 50, 10)
top_movies = filtered_df.sort_values(by="vote_average", ascending=False).head(top_n)

for _, row in top_movies.iterrows():
    cols = st.columns([1, 4])
    with cols[0]:
        if pd.notna(row["poster_path"]) and row["poster_path"].strip():
            st.image(row["poster_url"], width=100)
        else:
            st.image("https://via.placeholder.com/100x150.png?text=Brak+plakatu", width=100)
    with cols[1]:
        st.markdown(f"**{row['title']}** ({int(row['release_year'])}) — {row['vote_average']}⭐")
        if pd.notna(row.get("overview", "")):
            st.caption(row["overview"])

