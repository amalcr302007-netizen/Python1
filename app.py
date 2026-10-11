import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="I Love You ❤️",
    page_icon="❤️",
    layout="wide"
)

components.html("""
<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
html, body {
    margin: 0;
    padding: 0;
    background: #000;
    overflow: hidden;
}
canvas {
    display: block;
    width: 100%;
    height: 560px;
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
    const rect = canvas.getBoundingClientRect();
    W = rect.width;
    H = rect.height;
    canvas.width = W * dpr;
    canvas.height = H * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
}
resize();
window.addEventListener("resize", resize);

const totalLines = 90;
let progress = 0;
let lastTime = 0;

function heartPoint(t, scale) {
    return {
        x: 16 * Math.pow(Math.sin(t), 3) * scale,
        y: -(13 * Math.cos(t)
           - 5 * Math.cos(2*t)
           - 2 * Math.cos(3*t)
           - Math.cos(4*t)) * scale
    };
}

function drawHeart(scale, fraction, color) {
    const cx = W / 2;
    const cy = H / 2;
    const steps = 220;
    const end = Math.floor(steps * fraction);

    ctx.beginPath();

    for (let i = 0; i <= end; i++) {
        const t = (i / steps) * Math.PI * 2;
        const p = heartPoint(t, scale);

        if (i === 0) {
            ctx.moveTo(cx + p.x, cy + p.y);
        } else {
            ctx.lineTo(cx + p.x, cy + p.y);
        }
    }

    ctx.strokeStyle = color;
    ctx.lineWidth = 0.8;
    ctx.stroke();
}

function animate(time) {
    if (!lastTime) lastTime = time;
    const delta = Math.min(time - lastTime, 50);
    lastTime = time;

    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, W, H);

    const fit = Math.min(W / 38, H / 35);
    const maxScale = fit;
    const speed = 0.0007;

    progress += delta * speed;
    if (progress > totalLines) progress = 0;

    // Build the heart line by line
    for (let i = 0; i < Math.min(totalLines, Math.floor(progress) + 1); i++) {
        const scale = maxScale * (0.25 + 0.75 * (i + 1) / totalLines);
        const fraction = i < Math.floor(progress) ? 1 :
                         progress - Math.floor(progress);

        const pink = Math.floor(182 + 55 * i / totalLines);
        drawHeart(scale, fraction, `rgb(255,${pink},${pink})`);
    }

    requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
</script>
</body>
</html>
""", height=570, scrolling=False)
