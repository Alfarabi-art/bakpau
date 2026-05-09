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
    linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.72)),
    url("https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1974&auto=format&fit=crop");

    background-size:cover;
    background-position:center;
    background-attachment:fixed;
}

.block-container{
    padding-top:2rem;
}

/* TEXT */
h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

/* CARD */
.card{
    background:rgba(255,255,255,0.08);
    padding:25px;
    border-radius:22px;
    margin-bottom:25px;
    backdrop-filter:blur(10px);
    border:1px solid rgba(255,255,255,0.1);
}

/* METRIC */
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
}

.metric-value{
    color:white;
    font-size:34px;
    font-weight:bold;
    margin-top:10px;
}

/* BUTTON */
.stButton button{
    width:100%;
    background:#e63946;
    color:white;
    border:none;
    border-radius:14px;
    font-weight:bold;
    padding:12px;
    font-size:16px;
}

.stButton button:hover{
    background:#c1121f;
}

/* TABLE */
[data-testid="stDataFrame"]{
    background:white;
    border-radius:14px;
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

        <div class="metric-value">
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

nama = st.text_input(
    "Nama Pengambil / Reseller"
)

status = st.selectbox(
    "Status Pembayaran",
    ["Belum Bayar", "Lunas"]
)

st.markdown("## 🥟 Pilih Produk")

selected_items = []

total_modal = 0
total_jual = 0
total_keuntungan_input = 0
total_qty_input = 0

# =====================================================
# PRODUK LOOP
# =====================================================

for produk_nama, data in produk_list.items():

    st.markdown("---")

    col1, col2 = st.columns([3,1])

    with col1:

        pilih = st.checkbox(
            f"{produk_nama}",
            key=f"check_{produk_nama}"
        )

    with col2:

        qty = st.number_input(
            f"Qty {produk_nama}",
            min_value=0,
            value=0,
            key=f"qty_{produk_nama}"
        )

    # =================================================
    # JIKA DIPILIH
    # =================================================

    if pilih and qty > 0:

        modal = data["modal"]
        jual = data["jual"]

        subtotal_modal = modal * qty
        subtotal_jual = jual * qty
        keuntungan = subtotal_jual - subtotal_modal

        total_modal += subtotal_modal
        total_jual += subtotal_jual
        total_keuntungan_input += keuntungan
        total_qty_input += qty

        selected_items.append({

            "produk": produk_nama,
            "qty": qty,
            "modal": modal,
            "jual": jual,
            "subtotal_modal": subtotal_modal,
            "subtotal_jual": subtotal_jual,
            "keuntungan": keuntungan
        })

# =====================================================
# RINGKASAN
# =====================================================

st.markdown("## 💰 Ringkasan Distribusi")

st.markdown(f"""
### 📦 Total Produk
# {total_qty_input} pcs

### 💵 Total Omzet
# Rp {total_jual:,}

### 🟢 Total Keuntungan
# Rp {total_keuntungan_input:,}
""")

# =====================================================
# SIMPAN
# =====================================================

if st.button("💾 Simpan Distribusi"):

    if nama == "":

        st.warning("Masukkan nama reseller")

    elif len(selected_items) == 0:

        st.warning("Pilih minimal 1 produk")

    else:

        st.session_state.transaksi.append({

            "tanggal":
            datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            ),

            "nama": nama,

            "items": selected_items,

            "qty": total_qty_input,

            "total_modal": total_modal,

            "total_jual": total_jual,

            "keuntungan": total_keuntungan_input,

            "status": status
        })

        st.success("Distribusi berhasil disimpan")

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

    data_tampil = []

    for trx in st.session_state.transaksi:

        produk_text = ""

        for item in trx["items"]:

            produk_text += (
                f"{item['produk']} "
                f"({item['qty']} pcs), "
            )

        data_tampil.append({

            "Tanggal": trx["tanggal"],
            "Nama": trx["nama"],
            "Produk": produk_text,
            "Qty": trx["qty"],
            "Omzet": trx["total_jual"],
            "Keuntungan": trx["keuntungan"],
            "Status": trx["status"]
        })

    df = pd.DataFrame(data_tampil)

    st.dataframe(
        df,
        use_container_width=True
    )

    # =================================================
    # DOWNLOAD CSV
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
# RINGKASAN
# =====================================================

st.markdown("""
<div class="card">
""", unsafe_allow_html=True)

st.markdown("## 📈 Ringkasan Pendapatan")

st.markdown(f"""
### 💵 Total Omzet
# Rp {total_omzet:,}

### 🟢 Total Keuntungan
# Rp {total_keuntungan:,}

### 📦 Total Produk Keluar
# {total_produk} pcs
""")

st.markdown("""
</div>
""", unsafe_allow_html=True)
