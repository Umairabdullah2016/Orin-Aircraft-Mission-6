import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html_code = """
<style>
#game-container {
    position: relative;
    width: 100%;
    height: 80vh;  /* KEY FIX */
    background: black;
}

#game-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    border: none;
}
</style>

<div id="game-container">
    <iframe 
        src="https://arcade.makecode.com/---run?id=S00850-85347-54510-79145"
        allowfullscreen
        sandbox="allow-popups allow-forms allow-scripts allow-same-origin">
    </iframe>
</div>
"""

components.html(html_code, height=700)
