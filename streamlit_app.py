import streamlit as st
import pandas as pd
from datetime import datetime

# ======================================================
# CONFIG
# ======================================================

st.set_page_config(
    page_title="Distributor Bakpau",
    page_icon="🥟",
    layout="wide"
)

# ======================================================
# CSS
# ======================================================

st.markdown("""
<style>

.stApp{
    background-image:
    linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
    url("https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1974&auto=format&fit=crop");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

[data-testid="stHeader"]{
    background: transparent;
}

.block-container{
    padding-top: 2rem;
}

h1,h2,h3,h4,h5,h6,p,label{
    color: white !important;
}

.stTextInput label,
.stSelectbox label,
.stNumberInput label{
    color:white !important;
    font-weight:bold;
}

.stButton button{
    width:100%;
    background:#e63946;
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-weight:bold;
}

.stButton button:hover{
    background:#c1121f;
}

.card{
    background:rgba(255,255,255,0.10);
    padding:25px;
    border-radius:20px;
    backdrop-filter: blur(10px);
    border:1px solid rgba(255,255,255,0.1);
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# SESSION STATE
# ======================================================

if "data_distributor" not in st.session_state:
    st.session_state.data_distributor = []

# ======================================================
# DATA PRODUK
# ======================================================

produk_data = {

    "Bakpau Coklat": {
        "modal": 3000,
        "jual": 5000
    },

    "Bakpau Ayam": {
        "modal": 4000,
        "jual": 7000
    },

    "Bakpau Keju": {
        "modal": 5000,
        "jual": 8000
    },

    "Bakpau Kacang Hijau": {
        "modal": 3500,
        "jual": 6000
    }

}

# ======================================================
# HEADER
# ======================================================

st.markdown("""
<div style="
display:flex;
align-items:center;
gap:20px;
margin-bottom:40px;
">

<div style="font-size:70px;">
🥟
</div>

<div>

<div style="
font-size:55px;
font-weight:bold;
color:white;
">
Distributor Bakpau
</div>

<div style="
font-size:22px;
color:#dddddd;
">
Sistem Distribusi & Pendapatan UMKM
</div>

</div>

</div>
""", unsafe_allow_html=True)

# ======================================================
# HITUNG TOTAL
# ======================================================

total_omzet = 0
total_keuntungan = 0
total_produk = 0

for item in st.session_state.data_distributor:

    total_omzet += item["Total Jual"]
    total_keuntungan += item["Keuntungan"]
    total_produk += item["Qty"]

# ======================================================
# DASHBOARD
# ======================================================

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown(
        f"""
        <div class="card">

            <div style="
            color:#dddddd;
            font-size:20px;
            margin-bottom:15px;
            ">
                Total Omzet
            </div>

            <div style="
            color:white;
            font-size:42px;
            font-weight:bold;
            ">
                Rp {total_omzet:,}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with c2:

    st.markdown(
        f"""
        <div class="card">

            <div style="
            color:#dddddd;
            font-size:20px;
            margin-bottom:15px;
            ">
                Total Keuntungan
            </div>

            <div style="
            color:#00ff99;
            font-size:42px;
            font-weight:bold;
            ">
                Rp {total_keuntungan:,}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

with c3:

    st.markdown(
        f"""
        <div class="card">

            <div style="
            color:#dddddd;
            font-size:20px;
            margin-bottom:15px;
            ">
                Total Produk Keluar
            </div>

            <div style="
            color:#ffd166;
            font-size:42px;
            font-weight:bold;
            ">
                {total_produk} pcs
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

# ======================================================
# SPACING
# ======================================================

st.write("")
st.write("")

# ======================================================
# FORM
# ======================================================

st.markdown("""
<div class="card">
""", unsafe_allow_html=True)

st.markdown("""
<h1>
📦 Input Pengambilan Produk
</h1>
""", unsafe_allow_html=True)

nama = st.text_input(
    "Nama Pengambil / Reseller"
)

status = st.selectbox(
    "Status Pembayaran",
    ["Belum Bayar", "Lunas"]
)

jumlah_produk = st.number_input(
    "Jumlah Jenis Produk",
    min_value=1,
    max_value=10,
    value=1
)

produk_terpilih = []

grand_total_jual = 0
grand_keuntungan = 0
grand_qty = 0

# ======================================================
# MULTI PRODUK
# ======================================================

for i in range(jumlah_produk):

    st.markdown(f"""
    <h3 style="color:white;">
    Produk {i+1}
    </h3>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        produk = st.selectbox(
            f"Pilih Produk {i+1}",
            list(produk_data.keys()),
            key=f"produk_{i}"
        )

    with col2:

        qty = st.number_input(
            f"Qty Produk {i+1}",
            min_value=1,
            value=1,
            key=f"qty_{i}"
        )

    modal = produk_data[produk]["modal"]
    jual = produk_data[produk]["jual"]

    total_modal = modal * qty
    total_jual = jual * qty
    keuntungan = total_jual - total_modal

    grand_total_jual += total_jual
    grand_keuntungan += keuntungan
    grand_qty += qty

    produk_terpilih.append({

        "Produk": produk,
        "Qty": qty,
        "Harga Modal": modal,
        "Harga Jual": jual,
        "Total Modal": total_modal,
        "Total Jual": total_jual,
        "Keuntungan": keuntungan

    })

# ======================================================
# RINGKASAN
# ======================================================

st.markdown(f"""
<div style="
background:rgba(255,255,255,0.08);
padding:20px;
border-radius:15px;
margin-top:25px;
">

<h2 style="color:white;">
💰 Ringkasan
</h2>

<h1 style="color:#00ff99;">
Omzet : Rp {grand_total_jual:,}
</h1>

<h1 style="color:#ffd166;">
Keuntungan : Rp {grand_keuntungan:,}
</h1>

<h1 style="color:white;">
Total Produk : {grand_qty} pcs
</h1>

</div>
""", unsafe_allow_html=True)

st.write("")

# ======================================================
# BUTTON
# ======================================================

if st.button("💾 Simpan Distribusi"):

    if nama == "":

        st.warning("Masukkan nama reseller")

    else:

        for item in produk_terpilih:

            st.session_state.data_distributor.append({

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

        st.success("Data berhasil disimpan")

st.markdown("</div>", unsafe_allow_html=True)

# ======================================================
# SPACING
# ======================================================

st.write("")
st.write("")

# ======================================================
# RIWAYAT
# ======================================================

st.markdown("""
<div class="card">
""", unsafe_allow_html=True)

st.markdown("""
<h1>
📋 Riwayat Distribusi
</h1>
""", unsafe_allow_html=True)

if len(st.session_state.data_distributor) == 0:

    st.info("Belum ada data")

else:

    df = pd.DataFrame(
        st.session_state.data_distributor
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download CSV",
        csv,
        "laporan_distributor.csv",
        "text/csv"
    )

st.markdown("</div>", unsafe_allow_html=True)
