import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="I Love You ❤️", layout="wide")

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
    width: 100%;
    height: 600px;
    display: block;
}
</style>
</head>
<body>
<canvas id="c"></canvas>
<script>
const canvas = document.getElementById("c");
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

let start = performance.now();

function animate(now) {
    ctx.fillStyle = "black";
    ctx.fillRect(0, 0, W, H);

    const elapsed = (now - start) / 1000;
    const scale = Math.min(W / 38, H / 35);
    const count = Math.min(120, Math.floor(elapsed * 35));

    ctx.font = "bold 9px Arial";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillStyle = "#ffb6c1";
    ctx.shadowColor = "#ff69b4";
    ctx.shadowBlur = 6;

    for (let i = 0; i < count; i++) {
        const a = i * 2 * Math.PI / 120;

        const x = 16 * Math.pow(Math.sin(a), 3);
        const y = 13 * Math.cos(a)
                - 5 * Math.cos(2*a)
                - 2 * Math.cos(3*a)
                - Math.cos(4*a);

        ctx.fillText(
            "I love you",
            W / 2 + x * scale,
            H / 2 - y * scale
        );
    }

    if (count >= 120) {
        start = now;
    }

    requestAnimationFrame(animate);
}

requestAnimationFrame(animate);
</script>
</body>
</html>
""", height=610, scrolling=False)
