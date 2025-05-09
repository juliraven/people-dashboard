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

st.title("📊 Dashboard ludności Europy (2015–2024)")

df = pd.read_excel('plik.xlsx')

# Transpozycja danych do wykresów:
df1 = df.melt(id_vars=["Country"], var_name="Year", value_name="Population")
df1["Year"] = df1["Year"].astype(int)

# Filtr wyboru kraju/krajów:
countries = df["Country"].unique().tolist()

select_all = st.sidebar.checkbox("wszystkie kraje", value=True)

if select_all:
    selected_countries = countries
else:
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

st.dataframe(df)

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
    title=f"Populacja w Europie w roku {selected_year_for_map}",
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

missing_iso = set(geo.values()) - set(df_map["ISO3"])
df_missing = pd.DataFrame({"ISO3": list(missing_iso)})
df_missing["Country"] = df_missing["ISO3"].map({v: k for k, v in geo.items()})

fig2.add_trace(
    px.choropleth(
        df_missing,
        locations="ISO3",
        locationmode="ISO-3",
        scope="europe",
        color_discrete_sequence=["#a0a0a0"],  
        hover_name="Country",  
        hover_data={"ISO3": False, "Country": False}
    ).data[0]
)

fig2.add_trace(
    px.scatter_geo(
        pd.DataFrame({"ISO3": [None], "Population": [None], "label": ["Brak danych"]}),
        locationmode="ISO-3",
        hover_name="label",
        text="label"
    ).update_traces(
        marker=dict(color="gray", size=10),
        showlegend=False,
        name="Brak danych"
    ).data[0]
)

fig2.update_geos(
    scope="world",
    projection_type="natural earth",
    lataxis_range=[30, 72],   
    lonaxis_range=[-25, 60], 
    showland=True,
    landcolor="#f5f2d6",
    showframe=False,
    showcoastlines=True,
    bgcolor="#111111",
    showocean=True,
    oceancolor="#95bdff",
    showlakes=False
)

st.plotly_chart(fig2)






