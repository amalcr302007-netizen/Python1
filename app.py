import streamlit as st
import math
import time
import streamlit.components.v1 as components

st.set_page_config(page_title="Heart Animation", page_icon="💗")

st.title("💗 Heart Animation")
st.write("A glowing animated heart that runs in your browser.")

components.html("""
<!DOCTYPE html>
<html>
<head>
<style>
body {
    margin: 0;
    background: black;
    overflow: hidden;
}
canvas {
    display: block;
    width: 100%;
    height: 420px;
}
</style>
</head>
<body>
<canvas id="heart"></canvas>
<script>
const canvas = document.getElementById("heart");
const ctx = canvas.getContext("2d");

function resize() {
    canvas.width = window.innerWidth;
    canvas.height = 420;
}
resize();
window.addEventListener("resize", resize);

let start = performance.now();

function draw(now) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const scale = 13 + 2 * Math.sin((now-start)/250);
    const points = [];

    for (let i = 0; i < 600; i++) {
        const t = i * Math.PI * 2 / 600;
        const x = 16 * Math.pow(Math.sin(t), 3);
        const y = 13 * Math.cos(t)
                - 5 * Math.cos(2*t)
                - 2 * Math.cos(3*t)
                - Math.cos(4*t);

        points.push({
            x: canvas.width/2 + x*scale,
            y: canvas.height/2 - y*scale
        });
    }

    ctx.beginPath();
    points.forEach((p, i) => {
        if (i === 0) ctx.moveTo(p.x, p.y);
        else ctx.lineTo(p.x, p.y);
    });
    ctx.closePath();

    ctx.shadowColor = "#ff1744";
    ctx.shadowBlur = 25;
    ctx.fillStyle = "#ff4d88";
    ctx.fill();

    ctx.shadowBlur = 0;
    ctx.strokeStyle = "#ffc1d6";
    ctx.lineWidth = 2;
    ctx.stroke();

    requestAnimationFrame(draw);
}
requestAnimationFrame(draw);
</script>
</body>
</html>
""", height=440)
