import streamlit as st
import streamlit.components.v1 as components

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="For My Valentine 🌹", layout="centered")

# ---------------- STYLING ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #fff1f2, #ffe4e6);
    text-align: center;
}

.stButton > button {
    width: 100%;
    border-radius: 30px;
    background: linear-gradient(45deg, #ff4b4b, #e11d48);
    color: white;
    height: 3.5em;
    font-size: 18px;
    font-weight: bold;
    box-shadow: 0px 6px 20px rgba(255, 75, 75, 0.4);
    transition: all 0.3s ease;
}

.stButton > button:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "rose_count" not in st.session_state:
    st.session_state.rose_count = 1

# ---------------- BOUQUET FUNCTION ----------------
def draw_bouquet(count):

    rose_positions = [

        # Top Layer (5)
        (100, 55, 0),
        (70, 70, -25),
        (130, 70, 25),
        (50, 85, -35),
        (150, 85, 35),

        # Upper Middle (5)
        (85, 95, -15),
        (115, 95, 15),
        (65, 110, -25),
        (135, 110, 25),
        (100, 110, 0),

        # Lower Middle (5)
        (80, 130, -20),
        (120, 130, 20),
        (60, 145, -30),
        (140, 145, 30),
        (100, 145, 0),

        # Bottom Layer (5)
        (85, 165, -15),
        (115, 165, 15),
        (70, 180, -20),
        (130, 180, 20),
        (100, 185, 0),
    ]

    roses_svg = ""
    stems_svg = ""

    for i in range(min(count, 20)):
        x, y, angle = rose_positions[i]

        stems_svg += f"""
        <path d="M{x} {y+20} Q100 250 100 310"
              stroke="#2e7d32"
              stroke-width="3"
              fill="none" />
        """

        roses_svg += f"""
        <g transform="rotate({angle}, {x}, {y})">
            <ellipse cx="{x}" cy="{y}" rx="18" ry="16"
                     fill="url(#petalGrad)" />
            <ellipse cx="{x}" cy="{y}" rx="9" ry="9"
                     fill="#8b0000" />
        </g>
        """

    svg_code = f"""
    <svg viewBox="0 0 220 400" xmlns="http://www.w3.org/2000/svg">

        <defs>
            <radialGradient id="petalGrad">
                <stop offset="0%" stop-color="#ff8fa3"/>
                <stop offset="100%" stop-color="#c1121f"/>
            </radialGradient>

            <linearGradient id="outerWrapGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#ffffff"/>
                <stop offset="100%" stop-color="#eeeeee"/>
            </linearGradient>

            <linearGradient id="innerWrapGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#ffffff"/>
                <stop offset="100%" stop-color="#f5f5f5"/>
            </linearGradient>
        </defs>

        <!-- OUTER WRAP -->
        <path d="M100 370 L35 170 L165 170 Z"
              fill="url(#outerWrapGrad)"
              stroke="#dddddd"
              stroke-width="2"/>

        <!-- INNER WRAP -->
        <path d="M100 350 L65 220 L135 220 Z"
              fill="url(#innerWrapGrad)"
              stroke="#e0e0e0"
              stroke-width="1.5"/>

        <!-- FOLD LINES -->
        <line x1="65" y1="220" x2="100" y2="350"
              stroke="#dcdcdc" stroke-width="1"/>
        <line x1="135" y1="220" x2="100" y2="350"
              stroke="#dcdcdc" stroke-width="1"/>

        <!-- STEMS -->
        {stems_svg}

        <!-- RIBBON -->
        <ellipse cx="100" cy="280" rx="30" ry="12"
                 fill="#e11d48"/>
        <circle cx="100" cy="280" r="6"
                fill="#be123c"/>

        <!-- ROSES -->
        {roses_svg}

    </svg>
    """

    return svg_code

# ---------------- UI ----------------
st.title("🌹 How long will you go , Sarah !")

components.html(
    draw_bouquet(st.session_state.rose_count),
    height=420,
)

st.write("")
st.write("")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    if st.session_state.rose_count < 20:
        if st.button("Add a Rose 🌹", use_container_width=True):
            st.session_state.rose_count += 1
    else:
        st.balloons()
        st.success("So much love! 💖")
        if st.button("Start Over", use_container_width=True):
            st.session_state.rose_count = 1

