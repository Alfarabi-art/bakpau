# =====================================================
# FULL FIX - DISTRIBUTOR BAKPAU + STOK OTOMATIS
# TANPA FITUR MODAL
# =====================================================

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
    background:
    linear-gradient(rgba(0,0,0,0.72), rgba(0,0,0,0.72)),
    url("https://images.unsplash.com/photo-1569718212165-3a8278d5f624?q=80&w=1200");

    background-size:cover;
    background-position:center;
    background-attachment:fixed;
}

[data-testid="stHeader"]{
    background:transparent;
}

.block-container{
    padding-top:20px;
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

.metric-box{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.08);
    text-align:center;
    backdrop-filter:blur(10px);
}

.metric-title{
    color:#dddddd;
    font-size:18px;
}

.metric-value{
    color:white;
    font-size:36px;
    font-weight:bold;
}

.product-box{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    margin-bottom:25px;
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(10px);
}

.stButton button{
    width:100%;
    background:#ff4b4b;
    color:white;
    border:none;
    border-radius:14px;
    padding:14px;
    font-size:18px;
    font-weight:bold;
}

.stButton button:hover{
    background:#ff2e2e;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# DATA PRODUK + STOK
# =====================================================

produk_data = {

    "Bakpau Coklat": {
        "harga":5000,
        "stok":100,
        "gambar":"https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=1200"
    },

    "Bakpau Ayam": {
        "harga":7000,
        "stok":80,
        "gambar":"https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1200"
    },

    "Bakpau Kacang Hijau": {
        "harga":6000,
        "stok":70,
        "gambar":"https://images.unsplash.com/photo-1526318896980-cf78c088247c?q=80&w=1200"
    },

    "Bakpau Keju": {
        "harga":8000,
        "stok":50,
        "gambar":"https://images.unsplash.com/photo-1569718212165-3a8278d5f624?q=80&w=1200"
    }

}

# =====================================================
# SESSION
# =====================================================

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

if "stok_produk" not in st.session_state:
    st.session_state.stok_produk = {
        nama: data["stok"]
        for nama, data in produk_data.items()
    }

# =====================================================
# HEADER
# =====================================================

st.title("🥟 Distributor Bakpau")
st.subheader("Sistem Distribusi & Pendapatan UMKM")

st.write("")

# =====================================================
# TOTAL DASHBOARD
# =====================================================

total_omzet = sum(
    x["Total Omzet"]
    for x in st.session_state.riwayat
)

total_produk = sum(
    x["Total Qty"]
    for x in st.session_state.riwayat
)

total_transaksi = len(
    st.session_state.riwayat
)

# =====================================================
# DASHBOARD
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:

    st.markdown(f"""
    <div class="metric-box">
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
    <div class="metric-box">
        <div class="metric-title">
            📦 Produk Keluar
        </div>

        <div class="metric-value">
            {total_produk} pcs
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-title">
            🧾 Total Transaksi
        </div>

        <div class="metric-value">
            {total_transaksi}
        </div>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# STOK PRODUK
# =====================================================

st.write("")
st.markdown("## 📦 Stok Produk")

stok_df = pd.DataFrame({

    "Produk":
    list(st.session_state.stok_produk.keys()),

    "Sisa Stok":
    list(st.session_state.stok_produk.values())

})

st.dataframe(
    stok_df,
    use_container_width=True
)

# =====================================================
# FORM INPUT
# =====================================================

st.write("")
st.markdown("## 📋 Input Distribusi")

nama = st.text_input(
    "Nama Reseller"
)

status = st.selectbox(
    "Status Pembayaran",
    ["Belum Bayar", "Sudah Bayar"]
)

# =====================================================
# PRODUK
# =====================================================

st.write("")
st.markdown("## 🛒 Pilih Produk")

produk_terpilih = []

for nama_produk, data in produk_data.items():

    stok_sekarang = st.session_state.stok_produk[nama_produk]

    st.markdown("""
    <div class="product-box">
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3,1])

    # =================================================
    # GAMBAR
    # =================================================

    with col1:

        st.image(
            data["gambar"],
            use_container_width=True
        )

        st.markdown(
            f"### {nama_produk}"
        )

        st.markdown(
            f"## Rp {data['harga']:,}"
        )

        # STOK
        if stok_sekarang <= 10:

            st.error(
                f"Stok tersisa {stok_sekarang}"
            )

        else:

            st.success(
                f"Stok tersedia {stok_sekarang}"
            )

    # =================================================
    # INPUT QTY
    # =================================================

    with col2:

        st.write("")
        st.write("")
        st.write("")

        qty = st.number_input(
            f"Qty {nama_produk}",
            min_value=0,
            max_value=stok_sekarang,
            step=1,
            key=nama_produk
        )

    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

    # =================================================
    # SIMPAN
    # =================================================

    if qty > 0:

        total_jual = qty * data["harga"]

        produk_terpilih.append({

            "Produk": nama_produk,
            "Qty": qty,
            "Total Jual": total_jual

        })

# =====================================================
# TOTAL
# =====================================================

grand_qty = sum(
    x["Qty"]
    for x in produk_terpilih
)

grand_jual = sum(
    x["Total Jual"]
    for x in produk_terpilih
)

# =====================================================
# RINGKASAN
# =====================================================

st.write("")
st.markdown("## 🧾 Ringkasan")

col1, col2 = st.columns(2)

with col1:

    st.success(f"""
    Total Produk

    {grand_qty} pcs
    """)

with col2:

    st.info(f"""
    Total Omzet

    Rp {grand_jual:,}
    """)

# =====================================================
# BUTTON SIMPAN
# =====================================================

st.write("")

if st.button("💾 Simpan Distribusi"):

    if nama == "":
        st.warning("Masukkan nama reseller")

    elif len(produk_terpilih) == 0:
        st.warning("Pilih minimal 1 produk")

    else:

        # KURANGI STOK
        for item in produk_terpilih:

            st.session_state.stok_produk[
                item["Produk"]
            ] -= item["Qty"]

        daftar_produk = []

        for item in produk_terpilih:

            daftar_produk.append(
                f"{item['Produk']} ({item['Qty']} pcs)"
            )

        gabungan_produk = ", ".join(
            daftar_produk
        )

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

            "Status":
            status

        })

        st.success(
            "Distribusi berhasil disimpan"
        )

        st.rerun()

# =====================================================
# RIWAYAT
# =====================================================

st.write("")
st.write("")

st.markdown("## 📊 Riwayat Distribusi")

if len(st.session_state.riwayat) == 0:

    st.info(
        "Belum ada data distribusi"
    )

else:

    df = pd.DataFrame(
        st.session_state.riwayat
    )

    st.dataframe(
        df,
        use_container_width=True,
        height=400
    )

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "⬇️ Download CSV",
        csv,
        "laporan_distributor.csv",
        "text/csv"
    )
