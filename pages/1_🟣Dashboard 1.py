import streamlit as st

page_bg_img_sidebar = """
<style>
/* Ustawienie szerokości sidebaru */
section[data-testid="stSidebar"] {
    width: 340px !important;
    min-width: 340px !important;
    max-width: 340px !important;
    display: flex;
    align-items: center;       /* Wyśrodkowanie w pionie */
    justify-content: center;   /* Wyśrodkowanie w poziomie */
    flex-direction: column;
    height: 100vh;             /* Wysokość całego widoku */
    padding-top: 10px;
}

/* Styl samego wnętrza sidebaru */
[data-testid="stSidebar"] {
    background: linear-gradient(
        135deg,
        rgba(32, 33, 37, 0.6),
        rgba(45, 3, 94, 0.5),
        rgba(180, 68, 251, 0.4)
    );
    border: 1px solid rgba(180, 68, 251, 0.3);
    border-radius: 0px;
    padding: 24px;
    width: 100%;
    box-shadow:
        0 0 10px rgba(180, 68, 251, 0.25),
        0 4px 16px rgba(0, 0, 0, 0.25);
    backdrop-filter: blur(12px) brightness(1.05);
    background-blend-mode: overlay;
    transition: none;
    overflow: hidden;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;  /* Wyśrodkowanie zawartości */
}

/* Główna treść */
section.main > div {
    padding-left: 220px !important;
}

/* Nagłówek przezroczysty */
header[data-testid="stHeader"] {
    background-color: rgba(0, 0, 0, 0);
}

/* Tło strony */
body {
    background-color: #202125;
}
</style>
"""

st.markdown(page_bg_img_sidebar, unsafe_allow_html=True)

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pycountry
import numpy as np

st.title("Dashboard")

@st.cache_data
def load_data():
    df = pd.read_csv("igrzyska.csv")
    df = df[df["Year"] >= 2000]
    return df

df = load_data()

def noc_to_country_name(noc_code):
    try:
        country = pycountry.countries.get(alpha_3=noc_code) # Szuka kraju na podstawie kodu trzyliterowego
        if country:
            return country.name # Jeśli znajdzie, zwraca nazwę kraju
        else:
            return noc_code # Jeśli nie znajdzie, zwraca oryginalny kod
    except:
        return noc_code # W razie błędu (np. nieprawidłowy kod), również zwraca oryginalny kod

# Filtry w sidebar
st.sidebar.title("\U0001f3c5 Igrzyska Olimpijskie")
sex_option = st.sidebar.radio("Płeć", options=["Wszyscy", "Mężczyźni", "Kobiety"])
season_option = st.sidebar.radio("Sezon", options=["Letni i zimowy", "Letni", "Zimowy"])
min_year = int(df["Year"].min())
max_year = int(df["Year"].max())
year_range = st.sidebar.slider("Zakres lat", min_value=min_year, max_value=max_year, value=(min_year, max_year), step=1)
team_filter = st.sidebar.multiselect("Kraj", sorted(df["Team"].dropna().unique()), default=[])
sport_filter = st.sidebar.multiselect("Dyscyplina", sorted(df["Sport"].dropna().unique()), default=[])
medal_filter = st.sidebar.multiselect("Medal", options=["Gold", "Silver", "Bronze"], default=["Gold", "Silver", "Bronze"])

# Filtrowanie danych
filtered_df = df[df["Year"].between(year_range[0], year_range[1])]
if season_option == "Letni":
    filtered_df = filtered_df[filtered_df["Season"] == "Summer"]
elif season_option == "Zimowy":
    filtered_df = filtered_df[filtered_df["Season"] == "Winter"]
if sex_option == "Mężczyźni":
    filtered_df = filtered_df[filtered_df["Sex"] == "M"]
elif sex_option == "Kobiety":
    filtered_df = filtered_df[filtered_df["Sex"] == "F"]
if team_filter:
    filtered_df = filtered_df[filtered_df["Team"].isin(team_filter)]
if medal_filter:
    filtered_df = filtered_df[filtered_df["Medal"].isin(medal_filter)]
if sport_filter:
    filtered_df = filtered_df[filtered_df["Sport"].isin(sport_filter)]

# Sekcje 
section = st.sidebar.radio("Wybierz sekcję", ["🏠 Strona główna", "👥 Zawodnicy", "🥇 Medale", 
                                                 "📊 Dane fizyczne", "🔍 Dodatkowe wykresy"])

