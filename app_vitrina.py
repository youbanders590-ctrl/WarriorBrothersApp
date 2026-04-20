import streamlit as st
import streamlit.components.v1 as components
import base64

# --- 1. CONFIGURACIÓN INICIAL ---
st.set_page_config(page_title="The Warrior Brothers | Tienda y Taller", page_icon="🛡️", layout="wide")

def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except: return None

logo_base_64 = get_base64_image("logo.png")
logo_html = f'<img src="data:image/png;base64,{logo_base_64}" style="width:150px;">' if logo_base_64 else ""

# --- 2. ESTILOS CSS PERSONALIZADOS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;900&family=Open+Sans:wght@400;600&display=swap');
    
    .stApp { background-color: #ffffff; }
    
    /* Estilo del Menú Lateral */
    section[data-testid="stSidebar"] {
        background-color: #1a1a1a;
        color: white;
    }
    
    /* Secciones de la página */
    .hero-section {
        background: #1a1a1a; padding: 60px 20px; text-align: center; color: white;
        border-radius: 20px; margin-bottom: 30px;
    }
    .main-title { font-family: 'Montserrat', sans-serif; font-size: 3.5rem; font-weight: 900; color: #FFD700; }
    
    /* Tarjetas de Productos/Servicios */
    .product-card {
        background: white; border-radius: 15px; padding: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1); border: 1px solid #eee;
        text-align: center; margin-bottom: 20px;
    }
    .product-card h4 { color: #1a1a1a; margin-top: 10px; }
    .price-tag { color: #25D366; font-weight: 700; font-size: 1.2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. MENÚ DE NAVEGACIÓN (LAS TRES RAYITAS) ---
with st.sidebar:
    if logo_html:
        st.markdown(f"<center>{logo_html}</center>", unsafe_allow_html=True)
    st.markdown("---")
    opcion = st.radio("IR A:", ["🏠 Inicio", "🛠️ Servicios", "🛍️ Productos", "📍 Ubicación y Contacto"])
    st.markdown("---")
    st.markdown("📱 **WhatsApp:** 099 471 8745")

# --- 4. LÓGICA DE PÁGINAS ---

if opcion == "🏠 Inicio":
    st.markdown(f"""
        <div class="hero-section">
            <h1 class="main-title">THE WARRIOR BROTHERS</h1>
            <p style="letter-spacing: 2px;">CALIDAD ARTESANAL EN CADA REPARACIÓN</p>
        </div>
        """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Acerca de Nosotros")
        st.write("""
        En **The Warrior Brothers** somos especialistas en la reparación y mantenimiento de calzado, 
        mochilas y artículos de cuero. Con años de experiencia en Loja, combinamos técnicas tradicionales 
        con materiales modernos para devolverle la vida a tus objetos favoritos.
        """)
    with col2:
        st.info("💡 **Dato curioso:** Utilizamos pegamentos y tintes de grado europeo para garantizar que tu calzado resista el clima de Loja.")

elif opcion == "🛠️ Servicios":
    st.header("Servicios Profesionales")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="product-card"><h4>👞 Cambio de Suelas</h4><p>Vibram, cuero y goma antideslizante.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="product-card"><h4>🎨 Tinturado</h4><p>Recuperación de color y cambio de tono.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="product-card"><h4>👠 Tacos</h4><p>Cambio de tapas y refuerzo de estructura.</p></div>', unsafe_allow_html=True)

elif opcion == "🛍️ Productos":
    st.header("Nuestra Tienda")
    st.write("Complementos esenciales para el cuidado de tu calzado.")
    
    p1, p2, p3 = st.columns(3)
    with p1:
        st.markdown('<div class="product-card"><span>🧶</span><h4>Cordones Premium</h4><p>Varios colores y medidas reforzadas.</p><span class="price-tag">$2.50</span></div>', unsafe_allow_html=True)
    with p2:
        st.markdown('<div class="product-card"><span>👟</span><h4>Plantillas Confort</h4><p>Gel y espuma de alta densidad.</p><span class="price-tag">$5.00</span></div>', unsafe_allow_html=True)
    with p3:
        st.markdown('<div class="product-card"><span>🧼</span><h4>Limpiadores</h4><p>Kit especial para cuero y gamuza.</p><span class="price-tag">$8.00</span></div>', unsafe_allow_html=True)

elif opcion == "📍 Ubicación y Contacto":
    st.header("Dónde Encontrarnos")
    col_info, col_mapa = st.columns([1, 1.5])
    
    with col_info:
        st.success("📍 **Dirección:** Lauro Guerrero y José A. Eguiguren, Loja.")
        st.write("📞 **WhatsApp:** 099 471 8745")
        st.write("⏰ **Horario:** Lun-Vie 08:00 - 19:00 / Sáb 08:00 - 15:30")
        
    with col_mapa:
        mapa_html = f"""
        <iframe 
            src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2319.6535553983294!2d-79.20821527422483!3d-3.9967444553015996!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x91cb491f5912b73b%3A0xa1e733db367e07a6!2sThe%20Warrior%20Brothers!5e1!3m2!1ses!2sec!4v1776383384965!5m2!1ses!2sec" 
            width="100%" height="400" style="border:0; border-radius:15px;" 
            allowfullscreen="" loading="lazy">
        </iframe>
        """
        components.html(mapa_html, height=420)

# --- 5. FOOTER ---
st.markdown("---")
st.markdown("<center>© 2026 The Warrior Brothers | Loja, Ecuador 🛡️⚒️</center>", unsafe_allow_html=True)
