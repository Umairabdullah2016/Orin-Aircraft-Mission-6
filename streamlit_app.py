import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

html_code = """
<style>
html, body {
    margin: 0;
    padding: 0;
    overflow: hidden;
}

#game-container {
    position: relative;
    width: 100%;
    height: 1200px;
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

#fullscreen-btn {
    position: absolute;
    top: 10px;
    right: 10px;
    z-index: 9999;
    padding: 10px 14px;
    background: rgba(0,0,0,0.7);
    color: white;
    border: none;
    cursor: pointer;
    font-size: 14px;
}
</style>

<div id="game-container">
    <button id="fullscreen-btn" onclick="goFullscreen()">⛶ Fullscreen</button>
    
    <iframe 
        src="https://arcade.makecode.com/---run?id=S00850-85347-54510-79145"
        allowfullscreen
        sandbox="allow-popups allow-forms allow-scripts allow-same-origin">
    </iframe>
</div>

<script>
function goFullscreen() {
    const elem = document.getElementById("game-container");

    if (!document.fullscreenElement) {
        elem.requestFullscreen().catch(err => {
            alert("Fullscreen error: " + err.message);
        });
    } else {
        document.exitFullscreen();
    }
}
</script>
"""

components.html(html_code, height=620)
