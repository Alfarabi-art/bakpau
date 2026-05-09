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
# CSS
# =====================================================

st.markdown("""
<style>

.stApp{
    background-image:url("https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=1400");
    background-size:cover;
    background-position:center;
    background-attachment:fixed;
}

.main-card{
    background:rgba(0,0,0,0.55);
    padding:30px;
    border-radius:25px;
    backdrop-filter:blur(10px);
    margin-bottom:25px;
}

.metric-card{
    background:rgba(255,255,255,0.08);
    padding:25px;
    border-radius:20px;
    text-align:center;
    border:1px solid rgba(255,255,255,0.15);
}

.metric-title{
    color:#dddddd;
    font-size:18px;
    margin-bottom:10px;
}

.metric-value{
    color:white;
    font-size:36px;
    font-weight:bold;
}

.product-card{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    margin-bottom:20px;
    border:1px solid rgba(255,255,255,0.12);
}

.invoice-box{
    background:white;
    color:black;
    padding:30px;
    border-radius:20px;
}

.small-text{
    color:#cccccc;
    font-size:14px;
}

h1,h2,h3,h4,h5,h6{
    color:white !important;
}

label{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# DATA PRODUK
# =====================================================

produk_data = {
    "Bakpau Coklat": {
        "harga": 5000,
        "gambar": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=1000"
    },
    "Bakpau Ayam": {
        "harga": 7000,
        "gambar": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?q=80&w=1000"
    },
    "Bakpau Kacang Hijau": {
        "harga": 6000,
        "gambar": "https://images.unsplash.com/photo-1515003197210-e0cd71810b5f?q=80&w=1000"
    },
    "Bakpau Keju": {
        "harga": 8000,
        "gambar": "https://images.unsplash.com/photo-1490645935967-10de6ba17061?q=80&w=1000"
    }
}

# =====================================================
# SESSION
# =====================================================

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

if "invoice_terakhir" not in st.session_state:
    st.session_state.invoice_terakhir = None

# =====================================================
# HEADER
# =====================================================

st.markdown("""
<div class="main-card">

<h1 style="font-size:65px;">
🥟 Distributor Bakpau
</h1>

<p style="font-size:28px;color:#dddddd;">
Sistem Distribusi & Pendapatan UMKM
</p>

</div>
""", unsafe_allow_html=True)

# =====================================================
# METRIC
# =====================================================

df = pd.DataFrame(st.session_state.riwayat)

if len(df) > 0:
    total_omzet = df["Total"].sum()
    total_produk = df["Qty"].sum()
else:
    total_omzet = 0
    total_produk = 0

col1, col2 = st.columns(2)

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
            Total Produk Keluar
        </div>

        <div class="metric-value">
            {total_produk} pcs
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# =====================================================
# FORM INPUT
# =====================================================

st.markdown("""
<div class="main-card">
<h2>🛒 Input Pengambilan Produk</h2>
</div>
""", unsafe_allow_html=True)

nama = st.text_input("Nama Pengambil / Reseller")

status = st.selectbox(
    "Status Pembayaran",
    ["Belum Bayar", "Lunas"]
)

st.write("")

selected_items = []

for nama_produk, detail in produk_data.items():

    col1, col2 = st.columns([1.5, 1])

    with col1:
        st.image(detail["gambar"], use_container_width=True)

    with col2:

        st.markdown(f"""
        <div class="product-card">
            <h3>{nama_produk}</h3>
            <h2 style="color:#ffcc66;">
                Rp {detail['harga']:,}
            </h2>
        </div>
        """, unsafe_allow_html=True)

        qty = st.number_input(
            f"Qty {nama_produk}",
            min_value=0,
            step=1,
            key=nama_produk
        )

        if qty > 0:
            selected_items.append({
                "produk": nama_produk,
                "qty": qty,
                "harga": detail["harga"]
            })

st.write("")

# =====================================================
# SIMPAN
# =====================================================

if st.button("💾 Simpan Distribusi", use_container_width=True):

    if nama == "":
        st.warning("Masukkan nama reseller")
    elif len(selected_items) == 0:
        st.warning("Pilih minimal 1 produk")
    else:

        total_qty = 0
        total_omzet_invoice = 0
        daftar_produk = []

        for item in selected_items:

            subtotal = item["qty"] * item["harga"]

            total_qty += item["qty"]
            total_omzet_invoice += subtotal

            daftar_produk.append(
                f"{item['produk']} ({item['qty']} pcs)"
            )

            st.session_state.riwayat.append({
                "Tanggal": datetime.now().strftime("%d-%m-%Y %H:%M"),
                "Nama": nama,
                "Produk": item["produk"],
                "Qty": item["qty"],
                "Harga": item["harga"],
                "Total": subtotal,
                "Status": status
            })

        st.session_state.invoice_terakhir = {
            "Tanggal": datetime.now().strftime("%d-%m-%Y %H:%M"),
            "Nama": nama,
            "Produk": ", ".join(daftar_produk),
            "Total Qty": total_qty,
            "Total Omzet": total_omzet_invoice,
            "Status": status
        }

        st.success("Distribusi berhasil disimpan")

# =====================================================
# RIWAYAT
# =====================================================

if len(st.session_state.riwayat) > 0:

    st.write("")
    st.markdown("""
    <div class="main-card">
    <h2>📋 Riwayat Distribusi</h2>
    </div>
    """, unsafe_allow_html=True)

    df = pd.DataFrame(st.session_state.riwayat)

    st.dataframe(
        df,
        use_container_width=True
    )

# =====================================================
# INVOICE
# =====================================================

if st.session_state.invoice_terakhir is not None:

    invoice = st.session_state.invoice_terakhir

    st.write("")
    st.markdown("## 🧾 Invoice")

    st.markdown(f"""
    <div class="invoice-box">

        <h1 style="color:black;">
            🥟 Distributor Bakpau
        </h1>

        <hr>

        <p style="color:black;">
            <b>Tanggal:</b> {invoice['Tanggal']}
        </p>

        <p style="color:black;">
            <b>Nama:</b> {invoice['Nama']}
        </p>

        <p style="color:black;">
            <b>Status:</b> {invoice['Status']}
        </p>

        <hr>

        <h3 style="color:black;">
            Produk Diambil
        </h3>

        <p style="color:black;font-size:18px;">
            {invoice['Produk']}
        </p>

        <hr>

        <h2 style="color:black;">
            Total Produk: {invoice['Total Qty']} pcs
        </h2>

        <h1 style="
            color:#ff4b4b;
            font-size:42px;
        ">
            Rp {invoice['Total Omzet']:,}
        </h1>

    </div>
    """, unsafe_allow_html=True)
