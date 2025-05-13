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

col1, col2 = st.columns([2, 2])

col1.subheader('Wyświetlanie tekstu')

col1.markdown("""
| Funkcja                         | Opis                                                                 |
|---------------------------------|----------------------------------------------------------------------|
| `st.text('Tekst')`              | wyświetla zwykły tekst o stałej szerokości                           |
| `st.markdown('Markdown')`       | wyświetla tekst sformatowany za pomocą Markdown (np. _kursywa_)      |
| `st.caption('Opis')`            | pokazuje opis, np. do obrazka                                        |
| `st.latex(r'e^{x}')` | wyświetla wzór matematyczny w składni LaTeX                         |
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

col2.subheader('Wyświetlanie multimediów')

col2.markdown("""
| Funkcja                        | Opis                                                                 |
|--------------------------------|----------------------------------------------------------------------|
| `st.image('image.png')`     | wyświetla obrazek, może to być plik lokalny, URL lub obiekt w pamięci  |
| `st.audio(data)`               | odtwarza plik audio, `data` może być ścieżką, URL lub bajtami (np. z pliku `.mp3`) |
| `st.video(data)`               | odtwarza wideo, obsługuje pliki lokalne, URL lub strumienie danych|

""")

col2.subheader('Zakładki')

col2.markdown("""
| Funkcja                                     | Opis                                                                 |
|---------------------------------------------|----------------------------------------------------------------------|
| `tab1, tab2 = st.tabs(["Zakładka 1", "Zakładka 2"])` | tworzy dwie zakładki z nazwami „Zakładka 1” i „Zakładka 2”          |
| `tab1.write("To zakładka 1")`          | wyświetla zawartość wewnątrz wybranej zakładki                    |
| `with tab1:`                                | składnia `with` do grupowania kodu wewnątrz konkretnej zakładki    |

""")

col2.subheader('Układ kolumnowy')

col2.markdown("""
| Funkcja / składnia                           | Opis                                                                 |
|----------------------------------------------|----------------------------------------------------------------------|
| `col1, col2 = st.columns(2)`                 | tworzy dwie kolumny o równej szerokości  |
| `col1.write('Kolumna 1')` | umieszcza zawartość w odpowiedniej kolumnie                       |
| `st.columns([3, 1, 1])`                      | tworzy trzy kolumny o niestandardowych proporcjach szerokości (np. 3:1:1)|
| `with col1:`                 | alternatywna składnia z `with`, pozwala lepiej grupować kod wewnątrz kolumny |

""")

st.subheader('Wyświetlanie interaktywnych widżetów')

st.markdown("""
| Funkcja                                          | Opis                                                                 |
|--------------------------------------------------|----------------------------------------------------------------------|
| `st.button('Kliknij')`                       | tworzy przycisk, który użytkownik może kliknąć                      |
| `st.data_editor('Edytuj dane', data)`            | edytor danych - umożliwia użytkownikowi modyfikację danych w aplikacji |
| `st.checkbox('Zaznacz')`                    | tworzy pole wyboru (checkbox) – można je zaznaczyć lub odznaczyć.    |
| `st.radio('Wybierz jedną opcję:', ['cat', 'dog'])`| tworzy grupę opcji wyboru (radio buttons) – umożliwia wybór jednej z opcji |
| `st.selectbox('Wybierz', [1, 2, 3])`             | tworzy rozwijane menu, w którym użytkownik wybiera jedną z opcji   |
| `st.multiselect('Wybór wielu opcji', [1, 2, 3])` | tworzy rozwijane menu umożliwiające wybór wielu opcji                |
| `st.slider('Przesuń', min_value=0, max_value=10)` | tworzy suwak do wyboru wartości w określonym zakresie             |
| `st.select_slider('Przesuń, aby wybrać', options=[1, '2'])` | tworzy suwak z listą opcji do wyboru                              |
| `st.text_input('Wpisz tekst')`                   | tworzy pole tekstowe, w którym użytkownik może wprowadzić dane     |
| `st.number_input('Wpisz liczbę')`                | tworzy pole do wprowadzania liczb                                   |
| `st.text_area('Wpisz tekst w większym polu')`    | tworzy pole tekstowe z możliwością wprowadzania dłuższych danych (wielowierszowe) |
| `st.date_input('Wybierz datę')`                  | tworzy pole do wprowadzania daty                                    |
| `st.time_input('Wpisz godzinę')`                 | tworzy pole do wprowadzania godziny                                |
| `st.file_uploader('Prześlij plik')`              | tworzy widżet do przesyłania plików przez użytkownika               |
| `st.download_button('Pobierz dane', data)`      | tworzy przycisk do pobierania danych (np. pliku)                    |
| `st.camera_input("Kliknij, aby zrobić zdjęcie!")`| tworzy widżet do robienia zdjęć za pomocą kamery  |
| `st.color_picker('Wybierz kolor')`              | tworzy widżet do wybierania koloru                                  |

""")

st.subheader('Wyświetlanie postępu i statusu')

st.markdown("""
| Funkcja / składnia                                    | Opis                                                                 |
|-------------------------------------------------------|----------------------------------------------------------------------|
| `with st.spinner(text='W trakcie...'):`               | wyświetla spinner podczas trwającego procesu |
| `st.success('Ukończono')`                             | wyświetla komunikat o sukcesie, np. po zakończeniu procesu          |
| `bar = st.progress(50)`                              | wyświetla pasek postępu ustawiony na wartość 50%                     |
| `bar.progress(100)`                                   | aktualizuje pasek postępu do wartości 100%                          |
| `st.error('Wiadomość o błędzie')`                      | wyświetla komunikat o błędzie                                       |
| `st.warning('Wiadomość ostrzegawcza')`                 | wyświetla komunikat ostrzegawczy                                    |
| `st.info('Wiadomość informacyjna')`                   | wyświetla komunikat informacyjny                                    |
| `st.success('Wiadomość o sukcesie')`                  | wyświetla komunikat o sukcesie                                      |
| `st.exception(e)`                                     | wyświetla szczegóły wyjątku, np. w przypadku błędu w kodzie         |

""")

st.markdown(''' 
---
### Przykłady użycia wybrnaych funkcji:
''')

st.markdown('''
```python
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import time, date

st.title("📘 Przegląd funkcji Streamlit")
st.header("1. Teksty i formatowanie")
st.text("To jest tekst")
st.markdown("**Pogrubienie**, _kursywa_, `kod`, ~~przekreślenie~~")
st.caption("To jest podpis np. pod wykresem")
st.latex(r"e^{i\pi} + 1 = 0")
st.write("Lista:", [1, 2, 3])
st.code("for i in range(5):\n    print(i)", language="python")

st.header("2. Kolumny i zakładki")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Dane")
    df = pd.DataFrame({
    'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław'],
    'Liczba mieszkańców (mln)': [1.8, 0.8, 0.5, 0.6],
    'Powierzchnia (km²)': [517, 327, 262, 293],
    'PKB': [150000, 120000, 110000, 130000]})
    df['Liczba mieszkańców (mln)'] = df['Liczba mieszkańców (mln)'].map('{:.1f}'.format)
    st.dataframe(df)
    st.json({'name': 'Streamlit', 'type': 'framework'})
    st.metric(label="Temperatura", value="22°C", delta="1.2°C")
    

with col2:
    st.subheader("Multimedia")
    st.image("https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg?format=2500w", caption="Obrazek kota")

st.subheader("Wykres")
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

tab1, tab2 = st.tabs(["Zakładka 1", "Zakładka 2"])
with tab1:
    st.write("To jest zakładka 1")
with tab2:
    st.write("To jest zakładka 2")

st.header("3. Widżety interaktywne")

col1, col2 = st.columns(2)

with col1:
    st.button("Kliknij mnie")
    st.checkbox("Zaznacz mnie")
    st.radio("Wybierz zwierzę", ["Kot", "Pies"])
    st.selectbox("Wybierz liczbę", [1, 2, 3])
    st.multiselect("Wybierz wiele", ["A", "B", "C"])
    st.slider("Przesuń", 0, 100)
    st.select_slider("Przesuń, aby wybrać", options=["Mało", "Średnio", "Dużo"])

with col2:
    st.text_input("Wpisz imię")
    st.number_input("Wpisz liczbę", step=1)
    st.text_area("Opisz swój dzień")
    st.date_input("Wybierz datę", value=date.today())
    st.time_input("Wpisz godzinę", value=time(12, 0))
    st.file_uploader("Prześlij plik")
    data = pd.DataFrame({"kolumna": [1, 2, 3]})
    st.download_button("📥 Pobierz dane", data.to_csv().encode("utf-8"), "dane.csv")
    
st.header("4. Status i postęp")
with st.spinner("⏳ Ładowanie..."):
    st.success("✅ Gotowe!")

st.info("To jest informacja")
st.warning("To jest ostrzeżenie")
st.error("To jest błąd")
''')

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import time, date

st.title("📘 Przegląd funkcji Streamlit")
st.header("1. Teksty i formatowanie")
st.text("To jest tekst")
st.markdown("**Pogrubienie**, _kursywa_, `kod`, ~~przekreślenie~~")
st.caption("To jest podpis np. pod wykresem")
st.latex(r"e^{i\pi} + 1 = 0")
st.write("Lista:", [1, 2, 3])
st.code("for i in range(5):\n    print(i)", language="python")

st.header("2. Kolumny i zakładki")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Dane")
    df = pd.DataFrame({
    'Miasto': ['Warszawa', 'Kraków', 'Gdańsk', 'Wrocław'],
    'Liczba mieszkańców (mln)': [1.8, 0.8, 0.5, 0.6],
    'Powierzchnia (km²)': [517, 327, 262, 293],
    'PKB': [150000, 120000, 110000, 130000]})
    df['Liczba mieszkańców (mln)'] = df['Liczba mieszkańców (mln)'].map('{:.1f}'.format)
    st.dataframe(df)
    st.json({'name': 'Streamlit', 'type': 'framework'})
    st.metric(label="Temperatura", value="22°C", delta="1.2°C")
    

with col2:
    st.subheader("Multimedia")
    st.image("https://images.squarespace-cdn.com/content/v1/607f89e638219e13eee71b1e/1684821560422-SD5V37BAG28BURTLIXUQ/michael-sum-LEpfefQf4rU-unsplash.jpg?format=2500w", caption="Obrazek kota")

st.subheader("Wykres")
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

tab1, tab2 = st.tabs(["Zakładka 1", "Zakładka 2"])
with tab1:
    st.write("To jest zakładka 1")
with tab2:
    st.write("To jest zakładka 2")

st.header("3. Widżety interaktywne")

col1, col2 = st.columns(2)

with col1:
    st.button("Kliknij mnie")
    st.checkbox("Zaznacz mnie")
    st.radio("Wybierz zwierzę", ["Kot", "Pies"])
    st.selectbox("Wybierz liczbę", [1, 2, 3])
    st.multiselect("Wybierz wiele", ["A", "B", "C"])
    st.slider("Przesuń", 0, 100)
    st.select_slider("Przesuń, aby wybrać", options=["Mało", "Średnio", "Dużo"])

with col2:
    st.text_input("Wpisz imię")
    st.number_input("Wpisz liczbę", step=1)
    st.text_area("Opisz swój dzień")
    st.date_input("Wybierz datę", value=date.today())
    st.time_input("Wpisz godzinę", value=time(12, 0))
    st.file_uploader("Prześlij plik")
    data = pd.DataFrame({"kolumna": [1, 2, 3]})
    st.download_button("📥 Pobierz dane", data.to_csv().encode("utf-8"), "dane.csv")
    
st.header("4. Status i postęp")
with st.spinner("⏳ Ładowanie..."):
    st.success("✅ Gotowe!")

st.info("To jest informacja")
st.warning("To jest ostrzeżenie")
st.error("To jest błąd")
