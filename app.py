import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="I Love You ❤️", layout="wide")

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
html, body {
    margin: 0;
    padding: 0;
    background: black;
    overflow: hidden;
}
canvas {
    display: block;
    width: 100%;
    height: 600px;
}
</style>
</head>
<body>
<canvas id="heart"></canvas>

<script>
const canvas = document.getElementById("heart");
const ctx = canvas.getContext("2d");

let W, H;

function resize() {
    const dpr = window.devicePixelRatio || 1;
    W = canvas.clientWidth;
    H = canvas.clientHeight;
    canvas.width = W * dpr;
    canvas.height = H * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}

resize();
window.addEventListener("resize", resize);

const total = 120;
const duration = 3500;
const pause = 500;
const cycle = duration + pause;

function animate(now) {
    const elapsed = now % cycle;
    const progress = Math.min(1, elapsed / duration);
    const count = Math.floor(progress * total);

    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, W, H);

    const scale = Math.min(W / 38, H / 35);

    ctx.font = "bold 9px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillStyle = "#ffb6c1";
    ctx.shadowColor = "#ff69b4";
    ctx.shadowBlur = 5;

    for (let i = 0; i < count; i++) {
        const angle = i * Math.PI * 2 / total;

        const x = 16 * Math.pow(Math.sin(angle), 3);
        const y = 13 * Math.cos(angle)
                - 5 * Math.cos(2 * angle)
                - 2 * Math.cos(3 * angle)
                - Math.cos(4 * angle);

        ctx.fillText(
            "I love you",
            W / 2 + x * scale,
            H / 2 - y * scale
        );
    }

    requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
</script>
</body>
</html>
""", height=610, scrolling=False)
