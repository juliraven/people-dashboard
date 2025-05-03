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

import streamlit as st
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

code = '''def hello():\n    print("Hello, world!")'''

# Kolorowanie kodu HTML z Pygments
formatter = HtmlFormatter(style="monokai", full=False, noclasses=True)
highlighted_code = highlight(code, PythonLexer(), formatter)

# Stylizowany kontener przypominający `st.code()`, z efektem blur
custom_html = f"""
<div style="
    background-color: #0e1117;
    color: #ffffff;
    border-radius: 8px;
    padding: 1rem;
    font-family: monospace;
    font-size: 0.9rem;
    border: 1px solid #30363d;
    overflow-x: auto;
    filter: blur(1.5px);
">
{highlighted_code}
</div>
"""

# Wyświetlenie w Streamlit z HTML-em
st.markdown(custom_html, unsafe_allow_html=True)

