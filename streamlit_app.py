import streamlit as st
import pandas as pd

# =====================================================
# CONFIG
# =====================================================

st.set_page_config(
    page_title="Distributor Bakpau",
    layout="wide"
)

# =====================================================
# BACKGROUND
# =====================================================

page_bg = """
<style>

.stApp{
    background-image:url("https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=1974&auto=format&fit=crop");
    background-size:cover;
    background-position:center;
    background-attachment:fixed;
}

[data-testid="stHeader"]{
    background:rgba(0,0,0,0);
}

.block-container{
    padding-top:20px;
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# =====================================================
# DATA PRODUK
# =====================================================

produk_list = {
    "Bakpau Coklat": {
        "harga_jual": 5000,
        "modal": 3000
    },

    "Bakpau Ayam": {
        "harga_jual": 7000,
        "modal": 4500
    },

    "Bakpau Kacang Hijau": {
        "harga_jual": 6000,
        "modal": 3500
    },

    "Bakpau Keju": {
        "harga_jual": 8000,
        "modal": 5000
    }
}

# =====================================================
# SESSION STATE
# =====================================================

if "data_penjualan" not in st.session_state:
    st.session_state.data_penjualan = []

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div style="
    display:flex;
    align-items:center;
    gap:15px;
    margin-bottom:10px;
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
            font-size:20px;
            font-weight:500;
        ">
            Sistem Distribusi & Pendapatan UMKM
        </div>

    </div>

</div>
""", unsafe_allow_html=True)

st.write("")

# =====================================================
# HITUNG DASHBOARD
# =====================================================

total_omzet = 0
total_keuntungan = 0
total_produk = 0

for data in st.session_state.data_penjualan:

    total_omzet += data["total"]

    keuntungan = (
        data["harga_jual"] - data["modal"]
    ) * data["qty"]

    total_keuntungan += keuntungan

    total_produk += data["qty"]

# =====================================================
# DASHBOARD
# =====================================================

col1, col2, col3 = st.columns(3)

# =====================================================
# CARD 1
# =====================================================

with col1:

    st.markdown(f"""
    <div style="
        background:rgba(255,255,255,0.12);
        padding:25px;
        border-radius:20px;
        text-align:center;
        backdrop-filter:blur(10px);
        border:1px solid rgba(255,255,255,0.1);
    ">

        <div style="
            color:#dddddd;
            font-size:18px;
            margin-bottom:10px;
        ">
            Total Omzet
        </div>

        <div style="
            color:white;
            font-size:38px;
            font-weight:bold;
        ">
            Rp {total_omzet:,}
        </div>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# CARD 2
# =====================================================

with col2:

    st.markdown(f"""
    <div style="
        background:rgba(255,255,255,0.12);
        padding:25px;
        border-radius:20px;
        text-align:center;
        backdrop-filter:blur(10px);
        border:1px solid rgba(255,255,255,0.1);
    ">

        <div style="
            color:#dddddd;
            font-size:18px;
            margin-bottom:10px;
        ">
            Total Keuntungan
        </div>

        <div style="
            color:#00ff88;
            font-size:38px;
            font-weight:bold;
        ">
            Rp {total_keuntungan:,}
        </div>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# CARD 3
# =====================================================

with col3:

    st.markdown(f"""
    <div style="
        background:rgba(255,255,255,0.12);
        padding:25px;
        border-radius:20px;
        text-align:center;
        backdrop-filter:blur(10px);
        border:1px solid rgba(255,255,255,0.1);
    ">

        <div style="
            color:#dddddd;
            font-size:18px;
            margin-bottom:10px;
        ">
            Total Produk Keluar
        </div>

        <div style="
            color:#ffd166;
            font-size:38px;
            font-weight:bold;
        ">
            {total_produk} pcs
        </div>

    </div>
    """, unsafe_allow_html=True)

# =====================================================
# SPACER
# =====================================================

st.write("")
st.write("")

# =====================================================
# FORM INPUT
# =====================================================

st.markdown("""
<div style="
    color:white;
    font-size:40px;
    font-weight:bold;
    margin-bottom:20px;
">
📦 Input Pengambilan Produk
</div>
""", unsafe_allow_html=True)

nama = st.text_input(
    "Nama Pengambil / Reseller"
)

jumlah_produk = st.number_input(
    "Jumlah Jenis Produk",
    min_value=1,
    max_value=10,
    value=1
)

selected_produk = []

# =====================================================
# MULTI PRODUK
# =====================================================

for i in range(jumlah_produk):

    st.markdown(f"""
    <div style="
        color:#ffffff;
        font-size:22px;
        font-weight:bold;
        margin-top:20px;
        margin-bottom:10px;
    ">
        Produk {i+1}
    </div>
    """, unsafe_allow_html=True)

    colA, colB = st.columns(2)

    with colA:

        produk = st.selectbox(
            f"Pilih Produk {i+1}",
            list(produk_list.keys()),
            key=f"produk_{i}"
        )

    with colB:

        qty = st.number_input(
            f"Qty {produk}",
            min_value=1,
            value=1,
            key=f"qty_{i}"
        )

    selected_produk.append({
        "nama_produk": produk,
        "qty": qty
    })

# =====================================================
# BUTTON
# =====================================================

st.write("")

if st.button("Simpan Distribusi"):

    for item in selected_produk:

        nama_produk = item["nama_produk"]
        qty = item["qty"]

        harga_jual = produk_list[nama_produk]["harga_jual"]
        modal = produk_list[nama_produk]["modal"]

        total = harga_jual * qty

        st.session_state.data_penjualan.append({
            "nama": nama,
            "produk": nama_produk,
            "qty": qty,
            "harga_jual": harga_jual,
            "modal": modal,
            "total": total
        })

    st.success("Distribusi berhasil disimpan!")

# =====================================================
# TABEL DATA
# =====================================================

st.write("")
st.write("")

st.markdown("""
<div style="
    color:white;
    font-size:40px;
    font-weight:bold;
    margin-bottom:20px;
">
📋 Data Distribusi
</div>
""", unsafe_allow_html=True)

if len(st.session_state.data_penjualan) > 0:

    df = pd.DataFrame(
        st.session_state.data_penjualan
    )

    st.dataframe(
        df,
        use_container_width=True
    )

else:

    st.info("Belum ada data distribusi.")

# =====================================================
# RINGKASAN
# =====================================================

st.write("")
st.write("")

st.markdown("""
<div style="
    color:white;
    font-size:40px;
    font-weight:bold;
    margin-bottom:20px;
">
💰 Ringkasan Pendapatan
</div>
""", unsafe_allow_html=True)

ringkasan = []

for data in st.session_state.data_penjualan:

    keuntungan = (
        data["harga_jual"] - data["modal"]
    ) * data["qty"]

    ringkasan.append({
        "Nama": data["nama"],
        "Produk": data["produk"],
        "Qty": data["qty"],
        "Omzet": data["total"],
        "Keuntungan": keuntungan
    })

if len(ringkasan) > 0:

    df_ringkasan = pd.DataFrame(ringkasan)

    st.dataframe(
        df_ringkasan,
        use_container_width=True
    )

else:

    st.info("Belum ada ringkasan.")
