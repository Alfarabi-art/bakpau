import streamlit as st
from datetime import datetime

# =========================================
# CONFIG
# =========================================
st.set_page_config(
    page_title="Kasir Bakpau",
    page_icon="🥟",
    layout="wide"
)

# =========================================
# SESSION STATE
# =========================================
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

# =========================================
# DATA MENU
# =========================================
menu = [
    {
        "nama": "Bakpau Coklat",
        "harga": 5000,
        "gambar": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1200&auto=format&fit=crop"
    },
    {
        "nama": "Bakpau Ayam",
        "harga": 7000,
        "gambar": "https://images.unsplash.com/photo-1563245372-f21724e3856d?q=80&w=1200&auto=format&fit=crop"
    },
    {
        "nama": "Bakpau Kacang Hijau",
        "harga": 6000,
        "gambar": "https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=1200&auto=format&fit=crop"
    },
    {
        "nama": "Bakpau Keju",
        "harga": 8000,
        "gambar": "https://images.unsplash.com/photo-1544025162-d76694265947?q=80&w=1200&auto=format&fit=crop"
    }
]

# =========================================
# BACKGROUND + STYLE
# =========================================
st.markdown("""
<style>

.stApp {
    background:
    linear-gradient(rgba(0,0,0,0.55), rgba(0,0,0,0.55)),
    url("https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1600&auto=format&fit=crop");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

/* HIDE STREAMLIT */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* TEXT */
h1, h2, h3, h4, h5, h6, p, label {
    color:white !important;
}

/* INPUT */
.stNumberInput input,
.stSelectbox select,
.stTextInput input {
    border-radius:15px !important;
}

/* BUTTON */
.stButton button {
    width:100%;
    border:none;
    border-radius:16px;
    background:#D62828;
    color:white;
    font-weight:bold;
    padding:12px;
    font-size:18px;
    transition:0.3s;
}

.stButton button:hover {
    background:#a61c1c;
    transform:scale(1.02);
}

/* MOBILE */
@media(max-width:768px){

    .stApp{
        background-attachment:scroll;
    }

    h1{
        font-size:34px !important;
    }

    h2{
        font-size:28px !important;
    }

}

</style>
""", unsafe_allow_html=True)

