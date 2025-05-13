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
    <p style='font-size: 20px; font-weight: normal;'>
    <span style="color:red; font-weight:bold;">Streamlit</span> umożliwia tworzenie interaktywnych aplikacji internetowych opartych na danych.
    Aplikacje można tworzyć wyłącznie z użyciem Pythona i bez konieczności używania innych technologii, takich jak JavaScript, HTML, CSS.
    Dokumentacja dostępna jest na stronie: 
    <a href="https://docs.streamlit.io" style="color:#66ccff; font-weight:bold;">dokumentacja</a>.
    </p>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <p style='font-size: 20px; font-weight: normal;'>
    Utworzoną aplikację można w łatwy sposób wdrożyć dzięki <a href="https://docs.streamlit.io/" style="color:#66ccff; font-weight:bold;">chmurze</a> za pomocą kilku kliknięć.
    </p>
    ''',
    unsafe_allow_html=True
)

st.title("Pierwsze kroki")

st.markdown(
    '''
    <p style='font-size: 20px; font-weight: normal;'>
    Aby móc rozpocząć korzystanie z biblioteki, w celu stworzenia pierwszej aplikacji, należy najpierw ją zainstalować za pomocą polecenia:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
pip install streamlit
'''

st.code(code, language='python')

st.markdown(
    '''
    <p style='font-size: 20px; font-weight: normal;'>
    W celu uruchomienia przykładowej aplikacji należy wywołać polecenie:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
streamlit hello
'''

st.code(code, language='python')

st.markdown(
    '''
    <p style='font-size: 20px; font-weight: normal;'>
    Aplikację można utworzyć w dowolnym edytorze tekstowym. Należy ją zapisać następnie do pliku z rozszerzeniem <code>.py</code>, np. <code>app.py</code>. W pliku tym wpisujemy przykładowy kod:
    </p>
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
    <p style='font-size: 20px; font-weight: normal;'>
    Następnie w terminalu wiersza poleceń wpisujemy:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
