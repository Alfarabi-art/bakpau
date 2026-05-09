import streamlit as st
import pandas as pd
from datetime import datetime

# ======================================================
# CONFIG
# ======================================================

st.set_page_config(
    page_title="Distributor Bakpau",
    layout="wide"
)

# ======================================================
# CSS MODERN UI
# ======================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background-image:
    linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.72)),
    url("https://images.unsplash.com/photo-1569718212165-3a8278d5f624?q=80&w=1200");

    background-size:cover;
    background-position:center;
    background-attachment:fixed;
}

[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}

.block-container{
    padding-top:25px;
}

.title{
    font-size:70px;
    font-weight:700;
    color:white;
    line-height:1.1;
}

.subtitle{
    font-size:24px;
    color:#dddddd;
    margin-top:10px;
}

.glass{
    background:rgba(255,255,255,0.08);
    border:1px solid rgba(255,255,255,0.15);
    backdrop-filter: blur(14px);
    border-radius:28px;
    padding:28px;
    margin-bottom:25px;
    box-shadow:0 8px 32px rgba(0,0,0,0.35);
}

.metric-card{
    background:linear-gradient(
        135deg,
        rgba(255,255,255,0.12),
        rgba(255,255,255,0.05)
    );

    border-radius:25px;
    padding:25px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.12);
}

.metric-title{
    color:#dddddd;
    font-size:18px;
    margin-bottom:10px;
}

.metric-value{
    color:white;
    font-size:42px;
    font-weight:bold;
}

.section-title{
    color:white;
    font-size:40px;
    font-weight:bold;
}

.product-card{
    background:rgba(255,255,255,0.08);
    border-radius:22px;
    overflow:hidden;
    border:1px solid rgba(255,255,255,0.10);
    margin-bottom:20px;
}

.product-img{
    width:100%;
    height:220px;
    object-fit:cover;
}

.product-content{
    padding:20px;
}

.product-name{
    color:white;
    font-size:26px;
    font-weight:600;
}

.product-price{
    color:#ffd166;
    font-size:30px;
    font-weight:bold;
    margin-top:10px;
}

.label{
    color:white;
    font-weight:600;
    font-size:18px;
    margin-bottom:6px;
}

