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
import plotly.graph_objects as go
import altair as alt

st.markdown("<h1 style='text-align: center; margin-top: -50px;'>📊 Dashboard ludności świata (2000–2023)</h1>", unsafe_allow_html=True)
st.markdown('#')

col = st.columns((1.5, 5, 2), gap='medium')

df = pd.read_excel('plik.xlsx')

european_countries = [
    "Albania", "Andorra", "Austria", "Belarus", "Belgium", "Bosnia and Herzegovina",
    "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", "Finland",
    "France", "Germany", "Greece", "Hungary", "Iceland", "Ireland", "Italy", "Kosovo",
    "Latvia", "Liechtenstein", "Lithuania", "Luxembourg", "Malta", "Moldova", "Monaco",
    "Montenegro", "Netherlands", "North Macedonia", "Norway", "Poland", "Portugal",
    "Romania", "San Marino", "Serbia", "Slovakia", "Slovenia", "Spain",
    "Sweden", "Switzerland", "Ukraine", "United Kingdom", "Vatican City"
]

# Transpozycja danych do wykresów:
df1 = df.melt(id_vars=["Country"], var_name="Year", value_name="Population")
df1["Year"] = df1["Year"].astype(int)
df1 = df1[(df1["Year"] >= 2000) & (df1["Year"] <= 2023)]

# Wybór krajów europejskich::
df2 = df1[df1["Country"].isin(european_countries)]

# Filtr zakresu lat:
min_year = df2["Year"].min()
max_year = df2["Year"].max()

selected_years = st.sidebar.slider(
    "Wybierz zakres lat (dla heatmapy):",
    min_value=int(min_year),
    max_value=int(max_year),
    value=(int(min_year), int(max_year)),
    step=1
)

# Filtrowanie danych:
df3 = df2[(df2["Year"] >= selected_years[0]) &
    (df2["Year"] <= selected_years[1])
]

