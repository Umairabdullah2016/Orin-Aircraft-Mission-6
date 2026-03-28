import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html_code = """
<style>
body {
    margin: 0;
    background: black;
}

#game-container {
    width: 100%;
    height: 100%;
}

#game-container iframe {
    width: 100%;
    height: 1400px;  /* KEY FIX */
    border: none;
}
</style>

<div id="game-container">
    <iframe 
        src="https://arcade.makecode.com/---run?id=S87889-51924-82524-20479"
        allowfullscreen
        sandbox="allow-popups allow-forms allow-scripts allow-same-origin">
    </iframe>
</div>
"""

components.html(html_code, height=1400)
