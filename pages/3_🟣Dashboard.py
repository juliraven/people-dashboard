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


from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter

code = '''def hello():\n    print("Hello, world!")'''

formatter = HtmlFormatter(style="monokai", full=False, noclasses=True)
highlighted_code = highlight(code, PythonLexer(), formatter)

blurred = f"<div style='filter: blur(1px);'>{highlighted_code}</div>"
st.markdown(blurred, unsafe_allow_html=True)

