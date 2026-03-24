import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse
import pytz
from streamlit_gsheets import GSheetsConnection  # Asegúrate de que esta línea esté presente

# --- CONFIGURACIÓN ---
st.set_page_config(page_title="Warrior Brothers Admin", page_icon="🛡️")
zona_ec = pytz.timezone('America/Guayaquil')

# --- 1. SEGURIDAD ---
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    st.title("🔐 Acceso Privado")
    password = st.text_input("Ingresa la contraseña:", type="password")
    if st.button("Entrar"):
        if password == "WARRIOR2026":
            st.session_state["autenticado"] = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta.")
    st.stop()

# --- 2. APLICACIÓN PRINCIPAL ---
st.title("🛡️ Los Hermanos Guerreros")
st.subheader("Especialistas en Cuero y Calzado")

with st.form("form_warrior", clear_on_submit=True):
    col1, col2 = st.columns(2)
    with col1:
        nombre = st.text_input("👤 Cliente:")
        celular = st.text_input("📱 WhatsApp (ej: 09...):")
        articulo = st.text_input("💼 Tipo de Artículo (Zapato, Maleta, Chompa):")
    with col2:
        reparacion = st.text_input("🛠️ Reparación a realizar:")
        total = st.number_input("💰 Total ($):", min_value=0.0)
        abono = st.number_input("💵 Abono ($):", min_value=0.0)
        dias = st.number_input("📅 Días para entrega:", min_value=1, value=3)
    
    submit = st.form_submit_button("💾 GUARDAR Y GENERAR RECIBO")

if submit:
    if nombre and celular:
        # --- CÁLCULOS ---
        saldo = total - abono
        ahora = datetime.now(zona_ec)
        f_h = ahora.strftime("%d/%m/%Y %H:%M")
        f_e = (ahora + timedelta(days=dias)).strftime("%d/%m/%Y")

        nueva_fila = pd.DataFrame([{
            "Fecha": f_h,
            "Cliente": nombre.upper(),
            "Celular": celular,
            "Articulo": articulo,
            "Reparacion": reparacion,
            "Total": f"{total:.2f}",
            "Abono": f"{abono:.2f}",
            "Saldo": f"{saldo:.2f}",
            "Entrega": f_e
        }])

        # --- CONEXIÓN ---
        try:
            # CAMBIO CLAVE: Se agrega el tipo de conexión explícito
            conn = st.connection("gsheets", type=GSheetsConnection)

            try:
                df_actual = conn.read(worksheet="Data", ttl=0)
                # Limpiar columnas vacías "Unnamed" que a veces crea Google Sheets
                df_actual = df_actual.loc[:, ~df_actual.columns.str.contains('^Unnamed')]
            except Exception:
                df_actual = pd.DataFrame()

            df_final = pd.concat([df_actual, nueva_fila], ignore_index=True)
            
            # Guardar en la hoja "Data"
            conn.update(worksheet="Data", data=df_final)

            st.success("✅ ¡Registro guardado exitosamente en Google Sheets!")

            # --- WHATSAPP ---
            msg_wa = (
                "🛡️ *THE WARRIOR BROTHERS*\n"
                "------------------------------------------\n"
                f"¡Hola *{nombre.upper()}*! ✅\n"
                "Confirmamos la recepción de su artículo:\n\n"
                f"💼 *Artículo:* {articulo}\n"
                f"🛠️ *Trabajo:* {reparacion}\n"
                "------------------------------------------\n"
                f"💰 *Total:* ${total:.2f}\n"
                f"💵 *Abono:* ${abono:.2f}\n"
                f"💳 *Saldo pendiente:* *${saldo:.2f}*\n"
                "------------------------------------------\n"
                f"📅 *Entrega estimada:* {f_e}\n\n"
                "¡Gracias por su confianza! ✨"
            )

            texto_url = urllib.parse.quote(msg_wa)
            link_wa = f"https://api.whatsapp.com/send?phone=593{celular.lstrip('0')}&text={texto_url}"

            st.markdown(f"""
                <a href="{link_wa}" target="_blank" style="text-decoration:none;">
                    <div style="background-color:#25D366; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold; font-size:18px; margin-top:20px;">
                        📲 ENVIAR RECIBO POR WHATSAPP
                    </div>
                </a>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❌ Error al guardar: {e}")
            st.info("Asegúrate de que la versión de Python en Streamlit sea 3.11 y los Secrets estén bien pegados.")

    else:
        st.error("⚠️ Por favor completa el nombre y el celular.")


