import streamlit as st
from datetime import datetime

# ======================================================
# CONFIG
# ======================================================

st.set_page_config(
    page_title="Kasir Bakpau",
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
    linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
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

/* BUTTON */
.stButton button{
    width:100%;
    border:none;
    border-radius:14px;
    background:#e63946;
    color:white;
    font-weight:bold;
    padding:12px;
    font-size:16px;
}

.stButton button:hover{
    background:#c1121f;
}

/* INPUT */
.stNumberInput input{
    border-radius:12px !important;
}

</style>
""", unsafe_allow_html=True)

# ======================================================
# HEADER
# ======================================================

st.markdown("""
# 🥟 Kasir Bakpau
### Fresh & Warm Everyday
""")

# ======================================================
# DATA MENU
# ======================================================

menu = [

    {
        "nama":"Bakpau Coklat",
        "harga":5000,
        "gambar":"https://images.unsplash.com/photo-1544025162-d76694265947?q=80&w=1200&auto=format&fit=crop"
    },

    {
        "nama":"Bakpau Ayam",
        "harga":7000,
        "gambar":"https://images.unsplash.com/photo-1569718212165-3a8278d5f624?q=80&w=1200&auto=format&fit=crop"
    },

    {
        "nama":"Bakpau Kacang Hijau",
        "harga":6000,
        "gambar":"https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=1200&auto=format&fit=crop"
    },

    {
        "nama":"Bakpau Keju",
        "harga":8000,
        "gambar":"https://images.unsplash.com/photo-1526318896980-cf78c088247c?q=80&w=1200&auto=format&fit=crop"
    }

]

# ======================================================
# SESSION STATE
# ======================================================

if "cart" not in st.session_state:
    st.session_state.cart = []

# ======================================================
# LAYOUT
# ======================================================

col1, col2 = st.columns([1.2,1])

# ======================================================
# MENU
# ======================================================

with col1:

    st.markdown("## 🍽️ Menu Bakpau")

    for i, item in enumerate(menu):

        with st.container():

            st.image(
                item["gambar"],
                use_container_width=True
            )

            st.markdown(f"## {item['nama']}")

            st.markdown(
                f"### Rp {item['harga']:,}"
            )

            qty = st.number_input(
                f"Qty {item['nama']}",
                min_value=1,
                value=1,
                key=f"qty_{i}"
            )

            if st.button(
                f"Tambah {item['nama']}",
                key=f"btn_{i}"
            ):

                st.session_state.cart.append({
                    "nama": item["nama"],
                    "harga": item["harga"],
                    "qty": qty,
                    "subtotal": item["harga"] * qty
                })

                st.success("Berhasil ditambahkan")

            st.divider()

# ======================================================
# KERANJANG
# ======================================================

with col2:

    st.markdown("## 🛒 Keranjang")

    total = 0

    if len(st.session_state.cart) == 0:

        st.info("Keranjang kosong")

    else:

        for item in st.session_state.cart:

            total += item["subtotal"]

            st.markdown(f"""
<div style="
background:rgba(255,255,255,0.10);
padding:18px;
border-radius:18px;
margin-bottom:15px;
backdrop-filter:blur(8px);
border:1px solid rgba(255,255,255,0.12);
">

<div style="
display:flex;
justify-content:space-between;
align-items:center;
">

<div>

<div style="
font-size:22px;
font-weight:bold;
color:white;
">
{item['nama']}
</div>

<div style="
color:#dddddd;
margin-top:5px;
font-size:16px;
">
{item['qty']} x Rp {item['harga']:,}
</div>

</div>

<div style="
font-size:22px;
font-weight:bold;
color:white;
">
Rp {item['subtotal']:,}
</div>

</div>

</div>
""", unsafe_allow_html=True)

    st.markdown(f"# Total : Rp {total:,}")

    payment = st.selectbox(
        "Metode Pembayaran",
        ["Cash", "QRIS", "Transfer"]
    )

    bayar = st.number_input(
        "Jumlah uang diterima",
        min_value=0,
        value=0
    )

    kembali = bayar - total

    # ======================================================
    # CETAK STRUK
    # ======================================================

    if st.button("🧾 Cetak Struk"):

        if total == 0:

            st.warning("Keranjang kosong")

        elif bayar < total:

            st.error("Uang belum cukup")

        else:

            tanggal = datetime.now().strftime(
                "%d-%m-%Y %H:%M:%S"
            )

            st.success("Struk berhasil dicetak")

            struk_html = f"""
<div style="
background:#ffffff;
padding:35px;
border-radius:25px;
color:#111;
box-shadow:0 15px 40px rgba(0,0,0,0.45);
margin-top:20px;
border:4px solid #ffb703;
">

<!-- HEADER -->

<div style="text-align:center;">

<div style="
font-size:85px;
margin-bottom:10px;
">
🥟
</div>

<div style="
font-size:42px;
font-weight:900;
color:#d62828;
letter-spacing:1px;
">
TOKO BAKPAU
</div>

<div style="
color:#666;
font-size:17px;
margin-top:8px;
font-weight:500;
">
Fresh & Warm Everyday
</div>

</div>

<hr style="
margin-top:25px;
margin-bottom:25px;
border:1px dashed #bbb;
">

<!-- INFO -->

<div style="
display:flex;
justify-content:space-between;
font-size:15px;
margin-bottom:10px;
color:#444;
">

<span><b>Tanggal</b></span>
<span>{tanggal}</span>

</div>

<hr style="
margin-top:15px;
margin-bottom:20px;
border:1px dashed #ddd;
">
"""

            # ======================================================
            # ITEM STRUK
            # ======================================================

            for item in st.session_state.cart:

                subtotal = item["harga"] * item["qty"]

                struk_html += f"""

<div style="
padding:14px;
margin-bottom:14px;
background:#fff8ef;
border-radius:15px;
border-left:6px solid #ffb703;
">

<div style="
font-size:20px;
font-weight:bold;
color:#222;
margin-bottom:8px;
">
{item['nama']}
</div>

<div style="
display:flex;
justify-content:space-between;
font-size:16px;
color:#444;
">

<div>
{item['qty']} x Rp {item['harga']:,}
</div>

<div style="
font-weight:bold;
color:#d62828;
">
Rp {subtotal:,}
</div>

</div>

</div>
"""

            # ======================================================
            # TOTAL
            # ======================================================

            struk_html += f"""

<hr style="
margin-top:20px;
margin-bottom:20px;
border:1px dashed #bbb;
">

<div style="
background:#fff3cd;
padding:20px;
border-radius:18px;
">

<div style="
display:flex;
justify-content:space-between;
font-size:26px;
font-weight:bold;
margin-bottom:18px;
color:#111;
">

<div>TOTAL</div>
<div>Rp {total:,}</div>

</div>

<div style="
display:flex;
justify-content:space-between;
font-size:18px;
margin-bottom:12px;
color:#333;
">

<div>PEMBAYARAN</div>
<div>{payment}</div>

</div>

<div style="
display:flex;
justify-content:space-between;
font-size:18px;
margin-bottom:12px;
color:#333;
">

<div>TUNAI</div>
<div>Rp {bayar:,}</div>

</div>

<div style="
display:flex;
justify-content:space-between;
font-size:30px;
font-weight:900;
color:green;
margin-top:20px;
">

<div>KEMBALIAN</div>
<div>Rp {kembali:,}</div>

</div>

</div>

<!-- FOOTER -->

<div style="
text-align:center;
margin-top:35px;
padding-top:20px;
border-top:2px dashed #ccc;
">

<div style="
font-size:22px;
font-weight:bold;
color:#d62828;
margin-bottom:10px;
">
🙏 Terima Kasih 🙏
</div>

<div style="
font-size:16px;
color:#666;
">
Selamat menikmati bakpau hangat 🥟
</div>

</div>

</div>
"""

            st.markdown(
                struk_html,
                unsafe_allow_html=True
            )

            # kosongkan keranjang
            st.session_state.cart = []