.stButton>button{
    background:linear-gradient(135deg,#ff4b4b,#ff6b6b);
    color:white;
    border:none;
    border-radius:15px;
    padding:14px 28px;
    font-size:18px;
    font-weight:bold;
    width:100%;
}

.stButton>button:hover{
    transform:scale(1.02);
    background:linear-gradient(135deg,#ff2d2d,#ff5252);
}

div[data-baseweb="select"]{
    background:white;
    border-radius:12px;
}

input{
    border-radius:12px !important;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# DATA PRODUK
# ======================================================

produk_data = {
    "Bakpau Coklat": {
        "modal": 3000,
        "jual": 5000,
        "img":"https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=1200"
    },

    "Bakpau Ayam": {
        "modal": 4000,
        "jual": 7000,
        "img":"https://images.unsplash.com/photo-1526318896980-cf78c088247c?q=80&w=1200"
    },

    "Bakpau Kacang Hijau": {
        "modal": 3500,
        "jual": 6000,
        "img":"https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=1200"
    },

    "Bakpau Keju": {
        "modal": 5000,
        "jual": 8000,
        "img":"https://images.unsplash.com/photo-1569718212165-3a8278d5f624?q=80&w=1200"
    }
}

# ======================================================
# SESSION
# ======================================================

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

# ======================================================
# HEADER
# ======================================================

st.markdown("""
<div class="glass">

<div class="title">
🥟 Distributor Bakpau
</div>

<div class="subtitle">
Sistem Distribusi & Pendapatan UMKM
</div>

</div>
""", unsafe_allow_html=True)

# ======================================================
# METRIC
# ======================================================

total_omzet = sum(
    x["Total Omzet"]
    for x in st.session_state.riwayat
)

total_profit = sum(
    x["Keuntungan"]
    for x in st.session_state.riwayat
)

total_produk = sum(
    x["Total Qty"]
    for x in st.session_state.riwayat
)

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
        💰 Total Omzet
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
        📈 Total Keuntungan
        </div>

        <div class="metric-value" style="color:#00ff99;">
        Rp {total_profit:,}
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="metric-card">
        <div class="metric-title">
        📦 Produk Keluar
        </div>

        <div class="metric-value" style="color:#ffd166;">
        {total_produk} pcs
        </div>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# FORM INPUT
# ======================================================

st.write("")
st.markdown("""
<div class="glass">
<div class="section-title">
📋 Input Distribusi
</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="label">Nama Reseller</div>', unsafe_allow_html=True)
nama = st.text_input("", label_visibility="collapsed")

st.markdown('<div class="label">Status Pembayaran</div>', unsafe_allow_html=True)
status = st.selectbox(
    "",
    ["Belum Bayar", "Sudah Bayar"],
    label_visibility="collapsed"
)

# ======================================================
# PILIH PRODUK
# ======================================================

st.write("")
st.markdown("""
<div class="section-title">
🛒 Pilih Produk
</div>
""", unsafe_allow_html=True)

produk_terpilih = []

for nama_produk, data in produk_data.items():

    col1, col2 = st.columns([3,1])

    with col1:

        st.markdown(f"""
        <div class="product-card">

            <img class="product-img"
            src="{data['img']}">

            <div class="product-content">

                <div class="product-name">
                {nama_produk}
                </div>

                <div class="product-price">
                Rp {data['jual']:,}
                </div>

            </div>

        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("<br><br>", unsafe_allow_html=True)

        qty = st.number_input(
            f"Qty {nama_produk}",
            min_value=0,
            step=1,
            key=nama_produk
        )

    if qty > 0:

        total_modal = qty * data["modal"]
        total_jual = qty * data["jual"]
        keuntungan = total_jual - total_modal

        produk_terpilih.append({

            "Produk": nama_produk,
            "Qty": qty,
            "Total Modal": total_modal,
            "Total Jual": total_jual,
            "Keuntungan": keuntungan

        })

# ======================================================
# TOTAL
# ======================================================

grand_qty = sum(x["Qty"] for x in produk_terpilih)
grand_modal = sum(x["Total Modal"] for x in produk_terpilih)
grand_jual = sum(x["Total Jual"] for x in produk_terpilih)
grand_profit = sum(x["Keuntungan"] for x in produk_terpilih)

# ======================================================
# RINGKASAN
# ======================================================

st.write("")

st.markdown(f"""
<div class="glass">

<h1 style="color:white;">
🧾 Ringkasan Distribusi
</h1>

<h2 style="color:#ffd166;">
Total Produk : {grand_qty} pcs
</h2>

<h2 style="color:white;">
Omzet : Rp {grand_jual:,}
</h2>

<h2 style="color:#00ff99;">
Keuntungan : Rp {grand_profit:,}
</h2>

</div>
""", unsafe_allow_html=True)

# ======================================================
# BUTTON SIMPAN
# ======================================================

if st.button("💾 Simpan Distribusi"):

    if nama == "":
        st.warning("Masukkan nama reseller")

    elif len(produk_terpilih) == 0:
        st.warning("Pilih minimal 1 produk")

    else:

        daftar_produk = []

        for item in produk_terpilih:

            daftar_produk.append(
                f"{item['Produk']} ({item['Qty']} pcs)"
            )

        gabungan_produk = ", ".join(daftar_produk)

        st.session_state.riwayat.append({

            "Tanggal":
            datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            ),

            "Nama":
            nama,

            "Produk":
            gabungan_produk,

            "Total Qty":
            grand_qty,

            "Total Omzet":
            grand_jual,

            "Keuntungan":
            grand_profit,

            "Status":
            status

        })

        st.success("Distribusi berhasil disimpan")

# ======================================================
# RIWAYAT
# ======================================================

st.write("")
st.write("")

st.markdown("""
<div class="glass">

<div class="section-title">
📊 Riwayat Distribusi
</div>

</div>
""", unsafe_allow_html=True)

if len(st.session_state.riwayat) == 0:

    st.info("Belum ada data distribusi")

else:

    df = pd.DataFrame(
        st.session_state.riwayat
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=400
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Laporan CSV",
        csv,
        "laporan_distributor.csv",
        "text/csv"
    )
