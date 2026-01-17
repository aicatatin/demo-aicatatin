import streamlit as st
import time
import pandas as pd
import plotly.express as px

# 1. Konfigurasi Halaman & UI/UX Styling
st.set_page_config(page_title="aicatatin", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    /* Global Styling */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
    
    /* Background & Container */
    .stApp { background-color: #f8f9fa; }
    
    /* Splash Animation */
    @keyframes pulse { 0% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.1); opacity: 0.7; } 100% { transform: scale(1); opacity: 1; } }
    .splash-box { display: flex; flex-direction: column; align-items: center; justify-content: center; height: 70vh; }
    .splash-logo { width: 120px; animation: pulse 2s infinite; margin-bottom: 20px; }
    
    /* Card Styling */
    .custom-card {
        background: white;
        padding: 25px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    
    /* WA Style Chat List */
    .chat-item {
        background: white;
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        transition: 0.3s;
        cursor: pointer;
        border: 1px solid #f0f0f0;
    }
    .chat-item:hover { background-color: #f0fdf4; border-color: #25D366; }
    .avatar {
        width: 50px; height: 50px;
        background: linear-gradient(135deg, #25D366, #128C7E);
        border-radius: 50%;
        display: flex; align-items: center; justify-content: center;
        color: white; font-weight: bold; margin-right: 15px;
    }
    
    /* Modern Buttons */
    .stButton>button {
        border-radius: 12px;
        border: none;
        background: linear-gradient(135deg, #25D366, #128C7E);
        color: white;
        padding: 10px 24px;
        font-weight: 600;
        transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(37, 211, 102, 0.4); }
    </style>
    """, unsafe_allow_html=True)

# 2. Logika Navigasi
if 'page' not in st.session_state:
    st.session_state.page = 'splash'

# --- ROUTING HALAMAN ---

# A. SPLASH SCREEN
if st.session_state.page == 'splash':
    st.markdown("""
        <div class="splash-box">
            <img src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png" class="splash-logo">
            <h1 style='color: #128C7E; font-weight: 600;'>aicatatin</h1>
            <p style='color: #666;'>Tinggal Jepret, Laporan Beres.</p>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(2.5)
    st.session_state.page = 'login'
    st.rerun()

# B. HALAMAN LOGIN
elif st.session_state.page == 'login':
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #333;'>Selamat Datang Kembali</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888;'>Masuk untuk mengelola keuanganmu</p>", unsafe_allow_html=True)
    
    st.text_input("Email atau Nomor WA")
    st.text_input("Password", type="password")
    
    if st.button("Masuk Sekarang"):
        st.session_state.page = 'chat_list'
        st.rerun()
    
    st.markdown("<hr style='margin: 25px 0;'>", unsafe_allow_html=True)
    st.write("Belum punya akun?")
    if st.button("Daftar Akun Baru"):
        st.session_state.page = 'register'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# C. HALAMAN DAFTAR
elif st.session_state.page == 'register':
    st.markdown("<div class='custom-card'>", unsafe_allow_html=True)
    st.markdown("## Buat Akun aicatatin")
    st.text_input("Nama Lengkap")
    st.text_input("Nomor WhatsApp")
    st.selectbox("Tipe Pengguna", ["Personal", "UMKM Produktif", "UMKM Retail"])
    st.text_input("Password", type="password")
    
    if st.button("Daftar"):
        st.success("Pendaftaran Berhasil!")
        time.sleep(1.5)
        st.session_state.page = 'login'
        st.rerun()
    
    if st.button("⬅️ Kembali ke Login"):
        st.session_state.page = 'login'
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

# D. HALAMAN DAFTAR CHAT (WA STYLE)
elif st.session_state.page == 'chat_list':
    st.markdown("<h2 style='color: #128C7E;'>Pesan</h2>", unsafe_allow_html=True)
    
    chat_data = [
        {"icon": "🤖", "name": "Chatty AI", "msg": "Ada selisih Rp 15.000 di mutasi bank...", "time": "10:30"},
        {"icon": "🛍️", "name": "Supplier Kain", "msg": "Stok kain katun sudah dikirim ya.", "time": "09:15"},
        {"icon": "📉", "name": "Info Keuangan", "msg": "Laporan mingguanmu sudah terbit.", "time": "Yesterday"}
    ]
    
    for chat in chat_data:
        col1, col2 = st.columns([1, 5])
        with col1:
            st.markdown(f"<div class='avatar'>{chat['icon']}</div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"**{chat['name']}** <span style='float:right; color:#888; font-size:12px;'>{chat['time']}</span>", unsafe_allow_html=True)
            st.markdown(f"<span style='color:#666; font-size:14px;'>{chat['msg']}</span>", unsafe_allow_html=True)
        st.markdown("<hr style='margin: 10px 0; border: 0.5px solid #eee;'>", unsafe_allow_html=True)

    st.write("")
    if st.button("Buka Chatty Assistant 🤖"):
        st.session_state.page = 'main_app'
        st.rerun()

# E. HALAMAN UTAMA (THE AI DASHBOARD)
elif st.session_state.page == 'main_app':
    # Header Mini
    col_a, col_b = st.columns([4, 1])
    with col_a: st.markdown("### 🤖 Chatty Assistant")
    with col_b: 
        if st.button("🚪"): 
            st.session_state.page = 'chat_list'
            st.rerun()

    # Chat Interaction
    st.info("👋 **Halo Juragan!** Aku nemu mutasi masuk Rp 500.000, ini hasil jualan hari ini?")
    
    # Input Area
    with st.expander("📷 Upload Bon / Mutasi"):
        col1, col2 = st.columns(2)
        with col1: st.file_uploader("Scan Bon", type=['jpg', 'png'])
        with col2: st.file_uploader("Upload Mutasi", type=['pdf'])
        if st.button("Analisis Data"):
            st.balloons()

    # BI Dashboard Small
    st.markdown("#### Insight Bulan Ini")
    df = pd.DataFrame({'Cat': ['Profit', 'HPP', 'Operasional'], 'Val': [60, 25, 15]})
    fig = px.pie(df, values='Val', names='Cat', hole=0.5, color_discrete_sequence=['#25D366', '#128C7E', '#FFCC00'])
    fig.update_layout(margin=dict(t=0, b=0, l=0, r=0), height=250)
    st.plotly_chart(fig, use_container_width=True)

    st.chat_input("Tanya Chatty: 'Berapa laba bersih saya?'")