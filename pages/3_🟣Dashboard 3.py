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
import numpy as np
import plotly.express as px

# tworzenie zakładek w aplikacji
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Produkcja mleka", "Bezrobocie", "Ceny mieszkań", "Produkcja gazu", "Populacja", "PKB krajów"
])

# zakladka pierwsza 
with tab1:
    st.header("Produkcja mleka krowiego") 
    df_mleko = pd.read_excel("mleko.xlsx") # wczytanie danych z excela 
    df_mleko.replace(":", np.nan, inplace=True) # zamiana : na NaN
    df_long = df_mleko.melt(id_vars=["TIME"], var_name="Rok", value_name="Wartość") # zamiana kolumn z datami na jedna kolumne Rok; zamiana z formatu szerokiego na długi
    df_long.rename(columns={"TIME": "Region"}, inplace=True) 
    df_long.dropna(subset=["Wartość"], inplace=True) # czyszczenie danych
    df_long["Wartość"] = pd.to_numeric(df_long["Wartość"], errors="coerce")
    df_long["Rok"] = df_long["Rok"].astype(str)
    selected_region = st.selectbox("Wybierz region", df_long["Region"].unique().tolist(), key="mleko_region") # wybór regionu
    region_data = df_long[df_long["Region"] == selected_region] # filtrowanie danych dla regionu
    #mtworzenie wykresu liniowego
    fig = px.line(region_data, x="Rok", y="Wartość", title=f"Produkcja mleka w regionie: {selected_region}",
                  markers=True, labels={"Wartość": "Produkcja mleka (tys. litrów)", "Rok": "Rok"},
                  template="plotly_white")
    fig.update_traces(mode="lines+markers", hovertemplate="Rok: %{x}<br>Wartość: %{y:.2f} tys. litrów")
    st.plotly_chart(fig, use_container_width=True)

# zakładka druga 
with tab2:
    st.header("Bezrobocie")
    df_bezrobocie = pd.read_excel("bezrobocie.xlsx") # wczytanie danych 
    df_long = df_bezrobocie.melt(id_vars="Region", var_name="DateGender", value_name="Value") # rozdzielenie kolumny data-płeć na osobne
    df_long[['Date', 'Gender']] = df_long['DateGender'].str.extract(r'^(20\d{2}-\d{2})-(males|females)$')
    # usunięcie spacji, znaków specjalnych, puste pola
    df_long["Value"] = df_long["Value"].astype(str).str.replace("\xa0", "").str.replace(":", "").str.strip()
    df_long = df_long[df_long["Value"] != ""]
    df_long["Value"] = pd.to_numeric(df_long["Value"], errors='coerce')
    # wybor regionu i płci
    region = st.selectbox("Wybierz region", sorted(df_long["Region"].dropna().unique()), key="bezrobocie_region")
    
    plec = st.multiselect("Płeć", ["males", "females"], default=["males", "females"], key="bezrobocie_plec")
    # filtrowanie danych i przekształcenie do formatu tabeli
    filtered = df_long[(df_long["Region"] == region) & (df_long["Gender"].isin(plec))]
    pivot_df = filtered.pivot(index="Date", columns="Gender", values="Value").sort_index()
    st.bar_chart(pivot_df) # wykres słupkowy

# zakładka trzecia
with tab3:
    st.header("Indeks cen mieszkań")
    df_ceny = pd.read_excel("ceny.xlsx") # wczytanie danych do excela 
    selected_region = st.selectbox("Wybierz kraj (region):", df_ceny['Region'].unique(), key="ceny_region") # wybór kraju
    # filtrowanie danych, czyszczenie itd
    row = df_ceny[df_ceny['Region'] == selected_region].iloc[0]
    region_data = row.drop('Region')
    plot_df = pd.DataFrame({"Kwartał": region_data.index, "Indeks": region_data.values})
    # wykres słupkowy
    fig = px.bar(plot_df, x="Kwartał", y="Indeks", title=f"Indeks cen mieszkań w {selected_region}",
                 labels={"Indeks": "Index (2015 = 100)"}, hover_data={"Indeks": True},
                 template="plotly_white", height=500)
    fig.update_yaxes(range=[0, plot_df["Indeks"].max() * 1.1])
    st.plotly_chart(fig, use_container_width=True)

