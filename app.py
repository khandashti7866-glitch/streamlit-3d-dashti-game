import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="3D HD Car Game (Streamlit + Three.js)", layout="wide")

st.title("3D HD Car Game embedded in Streamlit")
st.markdown(
    "Playable 3D driving demo embedded in Streamlit using Three.js (client-side). "
    "Controls: W/S accelerate/brake, A/D steer, R reset. "
    "Note: This is a browser-based 3D game (WebGL) embedded in your Streamlit app."
)

# The entire HTML/JS game (Three.js) will be embedded as inline HTML.
# If you want to edit visuals, open this string and change geometry / materials / assets.
game_html = r"""
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Embedded 3D Car Game</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <style>
    html,body { margin:0; height:100%; overflow:hidden; background:#111; }
    #ui {
      position: absolute; left: 12px; top: 12px; color: #fff; font-family: Arial, sans-serif;
      z-index: 5; user-select:none;
    }
    #speed { font-size: 18px; margin-bottom: 8px; }
    #instructions { font-size:12px; color:#ddd; opacity:0.95; max-width:320px; }
    #buttons { margin-top:8px; }
    button { background:#1e1e1e; color:#fff; border:1px solid #444; padding:6px 10px; cursor:pointer; }
    button:hover { background:#2b2b2b; }
    canvas { display:block; width:100%; height:100%; }
    #message { position:absolute; right:12px; top:12px; color:#ffb3b3; font-family:monospace; z-index:5; }
  </style>
</head>
<body>
  <div id="ui">
    <div id="speed">Speed: 0 km/h</div>
    <div id="instructions">
      Controls: W / S =
