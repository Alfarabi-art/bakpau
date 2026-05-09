import streamlit as st
from datetime import datetime

# =====================================
# CONFIG
# =====================================

st.set_page_config(
    page_title="Kasir Bakpau",
    page_icon="🥟",
    layout="wide"
)

# =====================================
# BACKGROUND
# =====================================

background_image = "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1974&auto=format&fit=crop"

st.markdown(f"""
<style>

.stApp {{
    background-image: linear-gradient(
        rgba(0,0,0,0.55),
        rgba(0,0,0,0.55)
    ),
    url('{background_image}');
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.block-container {{
    padding-top: 2rem;
}}

h1, h2, h3, h4, h5, h6 {{
    color: white !important;
}}

p, label, span, div {{
    color: white;
}}

[data-testid="stNumberInput"] input {{
    background: rgba(255,255,255,0.95);
    border-radius: 12px;
}}

[data-testid="stSelectbox"] div {{
    border-radius: 12px;
}}

.stButton button {{
    width: 100%;
    border-radius: 14px;
    border: none;
    background: #e63946;
    color: white;
    font-weight: bold;
    padding: 12px;
    font-size: 16px;
}}

.stButton button:hover {{
    background: #c1121f;
}}

.receipt-box {{
    background: rgba(255,255,255,0.96);
    padding: 30px;
    border-radius: 20px;
    color: black;
}}

.cart-box {{
    background: rgba(255,255,255,0.14);
    padding: 20px;
    border-radius: 18px;
    backdrop-filter: blur(10px);
}}

.menu-card {{
    background: rgba(255,255,255,0.10);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(8px);
    margin-bottom: 20px;
}}

.menu-image {{
    width: 100%;
    border-radius: 18px;
}}

</style>
""", unsafe_allow_html=True)

# =====================================
# HEADER
# =====================================

header_html = """
<div style="
    display:flex;
    align-items:center;
    gap:20px;
    margin-bottom:30px;
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
            Kasir Bakpau
        </div>

        <div style="
            color:#dddddd;
            font-size:18px;
        ">
            Fresh & Warm Everyday
        </div>

    </div>

</div>
"""

st.markdown(header_html, unsafe_allow_html=True)

# =====================================
# DATA MENU
# =====================================

menu = [
    {
        "nama": "Bakpau Coklat",
        "harga": 5000,
        "gambar": "https://images.unsplash.com/photo-1544025162-d76694265947?q=80&w=1200&auto=format&fit=crop"
    },
    {
        "nama": "Bakpau Ayam",
        "harga": 7000,
        "gambar": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?q=80&w=1200&auto=format&fit=crop"
    },
    {
        "nama": "Bakpau Kacang Hijau",
        "harga": 6000,
        "gambar": "https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=1200&auto=format&fit=crop"
    },
    {
        "nama": "Bakpau Keju",
        "harga": 8000,
        "gambar": "https://images.unsplash.com/photo-1526318896980-cf78c088247c?q=80&w=1200&auto=format&fit=crop"
    }
]

# =====================================
# SESSION
# =====================================

if "cart" not in st.session_state:
    st.session_state.cart = []

# =====================================
# LAYOUT
# =====================================

col1, col2 = st.columns([1.2, 1])

# =====================================
# MENU
# =====================================

with col1:

    st.markdown("## 🍽️ Menu Bakpau")

    for i, item in enumerate(menu):

        st.markdown(f"""
        <div class="menu-card">
            <img src="{item['gambar']}" class="menu-image">
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"### {item['nama']}")
        st.markdown(f"### Rp {item['harga']:,}")

        qty = st.number_input(
            f"Qty {item['nama']}",
            min_value=1,
            value=1,
            key=f"qty_{i}"
        )

        if st.button(f"Tambah {item['nama']}", key=f"btn_{i}"):

            st.session_state.cart.append({
                "nama": item["nama"],
                "harga": item["harga"],
                "qty": qty,
                "subtotal": item["harga"] * qty
            })

            st.success(f"{item['nama']} ditambahkan")

# =====================================
# KERANJANG
# =====================================

with col2:

    st.markdown("## 🛒 Keranjang")

    total = 0

    if len(st.session_state.cart) == 0:

        st.markdown("""
        <div class="cart-box">
            Belum ada pesanan
        </div>
        """, unsafe_allow_html=True)

    else:

        cart_html = '<div class="cart-box">'

        for item in st.session_state.cart:

            total += item["subtotal"]

            cart_html += f"""
            <div style="
                display:flex;
                justify-content:space-between;
                margin-bottom:15px;
                border-bottom:1px solid rgba(255,255,255,0.2);
                padding-bottom:10px;
            ">

                <div>
                    <div style="font-size:22px;font-weight:bold;">
                        {item['nama']}
                    </div>

                    <div style="color:#dddddd;">
                        {item['qty']} x Rp {item['harga']:,}
                    </div>
                </div>

                <div style="
                    font-size:22px;
                    font-weight:bold;
                ">
                    Rp {item['subtotal']:,}
                </div>

            </div>
            """

        cart_html += "</div>"

        st.markdown(cart_html, unsafe_allow_html=True)

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

    if st.button("🧾 Cetak Struk"):

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        items_html = ""

        for item in st.session_state.cart:

            items_html += f"""
            <div style="
                display:flex;
                justify-content:space-between;
                margin-bottom:12px;
            ">
                <div>
                    <b>{item['nama']}</b><br>
                    {item['qty']} x Rp {item['harga']:,}
                </div>

                <div>
                    Rp {item['subtotal']:,}
                </div>
            </div>
            """

        receipt_html = f"""
        <div class="receipt-box">

            <div style="text-align:center;">

                <div style="font-size:70px;">
                    🥟
                </div>

                <div style="
                    font-size:34px;
                    font-weight:bold;
                    color:#e63946;
                ">
                    TOKO BAKPAU
                </div>

                <div style="
                    color:gray;
                    margin-top:5px;
                ">
                    Fresh & Warm Everyday
                </div>

            </div>

            <hr>

            <div style="
                display:flex;
                justify-content:space-between;
                color:#555;
                margin-bottom:20px;
            ">
                <span>Tanggal</span>
                <span>{now}</span>
            </div>

            {items_html}

            <hr>

            <div style="
                display:flex;
                justify-content:space-between;
                margin-top:20px;
                font-size:20px;
                font-weight:bold;
            ">
                <span>TOTAL</span>
                <span>Rp {total:,}</span>
            </div>

            <div style="
                display:flex;
                justify-content:space-between;
                margin-top:10px;
            ">
                <span>PEMBAYARAN</span>
                <span>{payment}</span>
            </div>

            <div style="
                display:flex;
                justify-content:space-between;
                margin-top:10px;
            ">
                <span>TUNAI</span>
                <span>Rp {bayar:,}</span>
            </div>

            <div style="
                display:flex;
                justify-content:space-between;
                margin-top:10px;
                color:green;
                font-weight:bold;
            ">
                <span>KEMBALIAN</span>
                <span>Rp {kembali:,}</span>
            </div>

            <div style="
                text-align:center;
                margin-top:30px;
                color:#666;
            ">
                Terima Kasih 🙏<br>
                Selamat menikmati bakpau 🥟
            </div>

        </div>
        """

        st.markdown(receipt_html, unsafe_allow_html=True)
