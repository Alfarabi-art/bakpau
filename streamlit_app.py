import streamlit as st
from datetime import datetime

# ====================================
# CONFIG
# ====================================
st.set_page_config(
    page_title="Kasir Bakpau",
    layout="wide"
)

# ====================================
# VIDEO BACKGROUND
# ====================================
VIDEO_URL = "https://cdn.coverr.co/videos/coverr-steaming-food-1567842363107?download=1080p"

# ====================================
# CSS
# ====================================
st.markdown(f"""
<style>

/* VIDEO BACKGROUND */
.video-container {{
    position: fixed;
    top:0;
    left:0;
    width:100%;
    height:100%;
    overflow:hidden;
    z-index:-100;
}}

.video-container video {{
    width:100%;
    height:100%;
    object-fit:cover;
    filter:brightness(0.35);
}}

/* GLOBAL */
.stApp {{
    background:transparent;
}}

[data-testid="stHeader"] {{
    background:rgba(0,0,0,0);
}}

h1,h2,h3,h4,h5,h6,p,label {{
    color:white !important;
}}

/* CARD */
div[data-testid="stVerticalBlockBorderWrapper"] {{
    background:rgba(255,255,255,0.10);
    backdrop-filter:blur(10px);
    border-radius:20px;
    border:1px solid rgba(255,255,255,0.10);
    padding:15px;
    margin-bottom:15px;
}}

/* BUTTON */
.stButton button {{
    width:100%;
    background:#dc2626;
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-size:16px;
    font-weight:bold;
}}

.stButton button:hover {{
    background:#b91c1c;
    color:white;
}}

/* INPUT */
.stNumberInput input {{
    background:white;
    color:black;
    border-radius:10px;
}}

.stSelectbox div[data-baseweb="select"] {{
    background:white;
    color:black;
    border-radius:10px;
}}

/* STRUK */
.struk {{
    background:white;
    color:black !important;
    padding:25px;
    border-radius:20px;
    box-shadow:0 8px 25px rgba(0,0,0,0.25);
}}

.struk * {{
    color:black !important;
}}

/* MOBILE */
@media(max-width:768px){{
    h1 {{
        font-size:30px !important;
        text-align:center;
    }}

    .struk {{
        padding:15px;
    }}
}}

</style>

<div class="video-container">
<video autoplay muted loop playsinline>
<source src="{VIDEO_URL}" type="video/mp4">
</video>
</div>

""", unsafe_allow_html=True)

# ====================================
# DATA MENU
# ====================================
menu = [
    {
        "id":1,
        "nama":"Bakpau Coklat",
        "harga":5000,
        "gambar":"https://i.postimg.cc/Xq1V5dFf/bakpau-coklat.jpg"
    },
    {
        "id":2,
        "nama":"Bakpau Ayam",
        "harga":7000,
        "gambar":"https://i.postimg.cc/mkL5Y9tt/bakpau-ayam.jpg"
    },
    {
        "id":3,
        "nama":"Bakpau Kacang Hijau",
        "harga":5000,
        "gambar":"https://i.postimg.cc/HnS2dnKq/bakpau-kacang.jpg"
    },
    {
        "id":4,
        "nama":"Bakpau Keju",
        "harga":6000,
        "gambar":"https://i.postimg.cc/Y0L7mYw5/bakpau-keju.jpg"
    }
]

# ====================================
# SESSION
# ====================================
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

# ====================================
# TITLE
# ====================================
st.title("🥟 Kasir Bakpau")

col1, col2 = st.columns(2)

