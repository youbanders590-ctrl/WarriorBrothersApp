import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import urllib.parse
import pytz

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="The Warrior Brothers - Registro", page_icon="💪")
zona_ec = pytz.timezone('America/Guayaquil')

# --- CONFIGURACIÓN DE GOOGLE SHEETS ---
# 1. VE A TU HOJA DE GOOGLE
# 2. CLICK EN 'COMPARTIR' -> CAMBIAR A 'CUALQUIER PERSONA CON EL ENLACE' -> CAMBIAR A 'EDITOR'
# 3. COPIA EL ID DE LA HOJA (está en la URL, entre /d/ y /edit)
# 4. REEMPLAZA AQUÍ ABAJO:
SHEET_ID = "10Te_l9X_7wb4qmQDhjqBzalil5DF1Gs06OZKjAviALY" 
SHEET_NAME = "Hoja1" # El nombre de la pestaña abajo en el Excel
from streamlit_gsheets import GSheetsConnection

def guardar_en_sheets(datos_dict):
    try:
        # Conexión simplificada usando los Secretos de Streamlit
        conn = st.connection("gsheets", type=GSheetsConnection)
        
        # Lee los datos que ya están en el Excel
        df_existente = conn.read()
        
        # Prepara la nueva fila
        nueva_fila = pd.DataFrame([datos_dict])
        
        # Une los datos y actualiza la hoja
        df_final = pd.concat([df_existente, nueva_fila], ignore_index=True)
        conn.update(data=df_final)
        return True
    except Exception as e:
        st.error(f"Error real de conexión: {e}")
        return False


# --- INTERFAZ DE LA APP ---
st.title("🛡️ Sistema The Warrior Brothers")
st.markdown("---")

with st.form("formulario_cliente", clear_on_submit=True):
    st.subheader("Nuevo Registro de Trabajo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        nombre = st.text_input("Nombre del Cliente:")
        celular = st.text_input("Número de Celular (ej: 099...)")
        articulo = st.text_input("Artículo (ej: Zapatos, Bolso)")
        
    with col2:
        trabajo = st.text_input("Reparación a realizar")
        precio_total = st.number_input("Precio Total ($)", min_value=0.0, format="%.2f")
        abono = st.number_input("Abono Inicial ($)", min_value=0.0, format="%.2f")
        dias_entrega = st.number_input("¿En cuántos días se entrega?", min_value=1, value=2)

    submit_button = st.form_submit_button(label="📄 Generar Recibo y Guardar")

# --- LÓGICA AL ENVIAR ---
if submit_button:
    if not nombre or not celular or not articulo:
        st.warning("⚠️ Por favor llena los campos básicos (Nombre, Celular, Artículo).")
    else:
        # CÁLCULOS
        saldo = precio_total - abono
        ahora_ec = datetime.now(zona_ec)
        
        # Saludo
        hora = ahora_ec.hour
        if 5 <= hora < 12: saludo = "Buenos días"
        elif 12 <= hora < 19: saludo = "Buenas tardes"
        else: saludo = "Buenas noches"
        
        # Fecha entrega
        fecha_entrega_dt = ahora_ec + timedelta(days=dias_entrega)
        fecha_entrega_str = fecha_entrega_dt.strftime("%d/%m/%Y")
        
        # Datos para guardar
        datos_cliente = {
            "Fecha": ahora_ec.strftime("%Y-%m-%d %H:%M"),
            "Cliente": nombre.upper(),
            "Celular": celular,
            "Artículo": articulo,
            "Trabajo": trabajo,
            "Total": precio_total,
            "Abono": abono,
            "Saldo": saldo,
            "Fecha_Entrega": fecha_entrega_str
        }
        
        # 1. Guardar en Google Sheets
        with st.spinner("Guardando en base de datos..."):
            # Para esta demostración rápida, si no configuraste secretos, guardará localmente.
            # En producción, usarás: exito = guardar_en_sheets(datos_cliente)
            # st.connection requiere pasos extras de configuración en el dashboard de Streamlit.
            
            # SIMULACIÓN DE GUARDADO (Para que pruebes la interfaz ahora)
            exito = guardar_en_sheets(datos_cliente)
           

        if exito:
            # 2. Generar Mensaje WhatsApp
            num_limpio = celular.lstrip('0').replace(" ", "").replace("-", "")
            num_final = f"593{num_limpio}"
            
            mensaje = (
                f"{saludo} *{nombre}*, le saludamos de *THE WARRIOR BROTHERS* 🛡️.\n\n"
                f"Confirmamos la recepción de su *{articulo}* para: *{trabajo}*.\n"
                f"💰 *Total:* ${precio_total:.2f}\n"
                f"💵 *Abono:* ${abono:.2f}\n"
                f"💳 *Saldo pendiente:* ${saldo:.2f}\n"
                f"🗓️ *Fecha estimada de entrega:* {fecha_entrega_str}\n\n"
                f"¡Gracias por su confianza!"
            )
            
            msg_encoded = urllib.parse.quote(mensaje)
            link_wa = f"https://wa.me/{num_final}?text={msg_encoded}"
            
            # 3. Mostrar Recibo y Botón
            st.markdown("---")
            st.subheader(f"Recibo para {nombre.upper()}")
            
            st.code(mensaje, language=None)
            
            # Botón de WhatsApp
            st.markdown(f'''
                <a href="{link_wa}" target="_blank">
                    <button style="background-color: #25D366; color: white; padding: 15px 25px;
                    border: none; border-radius: 10px; font-weight: bold; cursor: pointer;
                    width: 100%; font-size: 16px;">
                        📲 ENVIAR A WHATSAPP
                    </button>
                </a>
            ''', unsafe_allow_html=True)
