import streamlit as st
import base64

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="🛡️ The Warrior Brothers | Maestros en Reparación de Calzado",
    page_icon="👞",
    layout="wide",
)

# --- FUNCIÓN MAESTRA PARA CARGAR EL LOGO LOCAL ---
# Esto convierte tu logo.png en un código que el HTML entiende
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Intentamos cargar el logo localmente. Si no existe, usamos un emoji.
try:
    logo_base64 = get_base64_image("logo.png")
    # Si carga bien, creamos la etiqueta img con los datos
    logo_html = f'<img src="data:image/png;base64,{logo_base64}" class="logo-img">'
except FileNotFoundError:
    # Si el archivo no está, ponemos un emoji para no romper el diseño
    logo_html = '<span style="font-size: 80px; margin-right: 20px;">🐺</span>'

# --- ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    /* Fondo y texto general */
    .stApp { background-color: #fcfdfa; color: #1e1e1e; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    
    /* Botón de WhatsApp */
    .whatsapp-btn {
        background-color: #25D366; color: white !important; padding: 15px 30px; text-decoration: none;
        font-size: 1.1rem; border-radius: 50px; font-weight: bold; text-align: center;
        display: inline-block; transition: all 0.3s ease; box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .whatsapp-btn:hover { background-color: #1ebe57; transform: translateY(-3px); color: white !important; }

    /* Estilo de la Cabecera Negra (Hero) */
    .hero-black {
        background-color: #1e1e1e; color: white; padding: 100px 40px; text-align: center; border-radius: 20px; margin-bottom: 50px;
    }
    .header-box {
        display: flex; align-items: center; justify-content: center; margin-bottom: 25px;
    }
    .logo-img {
        max-width: 100px; height: auto; margin-right: 25px;
        /*filter: brightness(0) invert(1); /* Descomenta si tu logo es negro para hacerlo blanco */
    }
    .title-text {
        color: white !important; font-size: 3.5rem; font-weight: 900; letter-spacing: -2px; margin: 0;
    }
    
    /* Tarjetas de Servicios */
    .service-card {
        background-color: white; border-radius: 15px; padding: 25px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06); text-align: center; height: 100%; border: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. SECCIÓN HÉROE (CON EL LOGO CORREGIDO) ---
st.markdown(f"""
    <div class="hero-black">
        
        <div class="header-box">
            {logo_html}
            <h1 class="title-text">THE WARRIOR BROTHERS</h1>
        </div>
        
        <p style="font-size: 1.6rem; font-weight: 300; color: #ccc;">Maestría en Restauración de Calzado y Cuero</p>
        <p style="font-size: 1.1rem; margin-top: 20px; max-width: 800px; margin-left: auto; margin-right: auto;">
            No solo reparamos, devolvemos la esencia a tus artículos favoritos. Artesanía lojana con precisión digital.
        </p>
        <br>
        <a href="https://wa.me/593994718745?text=¡Hola%20Warrior%20Brothers!%20Quisiera%20cotizar%20una%20reparación" target="_blank" class="whatsapp-btn">Cotizar mi Trabajo Ahora</a>
    </div>
    """, unsafe_allow_html=True)

# --- SERVICIOS Y CONTACTO (Resto de la página) ---
st.header("🛠️ Nuestros Servicios")
c1, c2, c3 = st.columns(3)
with c1: st.info("👞 **Suelas y Pisos**")
with c2: st.info("🎨 **Tinturado Pro**")
with c3: st.info("👠 **Tacos y Tapas**")

st.write("")
st.header("📍 Encuéntranos en Loja")
st.markdown("""
    **Dirección:** Centro de la ciudad, Loja, Ecuador<br>
    **WhatsApp:** [0994718745](https://wa.me/593994718745)
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align: center; color: #777; padding: 40px; border-top: 1px solid #eee; margin-top: 60px;">
        <p>© 2026 The Warrior Brothers. Orgullosamente Lojanos. 🛡️⚒️</p>
    </div>
    """, unsafe_allow_html=True)