# ====================================
# MENU
# ====================================
with col1:

    st.subheader("Menu Bakpau")

    for item in menu:

        with st.container(border=True):

            st.image(
                item["gambar"],
                use_container_width=True
            )

            st.write(f"## {item['nama']}")
            st.write(f"Rp {item['harga']:,}")

            qty = st.number_input(
                f"Qty {item['nama']}",
                min_value=1,
                value=1,
                key=f"qty_{item['id']}"
            )

            if st.button(
                f"Tambah {item['nama']}",
                key=f"btn_{item['id']}"
            ):

                ditemukan = False

                for k in st.session_state.keranjang:

                    if k["nama"] == item["nama"]:
                        k["qty"] += qty
                        ditemukan = True
                        break

                if not ditemukan:
                    st.session_state.keranjang.append({
                        "nama":item["nama"],
                        "harga":item["harga"],
                        "qty":qty
                    })

                st.success("Berhasil ditambahkan")

# ====================================
# KERANJANG
# ====================================
with col2:

    st.subheader("Keranjang")

    total = 0

    if len(st.session_state.keranjang) == 0:

        st.info("Belum ada pesanan")

    else:

        for item in st.session_state.keranjang:

            subtotal = item["harga"] * item["qty"]
            total += subtotal

            with st.container(border=True):

                st.write(f"### {item['nama']}")
                st.write(
                    f"{item['qty']} x Rp {item['harga']:,}"
                )

                st.write(
                    f"Subtotal : Rp {subtotal:,}"
                )

    st.write(f"# Total : Rp {total:,}")

    metode = st.selectbox(
        "Metode Pembayaran",
        ["Cash","QRIS","Transfer","E-Wallet"]
    )

    uang = st.number_input(
        "Jumlah uang diterima",
        min_value=0
    )

    kembalian = uang - total

    if uang > 0:

        if uang >= total:
            st.success(
                f"Kembalian : Rp {kembalian:,}"
            )
        else:
            st.error("Uang kurang")

    # ====================================
    # STRUK
    # ====================================
    if st.button("Cetak Struk"):

        if total == 0:

            st.warning("Keranjang kosong")

        elif uang < total:

            st.error("Pembayaran kurang")

        else:

            tanggal = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            html = f"""
<div class="struk">

<div style="text-align:center;">

<h2 style="margin:0;">
🥟 TOKO BAKPAU
</h2>

<div style="
color:gray;
font-size:14px;
margin-top:5px;
">
Fresh & Warm Bakpau
</div>

</div>

<hr>

<div style="
display:flex;
justify-content:space-between;
margin-bottom:15px;
font-size:14px;
">

<div>Tanggal</div>
<div>{tanggal}</div>

</div>

<hr>
"""

            for item in st.session_state.keranjang:

                subtotal = (
                    item["harga"]
                    * item["qty"]
                )

                html += f"""

<div style="
margin-bottom:15px;
padding-bottom:10px;
border-bottom:1px dashed #ccc;
">

<div style="
font-weight:bold;
margin-bottom:5px;
">
{item['nama']}
</div>

<div style="
display:flex;
justify-content:space-between;
">

<div>
{item['qty']} x Rp {item['harga']:,}
</div>

<div>
Rp {subtotal:,}
</div>

</div>

</div>
"""

            html += f"""

<div style="
display:flex;
justify-content:space-between;
font-weight:bold;
font-size:18px;
margin-top:20px;
">

<div>TOTAL</div>
<div>Rp {total:,}</div>

</div>

<div style="
display:flex;
justify-content:space-between;
margin-top:10px;
">

<div>PEMBAYARAN</div>
<div>{metode}</div>

</div>

<div style="
display:flex;
justify-content:space-between;
margin-top:10px;
">

<div>TUNAI</div>
<div>Rp {uang:,}</div>

</div>

<div style="
display:flex;
justify-content:space-between;
margin-top:10px;
color:green;
font-weight:bold;
font-size:18px;
">

<div>KEMBALIAN</div>
<div>Rp {kembalian:,}</div>

</div>

<hr style="margin:20px 0;">

<div style="
text-align:center;
color:gray;
font-size:14px;
">

Terima Kasih 🙏 <br>
Selamat Menikmati Bakpau 🥟

</div>

</div>
"""

            st.markdown(
                html,
                unsafe_allow_html=True
            )

            st.session_state.keranjang = []
