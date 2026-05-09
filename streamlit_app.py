import streamlit as st
from datetime import datetime

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="Kasir Bakpau",
    page_icon="🥟",
    layout="wide"
)

# =========================
# BACKGROUND
# =========================
page_bg = """
<style>

[data-testid="stAppViewContainer"]{
    background:
    linear-gradient(
        rgba(0,0,0,0.45),
        rgba(0,0,0,0.45)
    ),
    url("https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1600&auto=format&fit=crop");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

[data-testid="stHeader"]{
    background: rgba(0,0,0,0);
}

.block-container{
    padding-top: 2rem;
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white !important;
}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# =========================
# DATA MENU
# =========================
menu = [
    {
        "id": 1,
        "nama": "Bakpau Coklat",
        "harga": 5000,
        "gambar": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1200&auto=format&fit=crop"
    },
    {
        "id": 2,
        "nama": "Bakpau Ayam",
        "harga": 7000,
        "gambar": "https://images.unsplash.com/photo-1563245372-f21724e3856d?q=80&w=1200&auto=format&fit=crop"
    },
    {
        "id": 3,
        "nama": "Bakpau Kacang Hijau",
        "harga": 5000,
        "gambar": "https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=1200&auto=format&fit=crop"
    },
    {
        "id": 4,
        "nama": "Bakpau Keju",
        "harga": 6000,
        "gambar": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=1200&auto=format&fit=crop"
    }
]

# =========================
# SESSION STATE
# =========================
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

# =========================
# HEADER
# =========================
st.markdown("""
<h1 style='font-size:60px;'>
🥟 Kasir Bakpau
</h1>
""", unsafe_allow_html=True)

# =========================
# LAYOUT
# =========================
col1, col2 = st.columns([1.2, 1])

# =========================
# MENU
# =========================
with col1:

    st.markdown("## Menu Bakpau")

    for item in menu:

        with st.container(border=True):

            st.image(
                item["gambar"],
                use_container_width=True
            )

            st.markdown(
                f"""
                <h2 style='margin-top:15px;'>
                {item['nama']}
                </h2>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <h3 style='color:#FFD166;'>
                Rp {item['harga']:,}
                </h3>
                """,
                unsafe_allow_html=True
            )

            qty = st.number_input(
                f"Qty {item['nama']}",
                min_value=1,
                value=1,
                key=f"qty_{item['id']}"
            )

            if st.button(
                f"Tambah {item['nama']}",
                key=f"btn_{item['id']}",
                use_container_width=True
            ):

                subtotal = qty * item["harga"]

                st.session_state.keranjang.append({
                    "nama": item["nama"],
                    "qty": qty,
                    "harga": item["harga"],
                    "subtotal": subtotal
                })

                st.success(f"{item['nama']} ditambahkan")

# =========================
# KERANJANG
# =========================
with col2:

    st.markdown("## Keranjang")

    total = 0

    if len(st.session_state.keranjang) == 0:

        st.info("Belum ada pesanan")

    else:

        for item in st.session_state.keranjang:

            total += item["subtotal"]

            st.markdown(
                f"""
                <div style="
                    background:rgba(255,255,255,0.12);
                    padding:15px;
                    border-radius:15px;
                    margin-bottom:10px;
                    backdrop-filter:blur(6px);
                ">
                    <div style="
                        display:flex;
                        justify-content:space-between;
                        color:white;
                        font-size:18px;
                        font-weight:bold;
                    ">
                        <span>{item['nama']}</span>
                        <span>Rp {item['subtotal']:,}</span>
                    </div>

                    <div style="
                        color:#ddd;
                        margin-top:5px;
                    ">
                        {item['qty']} x Rp {item['harga']:,}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        f"""
        <h1 style='margin-top:30px;'>
        Total : Rp {total:,}
        </h1>
        """,
        unsafe_allow_html=True
    )

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

    # =========================
    # CETAK STRUK
    # =========================
    if st.button("Cetak Struk", use_container_width=True):

        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        detail = ""

        for item in st.session_state.keranjang:

            detail += f"""
            <div style="
                margin-bottom:15px;
            ">
                <div style="
                    font-weight:bold;
                    font-size:17px;
                    color:#222;
                ">
                    {item['nama']}
                </div>

                <div style="
                    display:flex;
                    justify-content:space-between;
                    margin-top:5px;
                    color:#555;
                ">
                    <span>
                        {item['qty']} x Rp {item['harga']:,}
                    </span>

                    <span>
                        Rp {item['subtotal']:,}
                    </span>
                </div>
            </div>
            """

        receipt_html = f"""
        <div style="
            background:white;
            padding:30px;
            border-radius:25px;
            color:black;
            box-shadow:0 10px 30px rgba(0,0,0,0.3);
            margin-top:20px;
        ">

            <div style="
                text-align:center;
                margin-bottom:25px;
            ">
                <div style="
                    font-size:60px;
                ">
                    🥟
                </div>

                <div style="
                    font-size:32px;
                    font-weight:bold;
                    color:#D62828;
                ">
                    TOKO BAKPAU
                </div>

                <div style="
                    color:gray;
                    margin-top:5px;
                ">
                    Fresh & Warm Every Day
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
                <span>{waktu}</span>
            </div>

            {detail}

            <hr>

            <div style="
                margin-top:20px;
                font-size:18px;
            ">

                <div style="
                    display:flex;
                    justify-content:space-between;
                    margin-bottom:10px;
                ">
                    <b>TOTAL</b>
                    <b>Rp {total:,}</b>
                </div>

                <div style="
                    display:flex;
                    justify-content:space-between;
                    margin-bottom:10px;
                ">
                    <span>PEMBAYARAN</span>
                    <span>{metode}</span>
                </div>

                <div style="
                    display:flex;
                    justify-content:space-between;
                    margin-bottom:10px;
                ">
                    <span>TUNAI</span>
                    <span>Rp {uang:,}</span>
                </div>

                <div style="
                    display:flex;
                    justify-content:space-between;
                    margin-bottom:10px;
                    color:green;
                    font-weight:bold;
                ">
                    <span>KEMBALIAN</span>
                    <span>Rp {kembalian:,}</span>
                </div>

            </div>

            <div style="
                text-align:center;
                margin-top:30px;
                color:#666;
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
