import streamlit as st
import pandas as pd
from datetime import datetime

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="Distributor Bakpau",
    page_icon="🥟",
    layout="wide"
)

# =========================================================
# CSS
# =========================================================

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

h1,h2,h3,h4,h5,h6,label,p{
    color:white !important;
}

.box{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    margin-bottom:20px;
    border:1px solid rgba(255,255,255,0.08);
    backdrop-filter:blur(10px);
}

.stButton button{
    width:100%;
    background:#ff4b4b;
    color:white;
    border:none;
    border-radius:12px;
    padding:14px;
    font-size:16px;
    font-weight:bold;
}

.stButton button:hover{
    background:#ff2e2e;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA PRODUK
# =========================================================

produk_data = {

    "Bakpau Coklat": {
        "modal":3000,
        "jual":5000,
        "gambar":"https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=1200"
    },

    "Bakpau Ayam": {
        "modal":4000,
        "jual":7000,
        "gambar":"https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1200"
    },

    "Bakpau Kacang Hijau": {
        "modal":3500,
        "jual":6000,
        "gambar":"https://images.unsplash.com/photo-1526318896980-cf78c088247c?q=80&w=1200"
    },

    "Bakpau Keju": {
        "modal":5000,
        "jual":8000,
        "gambar":"https://images.unsplash.com/photo-1569718212165-3a8278d5f624?q=80&w=1200"
    }

}

# =========================================================
# SESSION
# =========================================================

if "riwayat" not in st.session_state:
    st.session_state.riwayat = []

# =========================================================
# HEADER
# =========================================================

st.title("🥟 Distributor Bakpau")
st.subheader("Sistem Distribusi & Pendapatan UMKM")

st.write("")

# =========================================================
# TOTAL SEMUA DATA
# =========================================================

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

# =========================================================
# DASHBOARD
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Total Omzet",
        f"Rp {total_omzet:,}"
    )

with col2:
    st.metric(
        "📈 Total Keuntungan",
        f"Rp {total_profit:,}"
    )

with col3:
    st.metric(
        "📦 Produk Keluar",
        f"{total_produk} pcs"
    )

# =========================================================
# FORM INPUT
# =========================================================

st.write("")
st.markdown("## 📋 Input Distribusi")

nama = st.text_input(
    "Nama Reseller"
)

status = st.selectbox(
    "Status Pembayaran",
    ["Belum Bayar", "Sudah Bayar"]
)

# =========================================================
# PRODUK DENGAN GAMBAR
# =========================================================

st.write("")
st.markdown("## 🛒 Pilih Produk")

produk_terpilih = []

for nama_produk, data in produk_data.items():

    st.markdown("""
    <div class="box">
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([2,1])

    # =====================================================
    # GAMBAR
    # =====================================================

    with col1:

        st.image(
            data["gambar"],
            use_container_width=True
        )

        st.markdown(f"""
        ### {nama_produk}
        """)

        st.markdown(f"""
        ## Rp {data['jual']:,}
        """)

    # =====================================================
    # INPUT QTY
    # =====================================================

    with col2:

        st.write("")
        st.write("")
        st.write("")

        qty = st.number_input(
            f"Qty {nama_produk}",
            min_value=0,
            step=1,
            key=nama_produk
        )

    st.markdown("""
    </div>
    """, unsafe_allow_html=True)

    # =====================================================
    # HITUNG
    # =====================================================

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

# =========================================================
# TOTAL TRANSAKSI
# =========================================================

grand_qty = sum(
    x["Qty"]
    for x in produk_terpilih
)

grand_modal = sum(
    x["Total Modal"]
    for x in produk_terpilih
)

grand_jual = sum(
    x["Total Jual"]
    for x in produk_terpilih
)

grand_profit = sum(
    x["Keuntungan"]
    for x in produk_terpilih
)

# =========================================================
# RINGKASAN
# =========================================================

st.write("")
st.markdown("## 🧾 Ringkasan")

col1, col2, col3 = st.columns(3)

with col1:
    st.success(f"""
    Total Produk

    {grand_qty} pcs
    """)

with col2:
    st.info(f"""
    Omzet

    Rp {grand_jual:,}
    """)

with col3:
    st.warning(f"""
    Keuntungan

    Rp {grand_profit:,}
    """)

# =========================================================
# BUTTON SIMPAN
# =========================================================

st.write("")

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

            "Total Modal":
            grand_modal,

            "Total Omzet":
            grand_jual,

            "Keuntungan":
            grand_profit,

            "Status":
            status

        })

        st.success(
            "Distribusi berhasil disimpan"
        )

# =========================================================
# RIWAYAT
# =========================================================

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
