import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html_code = """
<style>
#game-container {
    position: relative;
    width: 100%;
    height: 500px;
    transition: all 0.3s ease;
    z-index: 1;
}

#game-container.fullscreen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    z-index: 9999;
    background: black;
}

#game-container iframe {
    width: 100%;
    height: 100%;
    border: none;
}

#fullscreen-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    z-index: 10000;
    padding: 8px 12px;
    background: #000;
    color: #fff;
    border: none;
    cursor: pointer;
}
</style>

<div id="game-container">
    <button id="fullscreen-btn" onclick="toggleFullscreen()">Fullscreen</button>
    <iframe 
        src="https://arcade.makecode.com/---codeembed#pub:S00850-85347-54510-79145"
        allowfullscreen>
    </iframe>
</div>

<script>
function toggleFullscreen() {
    const container = document.getElementById("game-container");
    container.classList.toggle("fullscreen");
}
</script>
"""

components.html(html_code, height=600)
