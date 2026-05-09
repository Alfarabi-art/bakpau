import streamlit as st
from datetime import datetime

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Kasir Bakpau",
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
    linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
    url("https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1974&auto=format&fit=crop");

    background-size:cover;
    background-position:center;
    background-attachment:fixed;
}

.block-container{
    padding-top:2rem;
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

.menu-box{
    background:rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    margin-bottom:25px;
    backdrop-filter:blur(10px);
}

.cart-box{
    background:rgba(255,255,255,0.10);
    padding:18px;
    border-radius:18px;
    margin-bottom:15px;
    backdrop-filter:blur(8px);
}

.stButton button{
    width:100%;
    border:none;
    border-radius:12px;
    background:#e63946;
    color:white;
    font-weight:bold;
    padding:12px;
    font-size:16px;
}

.stButton button:hover{
    background:#c1121f;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER
# =====================================================

st.markdown("""
# 🥟 Kasir Bakpau
### Fresh & Warm Everyday
""")

# =====================================================
# DATA MENU
# =====================================================

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

# =====================================================
# SESSION STATE
# =====================================================

if "cart" not in st.session_state:
    st.session_state.cart = []

# =====================================================
# LAYOUT
# =====================================================

col1, col2 = st.columns([1.2,1])

# =====================================================
# MENU
# =====================================================

with col1:

    st.markdown("## 🍽️ Menu")

    for i, item in enumerate(menu):

        with st.container():

            st.markdown(
                '<div class="menu-box">',
                unsafe_allow_html=True
            )

            st.image(
                item["gambar"],
                use_container_width=True
            )

            st.markdown(
                f"### {item['nama']}"
            )

            st.markdown(
                f"## Rp {item['harga']:,}"
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

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

# =====================================================
# KERANJANG
# =====================================================

with col2:

    st.markdown("## 🛒 Keranjang")

    total = 0

    if len(st.session_state.cart) == 0:

        st.info("Keranjang kosong")

    else:

        for item in st.session_state.cart:

            total += item["subtotal"]

            st.markdown(
                '<div class="cart-box">',
                unsafe_allow_html=True
            )

            c1, c2 = st.columns([3,1])

            with c1:

                st.markdown(f"""
### {item['nama']}
{item['qty']} x Rp {item['harga']:,}
""")

            with c2:

                st.markdown(
                    f"### Rp {item['subtotal']:,}"
                )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

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

    # =====================================================
    # CETAK STRUK
    # =====================================================

    if st.button("🧾 Cetak Struk"):

        if total == 0:

            st.warning("Keranjang kosong")

        elif bayar < total:

            st.error("Uang belum cukup")

        else:

            tanggal = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            st.success("Struk berhasil dicetak")

            struk_html = f"""
<div style="
background:white;
padding:30px;
border-radius:25px;
color:black;
box-shadow:0 10px 30px rgba(0,0,0,0.3);
margin-top:20px;
">

<div style="text-align:center;">

<div style="
font-size:70px;
">
🥟
</div>

<h2 style="
margin:0;
font-size:34px;
color:#D62828;
">
TOKO BAKPAU
</h2>

<div style="
color:#666;
font-size:14px;
margin-top:5px;
">
Fresh & Warm Everyday
</div>

</div>

<hr style="margin:20px 0;">

<div style="
display:flex;
justify-content:space-between;
font-size:14px;
margin-bottom:15px;
color:#444;
">

<span>Tanggal</span>
<span>{tanggal}</span>

</div>

<hr style="margin:15px 0;">
"""

            # =====================================================
            # ITEM STRUK
            # =====================================================

            for item in st.session_state.cart:

                subtotal = (
                    item["harga"]
                    * item["qty"]
                )

                struk_html += f"""

<div style="
margin-bottom:18px;
padding-bottom:12px;
border-bottom:1px dashed #ccc;
">

<div style="
font-weight:bold;
font-size:16px;
margin-bottom:8px;
color:#222;
">
{item['nama']}
</div>

<div style="
display:flex;
justify-content:space-between;
font-size:15px;
color:#444;
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

            # =====================================================
            # TOTAL
            # =====================================================

            struk_html += f"""

<div style="margin-top:20px;">

<div style="
display:flex;
justify-content:space-between;
margin-bottom:10px;
font-size:18px;
">

<div><b>TOTAL</b></div>
<div><b>Rp {total:,}</b></div>

</div>

<div style="
display:flex;
justify-content:space-between;
margin-bottom:10px;
font-size:15px;
">

<div>PEMBAYARAN</div>
<div>{payment}</div>

</div>

<div style="
display:flex;
justify-content:space-between;
margin-bottom:10px;
font-size:15px;
">

<div>TUNAI</div>
<div>Rp {bayar:,}</div>

</div>

<div style="
display:flex;
justify-content:space-between;
font-size:20px;
font-weight:bold;
color:green;
">

<div>KEMBALIAN</div>
<div>Rp {kembali:,}</div>

</div>

</div>

<hr style="margin:20px 0;">

<div style="
text-align:center;
font-size:14px;
color:#666;
">

Terima Kasih 🙏 <br>
Selamat menikmati bakpau 🥟

</div>

</div>
"""

            st.markdown(
                struk_html,
                unsafe_allow_html=True
            )

            # kosongkan keranjang
            st.session_state.cart = []
