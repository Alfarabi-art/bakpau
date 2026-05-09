import streamlit as st
import pandas as pd
from datetime import datetime

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

[data-testid="stAppViewContainer"]{
background-image:url("https://images.unsplash.com/photo-1569718212165-3a8278d5f624?q=80&w=1200");
background-size:cover;
background-position:center;
background-repeat:no-repeat;
background-attachment:fixed;
}

[data-testid="stHeader"]{
background:rgba(0,0,0,0);
}

.block-container{
padding-top:20px;
}

.kotak{
background:rgba(0,0,0,0.55);
padding:25px;
border-radius:25px;
backdrop-filter: blur(10px);
margin-bottom:20px;
}

.title{
color:white;
font-size:60px;
font-weight:bold;
}

.subtitle{
color:#dddddd;
font-size:24px;
margin-top:-10px;
}

.metric-title{
color:#dddddd;
font-size:20px;
margin-bottom:10px;
}

.metric-value{
color:white;
font-size:40px;
font-weight:bold;
}

.card-produk{
background:rgba(255,255,255,0.08);
padding:20px;
border-radius:20px;
margin-bottom:15px;
}

.nama-produk{
color:white;
font-size:24px;
font-weight:bold;
}

.harga{
color:#ffd166;
font-size:22px;
font-weight:bold;
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# =====================================================
# DATA PRODUK
# =====================================================

produk_data = {
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
# SESSION STATE
# =====================================================

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="kotak">

<div class="title">
🥟 Distributor Bakpau
</div>

<div class="subtitle">
Sistem Distribusi & Pendapatan UMKM
</div>

</div>
""", unsafe_allow_html=True)

# =====================================================
# INPUT DATA
# =====================================================

st.markdown("""
<div class="kotak">
<h1 style='color:white;'>📦 Input Pengambilan Produk</h1>
</div>
""", unsafe_allow_html=True)

nama = st.text_input("Nama Pengambil / Reseller")

status = st.selectbox(
    "Status Pembayaran",
    ["Belum Bayar", "Sudah Bayar"]
)

# =====================================================
# MULTI PRODUK
# =====================================================

st.markdown("## 🛒 Pilih Produk")

produk_terpilih = []

for nama_produk, data in produk_data.items():

    st.markdown(f"""
    <div class="card-produk">
    <div class="nama-produk">{nama_produk}</div>
    <div class="harga">
    Rp {data['jual']:,}
    </div>
    </div>
    """, unsafe_allow_html=True)

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
            "Harga Modal": data["modal"],
            "Harga Jual": data["jual"],
            "Total Modal": total_modal,
            "Total Jual": total_jual,
            "Keuntungan": keuntungan

        })

# =====================================================
# TOTAL
# =====================================================

grand_qty = sum(x["Qty"] for x in produk_terpilih)
grand_modal = sum(x["Total Modal"] for x in produk_terpilih)
grand_jual = sum(x["Total Jual"] for x in produk_terpilih)
grand_keuntungan = sum(x["Keuntungan"] for x in produk_terpilih)

# =====================================================
# METRIC
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(f"""
    <div class="kotak">
    <div class="metric-title">
    Total Omzet
    </div>

    <div class="metric-value">
    Rp {grand_jual:,}
    </div>
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown(f"""
    <div class="kotak">
    <div class="metric-title">
    Total Keuntungan
    </div>

    <div class="metric-value" style="color:#00ff99;">
    Rp {grand_keuntungan:,}
    </div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="kotak">
    <div class="metric-title">
    Total Produk Keluar
    </div>

    <div class="metric-value" style="color:#ffd166;">
    {grand_qty} pcs
    </div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# SIMPAN DATA
# =====================================================

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

            "Total Modal":
            grand_modal,

            "Total Omzet":
            grand_jual,

            "Keuntungan":
            grand_keuntungan,

            "Status":
            status

        })

        st.success("Data berhasil disimpan")

# =====================================================
# RIWAYAT
# =====================================================

st.write("")
st.write("")

st.markdown("""
<div class="kotak">
<h1 style='color:white;'>📋 Riwayat Distribusi</h1>
</div>
""", unsafe_allow_html=True)

if len(st.session_state.riwayat) == 0:

    st.info("Belum ada data")

else:

    df = pd.DataFrame(
        st.session_state.riwayat
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
