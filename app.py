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

# --- PESTAÑA 1: REGISTRO ---
with tab_reg:
    with st.form("f_reg", clear_on_submit=True):
        col1, col2 = st.columns(2)
        nombre = col1.text_input("👤 Cliente:")
        celular = col1.text_input("📱 WhatsApp:")
        articulo = col1.text_input("💼 Artículo:")
        reparacion = col2.text_input("🛠️ Reparación:")
        total = col2.number_input("💰 Total $", min_value=0.0)
        abono = col2.number_input("💵 Abono $", min_value=0.0)
        f_ent = col2.date_input("📅 Entrega:")
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
                st.rerun()

# --- PESTAÑA 2: HISTORIAL CON EXCEL ---
with tab_hist:
    conn = sqlite3.connect('warrior_pro.db')
    df = pd.read_sql_query("SELECT * FROM recibos ORDER BY id DESC", conn)
    conn.close()

    if not df.empty:
        # Fila de botones arriba de la tabla
        col_btn1, col_btn2 = st.columns([1, 5])
        
        # Lógica de borrado (la X minimalista)
        df.insert(0, "X", False)
        df_ed = st.data_editor(
            df,
            hide_index=True,
            use_container_width=True,
            column_config={"X": st.column_config.CheckboxColumn("❌", default=False), "id": None},
            disabled=[col for col in df.columns if col != "X"]
        )

        selec = df_ed[df_ed["X"] == True]
        with col_btn1:
            if not selec.empty:
                if st.button("❌", type="primary"):
                    ids = selec["id"].tolist()
                    conn = sqlite3.connect('warrior_pro.db')
                    c = conn.cursor()
                    for i in ids:
                        c.execute("DELETE FROM recibos WHERE id=?", (i,))
                    conn.commit()
                    conn.close()
                    st.rerun()

        # --- BOTÓN PARA EXCEL ---
        st.divider()
        st.subheader("📥 Exportar Datos")
        
        # Preparamos el archivo para descargar (sin la columna de la X)
        df_excel = df.drop(columns=["X"]) 
        csv_data = df_excel.to_csv(index=False, encoding='utf-8-sig').encode('utf-8-sig')
        
        st.download_button(
            label="📊 DESCARGAR REPORTE PARA EXCEL",
            data=csv_data,
            file_name=f"Reporte_Warrior_{datetime.now().strftime('%d_%m_%Y')}.csv",
            mime="text/csv",
            help="Haz clic para bajar todos tus registros y abrirlos en Excel"
        )
    else:
        st.info("Sin registros.")
