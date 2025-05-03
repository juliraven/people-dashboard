import streamlit as st
from streamlit_extras.app_logo import add_logo

st.set_page_config(page_title="Wizualizacja danych - streamlit", layout="wide")

st.sidebar.image('logo.png', use_container_width=False)

def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url('../../logo.png'); /* Zmień URL na swoje logo */
                background-repeat: no-repeat;
                padding-top: 100px; /* Dostosuj przestrzeń, aby logo było widoczne */
                background-position: center top; /* Centruje tło */
                background-size: 80px 80px; /* Ustawia rozmiar logo */
            }
            [data-testid="stSidebarNav"]::before {
                font-size: 24px; /* Zmień rozmiar czcionki */
                font-weight: bold;
                color: #333; /* Kolor tekstu */
                position: relative;
                top: -40px; /* Przesunięcie tekstu w górę */
                margin-left: 20px; /* Odstęp od lewej strony */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Wywołanie funkcji, aby dodać logo i nazwę firmy
add_logo()

st.title("Czym jest Streamlit?")

st.markdown(
    '''
    <p>
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
    <p>
    Utworzoną aplikację można w łatwy sposób wdrożyć dzięki <a href="https://docs.streamlit.io/" style="color:#66ccff; font-weight:bold;">chmurze</a> za pomocą kilku kliknięć.
    </p>
    ''',
    unsafe_allow_html=True
)

st.title("Pierwsze kroki")

st.markdown(
    '''
    <p>
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
    <p>
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
    <p>
    Aplikację można utworzyć w dowolnym edytorze tekstowym. Należy ją zapisać następnie do pliku z rozszerzeniem <code>.py</code>, np. <code>streamlit_app.py</code>. W pliku tym wpisujemy przykładowy kod:
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
    <p>
    Następnie w terminalu wiersza poleceń wpisujemy:
    </p>
    ''',
    unsafe_allow_html=True
)

code = '''
streamlit run streamlit_app.py
'''

st.code(code, language='python')

st.markdown(
    '''
    <p>
    Powinno to uruchomić przeglądarkę, która wyświetli aplikację.
    </p>
    ''',
    unsafe_allow_html=True
)

st.title("Udostępnianie aplikacji")

st.markdown(
    '''
    <p>
    Utworzoną aplikację można udostępnić do publicznego użytku przy pomocy <a href="https://github.com/" style="color:#66ccff; font-weight:bold;">Githuba</a>. Wystarczy utworzyć konto i repozytorium, które można użyć do udostępnienia aplikacji za pomocą wyżej wspomnianej chmury.
    </p>
    ''',
    unsafe_allow_html=True
)


st.markdown(
    '''
    <p>
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
    <p>
    W pliku <code>requirements.txt</code> umieszczamy używane w apliakcji biblioteki. Może on wyglądać w następujący sposób:
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
