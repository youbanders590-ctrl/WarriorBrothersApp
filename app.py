import streamlit as st
import pandas as pd
from datetime import datetime
import urllib.parse
import pytz
import sqlite3

# --- 1. CONFIGURACIÓN ---
st.set_page_config(page_title="WARRIOR PRO", page_icon="👞", layout="wide")
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
    st.stop()

# --- 3. DISEÑO ---
st.markdown("<h1 style='text-align: center;'>🛡️ THE WARRIOR BROTHERS</h1>", unsafe_allow_html=True)

tab_reg, tab_hist = st.tabs(["📝 REGISTRAR", "📊 HISTORIAL"])

# --- REGISTRO ---
with tab_reg:
    with st.form("f_reg", clear_on_submit=True):
        c1, c2 = st.columns(2)
        nombre = c1.text_input("Cliente:")
        celular = c1.text_input("WhatsApp:")
        articulo = c1.text_input("Artículo:")
        reparacion = c2.text_input("Reparación:")
        total = c2.number_input("Total $", min_value=0.0)
        abono = c2.number_input("Abono $", min_value=0.0)
        f_ent = c2.date_input("Entrega:")
        if st.form_submit_button("💾 GUARDAR"):
            if nombre and celular:
                saldo = total - abono
                f_reg_str = datetime.now(zona_ec).strftime("%d/%m/%Y %H:%M")
                conn = sqlite3.connect('warrior_pro.db')
                c = conn.cursor()
                c.execute("INSERT INTO recibos (fecha, cliente, celular, articulo, reparacion, total, abono, saldo, entrega) VALUES (?,?,?,?,?,?,?,?,?)",
                          (f_reg_str, nombre.upper(), celular, articulo, reparacion, total, abono, saldo, f_ent.strftime("%d/%m/%Y")))
                conn.commit()
                conn.close()
                st.success("¡Registrado!")
                st.rerun()

# --- HISTORIAL CON "BOTÓN" DE BORRADO ---
with tab_hist:
    conn = sqlite3.connect('warrior_pro.db')
    df = pd.read_sql_query("SELECT * FROM recibos ORDER BY id DESC", conn)
    conn.close()

    if not df.empty:
        # Añadimos la columna de la "X" al inicio
        df.insert(0, "X", False)

        st.subheader("Selecciona la X y presiona el botón para borrar:")
        
        # Configuración de la tabla para que la X se vea como un botón de acción
        df_editado = st.data_editor(
            df,
            hide_index=True,
            use_container_width=True,
            column_config={
                "X": st.column_config.CheckboxColumn("❌", help="Clic para borrar fila", default=False),
                "id": None # Escondemos el ID para que se vea más limpio
            },
            disabled=[col for col in df.columns if col != "X"]
        )

        # Si hay filas marcadas con X, mostramos el botón de confirmación
        filas_borrar = df_editado[df_editado["X"] == True]
        if not filas_borrar.empty:
            if st.button(f"🗑️ BORRAR {len(filas_borrar)} FILA(S)", type="primary"):
                ids_borrar = filas_borrar["id"].tolist()
                conn = sqlite3.connect('warrior_pro.db')
                c = conn.cursor()
                for i in ids_borrar:
                    c.execute("DELETE FROM recibos WHERE id=?", (i,))
                conn.commit()
                conn.close()
                st.rerun()
    else:
        st.info("No hay registros.")
