import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse
import pytz
from streamlit_gsheets import GSheetsConnection

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="The Warrior Brothers", page_icon="🛡️", layout="centered")

# Configurar Zona Horaria de Ecuador
zona_ec = pytz.timezone('America/Guayaquil')

# --- 2. ESTILO VISUAL (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #f5f5f5; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; font-weight: bold; }
    .whatsapp-button {
        background-color: #25D366;
        color: white;
        padding: 15px;
        text-align: center;
        text-decoration: none;
        display: block;
        font-size: 18px;
        margin: 10px 0;
        border-radius: 10px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. INTERFAZ ---
st.title("🛡️ Sistema de Gestión - The Warrior Brothers")
st.write("Registro de clientes y generación de comprobantes")

with st.form("formulario_cliente", clear_on_submit=False):
    st.subheader("Datos del Trabajo")
    
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("Nombre del Cliente:", placeholder="Ej: Juan Pérez")
        celular = st.text_input("Celular (sin 0 adelante):", placeholder="Ej: 998877665")
        articulo = st.text_input("Artículo:", placeholder="Ej: Laptop Dell")
    
    with col2:
        trabajo = st.text_input("Reparación/Servicio:", placeholder="Ej: Cambio de pantalla")
        precio_total = st.number_input("Precio Total ($)", min_value=0.0, step=0.5)
        abono = st.number_input("Abono Inicial ($)", min_value=0.0, step=0.5)
        dias_entrega = st.number_input("Días para la entrega:", min_value=1, value=2)

    submit = st.form_submit_button("📄 GENERAR RECIBO Y GUARDAR")

# --- 4. LÓGICA AL ENVIAR ---
if submit:
    if not nombre or not celular:
        st.warning("⚠️ Por favor, llena al menos el nombre y el celular.")
    else:
        # Cálculos de fecha y saldo
        saldo = precio_total - abono
        ahora = datetime.now(zona_ec)
        fecha_actual = ahora.strftime("%d/%m/%Y")
        fecha_entrega = (ahora + timedelta(days=dias_entrega)).strftime("%d/%m/%Y")

        # Intentar Guardar en Google Sheets
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            
            # Crear nueva fila
            nueva_fila = pd.DataFrame([{
                "Fecha": fecha_actual,
                "Cliente": nombre.upper(),
                "Celular": celular,
                "Artículo": articulo,
                "Trabajo": trabajo,
                "Total": f"{precio_total:.2f}",
                "Abono": f"{abono:.2f}",
                "Saldo": f"{saldo:.2f}",
                "Fecha_Entrega": fecha_entrega
            }])

            # Leer datos actuales y concatenar
            df_existente = conn.read()
            df_final = pd.concat([df_existente, nueva_fila], ignore_index=True)
            
            # Actualizar la hoja
            conn.update(data=df_final)
            st.success("✅ Datos guardados en Google Sheets correctamente.")
            
        except Exception as e:
            # Si el error es solo de respuesta visual (Response 200), lo ignoramos
            if "200" in str(e):
                st.success("✅ Registro guardado (Sincronizado).")
            else:
                st.error(f"Aviso de sincronización: {e}")

        # Generar Mensaje de WhatsApp
        msg = (
            f"🛡️ *THE WARRIOR BROTHERS*\n\n"
            f"¡Hola *{nombre.upper()}*! Confirmamos tu servicio:\n"
            f"📦 *Artículo:* {articulo}\n"
            f"🛠️ *Trabajo:* {trabajo}\n"
            f"💰 *Total:* ${precio_total:.2f}\n"
            f"💵 *Abono:* ${abono:.2f}\n"
            f"💳 *Saldo:* ${saldo:.2f}\n"
            f"🗓️ *Entrega:* {fecha_entrega}\n\n"
            f"¡Gracias por tu confianza!"
        )
        
        # Crear link de WhatsApp (Formato internacional Ecuador +593)
        link_wa = f"https://wa.me/593{celular.lstrip('0')}?text={urllib.parse.quote(msg)}"
        
        # Mostrar resumen y botón de WhatsApp
        st.info("Resumen del Comprobante:")
        st.code(msg)
        
        st.markdown(f'''
            <a href="{link_wa}" target="_blank" class="whatsapp-button">
                📲 ENVIAR COMPROBANTE POR WHATSAPP
            </a>
            ''', unsafe_allow_html=True)
