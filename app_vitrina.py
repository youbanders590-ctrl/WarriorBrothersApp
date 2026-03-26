import streamlit as st
import base64

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="The Warrior Brothers", page_icon="👞", layout="wide")

# --- FUNCIÓN MAESTRA PARA CARGAR EL LOGO ---
# Usamos base64 para cargar el logo.png localmente y que no se rompa
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except:
        return None

logo_base_64 = get_base64_image("logo.png")
# Si el logo carga bien, creamos la etiqueta img con los datos
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" class="logo-img">' if logo_base_64 else ""

# --- MEJORAS GRÁFICAS (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@900&family=Roboto:wght@300;400&display=swap');

    /* Fondo general con un ligero degradado suave */
    .stApp { 
        background: linear-gradient(180deg, #fcfdfa 0%, #e9ecef 100%); 
    }

    /* Contenedor Negro Principal (Efecto Hero Elevado) */
    .hero-black {
        background-color: #121212; /* Negro profundo carbón */
        color: white; 
        padding: 90px 40px; 
        border-radius: 30px; 
        text-align: center; 
        margin-bottom: 50px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.5); /* Sombra suave para efecto de elevación */
        border: 1px solid #333; /* Borde sutil */
    }

    .flex-header { 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        margin-bottom: 25px; 
    }

    .logo-img { 
        max-width: 100px; 
        height: auto; 
        margin-right: 25px; 
        /* filter: brightness(0) invert(1); Descomenta si tu logo es negro para hacerlo blanco */
    }

    /* Tipografía Premium para el Título Principal */
    .title-text { 
        font-family: 'Montserrat', sans-serif; 
        font-size: 3.8rem; 
        font-weight: 900; 
        letter-spacing: -2px; 
        margin: 0; 
        background: linear-gradient(90deg, #ffffff, #a8a8a8); /* Brillo metálico sutil */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Subtítulo y Texto de Lectura */
    .subtitle-text {
        font-family: 'Roboto', sans-serif;
        font-size: 1.5rem;
        font-weight: 300;
        color: #ccc; /* Gris suave */
        margin-top: 15px;
    }

    /* Botón de WhatsApp con Animación de Pulso */
    .whatsapp-btn {
        background: linear-gradient(45deg, #25D366, #128C7E); /* Degradado verde */
        color: white !important; 
        padding: 18px 45px; 
        text-decoration: none;
        font-family: 'Montserrat', sans-serif;
        font-size: 1.2rem; 
        font-weight: 700; 
        border-radius: 50px; 
        text-align: center;
        display: inline-block; 
        transition: 0.3s ease; 
        box-shadow: 0 10px 20px rgba(37, 211, 102, 0.3); /* Sombra del botón */
        border: none;
    }
    .whatsapp-btn:hover { 
        background-color: #1ebe57; 
        transform: scale(1.05); /* Efecto de aumento al pasar el mouse */
        box-shadow: 0 15px 30px rgba(37, 211, 102, 0.5); 
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENIDO ---
# Usamos f-string para insertar el logo_html dentro del bloque HTML
st.markdown(f"""
    <div class="hero-black">
        
        <div class="flex-header">
            {logo_html}
            <h1 class="title-text">THE WARRIOR BROTHERS</h1>
        </div>
        
        <p class="subtitle-text">MAESTRÍA EN RESTAURACIÓN DE CALZADO Y CUERO</p>
        <p style="font-size: 1.1rem; margin-top: 20px; max-width: 800px; margin-left: auto; margin-right: auto;">
            No solo reparamos, devolvemos la esencia a tus artículos favoritos. Artesanía lojana con precisión digital.
        </p>
        <br><br>
        <a href="https://wa.me/593994718745?text=¡Hola%20Warrior%20Brothers!%20Quisiera%20cotizar%20una%20reparación" target="_blank" class="whatsapp-btn">COTIZAR MI TRABAJO</a>
    </div>
    """, unsafe_allow_html=True)
