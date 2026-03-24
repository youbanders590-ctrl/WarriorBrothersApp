import streamlit as st
from datetime import time

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="🛡️ The Warrior Brothers | Maestros en Reparación de Calzado",
    page_icon="👞",
    layout="wide",
)

# --- ESTILOS CSS PERSONALIZADOS (Estilo Kinetshop) ---
st.markdown("""
    <style>
    /* Fondo y texto general */
    .stApp { background-color: #fcfdfa; color: #1e1e1e; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    
    /* Títulos Principales */
    h1, h2, h3 { font-weight: 700; color: #1e1e1e; letter-spacing: -1px; }
    h1 { font-size: 3rem; margin-bottom: 1rem; }
    h2 { font-size: 2.2rem; border-bottom: 3px solid #1e1e1e; padding-bottom: 10px; margin-top: 40px; }
    
    /* Botones de WhatsApp Estilo Kinetshop */
    .whatsapp-btn {
        background-color: #25D366; color: white; padding: 15px 30px; text-decoration: none;
        font-size: 1.1rem; border-radius: 50px; font-weight: bold; text-align: center;
        display: inline-block; transition: all 0.3s ease; box-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .whatsapp-btn:hover { background-color: #1ebe57; color: white; transform: translateY(-3px); }

    /* Tarjetas de Servicios/Productos */
    .service-card {
        background-color: white; border-radius: 15px; padding: 25px;
        box-shadow: 0 6px 18px rgba(0,0,0,0.06); transition: transform 0.3s ease, box-shadow 0.3s ease;
        border: 1px solid #eee; text-align: center; height: 100%;
    }
    .service-card:hover { transform: translateY(-5px); box-shadow: 0 10px 25px rgba(0,0,0,0.1); border-color: #ddd; }
    .service-card h4 { margin-top: 15px; font-weight: 600; font-size: 1.3rem; }
    .service-card p { color: #555; font-size: 0.95rem; line-height: 1.5; }
    .service-img { border-radius: 10px; width: 100%; height: 200px; object-fit: cover; }
    </style>
    """, unsafe_allow_html=True)

# --- 1. SECCIÓN HÉROE (Encabezado Potente) ---
st.markdown("""
    <div style="background-color: #1e1e1e; color: white; padding: 80px 40px; text-align: center; border-radius: 15px; margin-bottom: 50px;">
        <h1 style="color: white; margin-bottom: 10px;">🛡️ The Warrior Brothers</h1>
        <p style="font-size: 1.4rem; font-weight: 300;">Maestros Artesanos en Cuero y Calzado</p>
        <p style="font-size: 1.1rem; margin-top: 20px;">Damos nueva vida a tus zapatos favoritos con la calidad de antes.</p>
        <br>
        <a href="#contacto" class="whatsapp-btn">Cotiza tu Reparación Aquí</a>
    </div>
    """, unsafe_allow_html=True)

# --- 2. SECCIÓN DE SERVICIOS (Mosaico) ---
st.header("🛠️ Nuestros Servicios de Especialidad")
st.markdown("Mostramos el arte de la restauración en cada par.")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
        <div class="service-card">
            <img src="https://via.placeholder.com/400x300.png?text=Antes+y+Después" class="service-img">
            <h4>Reparación de Pisos</h4>
            <p>Cambio total o parcial de suelas desgastadas para un agarre perfecto y duradero.</p>
        </div>
        """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="service-card">
            <img src="https://via.placeholder.com/400x300.png?text=Restauración+Color" class="service-img">
            <h4>Tinturado Profundo</h4>
            <p>Revive el color original o cámbialo por completo. Acabado profesional en cuero.</p>
        </div>
        """, unsafe_allow_html=True)

with col3:
    st.markdown("""
        <div class="service-card">
            <img src="https://via.placeholder.com/400x300.png?text=Cambio+Tapas" class="service-img">
            <h4>Cambio de Tapas</h4>
            <p>Reparación precisa de tacos y tapas para damas y caballeros. Rápido y seguro.</p>
        </div>
        """, unsafe_allow_html=True)

with col4:
    st.markdown("""
        <div class="service-card">
            <img src="https://via.placeholder.com/400x300.png?text=Arreglo+Maletas" class="service-img">
            <h4>Maletas y Chompas</h4>
            <p>Arreglamos cierres, asas y costuras en artículos de cuero y lona.</p>
        </div>
        """, unsafe_allow_html=True)

# --- 3. SECCIÓN DE PRODUCTOS WARRIOR ---
st.header("🛍️ Tienda de Cuidado Warrior")
st.markdown("Productos seleccionados para mantener tus zapatos impecables.")

p_col1, p_col2, p_col3 = st.columns(3)

