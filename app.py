import streamlit as st
import pandas as pd

# Konfigurasi Halaman & Logo
st.set_page_config(page_title="aicatatin - Demo", page_icon="🤖")
st.title("🤖 aicatatin")
st.caption("Tinggal Jepret, Laporan Beres.")

# Sidebar untuk Profiling (Sesuai User Journey)
with st.sidebar:
    st.header("Profil Pengguna")
    nama = st.text_input("Nama Kamu", "Juragan")
    tipe_akun = st.radio("Tipe Akun", ["Personal", "UMKM"])
    
    if tipe_akun == "UMKM":
        sektor = st.selectbox("Sektor Usaha", ["FnB", "Fashion", "Retail"])
        mode = st.selectbox("Mode Bisnis", ["Produktif (HPP)", "Retail (Margin)"])
    else:
        tema = st.selectbox("Tema Pengeluaran", ["Sewa Kos", "Jajan", "Harian"])

st.write(f"### Halo, {nama}! 👋")

# Fitur Utama: Upload
st.subheader("📸 Input Data Keuangan")
upload_type = st.tabs(["📷 Foto Bon", "📄 Mutasi Bank (PDF)", "⌨️ Manual"])

with upload_type[0]:
    foto = st.file_uploader("Upload Foto Struk", type=['jpg', 'png', 'jpeg'])
    if foto:
        st.success("AI sedang membaca bon... (Simulasi)")
        # Contoh Output AI
        st.info("**Hasil Analisis Chatty:**\n\nItem: Kain Katun | Total: Rp 500.000\n\n⚠️ *Harga naik 10% dari bulan lalu!*")

with upload_type[1]:
    pdf = st.file_uploader("Upload PDF Mutasi", type=['pdf'])
    if pdf:
        st.success("PDF Mutasi Bank Berhasil Diunggah!")
        st.write("Ditemukan 2 transaksi yang cocok dengan bon Anda (Rekonsiliasi Otomatis).")

# Fitur BI: Laporan Sederhana
st.divider()
st.subheader("📊 Laporan BI (Business Intelligence)")

# Data Dummy untuk Grafik
data_dummy = pd.DataFrame({
    'Kategori': ['Bahan Baku', 'Listrik', 'Sewa', 'Lainnya'],
    'Nominal': [5000000, 500000, 2000000, 300000]
})

col1, col2 = st.columns(2)
with col1:
    st.metric(label="Total Pengeluaran", value="Rp 7.800.000", delta="-5% (Lebih Hemat)")
with col2:
    st.write("Distribusi Biaya")
    st.bar_chart(data_dummy.set_index('Kategori'))

st.warning("🤖 **Insight AI:** Pengeluaran bahan baku meningkat. Sebaiknya cek supplier lain atau sesuaikan harga jual.")