# Heatmapa:
def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    heatmap = alt.Chart(input_df).mark_rect().encode(
        y=alt.Y(f'{input_y}:O', axis=alt.Axis(
            title="Year", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
        x=alt.X(f'{input_x}:O', axis=alt.Axis(
            title="", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
        color=alt.Color(f'{input_color}:Q',
                        legend=alt.Legend(title="Liczba ludności", titlePadding=20),
                        scale=alt.Scale(scheme=input_color_theme)),
        stroke=alt.value('black'),
        strokeWidth=alt.value(0.25),
    ).properties(width=900, title=f"Populacja Europy {selected_years[0]} - {selected_years[1]}").configure_axis(
        labelFontSize=12,
        titleFontSize=12
    )
    return heatmap

fig1 = make_heatmap(
    input_df=df3,
    input_y="Year",
    input_x="Country",
    input_color="Population",
    input_color_theme="redpurple"
)

geo = {'Afghanistan': 'AFG', 'Åland Islands': 'ALA', 'Albania': 'ALB', 'Algeria': 'DZA', 'American Samoa': 'ASM', 'Andorra': 'AND', 
       'Angola': 'AGO', 'Anguilla': 'AIA', 'Antigua and Barbuda': 'ATG', 'Argentina': 'ARG', 'Armenia': 'ARM', 'Aruba': 'ABW', 
       'Australia': 'AUS', 'Austria': 'AUT', 'Azerbaijan': 'AZE', 'Bahamas': 'BHS', 'Bahrain': 'BHR', 'Bangladesh': 'BGD', 
       'Barbados': 'BRB', 'Belarus': 'BLR', 'Belgium': 'BEL', 'Belize': 'BLZ', 'Benin': 'BEN', 'Bermuda': 'BMU', 'Bhutan': 'BTN', 
       'Bolivia': 'BOL', 'Bosnia and Herzegovina': 'BIH', 'Botswana': 'BWA', 'Brazil': 'BRA', 'British Virgin Islands': 'VGB', 
       'Brunei': 'BRN', 'Bulgaria': 'BGR', 'Burkina Faso': 'BFA', 'Burundi': 'BDI', 'Cambodia': 'KHM', 'Cameroon': 'CMR', 
       'Canada': 'CAN', 'Cape Verde': 'CPV', 'Cayman Islands': 'CYM', 'Central African Republic': 'CAF', 'Chad': 'TCD', 'Chile': 'CHL', 
       'China': 'CHN', 'Hong Kong Special Administrative Region of China': 'HKG', 'Macao Special Administrative Region of China': 'MAC', 
       'Colombia': 'COL', 'Comoros': 'COM', 'Congo': 'COG', 'Cook Islands': 'COK', 'Costa Rica': 'CRI', "Cote d'Ivoire": 'CIV', 'Croatia': 'HRV', 
       'Cuba': 'CUB', 'Cyprus': 'CYP', 'Czechia': 'CZE', "North Korea": 'PRK', 'Democratic Republic of Congo': 'COD', 'Congo': 'COG',
       'Denmark': 'DNK', 'Djibouti': 'DJI', 'Dominica': 'DMA', 'Dominican Republic': 'DOM', 'Ecuador': 'ECU', 'Egypt': 'EGY', 'El Salvador': 'SLV', 
       'Equatorial Guinea': 'GNQ', 'Eritrea': 'ERI', 'Estonia': 'EST', 'Ethiopia': 'ETH', 'Faeroe Islands': 'FRO', 'Falkland Islands': 'FLK', 
       'Fiji': 'FJI', 'Finland': 'FIN', 'France': 'FRA', 'French Guiana': 'GUF', 'French Polynesia': 'PYF', 'Gabon': 'GAB', 'Gambia': 'GMB', 'Georgia': 'GEO', 
       'Germany': 'DEU', 'Ghana': 'GHA', 'Gibraltar': 'GIB', 'Greece': 'GRC', 'Greenland': 'GRL', 'Grenada': 'GRD', 'Guadeloupe': 'GLP', 'Guam': 'GUM', 'Guatemala': 'GTM', 
       'Guernsey': 'GGY', 'Guinea': 'GIN', 'Guinea-Bissau': 'GNB', 'Guyana': 'GUY', 'Haiti': 'HTI', 'Holy See': 'VAT', 'Honduras': 'HND', 'Hungary': 'HUN', 'Iceland': 'ISL', 
       'India': 'IND', 'Indonesia': 'IDN', 'Iran': 'IRN', 'Iraq': 'IRQ', 'Ireland': 'IRL', 'Isle of Man': 'IMN', 'Israel': 'ISR', 'Italy': 'ITA', 
       'Jamaica': 'JAM', 'Japan': 'JPN', 'Jersey': 'JEY', 'Jordan': 'JOR', 'Kazakhstan': 'KAZ', 'Kenya': 'KEN', 'Kiribati': 'KIR', 'Kuwait': 'KWT', 'Kyrgyzstan': 'KGZ', 
       "Laos": 'LAO', 'Latvia': 'LVA', 'Lebanon': 'LBN', 'Lesotho': 'LSO', 'Liberia': 'LBR', 'Libya': 'LBY', 'Liechtenstein': 'LIE', 
       'Lithuania': 'LTU', 'Luxembourg': 'LUX', 'Madagascar': 'MDG', 'Malawi': 'MWI', 'Malaysia': 'MYS', 'Maldives': 'MDV', 'Mali': 'MLI', 'Malta': 'MLT', 'Marshall Islands': 'MHL', 
       'Martinique': 'MTQ', 'Mauritania': 'MRT', 'Mauritius': 'MUS', 'Mayotte': 'MYT', 'Mexico': 'MEX', 'Micronesia, Federated States of': 'FSM', 'Moldova': 'MDA', 'Monaco': 'MCO', 
       'Mongolia': 'MNG', 'Montenegro': 'MNE', 'Montserrat': 'MSR', 'Morocco': 'MAR', 'Mozambique': 'MOZ', 'Myanmar': 'MMR', 'Namibia': 'NAM', 'Nauru': 'NRU', 'Nepal': 'NPL', 
       'Netherlands': 'NLD', 'Netherlands Antilles': 'ANT', 'New Caledonia': 'NCL', 'New Zealand': 'NZL', 'Nicaragua': 'NIC', 'Niger': 'NER', 'Nigeria': 'NGA', 'Niue': 'NIU',
       'Norfolk Island': 'NFK', 'Northern Mariana Islands': 'MNP', 'Norway': 'NOR', 'Occupied Palestinian Territory': 'PSE', 'Oman': 'OMN', 'Pakistan': 'PAK', 'Palau': 'PLW', 
       'Panama': 'PAN', 'Papua New Guinea': 'PNG', 'Paraguay': 'PRY', 'Peru': 'PER', 'Philippines': 'PHL', 'Pitcairn': 'PCN', 'Poland': 'POL', 'Portugal': 'PRT', 
       'Puerto Rico': 'PRI', 'Qatar': 'QAT', 'South Korea': 'KOR', 'R_union': 'REU', 'Romania': 'ROU', 'Russia': 'RUS', 'Rwanda': 'RWA', 
       'Saint-Barthélemy': 'BLM', 'Saint Helena': 'SHN', 'Saint Kitts and Nevis': 'KNA', 'Saint Lucia': 'LCA', 'Saint-Martin (French part)': 'MAF', 'Saint Pierre and Miquelon': 'SPM', 
       'Saint Vincent and the Grenadines': 'VCT', 'Samoa': 'WSM', 'San Marino': 'SMR', 'Sao Tome and Principe': 'STP', 'Saudi Arabia': 'SAU', 'Senegal': 'SEN', 'Serbia': 'SRB', 
       'Seychelles': 'SYC', 'Sierra Leone': 'SLE', 'Singapore': 'SGP', 'Slovakia': 'SVK', 'Slovenia': 'SVN', 'Solomon Islands': 'SLB', 'Somalia': 'SOM', 'South Africa': 'ZAF', 
       'Spain': 'ESP', 'Sri Lanka': 'LKA', 'Sudan': 'SDN', 'South Sudan': 'SSD', 'Suriname': 'SUR', 'Svalbard and Jan Mayen Islands': 'SJM', 'Eswatini': 'SWZ', 'Sweden': 'SWE', 'Switzerland': 'CHE', 
       'Syria': 'SYR', 'Tajikistan': 'TJK', 'Thailand': 'THA', 'East Timor': 'TLS', 'Togo': 'TGO', 'Tokelau': 'TKL', 
       'Tonga': 'TON', 'Trinidad and Tobago': 'TTO', 'Tunisia': 'TUN', 'Turkey': 'TUR', 'Turkmenistan': 'TKM', 'Turks and Caicos Islands': 'TCA', 'Tuvalu': 'TUV', 'Tanzania' : 'TZA', 'Uganda': 'UGA', 
       'Ukraine': 'UKR', 'United Arab Emirates': 'ARE', 'United Kingdom': 'GBR', 'United Republic of Tanzania': 'TZA', 
       'United States': 'USA', 'United States Virgin Islands': 'VIR', 'Uruguay': 'URY', 'Uzbekistan': 'UZB', 'Vanuatu': 'VUT', 
       'Venezuela': 'VEN', 'Vietnam': 'VNM', 'Wallis and Futuna Islands': 'WLF', 'Western Sahara': 'ESH', 'Yemen': 'YEM', 
       'Zambia': 'ZMB', 'Zimbabwe': 'ZWE', 'North Macedonia': 'MKD', 'Kosovo': 'XK', 'Taiwan': 'TWN'}

# Suwak do wyboru konkretnego roku:
selected_year_for_map = st.sidebar.selectbox("Wybierz rok (dla mapy):", sorted(df1["Year"].unique()))

df_map = df1[df1["Year"] == selected_year_for_map].copy()

df_map["Population"] = pd.to_numeric(df_map["Population"], errors="coerce")
df_map = df_map.dropna(subset=["Population"])

df_map["ISO3"] = df_map["Country"].map(geo)

# Usunięcie braków:
df_map = df_map.dropna(subset=["ISO3"])

# Kategoryzowanie populacji:
colors = ['#fcbec0', '#faa9b8', '#f98faf', '#f571a5', '#ec539d', '#db3695', '#c41b8a', '#a90880', '#8d0179']
bins = [0, 5_000_000, 10_000_000, 25_000_000, 50_000_000, 100_000_000, 250_000_000, 500_000_000, 1_000_000_000, float('inf')]
labels = [
    "0–5 mln", "5–10 mln", "10–25 mln", "25–50 mln", "50–100 mln",
    "100–250 mln", "250–500 mln", "500 mln – 1 mld", "1+ mld"
]

color_map = {
    "0–5 mln": "#fcbec0", 
    "5–10 mln": "#faa9b8", 
    "10–25 mln": "#f98faf", 
    "25–50 mln": "#f571a5", 
    "50–100 mln": "#ec539d", 
    "100–250 mln": "#db3695", 
    "250–500 mln": "#c41b8a", 
    "500 mln – 1 mld": "#a90880", 
    "1+ mld": "#8d0179"
}

df_map["Population_Category"] = pd.cut(df_map["Population"], bins=bins, labels=labels, ordered=True)

fig2 = px.choropleth(
    df_map,
    locations="ISO3",
    color="Population_Category",
    hover_name="Country",
    locationmode="ISO-3",
    scope="world",
    color_discrete_map=color_map,
    hover_data={"ISO3": False, "Population": True, "Population_Category": False},
    width=1200,  
    height=1200,
    category_orders={"Population_Category": labels}
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
    showlakes=False
)

fig2.update_layout(
    title=f"Populacja świata w roku {selected_year_for_map}",
    margin=dict(l=0, r=150, t=30, b=30), 
    height=800,
    template="plotly_dark",
    plot_bgcolor="#111111",
    paper_bgcolor="#111111",

    legend=dict(
        title=dict(text="Liczba ludności", font=dict(size=22)),
        orientation="v",              
        yanchor="middle",
        y=0.5,                        
        xanchor="right",
        x=1.1,                        
        font=dict(size=18)
    )
)

df_map["Population"] = df_map["Population"].astype(int)
df_map = df_map.sort_values(by="Population", ascending=False)

with col[1]:
    st.plotly_chart(fig2)
    st.altair_chart(fig1, use_container_width=True)

with col[2]:
    st.markdown('#### Top 10 państw pod względem liczby ludności')

    st.dataframe(
    df_map.head(10),
    column_order=["Country", "Population"],
    hide_index=True,
    column_config={
        "Country": st.column_config.TextColumn("Kraj"),
        "Population": st.column_config.ProgressColumn(
            "Populacja",
            format="%d",
            min_value=0,
            max_value=int(df_map["Population"].max())  
        )
    }
)




