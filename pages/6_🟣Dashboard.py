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

st.markdown(page_bg_img_sidebar, unsafe_allow_html=True)

import numpy as np
import pandas as pd
import plotly.express as px
import altair as alt

st.title("📊 Dashboard ludności świata (2000–2023)")

df = pd.read_excel('plik.xlsx')

# Transpozycja danych do wykresów:
df1 = df.melt(id_vars=["Country"], var_name="Year", value_name="Population")
df1["Year"] = df1["Year"].astype(int)

df1 = df1[(df1["Year"] >= 2000) & (df1["Year"] <= 2023)]

# Filtr wyboru kraju/krajów:
countries = df["Country"].unique().tolist()
selected_countries = st.sidebar.multiselect("Wybierz kraj(e):", countries, default=["Poland"])

# Filtr zakresu lat:
min_year = df1["Year"].min()
max_year = df1["Year"].max()

selected_years = st.sidebar.slider(
    "Wybierz zakres lat (dla heatmapy):",
    min_value=int(min_year),
    max_value=int(max_year),
    value=(int(min_year), int(max_year)),
    step=1
)

# Filtrowanie danych:
df2 = df1[(df1["Country"].isin(selected_countries)) &
    (df1["Year"] >= selected_years[0]) &
    (df1["Year"] <= selected_years[1])
]

# Heatmapa:
def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    heatmap = alt.Chart(input_df).mark_rect().encode(
        y=alt.Y(f'{input_y}:O', axis=alt.Axis(
            title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
        x=alt.X(f'{input_x}:O', axis=alt.Axis(
            title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
        color=alt.Color(f'{input_color}:Q',
                        legend=alt.Legend(title="Liczba ludności"),
                        scale=alt.Scale(scheme=input_color_theme, reverse=True)),
        stroke=alt.value('black'),
        strokeWidth=alt.value(0.25),
    ).properties(width=900).configure_axis(
        labelFontSize=12,
        titleFontSize=12
    )
    return heatmap

fig1 = make_heatmap(
    input_df=df2,
    input_y="Year",
    input_x="Country",
    input_color="Population",
    input_color_theme="redpurple"
)

st.altair_chart(fig1, use_container_width=True)

geo = {
    'Albania': 'ALB', 'Andorra': 'AND', 'Armenia': 'ARM', 'Austria': 'AUT',
    'Azerbaijan': 'AZE', 'Belarus': 'BLR', 'Belgium': 'BEL', 'Bosnia and Herzegovina': 'BIH',
    'Bulgaria': 'BGR', 'Croatia': 'HRV', 'Cyprus': 'CYP', 'Czechia': 'CZE',
    'Denmark': 'DNK', 'Estonia': 'EST', 'Finland': 'FIN', 'France': 'FRA',
    'Georgia': 'GEO', 'Germany': 'DEU', 'Greece': 'GRC', 'Hungary': 'HUN',
    'Iceland': 'ISL', 'Ireland': 'IRL', 'Italy': 'ITA', 'Kazakhstan': 'KAZ',
    'Kosovo': 'XK', 'Latvia': 'LVA', 'Liechtenstein': 'LIE', 'Lithuania': 'LTU',
    'Luxembourg': 'LUX', 'Malta': 'MLT', 'Moldova': 'MDA', 'Monaco': 'MCO',
    'Montenegro': 'MNE', 'Netherlands': 'NLD', 'North Macedonia': 'MKD',
    'Norway': 'NOR', 'Poland': 'POL', 'Portugal': 'PRT', 'Romania': 'ROU',
    'Russia': 'RUS', 'San Marino': 'SMR', 'Serbia': 'SRB', 'Slovakia': 'SVK',
    'Slovenia': 'SVN', 'Spain': 'ESP', 'Sweden': 'SWE', 'Switzerland': 'CHE',
    'Türkiye': 'TUR', 'Ukraine': 'UKR', 'United Kingdom': 'GBR'
}

# Suwak do wyboru konkretnego roku:
selected_year_for_map = st.sidebar.selectbox("Wybierz rok (dla mapy):", sorted(df1["Year"].unique()))

df_map = df1[df1["Year"] == selected_year_for_map].copy()

df_map["Population"] = pd.to_numeric(df_map["Population"], errors="coerce")
df_map = df_map.dropna(subset=["Population"])

df_map["ISO3"] = df_map["Country"].map(geo)

# Usunięcie braków:
df_map = df_map.dropna(subset=["ISO3"])

colors = ['#fcbec0', '#faa9b8', '#f98faf', '#f571a5', '#ec539d', '#db3695', '#c41b8a', '#a90880', '#8d0179']

fig2 = px.choropleth(
    df_map,
    locations="ISO3",
    color="Population",
    hover_name="Country",
    locationmode="ISO-3",
    scope="world",
    color_continuous_scale=colors,
    range_color=(df_map["Population"].min(), df_map["Population"].max()),
    hover_data={"ISO3": False}
)

fig2.update_layout(
    title=f"Populacja świata w roku {selected_year_for_map}",
    margin=dict(l=0, r=0, t=30, b=0),
    height=600,
    template="plotly_dark",
    plot_bgcolor="#111111",    
    paper_bgcolor="#111111", 
    coloraxis_colorbar=dict(
        title="Liczba ludności",
        ticks="outside"
    )
)

fig2.update_geos(
    scope="world",
    projection_type="orthographic",
    showland=True,
    projection_rotation=dict(lat=45, lon=10),
    landcolor="#f5f2d6",
    showframe=False,
    showcoastlines=True,
    bgcolor="#111111",
    showocean=True,
    oceancolor="rgba(149, 189, 255, 0.9)",
    showlakes=False,
    width=1000,  
    height=700
)

st.plotly_chart(fig2)






