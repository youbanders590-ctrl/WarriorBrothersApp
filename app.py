import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse
import pytz
from streamlit_gsheets import GSheetsConnection

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
        # Cambio aquí: Ahora es más general para maletas, mochilas, etc.
        articulo = st.text_input("💼 Tipo de Artículo (Zapato, Maleta, Chompa):")
    with col2:
        reparacion = st.text_input("🛠️ Reparación a realizar:")
        total = st.number_input("💰 Total ($):", min_value=0.0)
        abono = st.number_input("💵 Abono ($):", min_value=0.0)
        dias = st.number_input("📅 Días para entrega:", min_value=1, value=3)
    
    submit = st.form_submit_button("💾 GUARDAR Y GENERAR RECIBO")

if submit:
    if nombre and celular:
        saldo = total - abono
        ahora = datetime.now(zona_ec)
        f_h = ahora.strftime("%d/%m/%Y %H:%M")
        f_e = (ahora + timedelta(days=dias)).strftime("%d/%m/%Y")

# --- 3. GUARDADO EN GOOGLE SHEETS (LIMPIO) ---
        try:
            conn = st.connection("gsheets", type=GSheetsConnection)
            
            # 1. Leer datos actuales
            df_actual = conn.read(worksheet="Hoja 1", ttl=0)
            
            # 2. Crear la nueva fila
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
            
            # 3. Unir los datos
            df_final = pd.concat([df_actual, nueva_fila], ignore_index=True)
            
            # 4. Enviar al Excel (Sin asignar a ninguna variable)
            conn.update(worksheet="Hoja 1", data=df_final)
            
            st.success("✅ ¡Registro guardado exitosamente!")
            
        except Exception as e:
            st.error(f"Error al guardar: {e}")
        
        # --- 4. WHATSAPP ACTUALIZADO (PARA TODO TIPO DE ARTÍCULOS) ---
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
            "⚠️ *NOTA IMPORTANTE:*\n"
            "- Una vez ingresada la obra, no se realizarán devoluciones de abonos ni entregas antes de la fecha acordada.\n"
            "- Los trabajos no retirados pasados los 2 meses serán liquidados para cubrir costos de material.\n\n"
            "¡Gracias por su confianza! ✨"
        )
        
        texto_url = urllib.parse.quote(msg_wa)
        link_wa = f"https://api.whatsapp.com/send?phone=593{celular.lstrip('0')}&text={texto_url}"
        
        st.markdown(f"""
            <a href="{link_wa}" target="_blank" style="text-decoration:none;">
                <div style="background-color:#25D366; color:white; padding:15px; border-radius:10px; text-align:center; font-weight:bold; font-size:18px;">
                    📲 ENVIAR RECIBO POR WHATSAPP
                </div>
            </a>
        """, unsafe_allow_html=True)
    else:
        st.error("⚠️ Por favor completa el nombre y el celular.")
