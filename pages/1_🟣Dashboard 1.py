import streamlit as st

page_bg_img_sidebar = """
<style>
/* Ustawienie szerokości sidebaru */
section[data-testid="stSidebar"] {
    width: 240px !important;
    min-width: 240px !important;
    max-width: 240px !important;
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

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import altair as alt
import base64

st.markdown("<h1 style='text-align: center; margin-top: -50px;'>📊 Ludność świata na przestrzeni lat</h1>", unsafe_allow_html=True)
st.markdown(' ')

col1, col2, col3 = st.columns([2, 2, 2])
col = st.columns((2.2, 4.9, 2.8), gap='medium')

df = pd.read_excel('plik.xlsx')

df1 = df.melt(id_vars=["Country"], var_name="Year", value_name="Population")
df1["Year"] = df1["Year"].astype(int)
df1 = df1[(df1["Year"] >= 1959) & (df1["Year"] <= 2023)]

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

excluded_year = 1959
years_available = sorted(df1["Year"].unique())
years_available = [year for year in years_available if year != excluded_year]

with col2:
    selected_year_for_map = st.selectbox("Wybierz rok:", years_available, index=years_available.index(2023))

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
    paper_bgcolor='rgba(0,0,0,0)', 
    plot_bgcolor='rgba(0,0,0,0)',
    geo=dict(
        bgcolor='rgba(0,0,0,0)'  
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
    bgcolor='rgba(0,0,0,0)',
    showocean=True,
    oceancolor="rgba(149, 189, 255, 0.9)",
    showlakes=False
)

fig2.update_layout(
    margin=dict(l=0, r=0, t=30, b=100), 
    height=600,
    template="plotly_dark",

    legend=dict(
        title=dict(text="Liczba ludności<br>", font=dict(size=16)),
        orientation="h",              
        yanchor="bottom",
        y=-0.2,                        
        xanchor="center",
        x=0.5,                        
        font=dict(size=14)
    )
)

df_map["Population"] = df_map["Population"].astype(int)
df_map = df_map.sort_values(by="Population", ascending=False)

df4 = df1[df1["Country"].isin(geo.keys())].copy()
df4["Population"] = pd.to_numeric(df4["Population"], errors="coerce")
df4 = df4.dropna(subset=["Population"])

df_this_year = df4[df4["Year"] == selected_year_for_map]
df_prev_year = df4[df4["Year"] == (selected_year_for_map - 1)]
    
df_diff = df_this_year.merge(df_prev_year, on="Country", suffixes=("_now", "_prev"))
df_diff["Population_Change"] = df_diff["Population_now"] - df_diff["Population_prev"]

df_diff = df_diff.dropna(subset=["Population_now", "Population_prev", "Population_Change"])
top_gain = df_diff.sort_values("Population_Change", ascending=False).iloc[0]
top_loss = df_diff.sort_values("Population_Change").iloc[0]

def load_data(file_path):
    return pd.read_csv(file_path)

data_famela = load_data("female.csv")
data_male = load_data("male.csv")

data = pd.merge(data_famela, data_male, on="Year", suffixes=('_Kobiety', '_Mężczyźni'))

selected_data = data[data['Year'] == selected_year_for_map]

liczba_kobiet = selected_data['all years_Kobiety'].values[0]
liczba_mezczyzn = selected_data['all years_Mężczyźni'].values[0]

suma = liczba_kobiet + liczba_mezczyzn
procent_kobiet = (liczba_kobiet / suma) * 100
procent_mezczyzn = (liczba_mezczyzn / suma) * 100

icon_kobieta = 'female.png'
icon_mezczyzna = 'male.png'

def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

icon_k = image_to_base64(icon_kobieta)
icon_m = image_to_base64(icon_mezczyzna)

st.markdown(
    """
    <style>
    div[data-testid="stVerticalBlock"]:has(div#gradient_container_marker):not(:has(div#outer_marker)) {
        background: linear-gradient(
            135deg,
            rgba(180, 68, 251, 0.25),
            rgba(45, 3, 94, 0.2),
            rgba(32, 33, 37, 0.1)
        );
        border: 1px solid rgba(180, 68, 251, 0.4);
        border-radius: 20px;
        padding: 24px;
        box-shadow:
            0 0 10px rgba(180, 68, 251, 0.25),
            0 4px 20px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(14px) brightness(1.1);
        background-blend-mode: overlay;
        transition: all 0.3s ease-in-out;
    }

    div[data-testid="stVerticalBlock"]:has(div#gradient_container_marker):not(:has(div#outer_marker)):hover {
        transform: translateY(-6px);
        box-shadow:
            0 0 18px rgba(180, 68, 251, 0.4),
            0 8px 30px rgba(0, 0, 0, 0.4);
    }
    </style>
    """,
    unsafe_allow_html=True
)


with col[0]:
    styled_container = st.container()
    st.markdown("<div id='outer_marker'></div>", unsafe_allow_html=True)

    with styled_container:
        st.markdown("<div id='gradient_container_marker'></div>", unsafe_allow_html=True)
        st.markdown(
        f"<h4 style='text-align: left; color: white;'>Największe wzrosty/spadki liczby ludności w {selected_year_for_map}</h4>",
        unsafe_allow_html=True)

        st.metric(
        label=top_gain["Country"],
        value=f"{top_gain['Population_now'] / 1_000_000:.1f} M",
        delta=f"{int(top_gain['Population_Change'] / 1_000):,} K")

        st.metric(
        label=top_loss["Country"],
        value=f"{top_loss['Population_now'] / 1_000_000:.1f} M",
        delta=f"{int(top_loss['Population_Change'] / 1_000):,} K")


    styled_container = st.container()
    st.markdown("<div id='outer_marker'></div>", unsafe_allow_html=True)

    with styled_container:
        st.markdown("<div id='gradient_container_marker'></div>", unsafe_allow_html=True)
        st.markdown(
        f"<h4 style='text-align: left; color: white;'>Rozkład procentowy płci w {selected_year_for_map}</h4>",
        unsafe_allow_html=True)
        
        
        col1, col2 = st.columns([2.2, 2.2])
        with col1:
            st.markdown(
    f"""
    <div style='border: 2px solid #FF69B4; border-radius: 10px; padding: 10px; width: 100px; height: 150px; text-align: center;'>
        <img src="data:image/jpg;base64,{icon_k}" width="200"><br>
        <span>Kobiety <span style='color: #FF69B4; font-weight: bold;'>{procent_kobiet:.1f}%</span></span>
    </div>
    """,
    unsafe_allow_html=True
)

        with col2:
            st.markdown(
    f"""
    <div style='border: 2px solid #1E90FF; border-radius: 10px; padding: 10px; width: 100px; height: 150px; text-align: center;'>
        <img src="data:image/jpg;base64,{icon_m}" width="100"><br>
        <span>Mężczyźni <span style='color: #1E90FF; font-weight: bold;'>{procent_mezczyzn:.1f}%</span></span>
    </div>
    """,
    unsafe_allow_html=True
)

with col[1]:
    styled_container = st.container()
    st.markdown("<div id='outer_marker'></div>", unsafe_allow_html=True)

    with styled_container:
        st.markdown("<div id='gradient_container_marker'></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; color: white;'>Populacja świata w {selected_year_for_map}</h3>",unsafe_allow_html=True)
        st.plotly_chart(fig2, use_container_width=True, config={"displayModeBar": False})

with col[2]:
    styled_container = st.container()
    st.markdown("<div id='outer_marker'></div>", unsafe_allow_html=True)

    with styled_container:
        st.markdown("<div id='gradient_container_marker'></div>", unsafe_allow_html=True)
        df_map["Population_M"] = df_map["Population"] / 1_000_000
        st.markdown(f"<h4 style='text-align: center;'>Top 10 państw pod względem liczby ludności w {selected_year_for_map}</h4>",unsafe_allow_html=True)
        st.dataframe(
        df_map.head(10),
        column_order=["Country", "Population_M"],
        hide_index=True,
        column_config={
        "Country": st.column_config.TextColumn("Kraj"),
        "Population_M": st.column_config.ProgressColumn(
            "Populacja (mln)",
            format="%.1f mln",
            min_value=0.0,
            max_value=df_map["Population_M"].max()
        )
    }
)

    styled_container = st.container()
    st.markdown("<div id='outer_marker'></div>", unsafe_allow_html=True)

    with styled_container:
        st.markdown("<div id='gradient_container_marker'></div>", unsafe_allow_html=True)
        with st.expander('Żródła danych:', expanded=False):
            st.markdown('<a href="https://ourworldindata.org/population-growth" target="_blank">https://ourworldindata.org/population-growth</a>', unsafe_allow_html=True)
            st.markdown('<a href="https://ourworldindata.org/grapher/population" target="_blank">https://ourworldindata.org/grapher/population</a>', unsafe_allow_html=True)

col11, col22 = st.columns([2,2])

with col11:
    styled_container = st.container()
    st.markdown("<div id='outer_marker'></div>", unsafe_allow_html=True)
    with styled_container:
        st.markdown("<div id='gradient_container_marker'></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; color: white;'>Zmiana liczby ludności</h3>",unsafe_allow_html=True)

        ob = pd.read_csv('population.csv')

        obszary = ob["Entity"].unique().tolist()
        wybrane_obszary = st.multiselect('Wybierz obszary:', obszary, default=['Africa', 'Europe', 'North America', 'South America', 'Oceania', 'Australia'])

        min_rok = ob['Year'].min()
        max_rok = ob['Year'].max()
        zakres_lat = st.slider('Wybierz zakres lat:', min_value=min_rok, max_value=max_rok, value=(min_rok, max_rok))

        df_filtered = ob[ob["Entity"].isin(wybrane_obszary)]
        df_filtered = df_filtered[(df_filtered["Year"] >= zakres_lat[0]) & (df_filtered["Year"] <= zakres_lat[1])]

        df_filtered = df_filtered[df_filtered["Year"] % 10 == 0]

        fig1 = px.line(df_filtered, 
              x="Year", 
              y="Population (historical)", 
              color="Entity",  
              labels={"Population": "Populacja", "Year": "Rok", "Country": "Obszar"})

        fig1.update_layout(
        legend_title="Obszary",
        xaxis_title="Rok", 
        yaxis_title="Populacja", 
        template="plotly_dark")

    
        fig1.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', 
        plot_bgcolor='rgba(0,0,0,0)',
        geo=dict(
        bgcolor='rgba(0,0,0,0)'  
    )
)

        fig1.update_layout(
        legend=dict(
        title=dict(font=dict(size=16)),                     
        font=dict(size=14)
    )
)

        fig1.update_traces(mode='lines+markers', 
                  marker=dict(size=4, symbol='circle'), line=dict(width=2))

        fig1.update_layout(
        xaxis=dict(
        tickmode='array', 
        tickvals=list(range(ob['Year'].min(), ob['Year'].max() + 1, 50)) + ['2023'],  
        ticktext=[str(i) for i in range(ob['Year'].min(), ob['Year'].max() + 1, 50)] + ['2023']
    )
)
        fig1.update_layout(height=600)

        st.plotly_chart(fig1, use_container_width=True, config={"displayModeBar": False}) 


with col22:
    styled_container = st.container()
    st.markdown("<div id='outer_marker'></div>", unsafe_allow_html=True)
    with styled_container:
        st.markdown("<div id='gradient_container_marker'></div>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; color: white;'>Oczekiwana długość życia</h3>",unsafe_allow_html=True)

        le = pd.read_csv('life-expentancy.csv')
        
        le["Year"] = le["Year"].astype(int)
        le = le[(le["Year"] >= 1959) & (le["Year"] <= 2023)]

        df_le = le[le["Year"] == selected_year_for_map].copy()

        st.dataframe(df_le)

       




