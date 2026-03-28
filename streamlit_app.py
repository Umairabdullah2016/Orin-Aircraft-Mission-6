import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html_code = """
<style>
#wrap {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    height: 95vh;
    background: #000;
}

#game {
    width: 100%;
    height: 100%;
    max-width: 900px;   /* keeps aspect ratio nice */
}

#game iframe {
    width: 100%;
    height: 100%;
    border: none;
}
</style>

<div id="wrap">
    <div id="game">
        <iframe 
            src="https://arcade.makecode.com/---run?id=S87889-51924-82524-20479"
            allowfullscreen
            sandbox="allow-popups allow-forms allow-scripts allow-same-origin">
        </iframe>
    </div>
</div>
"""

components.html(html_code, height=900)
