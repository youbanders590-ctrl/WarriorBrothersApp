import streamlit as st
import base64

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="The Warrior Brothers", page_icon="👞", layout="wide")

# --- FUNCIÓN LOGO ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

logo_base_64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" class="logo-img">' if logo_base_64 else ""

# --- MEJORAS GRÁFICAS (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Roboto:wght@300;400;700&display=swap');

    /* Fondo general */
    .stApp { 
        background-color: #f4f4f4; 
    }

    /* Contenedor Negro Principal */
    .hero-container {
        background: #121212;
        padding: 90px 40px;
        border-radius: 30px;
        text-align: center;
        color: white;
        box-shadow: 0 20px 50px rgba(0,0,0,0.6);
        border: 1px solid #333;
        margin-bottom: 50px;
    }

    .flex-header { 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        gap: 25px; 
        flex-wrap: wrap;
    }

    .logo-img { width: 110px; filter: drop-shadow(0 0 15px rgba(255,255,255,0.1)); }

    /* TÍTULO CON DIFUMINADO AMARILLO (SOLICITADO) */
    .main-title { 
        font-family: 'Montserrat', sans-serif; 
        font-size: 4.5rem; 
        letter-spacing: -2px; 
        margin: 0; 
        /* Degradado de Blanco a Amarillo Dorado */
        background: linear-gradient(90deg, #FFFFFF 30%, #FFD700 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900;
        line-height: 1.1;
    }

    /* Subtítulo */
    .sub-title {
        font-family: 'Roboto', sans-serif;
        font-size: 1.6rem;
        color: #FFD700; /* Amarillo para resaltar */
        font-weight: 400;
        margin-top: 15px;
        letter-spacing: 2px;
    }

    /* Botón WhatsApp */
    .btn-wa {
        background: linear-gradient(45deg, #25D366, #128C7E);
        color: white !important;
        padding: 20px 50px;
        text-decoration: none;
        border-radius: 50px;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        display: inline-block;
        transition: 0.4s;
        box-shadow: 0 10px 25px rgba(37, 211, 102, 0.4);
        margin-top: 30px;
        text-transform: uppercase;
    }
    .btn-wa:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(37, 211, 102, 0.6);
    }

    /* Tarjetas de Servicio - MEJORADA VISIBILIDAD */
    .service-card {
        background: white;
        border-radius: 20px;
        padding: 35px 25px;
        text-align: center;
        border: 2px solid #eeeeee;
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
        transition: 0.3s ease-in-out;
        height: 100%;
    }
    .service-card:hover {
        transform: translateY(-10px);
        border-color: #FFD700;
        box-shadow: 0 20px 45px rgba(0,0,0,0.15);
    }
    .service-card h3 {
        font-family: 'Montserrat', sans-serif;
        color: #121212;
        font-size: 1.8rem;
        margin-bottom: 15px;
    }
    .service-card p {
        font-family: 'Roboto', sans-serif;
        color: #444; /* Gris oscuro para lectura fácil */
        font-size: 1.1rem;
        line-height: 1.4;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO ---
st.markdown(f"""
    <div class="hero-container">
        <div class="flex-header">
            {logo_html}
            <h1 class="main-title">THE WARRIOR BROTHERS</h1>
        </div>
        <p class="sub-title">MAESTRÍA EN RESTAURACIÓN DE CALZADO Y CUERO</p>
        <p style="font-family: 'Roboto', sans-serif; font-size: 1.2rem; color: #a8a8a8; margin-top: 10px;">
            Artesanía Lojana con Precisión Digital
        </p>
        <a href="https://wa.me/593994718745" class="btn-wa">Cotizar mi Trabajo</a>
    </div>
    """, unsafe_allow_html=True)

# --- SERVICIOS ---
st.markdown("<h2 style='text-align: center; font-family: Montserrat; margin-bottom: 40px;'>Nuestras Especialidades</h2>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
servicios = [
    ["👞 Suelas", "Cambio de suelas de alta montaña y ciudad con pegado industrial."],
    ["🎨 Tinturado", "Restauración de color total con pigmentos de alta gama."],
    ["👠 Tacos", "Reparación estructural y tapas para calzado formal."],
    ["🎒 Cuero", "Mantenimiento y costura de bolsos, chaquetas y accesorios."]
]

for col, ser in zip([col1, col2, col3, col4], servicios):
    with col:
        st.markdown(f"""
            <div class="service-card">
                <h3>{ser[0]}</h3>
                <p>{ser[1]}</p>
            </div>
            """, unsafe_allow_html=True)

st.markdown("<br><br><center style='color: #888;'>© 2026 The Warrior Brothers | Loja, Ecuador</center>", unsafe_allow_html=True)