streamlit run app.py
'''

st.code(code, language='python')

st.markdown(
    '''
    <p style='font-size: 20px; font-weight: normal;'>
    Powinno to uruchomić przeglądarkę, która wyświetli aplikację.
    </p>
    ''',
    unsafe_allow_html=True
)

st.title("Udostępnianie aplikacji")

st.markdown(
    '''
    <p style='font-size: 20px; font-weight: normal;'>
    Utworzoną aplikację można udostępnić do publicznego użytku przy pomocy <a href="https://github.com/" style="color:#66ccff; font-weight:bold;">GitHuba</a>. Wystarczy utworzyć konto i repozytorium, które można użyć do udostępnienia aplikacji za pomocą wyżej wspomnianej chmury.
    </p>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <p style='font-size: 20px; font-weight: normal;'>
    Przykładowa struktura repoozytorium może wyglądać następująco:
    </p>
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
    <p style='font-size: 20px; font-weight: normal;'>
    W pliku <code>requirements.txt</code> umieszczamy używane w aplikacji biblioteki. Może on wyglądać w następujący sposób:
    </p>
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
    <p style='font-size: 20px; font-weight: normal;'>
    Gdy mamy już gotowy przynajmniej plik <code>home.py</code>, możemy udostępnić aplikację. W tym celu należy wejść na stronę: <a href="https://streamlit.io/" style="color:#66ccff; font-weight:bold;">streamlit</a> i założyć na niej konto, np. za pośrednictwem GitHuba lub Google.
    </p>
    ''',
    unsafe_allow_html=True
)

st.markdown(
    '''
    <p style='font-size: 20px; font-weight: normal;'>
    Następnie należy wybrać opcję <code>Create app</code> i pierwszą z dostępnych opcji wdrożenia, czyli z użyciem GitHuba.
    </p>
    ''',
    unsafe_allow_html=True
)

st.image('first.png', caption="Opcje wdrażania aplikacji", use_container_width=True)

st.markdown(
    '''
    <p style='font-size: 20px; font-weight: normal;'>
    Pojawią się pola, które należy wypełnić, a następnie kliknąć przycisk <code>Deploy</code>. Nasza aplikacja jest od tego momentu dostępna pod przypisanym (lub wskazanym przez nas) linkiem.
    </p>
    ''',
    unsafe_allow_html=True
)

st.image('second.png', caption="Wdrażanie", use_container_width=True)

st.title("Przydatne funkcje")

col1, col2, col3 = st.columns([2.5, 2, 2])

col1.subheader('Wyświetlanie tekstu')

col1.markdown("""
| Funkcja                         | Opis                                                                 |
|---------------------------------|----------------------------------------------------------------------|
| `st.text('Tekst')`              | wyświetla zwykły tekst o stałej szerokości                           |
| `st.markdown('Markdown')`       | wyświetla tekst sformatowany za pomocą Markdown (np. _kursywa_)      |
| `st.caption('Opis')`            | pokazuje opis, np. do obrazka                                        |
| `st.latex(r'e^{i\\pi} + 1 = 0')` | wyświetla wzór matematyczny w składni LaTeX                         |
| `st.write('Dowolny obiekt')`   | uniwersalna funkcja – obsługuje tekst, liczby, listy, DataFrame itp.  |
| `st.title('Tytuł')`            | wyświetla duży nagłówek (tytuł)                             |
| `st.header('Nagłówek')`        | wyświetla średni nagłówek – mniejszy niż `title`, większy niż `subheader`    |
| `st.subheader('Podnagłówek')`  | wyświetla mniejszy nagłówek, np. dla sekcji w aplikacji                   |
| `st.code('for i in range(8):')`| pokazuje blok kodu z zachowaniem formatowania                      |

""")

col1.subheader('Wyświetlanie danych')

col1.markdown("""
| Funkcja                                       | Opis                                                                 |
|-----------------------------------------------|----------------------------------------------------------------------|
| `st.dataframe(my_dataframe)`                 | wyświetla ramkę danych (np. Pandas DataFrame) w formie interaktywnej tabeli |
| `st.table(data.iloc[0:10])`                  | pokazuje dane jako statyczną tabelę – bez możliwości przewijania czy sortowania |
| `st.json({'foo': 'bar', 'fu': 'ba'})`        | wyświetla dane w formacie JSON w przejrzystej strukturze drzewa    |
| `st.metric(label="Temp", value="273 K", delta="1.2 K")` | prezentuje wartość liczbową z etykietą i zmianą (delta) – idealne do metryk |

""")

col1.subheader('Wyświetlanie multimediów')

col1.markdown("""
| Funkcja                        | Opis                                                                 |
|--------------------------------|----------------------------------------------------------------------|
| `st.image('image.png')`     | wyświetla obrazek, może to być plik lokalny, URL lub obiekt w pamięci  |
| `st.audio(data)`               | odtwarza plik audio. `data` może być ścieżką, URL lub bajtami (np. z pliku `.mp3`) |
| `st.video(data)`               | odtwarza wideo, obsługuje pliki lokalne, URL lub strumienie danych|

""")

col1.subheader('Układ kolumnowy')

col1.markdown("""
| Funkcja / składnia                           | Opis                                                                 |
|----------------------------------------------|----------------------------------------------------------------------|
| `col1, col2 = st.columns(2)`                 | tworzy dwie kolumny o równej szerokości  |
| `col1.write('Kolumna 1')` | umieszcza zawartość w odpowiedniej kolumnie                       |
| `st.columns([3, 1, 1])`                      | tworzy trzy kolumny o niestandardowych proporcjach szerokości (np. 3:1:1)|
| `with col1:                 | alternatywna składnia z `with`, pozwala lepiej grupować kod wewnątrz kolumny |

""")




st.markdown(""" 
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



