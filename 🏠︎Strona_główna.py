import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Wizualizacja danych - streamlit", layout="wide")

add_logo('logo.png', height=350)

st.sidebar.markdown(
    """
    <style>
        }
        [data-testid="stSidebar"] {
            padding-top: 0px;
            padding: 10px;
            font-family: sans-serif;
            font-size: 18px;
            width: 150px !important; /* Wymuszenie */
            min-width: 150px !important;
            max-width: 150px !important;
        }

        [data-testid="stSidebarHeader"] {
            height: 30px;
            padding: 5px 10px; 
            margin: 0; 
            display: flex; 
            align-items: center;
            justify-content: center; 
        }
        .main {
            margin-left: 170px;
    </style>
    """,
    unsafe_allow_html=True,
)

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

st.title("Czym jest Streamlit?")

st.markdown(
    '''
    <h5>
    <span style="color:red; font-weight:bold;">Streamlit</span> umożliwia tworzenie interaktywnych aplikacji internetowych opartych na danych.
    Aplikacje można tworzyć wyłącznie z użyciem Pythona i bez konieczności używania innych technologii, takich jak JavaScript, HTML, CSS.
    Dokumentacja dostępna jest na stronie: 
    <a href="https://docs.streamlit.io" style="color:#66ccff; font-weight:bold;">dokumentacja</a>.
    </h5>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <h5>
    Utworzoną aplikację można w łatwy sposób wdrożyć dzięki <a href="https://docs.streamlit.io/" style="color:#66ccff; font-weight:bold;">chmurze</a> za pomocą kilku kliknięć.
    </h5>
    ''',
    unsafe_allow_html=True
)

st.title("Pierwsze kroki")

st.markdown(
    '''
    <h5>
    Aby móc rozpocząć korzystanie z biblioteki, w celu stworzenia pierwszej aplikacji, należy najpierw ją zainstalować za pomocą polecenia:
    </h5>
    ''',
    unsafe_allow_html=True
)

code = '''
pip install streamlit
'''

st.code(code, language='python')

st.markdown(
    '''
    <h5>
    W celu uruchomienia przykładowej aplikacji należy wywołać polecenie:
    </h5>
    ''',
    unsafe_allow_html=True
)

code = '''
streamlit hello
'''

st.code(code, language='python')

st.markdown(
    '''
    <h5>
    Aplikację można utworzyć w dowolnym edytorze tekstowym. Należy ją zapisać następnie do pliku z rozszerzeniem <code>.py</code>, np. <code>app.py</code>. W pliku tym wpisujemy przykładowy kod:
    </h5>
    ''',
    unsafe_allow_html=True
)

code = '''
import streamlit as st

st.write("Hello world")
'''

st.code(code, language='python')

st.markdown(
    '''
    <h5>
    Następnie w terminalu wiersza poleceń wpisujemy:
    </h5>
    ''',
    unsafe_allow_html=True
)

code = '''
streamlit run app.py
'''

st.code(code, language='python')

st.markdown(
    '''
    <h5>
    Powinno to uruchomić przeglądarkę, która wyświetli aplikację.
    </h5>
    ''',
    unsafe_allow_html=True
)

st.title("Udostępnianie aplikacji")

st.markdown(
    '''
    <h5>
    Utworzoną aplikację można udostępnić do publicznego użytku przy pomocy <a href="https://github.com/" style="color:#66ccff; font-weight:bold;">GitHuba</a>. Wystarczy utworzyć konto i repozytorium, które można użyć do udostępnienia aplikacji za pomocą wyżej wspomnianej chmury.
    </h5>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <h5>
    Przykładowa struktura repoozytorium może wyglądać następująco:
    </h5>
    ''',
    unsafe_allow_html=True
)

code = '''
app/
├── home.py
└── pages/
    └── page1.py
    └── page2.py
├── requirements.txt
'''

st.code(code, language='python')

st.markdown(
    '''
    <h5>
    W pliku <code>requirements.txt</code> umieszczamy używane w aplikacji biblioteki. Może on wyglądać w następujący sposób:
    </h5>
    ''',
    unsafe_allow_html=True
)

