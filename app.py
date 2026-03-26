import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse
import pytz
import sqlite3

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="THE WARRIOR BROTHERS PRO", page_icon="👞", layout="wide")
zona_ec = pytz.timezone('America/Guayaquil')

def init_db():
    conn = sqlite3.connect('warrior_pro.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS recibos 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                  fecha TEXT, cliente TEXT, celular TEXT,
                  articulo TEXT, reparacion TEXT, total REAL, 
                  abono REAL, saldo REAL, entrega TEXT)''')
    conn.commit()
    conn.close()

init_db()

# --- 2. SEGURIDAD ---
if "autenticado" not in st.session_state:
    st.session_state["autenticado"] = False

if not st.session_state["autenticado"]:
    st.title("🔐 Acceso Privado")
    password = st.text_input("Contraseña:", type="password")
    if st.button("Entrar"):
        if password == "WARRIOR2026":
            st.session_state["autenticado"] = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta.")
    st.stop()

# --- 3. DISEÑO ---
st.markdown("<h1 style='text-align: center;'>🛡️ THE WARRIOR BROTHERS</h1>", unsafe_allow_html=True)

tab_registro, tab_historial = st.tabs(["📝 REGISTRAR TRABAJO", "📊 CAJA Y CONTROL"])

# --- PESTAÑA 1: REGISTRO ---
with tab_registro:
    with st.form("form_registro", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            nombre = st.text_input("👤 Cliente:")
            celular = st.text_input("📱 WhatsApp:")
            articulo = st.text_input("💼 Artículo:")
        with col2:
            reparacion = st.text_input("🛠️ Reparación:")
            total = st.number_input("💰 Total ($):", min_value=0.0, format="%.2f")
            abono = st.number_input("💵 Abono ($):", min_value=0.0, format="%.2f")
            fecha_entrega = st.date_input("📅 Fecha de entrega:")
            
        submit = st.form_submit_button("💾 GUARDAR Y GENERAR")

    if submit:
        if nombre and celular:
            saldo = total - abono
            f_registro = datetime.now(zona_ec).strftime("%d/%m/%Y %H:%M")
            f_entrega = fecha_entrega.strftime("%d/%m/%Y")
            
            conn = sqlite3.connect('warrior_pro.db')
            c = conn.cursor()
            c.execute("""INSERT INTO recibos (fecha, cliente, celular, articulo, reparacion, total, abono, saldo, entrega) 
                         VALUES (?,?,?,?,?,?,?,?,?)""", 
                      (f_registro, nombre.upper(), celular, articulo, reparacion, total, abono, saldo, f_entrega))
            conn.commit()
            conn.close()
            st.success(f"✅ ¡Trabajo de {nombre.upper()} registrado!")
            st.rerun() # Para actualizar la tabla de la otra pestaña de inmediato

# --- PESTAÑA 2: HISTORIAL Y BORRADO POR FILA ---
with tab_historial:
    conn = sqlite3.connect('warrior_pro.db')
    df = pd.read_sql_query("SELECT * FROM recibos ORDER BY id DESC", conn)
    conn.close()

    if not df.empty:
        # Métricas
        m1, m2, m3 = st.columns(3)
        m1.metric("Ingreso Total", f"${df['total'].sum():.2f}")
        m2.metric("Caja (Abonos)", f"${df['abono'].sum():.2f}")
        m3.metric("Por Cobrar", f"${df['saldo'].sum():.2f}")
        
        st.divider()
        st.subheader("🗂️ Registro de Trabajos")
        # Mostramos la tabla. El ID es la primera columna.
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        # --- SECCIÓN PARA BORRAR FILA ESPECÍFICA ---
        st.sidebar.title("🗑️ Eliminar Registro")
        id_a_borrar = st.sidebar.number_input("ID de la fila a borrar:", min_value=1, step=1)
        
        if st.sidebar.button("Eliminar Fila # " + str(id_a_borrar)):
            conn = sqlite3.connect('warrior_pro.db')
            c = conn.cursor()
            # Verificamos si existe el ID
            c.execute("SELECT cliente FROM recibos WHERE id=?", (id_a_borrar,))
            resultado = c.fetchone()
            
            if resultado:
                c.execute("DELETE FROM recibos WHERE id=?", (id_a_borrar,))
                conn.commit()
                st.sidebar.success(f"Fila {id_a_borrar} (Cliente: {resultado[0]}) eliminada.")
                conn.close()
                st.rerun()
            else:
                st.sidebar.error("Ese ID no existe.")
                conn.close()
    else:
        st.info("No hay registros todavía.")