# zakładka czwarta
with tab4:
    st.header("Produkcja gazu ziemnego w krajach UE")
    df = pd.read_excel("produkcja_gazu_ziemnego.xlsx") # wczytanie danych 
    df_long = df.melt(id_vars=["Kraj"], var_name="Date", value_name="Value") # kazdy miesiac jako kolumna; przeksztalcanie do formatu długiego
    df_long["Date"] = pd.to_datetime(df_long["Date"], format="%Y-%m") # konwersja kolumny Date do typu datetime
    df_long["Value"] = pd.to_numeric(df_long["Value"], errors="coerce") # konwersja wartości do typu numerycznego
    df_long = df_long.sort_values(by=["Kraj", "Date"]) # sortowanie wedlug kraju i daty
    selected_country = st.selectbox("Wybierz kraj", df_long['Kraj'].unique(), key="gaz_kraj") # wybór kraju z listy unikalnych nazw 
    filtered_df = df_long[df_long['Kraj'] == selected_country].copy().sort_values("Date") # filtrowanie danych tylko dla wybranego kraju
    # wykres liniowy
    fig_line = px.line(filtered_df, x="Date", y="Value",
                       title=f"Produkcja gazu ziemnego: {selected_country}",
                       markers=True,
                       labels={"Value": "Produkcja (mln m³)", "Date": "Data"},
                       template="plotly_white")
    fig_line.update_traces(mode="lines+markers", hovertemplate="Data: %{x|%Y-%m}<br>Produkcja: %{y:,.0f} mln m³")
    st.plotly_chart(fig_line, use_container_width=True)
    # dodanie kolumny z rokiem i miesiącem
    df_heat = filtered_df.copy()
    df_heat["Rok"] = df_heat["Date"].dt.year
    df_heat["Miesiąc"] = df_heat["Date"].dt.month
    # tworzenie tabely przestawnej, czyli rzędy = lata, kolumny = miesiące
    pivot = df_heat.pivot_table(index="Rok", columns="Miesiąc", values="Value")
    # dodanie brakujących danych z miesiąca
    for m in range(1, 13):
        if m not in pivot.columns:
            pivot[m] = np.nan
    pivot = pivot[sorted(pivot.columns)]
    # heatmapa- intensywnosc produkcji gazu
    fig_heat = px.imshow(pivot,
                         labels=dict(x="Miesiąc", y="Rok", color="Produkcja (mln m³)"),
                         x=list(range(1, 13)),
                         y=pivot.index,
                         title=f"Heatmapa miesięcznej produkcji gazu – {selected_country}",
                         color_continuous_scale="YlGnBu",
                         aspect="auto")
    st.plotly_chart(fig_heat, use_container_width=True)

# zakładka piąta 
with tab5:
    st.header("Zmiany liczby ludności w krajach Europy (1960–2026)")
    df_pop = pd.read_excel("ludzie.xlsx") # wczytanie danych
    df_pop = df_pop.rename(columns={df_pop.columns[0]: "Country"}) # pierwsza kolumna to Country
    # kolumny z latami zamieniamy na wartości w kolumnie 'Rok'
    df_long = df_pop.melt(id_vars="Country", var_name="Rok", value_name="Populacja")
    df_long["Rok"] = df_long["Rok"].astype(str)
    selected_country = st.selectbox("Wybierz kraj", sorted(df_long["Country"].unique()), key="populacja_kraj") # wybór kraju
    filtered_df = df_long[df_long["Country"] == selected_country] # filtrowanie danych
    # wykres liniowy
    fig = px.line(filtered_df, x="Rok", y="Populacja",
                  title=f"Liczba ludności w {selected_country} (1960–2026)",
                  labels={"Rok": "Rok", "Populacja": "Liczba ludności"},
                  markers=True,
                  template="plotly_white")
    fig.update_traces(mode="lines+markers", hovertemplate="Rok: %{x}<br>Ludność: %{y:,.0f}")
    st.plotly_chart(fig, use_container_width=True)

# zakładka szósta
with tab6:
    st.header("PKB krajów w czasie")
    df_pkb = pd.read_excel("waluta.xlsx") # wczytanie danych

    # usuwanie myślników, spacji i zamiana przecinków na kropki
    for col in df_pkb.columns[2:]:
        df_pkb[col] = df_pkb[col].replace('-', np.nan)
        df_pkb[col] = df_pkb[col].astype(str).str.replace(' ', '').str.replace(',', '.')
        df_pkb[col] = pd.to_numeric(df_pkb[col], errors='coerce')

    country = st.selectbox("Wybierz kraj:", df_pkb['Country'].unique(), key="pkb_kraj") # wybór kraju
    # wyodrębnienie wiersza z danymi danego kraju
    row = df_pkb[df_pkb['Country'] == country]
    unit = row['Unit'].values[0]  # jednostka np. EUR, mld EUR
    years = df_pkb.columns[2:] # kolumny z latami
    values = row[years].values.flatten() # wartosci Pkb
    
    # tworzenie dataframe do wykresu
    df_plot = pd.DataFrame({
        'Year': years,
        'Value': values
    })
    df_plot['Year'] = df_plot['Year'].astype(str)
    df_plot = df_plot[df_plot['Value'].notna()]  

    # wykres liniowy
    fig = px.line(df_plot, x='Year', y='Value', markers=True,
                  title=f"Wartość PKB dla {country} w czasie",
                  labels={'Value': f'Wartość ({unit})', 'Year': 'Rok'},
                  template="plotly_white")
    fig.update_traces(mode="lines+markers", hovertemplate="Rok: %{x}<br>PKB: %{y:,.2f}") # dostosowania wyglądu wykresu stworzonego za pomocą Plotly
    st.plotly_chart(fig, use_container_width=True)