code = '''
streamlit
pandas
numpy
plotly
matplotlib
seaborn
scikit-learn
'''

st.code(code, language='python')

st.markdown(
    '''
    <h5>
    Gdy mamy już gotowy przynajmniej plik <code>home.py</code>, możemy udostępnić aplikację. W tym celu należy wejść na stronę: <a href="https://streamlit.io/" style="color:#66ccff; font-weight:bold;">streamlit</a> i założyć na niej konto, np. za pośrednictwem GitHuba lub Google.
    </h5>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <h5>
    Następnie należy wybrać opcję <code>Create app</code> i pierwszą z dostępnych opcji wdrożenia, czyli z użyciem GitHuba.
    </h5>
    ''',
    unsafe_allow_html=True
)

st.image('first.png', caption="Opcje wdrażania aplikacji", use_container_width=True)

st.markdown(
    '''
    <h5>
    Pojawią się pola, które należy wypełnić, a następnie kliknąć przycisk <code>Deploy</code>. Nasza aplikacja jest od tego momentu dostępna pod przypisanym (lub wskazanym przez nas) linkiem.
    </h5>
    ''',
    unsafe_allow_html=True
)

st.image('second.png', caption="Wdrażanie", use_container_width=True)

st.title("Przydatne funkcje")

st.markdown(""" 
### 1. **`st.write()`** - wszechstronna funkcja, może wyświetlać tekst, Markdown, LaTeX, dane w posatci tabeli (ramki danych Pandas), wykresy, emoji i inne.

### 2. **`st.dataframe()` i `st.table()`** - funkcje służące do wyświetlania ramek danych i tabel, przy czym: `st.dataframe()` — interaktywna tabela, `st.table()` — statyczna tabela.

### 3. **`st.columns()`** - funkcja pozwalająca wyświetlać widżety obok siebie w układzie siatki.
        
### 4. **`st.expander()`** - funkcja tworząca rozwijany element, który może ukrywać lub pokazywać treść.
 
### 5. **`st.text_input()`, `st.slider()`, `st.selectbox()`** - funkcje do tworzenia filtrów, widżetów.

### 6. **`st.line_chart()`, `st.area_chart()`, `st.plotly_chart()`** - funkcje do wyświetlania wykresów.
---  

### Przykład użycia:

```python
import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław'],
    'Liczba mieszkańców (mln)': [1.8, 0.8, 0.5, 0.6],
    'Powierzchnia (km²)': [517, 327, 262, 293],
    'PKB per capita': [150000, 120000, 110000, 130000]
})

col1, col2 = st.columns([2.5, 3])

with col1:
    st.subheader("📋 Tabela danych")
    st.dataframe(df)

with col2:
    st.subheader("📈 Wykres bąbelkowy")
    fig = px.scatter(
        df,
        x='Powierzchnia (km²)',
        y='Liczba mieszkańców (mln)',
        size='PKB',
        color='PKB',
        hover_name='Miasto',
        size_max=60,
        color_continuous_scale='PuRd'
    )
    st.plotly_chart(fig, use_container_width=True)

""")

st.markdown(
    '''
    <p>
    
    ### Rezultat działania kodu:
    
    </p>
    ''',
    unsafe_allow_html=True
)

import pandas as pd
import plotly.express as px

df = pd.DataFrame({
    'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław'],
    'Liczba mieszkańców (mln)': [1.8, 0.8, 0.5, 0.6],
    'Powierzchnia (km²)': [517, 327, 262, 293],
    'PKB': [150000, 120000, 110000, 130000]
})

col1, col2 = st.columns([2.5, 3])

with col1:
    st.subheader("📋 Tabela danych")
    df['Liczba mieszkańców (mln)'] = df['Liczba mieszkańców (mln)'].map('{:.1f}'.format)
    st.markdown('##')
    st.dataframe(df)

with col2:
    st.subheader("📈 Wykres bąbelkowy")
    fig = px.scatter(
        df,
        x='Powierzchnia (km²)',
        y='Liczba mieszkańców (mln)',
        size='PKB',
        color='PKB',
        hover_name='Miasto',
        size_max=50,
        color_continuous_scale='PuRd'
    )
    st.plotly_chart(fig, use_container_width=True)



