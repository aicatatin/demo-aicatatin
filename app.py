import streamlit as st
import time
import pandas as pd

# 1. Konfigurasi Halaman (Mobile Look)
st.set_page_config(page_title="aicatatin", page_icon="🤖", layout="centered")

# Custom CSS untuk Gaya WhatsApp & Animasi Splash
st.markdown("""
    <style>
    /* Splash Screen Animation */
    @keyframes blink {
        0% { opacity: 1; }
        50% { opacity: 0.3; }
        100% { opacity: 1; }
    }
    .splash-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 80vh;
    }
    .blink-icon {
        width: 100px;
        animation: blink 1.5s infinite;
    }
    
    /* Login & WA Style */
    .stButton>button { width: 100%; border-radius: 20px; }
    .wa-chat-item {
        padding: 15px;
        border-bottom: 1px solid #f0f0f0;
        display: flex;
        align-items: center;
    }
    .wa-avatar {
        background-color: #25D366;
        color: white;
        border-radius: 50%;
        width: 45px;
        height: 45px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 15px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Logika State Aplikasi (Session State)
if 'page' not in st.session_state:
    st.session_state.page = 'splash'

# --- ROUTING HALAMAN ---

# A. SPLASH SCREEN
if st.session_state.page == 'splash':
    st.markdown("""
        <div class="splash-container">
            <img src="https://cdn-icons-png.flaticon.com/512/4712/4712035.png" class="blink-icon">
            <h2 style='color: #25D366;'>aicatatin</h2>
            <p>Tinggal Jepret, Laporan Beres.</p>
        </div>
    """, unsafe_allow_html=True)
    time.sleep(3) # Durasi animasi 3 detik
    st.session_state.page = 'login'
    st.rerun()

# B. HALAMAN LOGIN
elif st.session_state.page == 'login':
    st.markdown("<h2 style='text-align: center;'>Selamat Datang</h2>", unsafe_allow_html=True)
    st.text_input("Nomor WhatsApp atau Email")
    st.text_input("Password", type="password")
    if st.button("Masuk"):
        st.session_state.page = 'chat_list'
        st.rerun()
    st.markdown("<p style='text-align: center; font-size: 12px;'>Belum punya akun? Daftar di sini</p>", unsafe_allow_html=True)

# C. HALAMAN DAFTAR CHAT (ALA WHATSAPP)
elif st.session_state.page == 'chat_list':
    st.markdown("<h3 style='color: #075E54;'>aicatatin</h3>", unsafe_allow_html=True)
    
    # Daftar Chat (Mock Data)
    chats = [
        {"name": "Chatty AI", "msg": "Ada selisih Rp 20rb di mutasi kamu...", "time": "12:45"},
        {"name": "Supplier Kain", "msg": "Kirim nota bahan baku bulan ini.", "time": "10:20"},
        {"name": "Info Pajak", "msg": "Laporan bulanan sudah siap.", "time": "Yesterday"}
    ]
    
    for chat in chats:
        col1, col2 = st.columns([1, 4])
        with col1:
            st.markdown(f'<div class="wa-avatar">{chat["name"][0]}</div>', unsafe_allow_html=True)
        with col2:
            st.markdown(f"**{chat['name']}**")
            st.markdown(f"<small>{chat['msg']}</small>", unsafe_allow_html=True)
        st.divider()

    if st.button("Buka Chatty AI 🤖"):
        st.session_state.page = 'main_app'
        st.rerun()

# D. HALAMAN UTAMA (Aplikasi yang kita buat sebelumnya)
elif st.session_state.page == 'main_app':
    if st.button("⬅️ Kembali ke Daftar Chat"):
        st.session_state.page = 'chat_list'
        st.rerun()
    
    st.write("### 🤖 Chatty AI Assistant")
    # ... Masukkan kode dashboard BI & input yang kita buat sebelumnya di sini ...
    st.info("Fitur Input Mutasi & Bon Aktif.")
    uploaded = st.file_uploader("Upload Mutasi atau Struk")