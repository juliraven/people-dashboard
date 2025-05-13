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

st.title("Tworzenie dashboardu")

st.markdown(
    '''
    <p>
    W celu utworzenia dashboardu zawierającego wizualizacje danych np. zawartych w pliku z rozszerzeniem <code>.csv</code>, należy ten plik umieścić w repozytorium wraz z innymi plikami. Repozytorium będzie miało wtedy następującą strukturę:
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
st.title("Dashboard")
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Kolejnym krokiem może być wczytanie i przekształcenie danych do dalszej analizy oraz zdeifniowanie liczby kolumn, w których umieszczane będą wizualizacje. Wykorzystuje się w tym celu polecenie <code>st.columns()</code>, np.:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
col1, col2, col3 = st.columns([2, 2, 2])
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Aby umieścić wybraną wizualizację, np. wcześniej utworzony wykres pod nazwą <code>fig</code> wystarczy użyć struktury:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
with col1:
    st.plotly_chart(fig)
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    W celu dodania interakcji do aplikacji można utworzyć filtry, które pozwolą użytkownikowi zmieniać opcje w wyświetlanych wizualizacjach. Taki filtr można utworzyć np. wykorzystując funkcję <code>st.selectbox()</code>. W poniższym kodzie wykorzystujemy taki filtr do wybrania danych z konkretnego roku, w celu ich późniejszej wizualizacji.
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
years_available = sorted(df1["Year"].unique())
selected_year = st.selectbox("Wybierz rok:", years_available, index=years_available.index(2023))
df_map = df1[df1["Year"] == selected_year].copy()
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Innym przykładem ciekawego filtrowania dnaych jest wykorzystanie funkcji <code>st.slider()</code>, tworzącej suwak do wyboru zakresu wartości. Przykładem wykorzystania tej funkcji może być utworzenie suwaka, zawierającego zakres lat, z których pochodzą dane:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
min_rok = df1['Year'].min()
max_rok = df1['Year'].max()
zakres_lat = st.slider('Wybierz zakres lat:', min_value=min_rok, max_value=max_rok, value=(min_rok, max_rok))
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Przydatną funkcją podczas tworzenia dashboardu jest także funkcja <code>st.container()</code>. Pozwala ona tworzyć "kafelki", w których można umieszczać filtry lub wizualizację. Gdy chcemy np. wyświetlić tabelę w takim kafelku, należy użyć struktury:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
with st.container():
    st.dataframe(df1)
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Ciekawą opcją jest też funkcja <code>st.expander()</code>, pozwalająca na wyświetlenie np. tekstu w formie listy rozwijanej. Przykadem wykorzystania tej funkcji może być wyświetlenie źródeł wykorzystywanaych w ramach tworzenia dashboardu danych:
    </p>
    ''',
    unsafe_allow_html=True
)

code ='''
with st.expander('Żródła danych:', expanded=False):
    st.markdown('<a href="https://ourworldindata.org" target="_blank">https://ourworldindata.org</a>', unsafe_allow_html=True)
'''

st.code(code, language='python')
