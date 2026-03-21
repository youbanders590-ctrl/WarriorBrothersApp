import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse
import pytz
from streamlit_gsheets import GSheetsConnection

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Warrior Brothers Admin", page_icon="🛡️")
zona_ec = pytz.timezone('America/Guayaquil')

# --- SISTEMA DE SEGURIDAD ---
if "password_correct" not in st.session_state:
    st.session_state["password_correct"] = False

if not st.session_state["password_correct"]:
    st.title("🔐 Acceso Restringido")
    password = st.text_input("Contraseña:", type="password")
    if st.button("Entrar"):
        if password == "WARRIOR2026":
            st.session_state["password_correct"] = True
            st.rerun()
        else:
            st.error("❌ Clave incorrecta")
    st.stop()

# --- APP PRINCIPAL ---
st.title("🛡️ Los Hermanos Guerreros")

with st.form("formulario_calzado", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("👤 Nombre del Cliente:")
        celular = st.text_input("📱 Celular (WhatsApp):")
        zapato = st.text_input("👞 Tipo de Calzado:")
    with col2:
        reparacion = st.text_input("🛠️ Reparación:")
        total = st.number_input("💰 Total ($)", min_value=0.0)
        abono = st.number_input("💵 Abono ($)", min_value=0.0)
        dias = st.number_input("📅 Días entrega:", min_value=1, value=3)
    submit = st.form_submit_button("💾 REGISTRAR Y GUARDAR")

if submit:
    if nombre and celular:
        saldo = total - abono
        ahora = datetime.now(zona_ec)
        f_h = ahora.strftime("%d/%m/%Y %H:%M")
        f_e = (ahora + timedelta(days=dias)).strftime("%d/%m/%Y")
        
        # --- GUARDAR EN GOOGLE SHEETS (MÉTODO ROBUSTO) ---
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            # 1. Forzamos la lectura para asegurar que la conexión está viva
            df_existente = conn.read(worksheet="Hoja 1", ttl=0)
            
            # 2. Creamos la nueva fila con los nombres EXACTOS de tus columnas de Excel
            nueva_fila = pd.DataFrame([{
                "Fecha": f_h,
                "Cliente": nombre.upper(),
                "Celular": celular,
                "Calzado": zapato,
                "Reparacion": reparacion,
                "Total": f"{total:.2f}",
                "Abono": f"{abono:.2f}",
                "Saldo": f"{saldo:.2f}",
                "Entrega": f_e
            }])
            
            # 3. Concatenamos y actualizamos
            df_final = pd.concat([df_existente, nueva_fila], ignore_index=True)
            conn.update(worksheet="Hoja 1", data=df_final)
            st.success("✅ ¡Datos guardados en el Excel con éxito!")
        except Exception as e:
            st.error(f"Error al guardar: {e}")

        # --- MENSAJE DE WHATSAPP (CON CODIFICACIÓN SEGURA) ---
        # Definimos los emojis como variables para que no se rompan
        e_escudo = "🛡️"
        e_hola = "👋"
        e_zapato = "👞"
        e_herram = "🛠️"
        e_dinero = "💰"
        e_abono = "💵"
        e_tarjeta = "💳"
        e_calend = "📅"
        e_chispa = "✨"

        msg_wa = (
            f"*{e_escudo} THE WARRIOR BROTHERS*\n"
            f"------------------------------------------\n"
            f"¡Hola *{nombre.upper()}*! {e_hola}\n"
            f"Confirmamos la recepción de su calzado:\n\n"
            f"{e_zapato} *Calzado:* {zapato}\n"
            f"{e_herram} *Trabajo:* {reparacion}\n"
            f"------------------------------------------\n"
            f"{e_dinero} *Total:* ${total:.2f}\n"
            f"{e_abono} *Abono:* ${abono:.2f}\n"
            f"{e_tarjeta} *Saldo pendiente:* *${saldo:.2f}*\n"
            f"------------------------------------------\n"
            f"{e_calend} *Fecha de entrega:* {f_e}\n\n"
            f"¡Gracias por su confianza! {e_chispa}"
        )
        
        # ESTA ES LA CLAVE: urllib.parse.quote_plus maneja mejor los espacios y emojis
        texto_final = urllib.parse.quote(msg_wa)
        link_wa = f"https://wa.me/593{celular.lstrip('0')}?text={texto_final}"
        
        st.markdown(f'''
            <a href="{link_wa}" target="_blank" style="
                background-color: #25D366; color: white; padding: 18px; 
                text-align: center; display: block; border-radius: 12px; 
                font-weight: bold; text-decoration: none; margin-top: 20px;">
                📲 ENVIAR COMPROBANTE POR WHATSAPP
            </a>
            ''', unsafe_allow_html=True)
    else:
        st.error("❌ Llena los campos obligatorios.")