with p_col1:
    st.markdown("""
        <div class="service-card">
            <img src="https://via.placeholder.com/400x300.png?text=Limpia+Warrior" class="service-img">
            <h4>Limpia Warrior</h4>
            <p>Fórmula exclusiva para limpiar profundamente sin dañar el cuero.</p>
            <p style="font-weight: bold; font-size: 1.2rem; color: #1e1e1e; margin-top: 10px;">$X.XX</p>
        </div>
        """, unsafe_allow_html=True)

with p_col2:
    st.markdown("""
        <div class="service-card">
            <img src="https://via.placeholder.com/400x300.png?text=Plantillas+Suaves" class="service-img">
            <h4>Plantillas Confort</h4>
            <p>Plantillas de memory foam para una comodidad superior todo el día.</p>
            <p style="font-weight: bold; font-size: 1.2rem; color: #1e1e1e; margin-top: 10px;">$X.XX</p>
        </div>
        """, unsafe_allow_html=True)

with p_col3:
    st.markdown("""
        <div class="service-card">
            <img src="https://via.placeholder.com/400x300.png?text=Cordones" class="service-img">
            <h4>Cordones Premium</h4>
            <p>Variedad de colores y largos en algodón encerado y nylon.</p>
            <p style="font-weight: bold; font-size: 1.2rem; color: #1e1e1e; margin-top: 10px;">$X.XX</p>
        </div>
        """, unsafe_allow_html=True)

# --- 4. SECCIÓN A DOMICILIO ---
st.markdown("""
    <div style="background-color: #f1f1f1; padding: 50px 30px; border-radius: 15px; margin-top: 50px; text-align: center;">
        <h2>🚀 Servicio a Domicilio Warrior</h2>
        <p style="font-size: 1.2rem; max-width: 700px; margin: 20px auto;">¿No tienes tiempo? Recogemos y entregamos tus zapatos en la puerta de tu casa o trabajo.</p>
        <p style="font-weight: bold; font-size: 2.5rem; color: #25D366; margin-top: 10px;">+$5.00</p>
        <p style="color: #777;">Valor adicional por trayecto completo (recepción y entrega).</p>
        <br>
        <a href="#contacto" class="whatsapp-btn">Solicitar Retiro a Domicilio</a>
    </div>
    """, unsafe_allow_html=True)

# --- 5. SECCIÓN DE CONTACTO Y MAPA (Estilo Tienda) ---
st.header("📍 Visítanos o Contáctanos")
st.markdown("Encuentra nuestra matriz o agenda tu servicio.")

c_col1, c_col2 = st.columns([1, 1.5])

with c_col1:
    st.subheader("Datos de Contacto")
    st.markdown("""
        **Dirección:**<br>
        Calle Principal N12-34 y Av. Secundaria<br>
        Quito, Ecuador
        
        **WhatsApp:**<br>
        [+593 9X XXX XXXX](https://wa.me/5939XXXXXXXX)
        
        **Horarios de Atención:**<br>
        Lunes a Viernes: 8:00 AM - 6:00 PM<br>
        Sábado: 9:00 AM - 1:00 PM<br>
        Domingo: Cerrado
        """, unsafe_allow_html=True)
    
    # Llamado a la Acción Principal
    st.markdown("<br><br>", unsafe_allow_html=True)
    whatsapp_cotizar = "https://wa.me/5939XXXXXXXX?text=Hola%20Warrior%20Brothers,%20quisiera%20cotizar%20una%20reparación..."
    st.markdown(f'<a href="{whatsapp_cotizar}" class="whatsapp-btn" style="width: 100%;">Quiero una Cotización Gratuita</a>', unsafe_allow_html=True)

with c_col2:
    st.subheader("Nuestra Ubicación")
    # Google Maps Embebido (Placeholder)
    # Debes reemplazar este iframe con el código real de 'Compartir > Insertar Mapa' de Google Maps
    maps_iframe = """
        <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3989.7578!2d-78.4727!3d-0.1873!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x91d599!2sThe+Warrior+Brothers!5e0!3m2!1ses!2sec!4v1700000000000!5m2!1ses!2sec" 
        width="100%" height="450" style="border:0; border-radius: 15px;" allowfullscreen="" loading="lazy"></iframe>
        """
    st.markdown(maps_iframe, unsafe_allow_html=True)

# --- PIE DE PÁGINA ---
st.markdown("""
    <div style="text-align: center; color: #777; padding: 30px; border-top: 1px solid #eee; margin-top: 60px;">
        <p>© 2024 The Warrior Brothers. Maestros en Reparación de Calzado. Quito, Ecuador.</p>
        <p style="font-size: 0.8rem;">Desarrollado con ❤️ para artesanos ecuatorianos.</p>
    </div>
    """, unsafe_allow_html=True)