# Strona główna
if section == "🏠 Strona główna":

    total_athletes = filtered_df['ID'].nunique()
    total_teams = filtered_df['Team'].nunique()
    total_medals = filtered_df['Medal'].notna().sum()
    total_disciplines = filtered_df["Sport"].nunique()
    total_games = filtered_df['Games'].nunique()

    # 3 kolumny 
    col_kpi, col_map_trend, col_charts = st.columns([1, 3, 2]) # szerokość kolumn

    with col_kpi:
        st.metric("👤 Liczba zawodników", filtered_df['ID'].nunique())
        st.metric("🌍 Liczba krajów", filtered_df['Team'].nunique())
        st.metric("🥇 Liczba medali", filtered_df['Medal'].notna().sum())
        st.metric("🏅 Liczba dyscyplin", filtered_df["Sport"].nunique())
        st.metric("🏅 Liczba konkurencji", filtered_df["Event"].nunique())
        st.metric("📆 Liczba edycji", filtered_df['Games'].nunique())
        st.markdown("### ℹ️ Opis")
        st.markdown("""
        Dane wykorzystane w dashboardzie pochodzą z Igrzysk Olimpijskich w latach 2002-2016.
        Zawierają informacje wyłącznie o zawodnikach, którzy zdobyli medale (złote, srebrne i brązowe)
        i obejmują różne dyscypliny sportowe oraz kraje uczestniczące w igrzyskach.
        """)
    # Wykres mapy
    with col_map_trend:
        medals_country = (filtered_df[filtered_df['Medal'].notna()]
                          .groupby('NOC').size().reset_index(name='Medale'))
        fig_map = px.choropleth(
            medals_country,
            locations='NOC',
            color='Medale',
            hover_name='NOC',
            color_continuous_scale='Blues',
            title='Liczba medali zdobytych przez kraje',
            labels={'Medale': 'Liczba medali'}
        )
        fig_map.update_layout(height=400, margin=dict(t=50))
        st.plotly_chart(fig_map, use_container_width=True)
        # Wykres liniowy, trend
        participants_year_season = (filtered_df.groupby(['Year', 'Season'])['ID']
                                   .nunique().reset_index(name='Uczestnicy'))
        fig_line_participants = px.line(
            participants_year_season,
            x='Year',
            y='Uczestnicy',
            color='Season',
            markers=True,
            title='Trend liczby uczestników wg sezonu',
            color_discrete_map={'Winter': '#1f3b70', 'Summer': 'green'}
        )
        fig_line_participants.update_layout(
            xaxis=dict(tickmode='linear', tick0=participants_year_season['Year'].min(),
                       dtick=2, tickangle=-45),
            height=400 
        )
        fig_line_participants.update_yaxes(range=[0, participants_year_season['Uczestnicy'].max() + 200])
        st.plotly_chart(fig_line_participants, use_container_width=True)
    
    with col_charts:
        #Wykres kołowy
        medals_sex = (filtered_df[filtered_df['Medal'].notna()]['Sex']
                      .value_counts().reset_index(name="Count"))
        fig_pie_sex = px.pie(
            medals_sex,
            values='Count',
            names='Sex',
            title='Procentowy udział medali wg płci',
            color='Sex',
            color_discrete_map={'M': "#003eb1", 'F': 'deeppink'}
        )
        fig_pie_sex.update_layout(title={'text': 'Procentowy udział medali wg płci', 'x': 0.5, 'xanchor': 'center'}, height=400)
        st.plotly_chart(fig_pie_sex, use_container_width=True)
        # Wykres słupkowy
        medals = filtered_df[filtered_df['Medal'].notna()]
        countries_per_year = medals.groupby('Year')['Team'].nunique().reset_index(name='UniqueCountries')
        fig_bar_countries = px.bar(
            countries_per_year,
            x='Year',
            y='UniqueCountries',
            title='Liczba różnych krajów zdobywających medale w poszczególnych latach',
            labels={'UniqueCountries': 'Liczba krajów', 'Year': 'Rok'},
            text='UniqueCountries'
        )
        fig_bar_countries.update_layout(
            xaxis=dict(tickmode='linear', dtick=2, tickangle=-45),
            height=400,  # taka sama wysokość jak kołowy
            margin=dict(t=30, b=50)
        )
        fig_bar_countries.update_traces(textposition='outside')
        st.plotly_chart(fig_bar_countries, use_container_width=True)
    # Zbiór danych 
    with st.expander("Pokaż fragment danych (tabela)"):
        st.dataframe(filtered_df.head(20))
    # Kod
    with st.expander("📄 Kod źródłowy:"):
        st.code("""
        import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import pycountry
import numpy as np

st.set_page_config(page_title="Dashboard", layout="wide")

@st.cache_data
def load_data():
    df = pd.read_csv("igrzyska.csv")
    df = df[df["Year"] >= 2000]
    return df

df = load_data()

def noc_to_country_name(noc_code):
    try:
        country = pycountry.countries.get(alpha_3=noc_code) # Szuka kraju na podstawie kodu trzyliterowego
        if country:
            return country.name # Jeśli znajdzie, zwraca nazwę kraju
        else:
            return noc_code # Jeśli nie znajdzie, zwraca oryginalny kod
    except:
        return noc_code # W razie błędu (np. nieprawidłowy kod), również zwraca oryginalny kod

# Filtry w sidebar
st.sidebar.title("\U0001f3c5 Igrzyska Olimpijskie")
sex_option = st.sidebar.radio("Płeć", options=["Wszyscy", "Mężczyźni", "Kobiety"])
season_option = st.sidebar.radio("Sezon", options=["Letni i zimowy", "Letni", "Zimowy"])
min_year = int(df["Year"].min())
max_year = int(df["Year"].max())
year_range = st.sidebar.slider("Zakres lat", min_value=min_year, max_value=max_year, value=(min_year, max_year), step=1)
team_filter = st.sidebar.multiselect("Kraj", sorted(df["Team"].dropna().unique()), default=[])
sport_filter = st.sidebar.multiselect("Dyscyplina", sorted(df["Sport"].dropna().unique()), default=[])
medal_filter = st.sidebar.multiselect("Medal", options=["Gold", "Silver", "Bronze"], default=["Gold", "Silver", "Bronze"])

# Filtrowanie danych
filtered_df = df[df["Year"].between(year_range[0], year_range[1])]
if season_option == "Letni":
    filtered_df = filtered_df[filtered_df["Season"] == "Summer"]
elif season_option == "Zimowy":
    filtered_df = filtered_df[filtered_df["Season"] == "Winter"]
if sex_option == "Mężczyźni":
    filtered_df = filtered_df[filtered_df["Sex"] == "M"]
elif sex_option == "Kobiety":
    filtered_df = filtered_df[filtered_df["Sex"] == "F"]
if team_filter:
    filtered_df = filtered_df[filtered_df["Team"].isin(team_filter)]
if medal_filter:
    filtered_df = filtered_df[filtered_df["Medal"].isin(medal_filter)]
if sport_filter:
    filtered_df = filtered_df[filtered_df["Sport"].isin(sport_filter)]

# Sekcje 
section = st.sidebar.radio("Wybierz sekcję", ["🏠 Strona główna", "👥 Zawodnicy", "🥇 Medale", 
                                                 "📊 Dane fizyczne", "🔍 Dodatkowe wykresy"])

# Strona główna
if section == "🏠 Strona główna":

    total_athletes = filtered_df['ID'].nunique()
    total_teams = filtered_df['Team'].nunique()
    total_medals = filtered_df['Medal'].notna().sum()
    total_disciplines = filtered_df["Sport"].nunique()
    total_games = filtered_df['Games'].nunique()

    # 3 kolumny 
    col_kpi, col_map_trend, col_charts = st.columns([1, 3, 2]) # szerokość kolumn

    with col_kpi:
        st.metric("👤 Liczba zawodników", filtered_df['ID'].nunique())
        st.metric("🌍 Liczba krajów", filtered_df['Team'].nunique())
        st.metric("🥇 Liczba medali", filtered_df['Medal'].notna().sum())
        st.metric("🏅 Liczba dyscyplin", filtered_df["Sport"].nunique())
        st.metric("🏅 Liczba konkurencji", filtered_df["Event"].nunique())
        st.metric("📆 Liczba edycji", filtered_df['Games'].nunique())
        st.markdown("### ℹ️ Opis")
        st.markdown(
        Dane wykorzystane w dashboardzie pochodzą z Igrzysk Olimpijskich w latach 2002-2016.
        Zawierają informacje wyłącznie o zawodnikach, którzy zdobyli medale (złote, srebrne i brązowe)
        i obejmują różne dyscypliny sportowe oraz kraje uczestniczące w igrzyskach.
        )
    # Wykres mapy
    with col_map_trend:
        medals_country = (filtered_df[filtered_df['Medal'].notna()]
                          .groupby('NOC').size().reset_index(name='Medale'))
        fig_map = px.choropleth(
            medals_country,
            locations='NOC',
            color='Medale',
            hover_name='NOC',
            color_continuous_scale='Blues',
            title='Liczba medali zdobytych przez kraje',
            labels={'Medale': 'Liczba medali'}
        )
        fig_map.update_layout(height=400, margin=dict(t=50))
        st.plotly_chart(fig_map, use_container_width=True)
        # Wykres liniowy, trend
        participants_year_season = (filtered_df.groupby(['Year', 'Season'])['ID']
                                   .nunique().reset_index(name='Uczestnicy'))
        fig_line_participants = px.line(
            participants_year_season,
            x='Year',
            y='Uczestnicy',
            color='Season',
            markers=True,
            title='Trend liczby uczestników wg sezonu',
            color_discrete_map={'Winter': '#1f3b70', 'Summer': 'green'}
        )
        fig_line_participants.update_layout(
            xaxis=dict(tickmode='linear', tick0=participants_year_season['Year'].min(),
                       dtick=2, tickangle=-45),
            height=400 
        )
        fig_line_participants.update_yaxes(range=[0, participants_year_season['Uczestnicy'].max() + 200])
        st.plotly_chart(fig_line_participants, use_container_width=True)
    
    with col_charts:
        #Wykres kołowy
        medals_sex = (filtered_df[filtered_df['Medal'].notna()]['Sex']
                      .value_counts().reset_index(name="Count"))
        fig_pie_sex = px.pie(
            medals_sex,
            values='Count',
            names='Sex',
            title='Procentowy udział medali wg płci',
            color='Sex',
            color_discrete_map={'M': "#003eb1", 'F': 'deeppink'}
        )
        fig_pie_sex.update_layout(title={'text': 'Procentowy udział medali wg płci', 'x': 0.5, 'xanchor': 'center'}, height=400)
        st.plotly_chart(fig_pie_sex, use_container_width=True)
        # Wykres słupkowy
        medals = filtered_df[filtered_df['Medal'].notna()]
        countries_per_year = medals.groupby('Year')['Team'].nunique().reset_index(name='UniqueCountries')
        fig_bar_countries = px.bar(
            countries_per_year,
            x='Year',
            y='UniqueCountries',
            title='Liczba różnych krajów zdobywających medale w poszczególnych latach',
            labels={'UniqueCountries': 'Liczba krajów', 'Year': 'Rok'},
            text='UniqueCountries'
        )
        fig_bar_countries.update_layout(
            xaxis=dict(tickmode='linear', dtick=2, tickangle=-45),
            height=400,  # taka sama wysokość jak kołowy
            margin=dict(t=30, b=50)
        )
        fig_bar_countries.update_traces(textposition='outside')
        st.plotly_chart(fig_bar_countries, use_container_width=True)
    # Zbiór danych 
    with st.expander("Pokaż fragment danych (tabela)"):
        st.dataframe(filtered_df.head(20))
    # Kod
    with st.expander("📄 Kod źródłowy:"):
        st.code("""
    
        """, language='python')
        """, language='python')

