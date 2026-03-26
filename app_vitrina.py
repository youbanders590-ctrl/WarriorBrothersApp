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
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Roboto:wght@300;400&display=swap');

    /* Fondo general con un ligero degradado */
    .stApp { 
        background: linear-gradient(180deg, #f8f9fa 0%, #e9ecef 100%); 
    }

    /* Contenedor Negro Principal (Efecto Elevado) */
    .hero-container {
        background: #121212;
        padding: 80px 40px;
        border-radius: 30px;
        text-align: center;
        color: white;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        border: 1px solid #333;
        margin-bottom: 50px;
    }

    .flex-header { 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        gap: 25px; 
    }

    .logo-img { width: 100px; filter: drop-shadow(0 0 10px rgba(255,255,255,0.2)); }

    /* Tipografía Premium */
    .main-title { 
        font-family: 'Montserrat', sans-serif; 
        font-size: 4rem; 
        letter-spacing: -2px; 
        margin: 0; 
        background: linear-gradient(90deg, #ffffff, #a8a8a8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Botón WhatsApp con Animación de Pulso */
    .btn-wa {
        background: linear-gradient(45deg, #25D366, #128C7E);
        color: white !important;
        padding: 18px 45px;
        text-decoration: none;
        border-radius: 15px;
        font-family: 'Montserrat', sans-serif;
        font-weight: 700;
        display: inline-block;
        transition: 0.3s;
        box-shadow: 0 10px 20px rgba(37, 211, 102, 0.3);
    }
    .btn-wa:hover {
        transform: scale(1.05);
        box-shadow: 0 15px 30px rgba(37, 211, 102, 0.5);
    }

    /* Tarjetas de Servicio Estilo Apple */
    .service-card {
        background: white;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        border: 1px solid rgba(0,0,0,0.05);
        box-shadow: 0 10px 30px rgba(0,0,0,0.05);
        transition: 0.3s;
    }
    .service-card:hover {
        transform: translateY(-10px);
        box-shadow: 0 20px 40px rgba(0,0,0,0.1);
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
        <p style="font-family: 'Roboto', sans-serif; font-size: 1.4rem; color: #a8a8a8; font-weight: 300; margin-top: 15px;">
            MAESTRÍA EN RESTAURACIÓN DE CALZADO Y CUERO
        </p>
        <br><br>
        <a href="https://wa.me/593994718745" class="btn-wa">COTIZAR TRABAJO</a>
    </div>
    """, unsafe_allow_html=True)

# --- SERVICIOS ---
col1, col2, col3, col4 = st.columns(4)
servicios = [
    ["👞 Suelas", "Cambio de suelas de alta montaña y ciudad."],
    ["🎨 Tinturado", "Restauración de color con pigmentos europeos."],
    ["👠 Tacos", "Reparación estructural para calzado fino."],
    ["🎒 Cuero", "Costura y restauración de bolsos y chaquetas."]
]

for col, ser in zip([col1, col2, col3, col4], servicios):
    with col:
        st.markdown(f"""<div class="service-card"><h3>{ser[0]}</h3><p>{ser[1]}</p></div>""", unsafe_allow_html=True)