# =========================================
# HEADER
# =========================================
st.markdown("""
<div style="
    display:flex;
    align-items:center;
    gap:20px;
    margin-bottom:30px;
">
    <div style="font-size:70px;">🥟</div>

    <div>
        <div style="
            color:white;
            font-size:60px;
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

# =========================================
# LAYOUT
# =========================================
col1, col2 = st.columns([1.1, 1])

# =========================================
# MENU
# =========================================
with col1:

    st.markdown("## Menu Bakpau")

    for i, item in enumerate(menu):

        with st.container():

            st.markdown(f"""
            <div style="
                background:rgba(255,255,255,0.08);
                backdrop-filter:blur(10px);
                border-radius:25px;
                padding:20px;
                margin-bottom:25px;
                border:1px solid rgba(255,255,255,0.15);
            ">
            """, unsafe_allow_html=True)

            st.image(item["gambar"])

            st.markdown(f"""
            <div style="
                color:white;
                font-size:38px;
                font-weight:bold;
                margin-top:15px;
            ">
                {item['nama']}
            </div>

            <div style="
                color:#FFD166;
                font-size:28px;
                font-weight:bold;
                margin-top:10px;
                margin-bottom:15px;
            ">
                Rp {item['harga']:,}
            </div>
            """, unsafe_allow_html=True)

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

                subtotal = qty * item["harga"]

                st.session_state.keranjang.append({
                    "nama": item["nama"],
                    "harga": item["harga"],
                    "qty": qty,
                    "subtotal": subtotal
                })

                st.success(f"{item['nama']} ditambahkan")

            st.markdown("</div>", unsafe_allow_html=True)

# =========================================
# KERANJANG
# =========================================
with col2:

    st.markdown("## Keranjang")

    total = 0

    if len(st.session_state.keranjang) == 0:

        st.info("Belum ada pesanan")

    else:

        for i, item in enumerate(st.session_state.keranjang):

            total += item["subtotal"]

            st.markdown(
                f"""
                <div style="
                    background:rgba(255,255,255,0.13);
                    padding:18px;
                    border-radius:20px;
                    margin-bottom:12px;
                    backdrop-filter:blur(10px);
                    border:1px solid rgba(255,255,255,0.15);
                ">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        align-items:center;
                    ">

                        <div>

                            <div style="
                                color:white;
                                font-size:22px;
                                font-weight:bold;
                            ">
                                {item['nama']}
                            </div>

                            <div style="
                                color:#dddddd;
                                margin-top:5px;
                                font-size:15px;
                            ">
                                {item['qty']} x Rp {item['harga']:,}
                            </div>

                        </div>

                        <div style="
                            color:#FFD166;
                            font-size:22px;
                            font-weight:bold;
                        ">
                            Rp {item['subtotal']:,}
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

    # =====================================
    # TOTAL
    # =====================================
    st.markdown(
        f"""
        <h1 style='
            color:white;
            margin-top:25px;
            margin-bottom:25px;
        '>
            Total : Rp {total:,}
        </h1>
        """,
        unsafe_allow_html=True
    )

    # =====================================
    # PEMBAYARAN
    # =====================================
    metode = st.selectbox(
        "Metode Pembayaran",
        ["Cash", "QRIS", "Transfer"]
    )

    uang = st.number_input(
        "Jumlah uang diterima",
        min_value=0,
        value=0
    )

    kembalian = uang - total

    if uang > 0:

        if kembalian >= 0:
            st.success(f"Kembalian : Rp {kembalian:,}")
        else:
            st.error("Uang kurang")

    # =====================================
    # CETAK STRUK
    # =====================================
    if st.button("Cetak Struk"):

        if len(st.session_state.keranjang) == 0:

            st.warning("Keranjang kosong")

        elif uang < total:

            st.error("Uang pembayaran kurang")

        else:

            waktu = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            detail_item = ""

            for item in st.session_state.keranjang:

                detail_item += f"""
                <div style="
                    padding:15px 0;
                    border-bottom:1px dashed #cccccc;
                ">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        font-weight:bold;
                        font-size:18px;
                    ">

                        <span>{item['nama']}</span>
                        <span>Rp {item['subtotal']:,}</span>

                    </div>

                    <div style="
                        color:#777;
                        margin-top:5px;
                        font-size:14px;
                    ">
                        {item['qty']} x Rp {item['harga']:,}
                    </div>

                </div>
                """

            receipt_html = f"""
            <div style="
                background:white;
                padding:35px;
                border-radius:25px;
                margin-top:25px;
                color:black;
                box-shadow:0 10px 30px rgba(0,0,0,0.35);
            ">

                <div style="text-align:center;">

                    <div style="font-size:70px;">
                        🥟
                    </div>

                    <div style="
                        font-size:34px;
                        font-weight:bold;
                        color:#D62828;
                    ">
                        TOKO BAKPAU
                    </div>

                    <div style="
                        color:#666;
                        margin-top:5px;
                        font-size:15px;
                    ">
                        Fresh & Warm Everyday
                    </div>

                </div>

                <hr style="
                    margin-top:25px;
                    margin-bottom:25px;
                ">

                <div style="
                    display:flex;
                    justify-content:space-between;
                    color:#555;
                    font-size:15px;
                    margin-bottom:20px;
                ">

                    <span>Tanggal</span>
                    <span>{waktu}</span>

                </div>

                {detail_item}

                <div style="
                    margin-top:25px;
                    padding-top:20px;
                    border-top:2px dashed #cccccc;
                ">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        font-size:24px;
                        font-weight:bold;
                        margin-bottom:15px;
                    ">

                        <span>TOTAL</span>
                        <span>Rp {total:,}</span>

                    </div>

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        margin-bottom:10px;
                        color:#555;
                    ">

                        <span>PEMBAYARAN</span>
                        <span>{metode}</span>

                    </div>

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        margin-bottom:10px;
                        color:#555;
                    ">

                        <span>TUNAI</span>
                        <span>Rp {uang:,}</span>

                    </div>

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        margin-top:18px;
                        font-size:22px;
                        font-weight:bold;
                        color:green;
                    ">

                        <span>KEMBALIAN</span>
                        <span>Rp {kembalian:,}</span>

                    </div>

                </div>

                <div style="
                    text-align:center;
                    margin-top:35px;
                    color:#777;
                    font-size:15px;
                ">
                    Terima Kasih 🙏
                    <br>
                    Selamat menikmati bakpau 🥟
                </div>

            </div>
            """

            st.success("Struk berhasil dicetak")

            st.markdown(
                receipt_html,
                unsafe_allow_html=True
            )
