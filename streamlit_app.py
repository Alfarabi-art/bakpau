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
    linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
    url("https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1974&auto=format&fit=crop");

    background-size:cover;
    background-position:center;
    background-attachment:fixed;
}

.block-container{
    padding-top:2rem;
}

[data-testid="stHeader"]{
    background:transparent;
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

.card{
    background:rgba(255,255,255,0.08);
    padding:25px;
    border-radius:20px;
    margin-bottom:25px;
    backdrop-filter:blur(10px);
    border:1px solid rgba(255,255,255,0.1);
}

.metric-card{
    background:rgba(255,255,255,0.12);
    padding:25px;
    border-radius:20px;
    text-align:center;
    backdrop-filter:blur(10px);
    border:1px solid rgba(255,255,255,0.1);
}

.metric-title{
    color:#dddddd;
    font-size:18px;
    margin-bottom:10px;
}

.metric-value{
    color:white;
    font-size:38px;
    font-weight:bold;
}

.stButton button{
    width:100%;
    background:#e63946;
    color:white;
    border:none;
    border-radius:12px;
    font-weight:bold;
    padding:14px;
    font-size:16px;
}

.stButton button:hover{
    background:#c1121f;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# SESSION
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
<div style="
    display:flex;
    align-items:center;
    gap:15px;
    margin-bottom:20px;
">

    <div style="font-size:70px;">
        🥟
    </div>

    <div>

        <div style="
            color:white;
            font-size:55px;
            font-weight:bold;
        ">
            Distributor Bakpau
        </div>

        <div style="
            color:#dddddd;
            font-size:22px;
        ">
            Sistem Distribusi & Pendapatan UMKM
        </div>

    </div>

</div>
""", unsafe_allow_html=True)

# =====================================================
# HITUNG DASHBOARD
# =====================================================

total_omzet = 0
total_keuntungan = 0
total_produk = 0

for trx in st.session_state.transaksi:

    total_omzet += trx["Total Jual"]
    total_keuntungan += trx["Keuntungan"]
    total_produk += trx["Qty"]

# =====================================================
# DASHBOARD
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            Total Omzet
        </div>

        <div class="metric-value">
            Rp {total_omzet:,}
        </div>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            Total Keuntungan
        </div>

        <div class="metric-value" style="color:#00ff99;">
            Rp {total_keuntungan:,}
        </div>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="metric-card">

        <div class="metric-title">
            Total Produk Keluar
        </div>

        <div class="metric-value" style="color:#ffd166;">
            {total_produk} pcs
        </div>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# FORM
# =====================================================

st.write("")

st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("## 📦 Input Pengambilan Produk")

nama = st.text_input(
    "Nama Pengambil / Reseller"
)

status = st.selectbox(
    "Status Pembayaran",
    ["Belum Bayar", "Lunas"]
)

jumlah_menu = st.number_input(
    "Jumlah Jenis Produk",
    min_value=1,
    max_value=10,
    value=1
)

produk_dipilih = []

grand_modal = 0
grand_jual = 0
grand_keuntungan = 0
grand_qty = 0

# =====================================================
# MULTI MENU
# =====================================================

for i in range(jumlah_menu):

    st.markdown(f"### Produk {i+1}")

    col1, col2 = st.columns(2)

    with col1:

        produk = st.selectbox(
            f"Pilih Produk {i+1}",
            list(produk_list.keys()),
            key=f"produk_{i}"
        )

    with col2:

        qty = st.number_input(
            f"Qty Produk {i+1}",
            min_value=1,
            value=1,
            key=f"qty_{i}"
        )

    modal = produk_list[produk]["modal"]
    jual = produk_list[produk]["jual"]

    total_modal = modal * qty
    total_jual = jual * qty
    keuntungan = total_jual - total_modal

    grand_modal += total_modal
    grand_jual += total_jual
    grand_keuntungan += keuntungan
    grand_qty += qty

    produk_dipilih.append({

        "Produk": produk,
        "Qty": qty,
        "Harga Modal": modal,
        "Harga Jual": jual,
        "Total Modal": total_modal,
        "Total Jual": total_jual,
        "Keuntungan": keuntungan
    })

# =====================================================
# PREVIEW
# =====================================================

st.markdown(f"""
<div style="
    background:rgba(255,255,255,0.06);
    padding:20px;
    border-radius:15px;
    margin-top:20px;
">

<h3 style="color:white;">
💰 Total Keseluruhan
</h3>

<h2 style="color:#00ff99;">
Omzet : Rp {grand_jual:,}
</h2>

<h2 style="color:#ffd166;">
Keuntungan : Rp {grand_keuntungan:,}
</h2>

<h2 style="color:white;">
Total Produk : {grand_qty} pcs
</h2>

</div>
""", unsafe_allow_html=True)

# =====================================================
# BUTTON
# =====================================================

st.write("")

if st.button("💾 Simpan Distribusi"):

    if nama == "":

        st.warning("Masukkan nama pengambil")

    else:

        for item in produk_dipilih:

            st.session_state.transaksi.append({

                "Tanggal":
                datetime.now().strftime(
                    "%d-%m-%Y %H:%M:%S"
                ),

                "Nama": nama,

                "Produk": item["Produk"],

                "Qty": item["Qty"],

                "Harga Modal": item["Harga Modal"],

                "Harga Jual": item["Harga Jual"],

                "Total Modal": item["Total Modal"],

                "Total Jual": item["Total Jual"],

                "Keuntungan": item["Keuntungan"],

                "Status": status
            })

        st.success("Distribusi berhasil disimpan")

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# TABEL
# =====================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

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

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download Laporan CSV",
        data=csv,
        file_name="laporan_distributor_bakpau.csv",
        mime="text/csv"
    )

st.markdown("</div>", unsafe_allow_html=True)
