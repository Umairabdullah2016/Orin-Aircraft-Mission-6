import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html_code = """
<style>
#game-container {
    position: relative;
    width: 100%;
    height: 85vh;   /* enough space for controls */
    background: black;
}

#game-container iframe {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;   /* critical: NOT 200% */
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

components.html(html_code, height=750)
