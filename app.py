import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="I Love You ❤️",
    page_icon="❤️",
    layout="centered"
)

components.html("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
    body {
        margin: 0;
        background: black;
        overflow: hidden;
        font-family: Arial, sans-serif;
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

let width, height;

function resize() {
    const dpr = window.devicePixelRatio || 1;
    const rect = canvas.getBoundingClientRect();

    width = rect.width;
    height = rect.height;

    canvas.width = width * dpr;
    canvas.height = height * dpr;

    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}

resize();
window.addEventListener("resize", resize);

let startTime = performance.now();

function draw(now) {
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, width, height);

    // Six stages, corresponding to scales 11 through 16
    const stage = Math.floor((now - startTime) / 300) % 6;
    const scale = 11 + stage;

    // Fit the heart to both mobile and computer screens
    const size = Math.min(width / 36, height / 34);
    const s = scale * size / 14;

    const cx = width / 2;
    const cy = height / 2;

    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.font = "bold 8px Arial";
    ctx.fillStyle = "#ffb6c1";
    ctx.shadowColor = "#ff69b4";
    ctx.shadowBlur = 5;

    // Draw repeated text along the heart outline
    for (let i = 0; i < 120; i++) {
        const angle = i * Math.PI * 2 / 120;

        const x = 16 * Math.pow(Math.sin(angle), 3);
        const y = 13 * Math.cos(angle)
                - 5 * Math.cos(2 * angle)
                - 2 * Math.cos(3 * angle)
                - Math.cos(4 * angle);

        ctx.fillText(
            "I love you",
            cx + x * s,
            cy - y * s
        );
    }

    ctx.shadowBlur = 0;
    requestAnimationFrame(draw);
}

requestAnimationFrame(draw);
</script>

</body>
</html>
""", height=620, scrolling=False)
