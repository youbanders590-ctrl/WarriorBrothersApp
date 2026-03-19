import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse
import pytz
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="The Warrior Brothers", page_icon="👞")
zona_ec = pytz.timezone('America/Guayaquil')

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3.5em; font-weight: bold; background-color: #1E1E1E; color: white; }
    .whatsapp-button {
        background-color: #25D366; color: white; padding: 18px; text-align: center;
        text-decoration: none; display: block; font-size: 18px; border-radius: 12px; font-weight: bold; margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🛡️ The Warrior Brothers")
st.subheader("Maestros en Reparación de Calzado")

# --- FORMULARIO ---
with st.form("formulario_calzado", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("👤 Nombre del Cliente:")
        celular = st.text_input("📱 Celular (WhatsApp):")
        zapato = st.text_input("👞 Tipo de Calzado:")
    with col2:
        reparacion = st.text_input("🛠️ ¿Qué reparación se hará?:")
        total = st.number_input("💰 Precio Total ($)", min_value=0.0)
        abono = st.number_input("💵 Abono Inicial ($)", min_value=0.0)
        dias = st.number_input("📅 Días para entrega:", min_value=1, value=3)
    submit = st.form_submit_button("💾 REGISTRAR Y GUARDAR")

if submit:
    if nombre and celular:
        saldo = total - abono
        ahora = datetime.now(zona_ec)
        fecha_h = ahora.strftime("%d/%m/%Y %H:%M")
        fecha_e = (ahora + timedelta(days=dias)).strftime("%d/%m/%Y")
        
        # 1. Guardar en Google Sheets
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            df_existente = conn.read(worksheet="Hoja 1")
            datos = {
                "Fecha": fecha_h, "Cliente": nombre.upper(), "Celular": celular,
                "Calzado": zapato, "Reparacion": reparacion, "Total": f"{total:.2f}",
                "Abono": f"{abono:.2f}", "Saldo": f"{saldo:.2f}", "Entrega": fecha_e
            }
            df_nuevo = pd.concat([df_existente, pd.DataFrame([datos])], ignore_index=True)
            conn.update(worksheet="Hoja 1", data=df_nuevo)
            st.success("✅ ¡Registrado en el Excel!")
        except Exception as e:
            st.info("Sincronizando...")

        # 2. Mensaje de WhatsApp (Diseño Bonito)
        # Usamos códigos que WhatsApp entiende mejor para evitar los "?"
        msg_wa = (
            f"*🛡️ THE WARRIOR BROTHERS*\n"
            f"------------------------------------------\n"
            f"¡Hola *{nombre.upper()}*! 👋\n"
            f"Confirmamos la recepción de su calzado:\n\n"
            f"👞 *Calzado:* {zapato}\n"
            f"🛠️ *Trabajo:* {reparacion}\n"
            f"------------------------------------------\n"
            f"💰 *Total:* ${total:.2f}\n"
            f"💵 *Abono:* ${abono:.2f}\n"
            f"💳 *Saldo pendiente:* *${saldo:.2f}*\n"
            f"------------------------------------------\n"
            f"📅 *Fecha de entrega:* {fecha_e}\n\n"
            f"¡Gracias por su confianza! ✨"
        )
        
        # Codificar mensaje para URL
        texto_final = urllib.parse.quote(msg_wa)
        link_wa = f"https://wa.me/593{celular.lstrip('0')}?text={texto_final}"
        
        st.markdown(f'<a href="{link_wa}" target="_blank" class="whatsapp-button">📲 ENVIAR COMPROBANTE POR WHATSAPP</a>', unsafe_allow_html=True)
    else:
        st.error("❌ Por favor completa nombre y celular.")