# Zawodnicy
elif section == "👥 Zawodnicy":
    st.title("👥 Zawodnicy Igrzysk Olimpijskich")
    from scipy.stats import gaussian_kde
    # Dane do KDE
    ages_all = filtered_df[filtered_df['Age'].notna()]['Age']
    age_male = filtered_df[(filtered_df['Sex'] == 'M') & (filtered_df['Age'].notna())]['Age']
    age_female = filtered_df[(filtered_df['Sex'] == 'F') & (filtered_df['Age'].notna())]['Age']
    x_range = np.linspace(0, 75, 500)
    fig = go.Figure()
    if sex_option == "Wszyscy":
        if len(ages_all) > 1:
            kde_all = gaussian_kde(ages_all)
            fig.add_trace(go.Scatter(x=x_range, y=kde_all(x_range),mode='lines',name='Wszyscy',line=dict(color='green'),
                                     fill='tozeroy',opacity=0.3))
        if len(age_male) > 1:
            kde_male = gaussian_kde(age_male)
            fig.add_trace(go.Scatter(x=x_range, y=kde_male(x_range),mode='lines',name='Mężczyźni',line=dict(color='blue'),
                                     fill='tozeroy',opacity=0.6))
        if len(age_female) > 1:
            kde_female = gaussian_kde(age_female)
            fig.add_trace(go.Scatter(x=x_range, y=kde_female(x_range),mode='lines',name='Kobiety',line=dict(color='deeppink'),
                                     fill='tozeroy',opacity=0.6))
    elif sex_option == "Mężczyźni":
        if len(age_male) > 1:
            kde_male = gaussian_kde(age_male)
            fig.add_trace(go.Scatter(x=x_range, y=kde_male(x_range),mode='lines',name='Mężczyźni',line=dict(color='blue'),
                                     fill='tozeroy',opacity=0.6))
    elif sex_option == "Kobiety":
        if len(age_female) > 1:
            kde_female = gaussian_kde(age_female)
            fig.add_trace(go.Scatter(x=x_range, y=kde_female(x_range),mode='lines',name='Kobiety',line=dict(color='deeppink'),
                                     fill='tozeroy',opacity=0.6))
    # Wykres słupkowy
    participants_by_year_sex = (filtered_df.groupby(['Year', 'Sex'])['ID'].nunique().reset_index(name='Uczestnicy'))
    fig_bar_sex_year = px.bar(participants_by_year_sex,x='Year',y='Uczestnicy',color='Sex',barmode='group',
                              title='Liczba uczestników wg płci i roku',color_discrete_map={'M': 'blue', 'F': 'deeppink'})
    col1, col2 = st.columns(2)
    with col1:
        if len(fig.data) == 0:
            st.warning("Brak wystarczających danych do wyświetlenia wykresu.")
        else:
            fig.update_layout(
                title='Rozkład wieku zawodników wg płci',
                xaxis_title='Wiek',
                yaxis_title='Gęstość',
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig_bar_sex_year.update_layout(height=400)
        st.plotly_chart(fig_bar_sex_year, use_container_width=True)
    # Wykres słupkowy poziomy
    participants_by_country = (filtered_df.groupby('NOC')['ID'].nunique().sort_values(ascending=False).head(10)
                               .reset_index(name='Uczestnicy'))
    participants_by_country = participants_by_country.sort_values('Uczestnicy', ascending=True)
    fig_top_countries = px.bar(participants_by_country,x='Uczestnicy',y='NOC',orientation='h',
                               title='Top 10 krajów wg liczby uczestników')
    fig_top_countries.update_layout(yaxis_title='Kraj',xaxis_title='Liczba uczestników',yaxis={'categoryorder': 'total ascending'},
                                    height=400)
    # Tabela
    top_athletes_starts = (filtered_df["Name"].value_counts().head(10).reset_index()
                           .rename(columns={"Name": "Imię i nazwisko", "count": "Liczba startów"}))
    # kolumna od 1
    top_athletes_starts.insert(0, "Lp.", range(1, len(top_athletes_starts) + 1))
    # koljeność kolumn
    top_athletes_starts = top_athletes_starts[["Lp.", "Imię i nazwisko", "Liczba startów"]]
    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(fig_top_countries, use_container_width=True)
    with col4:
        st.markdown("**Top 10 zawodników wg liczby startów**")
        st.dataframe(top_athletes_starts, hide_index=True)
    # Kod
    with st.expander("📄 Kod źródłowy:"):
        st.code("""
                elif section == "👥 Zawodnicy":
    st.title("👥 Zawodnicy Igrzysk Olimpijskich")
    from scipy.stats import gaussian_kde
    # Dane do KDE
    ages_all = filtered_df[filtered_df['Age'].notna()]['Age']
    age_male = filtered_df[(filtered_df['Sex'] == 'M') & (filtered_df['Age'].notna())]['Age']
    age_female = filtered_df[(filtered_df['Sex'] == 'F') & (filtered_df['Age'].notna())]['Age']
    x_range = np.linspace(0, 75, 500)
    fig = go.Figure()

    if sex_option == "Wszyscy":
        if len(ages_all) > 1:
            kde_all = gaussian_kde(ages_all)
            fig.add_trace(go.Scatter(x=x_range, y=kde_all(x_range),mode='lines',name='Wszyscy',line=dict(color='green'),
                                     fill='tozeroy',opacity=0.3))
        if len(age_male) > 1:
            kde_male = gaussian_kde(age_male)
            fig.add_trace(go.Scatter(x=x_range, y=kde_male(x_range),mode='lines',name='Mężczyźni',line=dict(color='blue'),
                                     fill='tozeroy',opacity=0.6))
        if len(age_female) > 1:
            kde_female = gaussian_kde(age_female)
            fig.add_trace(go.Scatter(x=x_range, y=kde_female(x_range),mode='lines',name='Kobiety',line=dict(color='deeppink'),
                                     fill='tozeroy',opacity=0.6))
    elif sex_option == "Mężczyźni":
        if len(age_male) > 1:
            kde_male = gaussian_kde(age_male)
            fig.add_trace(go.Scatter(x=x_range, y=kde_male(x_range),mode='lines',name='Mężczyźni',line=dict(color='blue'),
                                     fill='tozeroy',opacity=0.6))
    elif sex_option == "Kobiety":
        if len(age_female) > 1:
            kde_female = gaussian_kde(age_female)
            fig.add_trace(go.Scatter(x=x_range, y=kde_female(x_range),mode='lines',name='Kobiety',line=dict(color='deeppink'),
                                     fill='tozeroy',opacity=0.6))
    # Wykres słupkowy
    participants_by_year_sex = (filtered_df.groupby(['Year', 'Sex'])['ID'].nunique().reset_index(name='Uczestnicy'))
    fig_bar_sex_year = px.bar(participants_by_year_sex,x='Year',y='Uczestnicy',color='Sex',barmode='group',
                              title='Liczba uczestników wg płci i roku',color_discrete_map={'M': 'blue', 'F': 'deeppink'})
    col1, col2 = st.columns(2)
    with col1:
        if len(fig.data) == 0:
            st.warning("Brak wystarczających danych do wyświetlenia wykresu.")
        else:
            fig.update_layout(
                title='Rozkład wieku zawodników wg płci',
                xaxis_title='Wiek',
                yaxis_title='Gęstość',
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)
    with col2:
        fig_bar_sex_year.update_layout(height=400)
        st.plotly_chart(fig_bar_sex_year, use_container_width=True)
    # Wykres słupkowy poziomy
    participants_by_country = (filtered_df.groupby('NOC')['ID'].nunique().sort_values(ascending=False).head(10)
                               .reset_index(name='Uczestnicy'))
    participants_by_country = participants_by_country.sort_values('Uczestnicy', ascending=True)
    fig_top_countries = px.bar(participants_by_country,x='Uczestnicy',y='NOC',orientation='h',
                               title='Top 10 krajów wg liczby uczestników',)
    fig_top_countries.update_layout(yaxis_title='Kraj',xaxis_title='Liczba uczestników',yaxis={'categoryorder': 'total ascending'},
                                    height=400)
    # Tabela
    top_athletes_starts = (filtered_df["Name"].value_counts().head(10).reset_index()
                           .rename(columns={"Name": "Imię i nazwisko", "count": "Liczba startów"}))
    # kolumna od 1
    top_athletes_starts.insert(0, "Lp.", range(1, len(top_athletes_starts) + 1))
    # koljeność kolumn
    top_athletes_starts = top_athletes_starts[["Lp.", "Imię i nazwisko", "Liczba startów"]]
    col3, col4 = st.columns(2)
    with col3:
        st.plotly_chart(fig_top_countries, use_container_width=True)
    with col4:
        st.markdown("**Top 10 zawodników wg liczby startów**")
        st.dataframe(top_athletes_starts, hide_index=True)
                """,language='python')
# Medale
elif section == "🥇 Medale":
    st.title("🥇 Analiza Medali")
    medals_df = filtered_df[filtered_df['Medal'].notna()]
    medals_country = medals_df.groupby('Team').size().reset_index(name='Medale').sort_values(by='Medale', ascending=False).head(20)
    medals_sport = medals_df.groupby('Sport').size().reset_index(name='Medale').sort_values(by='Medale', ascending=False).head(20)
    countries = medals_df['Team'].value_counts().index.tolist()
    top_countries = medals_df['Team'].value_counts().nlargest(10).index.tolist()
    # pierwszy wiersz
    col1, col2 = st.columns(2)
    with col1:
        fig_bar_country = px.bar(medals_country, x='Team', y='Medale',
                                 title='Liczba medali wg kraju (top 20)',
                                 labels={'Medale': 'Liczba medali', 'Team': 'Kraj'})
        fig_bar_country.update_layout(
            height=400,
            margin=dict(t=50, b=70, l=50, r=50),
            title={'x': 0.5, 'xanchor': 'center'}
        )
        fig_bar_country.update_xaxes(tickangle=45, tickfont=dict(size=10), ticks="outside")
        st.plotly_chart(fig_bar_country, use_container_width=True)        
    with col2:
        fig_bar_sport = px.bar(medals_sport, x='Sport', y='Medale',
                               title='Liczba medali wg dyscypliny (top 20)',
                               labels={'Medale': 'Liczba medali', 'Sport': 'Dyscyplina'})
        fig_bar_sport.update_layout(
            height=400,
            margin=dict(t=50, b=70, l=50, r=50),
            title={'x': 0.5, 'xanchor': 'center'}
        )
        fig_bar_sport.update_xaxes(tickangle=45, tickfont=dict(size=10), ticks="outside")
        st.plotly_chart(fig_bar_sport, use_container_width=True)
    # drugi wiersz
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Heatmapa: liczba medali w latach ")
        selected_countries = st.multiselect("Wybierz kraje do heatmapy", options=countries, default=top_countries[:5])
        if selected_countries:
            heatmap_data = medals_df[medals_df['Team'].isin(selected_countries)].groupby(['Year', 'Team']).size().reset_index(name='Medale')
            heatmap_pivot = heatmap_data.pivot(index='Team', columns='Year', values='Medale').fillna(0)

            fig_heatmap = px.imshow(heatmap_pivot,
                                    labels=dict(x="Rok", y="Kraj", color="Liczba medali"),
                                    title="Heatmapa medali w latach dla wybranych krajów",
                                    aspect="auto",
                                    color_continuous_scale='Blues')

            years = heatmap_pivot.columns.tolist()
            fig_heatmap.update_layout(
                height=400,
                margin=dict(t=50, b=70, l=50, r=50),
                title={'x': 0.5, 'xanchor': 'center'}
            )
            fig_heatmap.update_xaxes(tickvals=years, tickfont=dict(size=10), ticks="outside")
            st.plotly_chart(fig_heatmap, use_container_width=True)
    with col4:
        st.subheader("Trend medali wybranych krajów")
        df_medals = df[df['Medal'].notna()]
        medals = filtered_df[filtered_df['Medal'].notna()]
        # Lista krajów do wyboru
        teams_list = sorted(medals['Team'].unique())
        # Domyślne kraje, jeśli istnieją w teams_list, inaczej pierwsze 3 dostępne
        default_teams = [team for team in ["Spain", "Croatia", "Poland"] if team in teams_list]
        if not default_teams:
            default_teams = teams_list[:3]  # pierwsze 3 kraje, jeśli żadne z default nie pasuje
        # Multiselect 
        teams_to_compare = st.multiselect("Wybierz kraje do porównania", options=teams_list, default=default_teams)
        if teams_to_compare:
            medals_selected = medals[medals['Team'].isin(teams_to_compare)]
            trend_df = medals_selected.groupby(['Year', 'Team']).size().reset_index(name='MedalCount')

            fig_trends = px.line(trend_df, x='Year', y='MedalCount', color='Team',
                                markers=True,
                                title="Porównanie trendów liczby medali wybranych krajów",
                                labels={'MedalCount': 'Liczba medali', 'Year': 'Rok'})
            fig_trends.update_layout(
                height=400,
                margin=dict(t=50, b=70, l=50, r=50),
                title={'x': 0.5, 'xanchor': 'center'}
            )
            fig_heatmap.update_xaxes(tickvals=years, tickfont=dict(size=10), ticks="outside")
            st.plotly_chart(fig_trends, use_container_width=True)
        else:
            st.info("Wybierz przynajmniej jeden kraj z listy.")
    # Trzeci wiersz
    col_bubble, col_top10 = st.columns([3, 2])
    with col_bubble:
        st.markdown("### Medale vs liczba zawodników w kraju")
        athletes_per_country = filtered_df.groupby('Team')['ID'].nunique().reset_index(name='Liczba zawodników')
        medals_per_country = medals_df.groupby('Team').size().reset_index(name='Liczba medali')

        bubble_data = pd.merge(athletes_per_country, medals_per_country, on='Team', how='left').fillna(0)

        fig_bubble = px.scatter(
            bubble_data,
            x='Liczba zawodników',
            y='Liczba medali',
            size='Liczba medali',
            color='Team',
            hover_name='Team',
            title='Medale vs liczba zawodników w kraju',
            labels={'Liczba zawodników': 'Liczba zawodników', 'Liczba medali': 'Liczba medali'},
            size_max=40
        )
        fig_bubble.update_layout(
            height=400,
            margin=dict(t=50, b=70, l=50, r=50),
            title={'x': 0.5, 'xanchor': 'center'}
        )
        fig_bubble.update_xaxes(tickangle=45, tickfont=dict(size=10), ticks="outside")

        st.plotly_chart(fig_bubble, use_container_width=True)

    with col_top10:
        st.markdown("**Top 10 zawodników wg liczby medali**")
        medalists = filtered_df[filtered_df['Medal'].notna()]
        medals_by_athlete_color = (
            medalists.groupby(['Name', 'Medal'])
            .size()
            .unstack(fill_value=0)
            .reset_index()
        )

        medals_by_athlete_color['Łączna liczba medali'] = medals_by_athlete_color[['Bronze', 'Silver', 'Gold']].sum(axis=1)
        cols = ['Name', 'Gold', 'Silver', 'Bronze', 'Łączna liczba medali']
        medals_by_athlete_color = medals_by_athlete_color[cols]
        medals_by_athlete_color = medals_by_athlete_color.sort_values(by='Łączna liczba medali', ascending=False)
        top_10_athletes_color = medals_by_athlete_color.head(10).reset_index(drop=True)
        top_10_athletes_color.insert(0, "Lp.", range(1, len(top_10_athletes_color) + 1))
        st.dataframe(top_10_athletes_color, use_container_width=True, hide_index=True)

    with st.expander("📄 Kod źródłowy:"):
        st.code("""
                elif section == "🥇 Medale":
    st.title("🥇 Analiza Medali")
    medals_df = filtered_df[filtered_df['Medal'].notna()]
    medals_country = medals_df.groupby('Team').size().reset_index(name='Medale').sort_values(by='Medale', ascending=False).head(20)
    medals_sport = medals_df.groupby('Sport').size().reset_index(name='Medale').sort_values(by='Medale', ascending=False).head(20)
    countries = medals_df['Team'].value_counts().index.tolist()
    top_countries = medals_df['Team'].value_counts().nlargest(10).index.tolist()
    # pierwszy wiersz
    col1, col2 = st.columns(2)
    with col1:
        fig_bar_country = px.bar(medals_country, x='Team', y='Medale',
                                 title='Liczba medali wg kraju (top 20)',
                                 labels={'Medale': 'Liczba medali', 'Team': 'Kraj'})
        fig_bar_country.update_layout(
            height=400,
            margin=dict(t=50, b=70, l=50, r=50),
            title={'x': 0.5, 'xanchor': 'center'}
        )
        fig_bar_country.update_xaxes(tickangle=45, tickfont=dict(size=10), ticks="outside")
        st.plotly_chart(fig_bar_country, use_container_width=True)        
    with col2:
        fig_bar_sport = px.bar(medals_sport, x='Sport', y='Medale',
                               title='Liczba medali wg dyscypliny (top 20)',
                               labels={'Medale': 'Liczba medali', 'Sport': 'Dyscyplina'})
        fig_bar_sport.update_layout(
            height=400,
            margin=dict(t=50, b=70, l=50, r=50),
            title={'x': 0.5, 'xanchor': 'center'}
        )
        fig_bar_sport.update_xaxes(tickangle=45, tickfont=dict(size=10), ticks="outside")
        st.plotly_chart(fig_bar_sport, use_container_width=True)
    # drugi wiersz
    col3, col4 = st.columns(2)
    with col3:
        st.subheader("Heatmapa: liczba medali w latach ")
        selected_countries = st.multiselect("Wybierz kraje do heatmapy", options=countries, default=top_countries[:5])
        if selected_countries:
            heatmap_data = medals_df[medals_df['Team'].isin(selected_countries)].groupby(['Year', 'Team']).size().reset_index(name='Medale')
            heatmap_pivot = heatmap_data.pivot(index='Team', columns='Year', values='Medale').fillna(0)

            fig_heatmap = px.imshow(heatmap_pivot,
                                    labels=dict(x="Rok", y="Kraj", color="Liczba medali"),
                                    title="Heatmapa medali w latach dla wybranych krajów",
                                    aspect="auto",
                                    color_continuous_scale='Blues')

            years = heatmap_pivot.columns.tolist()
            fig_heatmap.update_layout(
                height=400,
                margin=dict(t=50, b=70, l=50, r=50),
                title={'x': 0.5, 'xanchor': 'center'}
            )
            fig_heatmap.update_xaxes(tickvals=years, tickfont=dict(size=10), ticks="outside")
            st.plotly_chart(fig_heatmap, use_container_width=True)
    with col4:
        st.subheader("Trend medali wybranych krajów")
        df_medals = df[df['Medal'].notna()]
        medals = filtered_df[filtered_df['Medal'].notna()]
        # Lista krajów do wyboru
        teams_list = sorted(medals['Team'].unique())
        # Domyślne kraje, jeśli istnieją w teams_list, inaczej pierwsze 3 dostępne
        default_teams = [team for team in ["Spain", "Croatia", "Poland"] if team in teams_list]
        if not default_teams:
            default_teams = teams_list[:3]  # pierwsze 3 kraje, jeśli żadne z default nie pasuje
        # Multiselect 
        teams_to_compare = st.multiselect("Wybierz kraje do porównania", options=teams_list, default=default_teams)
        if teams_to_compare:
            medals_selected = medals[medals['Team'].isin(teams_to_compare)]
            trend_df = medals_selected.groupby(['Year', 'Team']).size().reset_index(name='MedalCount')

            fig_trends = px.line(trend_df, x='Year', y='MedalCount', color='Team',
                                markers=True,
                                title="Porównanie trendów liczby medali wybranych krajów",
                                labels={'MedalCount': 'Liczba medali', 'Year': 'Rok'})
            fig_trends.update_layout(
                height=400,
                margin=dict(t=50, b=70, l=50, r=50),
                title={'x': 0.5, 'xanchor': 'center'}
            )
            fig_heatmap.update_xaxes(tickvals=years, tickfont=dict(size=10), ticks="outside")
            st.plotly_chart(fig_trends, use_container_width=True)
        else:
            st.info("Wybierz przynajmniej jeden kraj z listy.")
    # Trzeci wiersz
    col_bubble, col_top10 = st.columns([3, 2])
    with col_bubble:
        st.markdown("### Medale vs liczba zawodników w kraju")
        athletes_per_country = filtered_df.groupby('Team')['ID'].nunique().reset_index(name='Liczba zawodników')
        medals_per_country = medals_df.groupby('Team').size().reset_index(name='Liczba medali')

        bubble_data = pd.merge(athletes_per_country, medals_per_country, on='Team', how='left').fillna(0)

        fig_bubble = px.scatter(
            bubble_data,
            x='Liczba zawodników',
            y='Liczba medali',
            size='Liczba medali',
            color='Team',
            hover_name='Team',
            title='Medale vs liczba zawodników w kraju',
            labels={'Liczba zawodników': 'Liczba zawodników', 'Liczba medali': 'Liczba medali'},
            size_max=40
        )
        fig_bubble.update_layout(
            height=400,
            margin=dict(t=50, b=70, l=50, r=50),
            title={'x': 0.5, 'xanchor': 'center'}
        )
        fig_bubble.update_xaxes(tickangle=45, tickfont=dict(size=10), ticks="outside")

        st.plotly_chart(fig_bubble, use_container_width=True)

    with col_top10:
        st.markdown("**Top 10 zawodników wg liczby medali**")
        medalists = filtered_df[filtered_df['Medal'].notna()]
        medals_by_athlete_color = (
            medalists.groupby(['Name', 'Medal'])
            .size()
            .unstack(fill_value=0)
            .reset_index()
        )

        medals_by_athlete_color['Łączna liczba medali'] = medals_by_athlete_color[['Bronze', 'Silver', 'Gold']].sum(axis=1)
        cols = ['Name', 'Gold', 'Silver', 'Bronze', 'Łączna liczba medali']
        medals_by_athlete_color = medals_by_athlete_color[cols]
        medals_by_athlete_color = medals_by_athlete_color.sort_values(by='Łączna liczba medali', ascending=False)
        top_10_athletes_color = medals_by_athlete_color.head(10).reset_index(drop=True)
        top_10_athletes_color.insert(0, "Lp.", range(1, len(top_10_athletes_color) + 1))
        st.dataframe(top_10_athletes_color, use_container_width=True, hide_index=True)
                    """, language='python')

# dane fizyczne
elif section == "📊 Dane fizyczne":
    st.title("📊 Dane Fizyczne Zawodników")
    # Ustawienia layoutu 
    common_height = 400
    common_margin = dict(t=40, b=40, l=30, r=30)
    df_phys = filtered_df.copy()
    # Zakodowanie medalu numerycznie: Gold=3, Silver=2, Bronze=1, brak=0
    df_phys['Kolor medalu'] = df_phys['Medal'].map({'Gold': 3, 'Silver': 2, 'Bronze': 1}).fillna(0).astype(int)
    st.subheader("Wzrost vs Waga zawodników oraz korelacje z medalami")
    col1, col2 = st.columns([1, 1])
    with col1:
        fig_scatter_hw = px.scatter(
            df_phys,
            x='Height',
            y='Weight',
            color='Sex',
            title='Wzrost vs Waga (kolor wg płci)',
            labels={'Height': 'Wzrost (cm)', 'Weight': 'Waga (kg)', 'Sex': 'Płeć'},
            color_discrete_map={'M': "#003eb1", 'F': 'deeppink'}
        )
        fig_scatter_hw.update_layout(height=common_height, margin=common_margin)
        st.plotly_chart(fig_scatter_hw, use_container_width=True)
    with col2:
        # liczba medali na zawodnika
        medals_per_athlete = (filtered_df[filtered_df['Medal'].notna()]
                            .groupby('ID')
                            .size()
                            .reset_index(name='Liczba medali'))
        df_corr = df_phys.merge(medals_per_athlete, on='ID', how='left').fillna({'Liczba medali': 0})
        # Tmacierz korelacji
        fig_heatmap_corr = px.imshow(
            df_corr[['Age', 'Height', 'Weight', 'Liczba medali']].corr(),
            text_auto=True,
            aspect="auto",
            color_continuous_scale='Blues',
            title='Macierz korelacji: Wiek, Wzrost, Waga, Liczba medali'
        )
        fig_heatmap_corr.update_layout(height=common_height, margin=common_margin)
        st.plotly_chart(fig_heatmap_corr, use_container_width=True)

    st.subheader("📊 Histogramy cech fizycznych")
    h1, h2 = st.columns(2)
    with h1:
        fig_hist_height = px.histogram(df_phys, x='Height', nbins=30,
                                       title='Rozkład wzrostu',
                                       labels={'Height': 'Wzrost (cm)'}
                                       )
        fig_hist_height.update_traces(marker_line_color='black', marker_line_width=1)
        fig_hist_height.update_layout(yaxis_title='Częstość',height=common_height, margin=common_margin)
        st.plotly_chart(fig_hist_height, use_container_width=True)
    with h2:
        fig_hist_weight = px.histogram(df_phys, x='Weight', nbins=30,
                                       title='Rozkład wagi',
                                       labels={'Weight': 'Waga (kg)'})
        fig_hist_weight.update_traces(marker_line_color='black', marker_line_width=1)
        fig_hist_weight.update_layout(yaxis_title='Częstość',height=common_height, margin=common_margin)
        st.plotly_chart(fig_hist_weight, use_container_width=True)

    st.subheader("Wykresy skrzynkowe: Wzrost i Waga wg płci")
    b1, b2 = st.columns(2)
    with b1:
        fig_box_height = px.box(df_phys, x='Sex', y='Height', color='Sex',
                                title='Wzrost wg płci',
                                labels={'Height': 'Wzrost (cm)', 'Sex': 'Płeć'},
                                color_discrete_map={'M': "#003eb1", 'F': 'deeppink'})
        fig_box_height.update_layout(height=common_height, margin=common_margin)
        st.plotly_chart(fig_box_height, use_container_width=True)
    with b2:
        fig_box_weight = px.box(df_phys, x='Sex', y='Weight', color='Sex',
                                title='Waga wg płci',
                                labels={'Weight': 'Waga (kg)', 'Sex': 'Płeć'},
                                color_discrete_map={'M': "#003eb1", 'F': 'deeppink'})
        fig_box_weight.update_layout(height=common_height, margin=common_margin)
        st.plotly_chart(fig_box_weight, use_container_width=True)
    
    with st.expander("📄 Kod źródłowy:"):
        st.code("""
                elif section == "📊 Dane fizyczne":
    st.title("📊 Dane Fizyczne Zawodników")
    # Ustawienia layoutu 
    common_height = 400
    common_margin = dict(t=40, b=40, l=30, r=30)
    df_phys = filtered_df.copy()
    # Zakodowanie medalu numerycznie: Gold=3, Silver=2, Bronze=1, brak=0
    df_phys['Kolor medalu'] = df_phys['Medal'].map({'Gold': 3, 'Silver': 2, 'Bronze': 1}).fillna(0).astype(int)
    st.subheader("Wzrost vs Waga zawodników oraz korelacje z medalami")
    col1, col2 = st.columns([1, 1])
    with col1:
        fig_scatter_hw = px.scatter(
            df_phys,
            x='Height',
            y='Weight',
            color='Sex',
            title='Wzrost vs Waga (kolor wg płci)',
            labels={'Height': 'Wzrost (cm)', 'Weight': 'Waga (kg)', 'Sex': 'Płeć'}
        )
        fig_scatter_hw.update_layout(height=common_height, margin=common_margin)
        st.plotly_chart(fig_scatter_hw, use_container_width=True)
    with col2:
        # liczba medali na zawodnika
        medals_per_athlete = (filtered_df[filtered_df['Medal'].notna()]
                            .groupby('ID')
                            .size()
                            .reset_index(name='Liczba medali'))
        df_corr = df_phys.merge(medals_per_athlete, on='ID', how='left').fillna({'Liczba medali': 0})
        # Tmacierz korelacji
        fig_heatmap_corr = px.imshow(
            df_corr[['Age', 'Height', 'Weight', 'Liczba medali']].corr(),
            text_auto=True,
            aspect="auto",
            color_continuous_scale='Blues',
            title='Macierz korelacji: Wiek, Wzrost, Waga, Liczba medali'
        )
        fig_heatmap_corr.update_layout(height=common_height, margin=common_margin)
        st.plotly_chart(fig_heatmap_corr, use_container_width=True)

    st.subheader("📊 Histogramy cech fizycznych")
    h1, h2 = st.columns(2)
    with h1:
        fig_hist_height = px.histogram(df_phys, x='Height', nbins=30,
                                       title='Rozkład wzrostu',
                                       labels={'Height': 'Wzrost (cm)'})
        fig_hist_height.update_traces(marker_line_color='black', marker_line_width=1)
        fig_hist_height.update_layout(yaxis_title='Częstość',height=common_height, margin=common_margin)
        st.plotly_chart(fig_hist_height, use_container_width=True)
    with h2:
        fig_hist_weight = px.histogram(df_phys, x='Weight', nbins=30,
                                       title='Rozkład wagi',
                                       labels={'Weight': 'Waga (kg)'})
        fig_hist_weight.update_traces(marker_line_color='black', marker_line_width=1)
        fig_hist_weight.update_layout(yaxis_title='Częstość',height=common_height, margin=common_margin)
        st.plotly_chart(fig_hist_weight, use_container_width=True)

    st.subheader("Wykresy skrzynkowe: Wzrost i Waga wg płci")
    b1, b2 = st.columns(2)
    with b1:
        fig_box_height = px.box(df_phys, x='Sex', y='Height', color='Sex',
                                title='Wzrost wg płci',
                                labels={'Height': 'Wzrost (cm)', 'Sex': 'Płeć'})
        fig_box_height.update_layout(height=common_height, margin=common_margin)
        st.plotly_chart(fig_box_height, use_container_width=True)
    with b2:
        fig_box_weight = px.box(df_phys, x='Sex', y='Weight', color='Sex',
                                title='Waga wg płci',
                                labels={'Weight': 'Waga (kg)', 'Sex': 'Płeć'})
        fig_box_weight.update_layout(height=common_height, margin=common_margin)
        st.plotly_chart(fig_box_weight, use_container_width=True)
                """, language='python')

# dodatkowe wykresy  
elif section == "🔍 Dodatkowe wykresy":
    st.title("🔍 Wykres strumieniowy, treemap i animowany")

    st.header("Sankey Diagram (wykres strumieniowy): przepływ zawodników między krajami, dyscyplinami i sezonami")
    # Przygotowanie danych do Sankey
    sankey_df = filtered_df.dropna(subset=['Team', 'Sport', 'Season'])
    sankey_df = sankey_df[['Team', 'Sport', 'Season']]
    # unikalne etykiety i indeksy
    labels = list(pd.unique(sankey_df['Team'])) + list(pd.unique(sankey_df['Sport'])) + list(pd.unique(sankey_df['Season']))
    label_indices = {label: i for i, label in enumerate(labels)}
    # Łączenie Team -> Sport
    team_sport = sankey_df.groupby(['Team', 'Sport']).size().reset_index(name='count')
    # Łączenie Sport -> Season
    sport_season = sankey_df.groupby(['Sport', 'Season']).size().reset_index(name='count')
    # Budujemy źródła i cele oraz wartości
    source = []
    target = []
    value = []
    # Team -> Sport
    for _, row in team_sport.iterrows():
        source.append(label_indices[row['Team']])
        target.append(label_indices[row['Sport']])
        value.append(row['count'])
    # Sport -> Season
    for _, row in sport_season.iterrows():
        source.append(label_indices[row['Sport']])
        target.append(label_indices[row['Season']])
        value.append(row['count'])
    fig_sankey = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels,
            color="blue"
        ),
        link=dict(
            source=source,
            target=target,
            value=value
        )
    )])
    fig_sankey.update_layout(title_text="Sankey Diagram: Team → Sport → Season", font_size=10)
    st.plotly_chart(fig_sankey, use_container_width=True)

    st.header("Treemap (mapa drzewa): udział medali wg krajów i dyscyplin")
    medals = filtered_df[filtered_df['Medal'].notna()]
    treemap_df = medals.groupby(['Team', 'Sport']).size().reset_index(name='Medals')
    fig_treemap = px.treemap(treemap_df, path=['Team', 'Sport'], values='Medals',
                             color='Medals', color_continuous_scale='Viridis',
                             title="Treemap: udział medali wg krajów i dyscyplin")
    st.plotly_chart(fig_treemap, use_container_width=True)

    st.header("Animowany wykres: zmiana liczby medali na przestrzeni lat (Top 5 krajów)")
    # Grupowanie liczby medali dla każdego kraju i roku
    medals_year_team = medals.groupby(['Year', 'Team']).size().reset_index(name='MedalCount')
    # Sumaryczna liczba medali dla każdego kraju w całym okresie (do ustalenia top 5 stałych krajów)
    total_medals_per_team = medals_year_team.groupby('Team')['MedalCount'].sum().reset_index()
    top_5_teams = total_medals_per_team.sort_values('MedalCount', ascending=False).head(5)['Team'].tolist()
    # Filtrujemy dane do top 5 krajów (stałych przez cały czas)
    top_medals_per_year = medals_year_team[medals_year_team['Team'].isin(top_5_teams)]
    # Zamiana 'Year' na string dla animacji
    top_medals_per_year['Year'] = top_medals_per_year['Year'].astype(str)
    # Ustal kolejność krajów na osi Y wg sumy medali malejąco 
    top_5_teams_ordered = top_5_teams[::-1]  # odwrócone, bo oś Y będzie z autorange="reversed"
    # Zzamiana kolumny na kategoryczną ze stałym uporządkowaniem
    top_medals_per_year['Team_cat'] = pd.Categorical(top_medals_per_year['Team'], categories=top_5_teams_ordered, ordered=True)
    # Tworzymy wykres z y = Team_cat, aby mieć stałą kolejność krajów
    fig_animated = px.bar(
        top_medals_per_year,
        x='MedalCount',
        y='Team_cat',
        color='Team',
        animation_frame='Year',
        animation_group='Team',
        orientation='h',
        title="Top 5 krajów z największą liczbą medali (na przestrzeni lat)",
        labels={'Team_cat': 'Kraj', 'MedalCount': 'Liczba medali'},
        color_discrete_sequence=px.colors.qualitative.Safe,
        range_x=[0, top_medals_per_year['MedalCount'].max() + 5],
        text=None  # brak tekstu na słupkach
    )
    fig_animated.update_layout(
        height=700,
        margin=dict(t=70, b=40, l=140, r=40),
        xaxis_title="Liczba medali",
        yaxis_title="Kraj",
        yaxis=dict(title='Kraj', autorange="reversed"),  # odwróć oś Y, top na górze
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14),
        bargap=0.15,  # szerokość słupków
        bargroupgap=0.1,
        updatemenus=[{
            "type": "buttons",
            "buttons": [
                {
                    "label": "▶️ Odtwórz",
                    "method": "animate",
                    "args": [None, {
                        "frame": {"duration": 1000, "redraw": True},
                        "fromcurrent": True,
                        "transition": {"duration": 500, "easing": "quadratic-in-out"}
                    }]
                },
                {
                    "label": "⏸️ Pauza",
                    "method": "animate",
                    "args": [[None], {
                        "frame": {"duration": 0, "redraw": False},
                        "mode": "immediate",
                        "transition": {"duration": 0}
                    }]
                }
            ]
        }]
    )
    st.plotly_chart(fig_animated, use_container_width=True)
    
    with st.expander("📄 Kod źródłowy:"):
        st.code("""
            elif section == "🔍 Dodatkowe wykresy":
    st.title("🔍 Wykres strumieniowy, treemap i animowany")

    st.header("Sankey Diagram (wykres strumieniowy): przepływ zawodników między krajami, dyscyplinami i sezonami")
    # Przygotowanie danych do Sankey
    sankey_df = filtered_df.dropna(subset=['Team', 'Sport', 'Season'])
    sankey_df = sankey_df[['Team', 'Sport', 'Season']]
    # unikalne etykiety i indeksy
    labels = list(pd.unique(sankey_df['Team'])) + list(pd.unique(sankey_df['Sport'])) + list(pd.unique(sankey_df['Season']))
    label_indices = {label: i for i, label in enumerate(labels)}
    # Łączenie Team -> Sport
    team_sport = sankey_df.groupby(['Team', 'Sport']).size().reset_index(name='count')
    # Łączenie Sport -> Season
    sport_season = sankey_df.groupby(['Sport', 'Season']).size().reset_index(name='count')
    # Budujemy źródła i cele oraz wartości
    source = []
    target = []
    value = []
    # Team -> Sport
    for _, row in team_sport.iterrows():
        source.append(label_indices[row['Team']])
        target.append(label_indices[row['Sport']])
        value.append(row['count'])
    # Sport -> Season
    for _, row in sport_season.iterrows():
        source.append(label_indices[row['Sport']])
        target.append(label_indices[row['Season']])
        value.append(row['count'])
    fig_sankey = go.Figure(data=[go.Sankey(
        node=dict(
            pad=15,
            thickness=20,
            line=dict(color="black", width=0.5),
            label=labels,
            color="blue"
        ),
        link=dict(
            source=source,
            target=target,
            value=value
        )
    )])
    fig_sankey.update_layout(title_text="Sankey Diagram: Team → Sport → Season", font_size=10)
    st.plotly_chart(fig_sankey, use_container_width=True)

    st.header("Treemap (mapa drzewa): udział medali wg krajów i dyscyplin")
    medals = filtered_df[filtered_df['Medal'].notna()]
    treemap_df = medals.groupby(['Team', 'Sport']).size().reset_index(name='Medals')
    fig_treemap = px.treemap(treemap_df, path=['Team', 'Sport'], values='Medals',
                             color='Medals', color_continuous_scale='Viridis',
                             title="Treemap: udział medali wg krajów i dyscyplin")
    st.plotly_chart(fig_treemap, use_container_width=True)

    st.header("Animowany wykres: zmiana liczby medali na przestrzeni lat (Top 5 krajów)")
    # Grupowanie liczby medali dla każdego kraju i roku
    medals_year_team = medals.groupby(['Year', 'Team']).size().reset_index(name='MedalCount')
    # Sumaryczna liczba medali dla każdego kraju w całym okresie (do ustalenia top 5 stałych krajów)
    total_medals_per_team = medals_year_team.groupby('Team')['MedalCount'].sum().reset_index()
    top_5_teams = total_medals_per_team.sort_values('MedalCount', ascending=False).head(5)['Team'].tolist()
    # Filtrujemy dane do top 5 krajów (stałych przez cały czas)
    top_medals_per_year = medals_year_team[medals_year_team['Team'].isin(top_5_teams)]
    # Zamiana 'Year' na string dla animacji
    top_medals_per_year['Year'] = top_medals_per_year['Year'].astype(str)
    # Ustal kolejność krajów na osi Y wg sumy medali malejąco 
    top_5_teams_ordered = top_5_teams[::-1]  # odwrócone, bo oś Y będzie z autorange="reversed"
    # Zzamiana kolumny na kategoryczną ze stałym uporządkowaniem
    top_medals_per_year['Team_cat'] = pd.Categorical(top_medals_per_year['Team'], categories=top_5_teams_ordered, ordered=True)
    # Tworzymy wykres z y = Team_cat, aby mieć stałą kolejność krajów
    fig_animated = px.bar(
        top_medals_per_year,
        x='MedalCount',
        y='Team_cat',
        color='Team',
        animation_frame='Year',
        animation_group='Team',
        orientation='h',
        title="Top 5 krajów z największą liczbą medali (na przestrzeni lat)",
        labels={'Team_cat': 'Kraj', 'MedalCount': 'Liczba medali'},
        color_discrete_sequence=px.colors.qualitative.Safe,
        range_x=[0, top_medals_per_year['MedalCount'].max() + 5],
        text=None  # brak tekstu na słupkach
    )
    fig_animated.update_layout(
        height=700,
        margin=dict(t=70, b=40, l=140, r=40),
        xaxis_title="Liczba medali",
        yaxis_title="Kraj",
        yaxis=dict(title='Kraj', autorange="reversed"),  # odwróć oś Y, top na górze
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(size=14),
        bargap=0.15,  # szerokość słupków
        bargroupgap=0.1,
        updatemenus=[{
            "type": "buttons",
            "buttons": [
                {
                    "label": "▶️ Odtwórz",
                    "method": "animate",
                    "args": [None, {
                        "frame": {"duration": 1000, "redraw": True},
                        "fromcurrent": True,
                        "transition": {"duration": 500, "easing": "quadratic-in-out"}
                    }]
                },
                {
                    "label": "⏸️ Pauza",
                    "method": "animate",
                    "args": [[None], {
                        "frame": {"duration": 0, "redraw": False},
                        "mode": "immediate",
                        "transition": {"duration": 0}
                    }]
                }
            ]
        }]
    )
    st.plotly_chart(fig_animated, use_container_width=True)
                """)
