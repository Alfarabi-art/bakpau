import streamlit as st
import pandas as pd
from datetime import datetime

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Distributor Bakpau",
    page_icon="🥟",
    layout="wide"
)

# =====================================================
# CSS
# =====================================================

st.markdown("""
<style>

.stApp{
    background-image:
    linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)),
    url("https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1974&auto=format&fit=crop");

    background-size:cover;
    background-position:center;
    background-attachment:fixed;
}

.block-container{
    padding-top:2rem;
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

.card{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    margin-bottom:20px;
    backdrop-filter:blur(10px);
    border:1px solid rgba(255,255,255,0.1);
}

.metric-card{
    background:rgba(255,255,255,0.12);
    padding:20px;
    border-radius:20px;
    text-align:center;
    backdrop-filter:blur(10px);
    border:1px solid rgba(255,255,255,0.1);
}

.metric-title{
    color:#dddddd;
    font-size:18px;
}

.metric-value{
    color:white;
    font-size:34px;
    font-weight:bold;
    margin-top:10px;
}

.stButton button{
    width:100%;
    background:#e63946;
    color:white;
    border:none;
    border-radius:12px;
    font-weight:bold;
    padding:12px;
}

.stButton button:hover{
    background:#c1121f;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SESSION STATE
# =====================================================

if "transaksi" not in st.session_state:
    st.session_state.transaksi = []

# =====================================================
# DATA PRODUK
# =====================================================

produk_list = {
    "Bakpau Coklat": {
        "modal": 3000,
        "jual": 5000
    },

    "Bakpau Ayam": {
        "modal": 4000,
        "jual": 7000
    },

    "Bakpau Kacang Hijau": {
        "modal": 3500,
        "jual": 6000
    },

    "Bakpau Keju": {
        "modal": 5000,
        "jual": 8000
    }
}

# =====================================================
# HEADER
# =====================================================

st.markdown("""
# 🥟 Distributor Bakpau
### Sistem Distribusi & Pendapatan UMKM
""")

# =====================================================
# DASHBOARD
# =====================================================

total_omzet = 0
total_keuntungan = 0
total_produk = 0

for trx in st.session_state.transaksi:

    total_omzet += trx["total_jual"]
    total_keuntungan += trx["keuntungan"]
    total_produk += trx["qty"]

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Total Omzet</div>
        <div class="metric-value">
            Rp {total_omzet:,}
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Total Keuntungan</div>
        <div class="metric-value">
            Rp {total_keuntungan:,}
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">Total Produk Keluar</div>
        <div class="metric-value">
            {total_produk} pcs
        </div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# INPUT DISTRIBUSI
# =====================================================

st.markdown("""
<div class="card">
""", unsafe_allow_html=True)

st.markdown("## 📦 Input Pengambilan Produk")

col1, col2 = st.columns(2)

with col1:

    nama = st.text_input(
        "Nama Pengambil / Reseller"
    )

    produk = st.selectbox(
        "Pilih Produk",
        list(produk_list.keys())
    )

with col2:

    qty = st.number_input(
        "Jumlah Produk",
        min_value=1,
        value=1
    )

    status = st.selectbox(
        "Status Pembayaran",
        ["Belum Bayar", "Lunas"]
    )

# =====================================================
# HITUNG
# =====================================================

modal = produk_list[produk]["modal"]
jual = produk_list[produk]["jual"]

total_modal = modal * qty
total_jual = jual * qty
keuntungan = total_jual - total_modal

# =====================================================
# PREVIEW
# =====================================================

st.markdown(f"""
### 💰 Rincian

- Harga Modal : Rp {modal:,}
- Harga Jual : Rp {jual:,}
- Total Modal : Rp {total_modal:,}
- Total Jual : Rp {total_jual:,}
- Keuntungan : Rp {keuntungan:,}
""")

# =====================================================
# SIMPAN
# =====================================================

if st.button("💾 Simpan Distribusi"):

    if nama == "":

        st.warning("Masukkan nama pengambil")

    else:

        st.session_state.transaksi.append({

            "tanggal":
            datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            ),

            "nama": nama,

            "produk": produk,

            "qty": qty,

            "modal": modal,

            "jual": jual,

            "total_modal": total_modal,

            "total_jual": total_jual,

            "keuntungan": keuntungan,

            "status": status
        })

        st.success("Data distribusi berhasil disimpan")

st.markdown("""
</div>
""", unsafe_allow_html=True)

# =====================================================
# RIWAYAT DISTRIBUSI
# =====================================================

st.markdown("""
<div class="card">
""", unsafe_allow_html=True)

st.markdown("## 📋 Riwayat Distribusi")

if len(st.session_state.transaksi) == 0:

    st.info("Belum ada transaksi")

else:

    df = pd.DataFrame(
        st.session_state.transaksi
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    # =================================================
    # DOWNLOAD EXCEL
    # =================================================

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Laporan CSV",
        data=csv,
        file_name="laporan_distributor_bakpau.csv",
        mime="text/csv"
    )

st.markdown("""
</div>
""", unsafe_allow_html=True)

# =====================================================
# RESUMEN PENDAPATAN
# =====================================================

st.markdown("""
<div class="card">
""", unsafe_allow_html=True)

st.markdown("## 📈 Ringkasan Pendapatan")

st.markdown(f"""
### 🧾 Total Omzet
# Rp {total_omzet:,}

### 💵 Total Keuntungan
# Rp {total_keuntungan:,}

### 📦 Total Produk Terjual
# {total_produk} pcs
""")

st.markdown("""
</div>
""", unsafe_allow_html=True)
