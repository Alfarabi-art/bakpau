import streamlit as st
from datetime import datetime

# ======================================================
# PAGE CONFIG
# ======================================================

st.set_page_config(
    page_title="Kasir Bakpau",
    page_icon="🥟",
    layout="wide"
)

# ======================================================
# CSS
# ======================================================

background_image = "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1974&auto=format&fit=crop"

st.markdown(f"""
<style>

.stApp {{
    background-image:
        linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)),
        url("{background_image}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.block-container {{
    padding-top: 2rem;
}}

h1,h2,h3,h4,h5,h6,p,label {{
    color:white !important;
}}

.menu-card {{
    background: rgba(255,255,255,0.08);
    padding:20px;
    border-radius:20px;
    margin-bottom:25px;
    backdrop-filter: blur(10px);
}}

.menu-image {{
    width:100%;
    border-radius:20px;
}}

.cart-card {{
    background: rgba(255,255,255,0.12);
    padding:18px;
    border-radius:18px;
    margin-bottom:15px;
}}

.receipt {{
    background:white;
    color:black;
    padding:30px;
    border-radius:20px;
    margin-top:20px;
}}

.stButton button {{
    width:100%;
    border:none;
    border-radius:12px;
    background:#e63946;
    color:white;
    font-weight:bold;
    padding:12px;
}}

.stButton button:hover {{
    background:#c1121f;
}}

</style>
""", unsafe_allow_html=True)

# ======================================================
# HEADER
# ======================================================

st.markdown("""
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
""", unsafe_allow_html=True)

# ======================================================
# DATA MENU
# ======================================================

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

# ======================================================
# SESSION STATE
# ======================================================

if "cart" not in st.session_state:
    st.session_state.cart = []

# ======================================================
# LAYOUT
# ======================================================

col1, col2 = st.columns([1.2, 1])

# ======================================================
# MENU
# ======================================================

with col1:

    st.markdown("## 🍽️ Menu Bakpau")

    for i, item in enumerate(menu):

        st.markdown(f"""
        <div class="menu-card">

            <img src="{item['gambar']}" class="menu-image">

            <div style="margin-top:20px;">

                <div style="
                    font-size:32px;
                    font-weight:bold;
                    color:white;
                ">
                    {item['nama']}
                </div>

                <div style="
                    font-size:24px;
                    color:#ffd166;
                    font-weight:bold;
                    margin-top:10px;
                ">
                    Rp {item['harga']:,}
                </div>

            </div>

        </div>
        """, unsafe_allow_html=True)

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

            st.success(f"{item['nama']} berhasil ditambahkan")

# ======================================================
# KERANJANG
# ======================================================

with col2:

    st.markdown("## 🛒 Keranjang")

    total = 0

    if len(st.session_state.cart) == 0:

        st.info("Belum ada pesanan")

    else:

        for item in st.session_state.cart:

            total += item["subtotal"]

            st.markdown(f"""
            <div class="cart-card">

                <div style="
                    display:flex;
                    justify-content:space-between;
                    align-items:center;
                ">

                    <div>

                        <div style="
                            color:white;
                            font-size:24px;
                            font-weight:bold;
                        ">
                            {item['nama']}
                        </div>

                        <div style="
                            color:#dddddd;
                            margin-top:5px;
                        ">
                            {item['qty']} x Rp {item['harga']:,}
                        </div>

                    </div>

                    <div style="
                        color:#ffd166;
                        font-size:22px;
                        font-weight:bold;
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
    # STRUK
    # ======================================================

    if st.button("🧾 Cetak Struk"):

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        items_html = ""

        for item in st.session_state.cart:

            items_html += f"""
            <div style="
                display:flex;
                justify-content:space-between;
                margin-bottom:15px;
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
        <div class="receipt">

            <div style="text-align:center;">

                <div style="font-size:60px;">
                    🥟
                </div>

                <div style="
                    font-size:32px;
                    font-weight:bold;
                    color:#d62828;
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
                margin-top:15px;
                margin-bottom:25px;
                color:#444;
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
                font-size:22px;
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

        # PENTING
        st.markdown(receipt_html, unsafe_allow_html=True)
