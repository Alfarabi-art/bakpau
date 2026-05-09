import streamlit as st
from datetime import datetime

# ==========================================
# CONFIG
# ==========================================
st.set_page_config(
    page_title="Kasir Bakpau",
    page_icon="🥟",
    layout="wide"
)

# ==========================================
# BACKGROUND & STYLE
# ==========================================
st.markdown("""
<style>

html, body, [class*="css"]{
    font-family: 'Poppins', sans-serif;
}

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

.stButton>button{
    background:#D62828;
    color:white;
    border:none;
    border-radius:12px;
    padding:12px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#B71C1C;
    color:white;
}

[data-testid="stNumberInput"] input{
    border-radius:12px;
}

[data-testid="stSelectbox"]{
    border-radius:12px;
}

@media (max-width: 768px){

    h1{
        font-size:38px !important;
    }

    .block-container{
        padding-top:1rem;
        padding-left:1rem;
        padding-right:1rem;
    }
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# DATA MENU
# ==========================================
menu = [
    {
        "id": 1,
        "nama": "Bakpau Coklat",
        "harga": 5000,
        "gambar": "https://images.unsplash.com/photo-1512058564366-18510be2db19?q=80&w=1200&auto=format&fit=crop"
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
        "gambar": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?q=80&w=1200&auto=format&fit=crop"
    },
    {
        "id": 4,
        "nama": "Bakpau Keju",
        "harga": 6000,
        "gambar": "https://images.unsplash.com/photo-1504674900247-0877df9cc836?q=80&w=1200&auto=format&fit=crop"
    }
]

# ==========================================
# SESSION STATE
# ==========================================
if "keranjang" not in st.session_state:
    st.session_state.keranjang = []

# ==========================================
# HEADER
# ==========================================
st.markdown("""
<h1 style='font-size:65px; font-weight:bold;'>
🥟 Kasir Bakpau
</h1>
""", unsafe_allow_html=True)

# ==========================================
# LAYOUT
# ==========================================
col1, col2 = st.columns([1.2, 1])

# ==========================================
# MENU
# ==========================================
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

                st.success(f"{item['nama']} berhasil ditambahkan")

# ==========================================
# KERANJANG
# ==========================================
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
                    padding:18px;
                    border-radius:18px;
                    margin-bottom:12px;
                    backdrop-filter:blur(8px);
                ">

                    <div style="
                        display:flex;
                        justify-content:space-between;
                        color:white;
                        font-size:20px;
                        font-weight:bold;
                    ">
                        <span>{item['nama']}</span>
                        <span>Rp {item['subtotal']:,}</span>
                    </div>

                    <div style="
                        color:#ddd;
                        margin-top:6px;
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

    # ==========================================
    # CETAK STRUK
    # ==========================================
    if st.button("Cetak Struk", use_container_width=True):

        waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        detail = ""

        for item in st.session_state.keranjang:

            detail += f"""
            <div style="
                margin-bottom:15px;
                padding-bottom:12px;
                border-bottom:1px dashed #ddd;
            ">

                <div style="
                    display:flex;
                    justify-content:space-between;
                    font-size:18px;
                    font-weight:bold;
                    color:#222;
                ">
                    <span>{item['nama']}</span>
                    <span>Rp {item['subtotal']:,}</span>
                </div>

                <div style="
                    color:#777;
                    margin-top:6px;
                    font-size:15px;
                ">
                    {item['qty']} x Rp {item['harga']:,}
                </div>

            </div>
            """

        receipt_html = f"""
        <div style="
            background:white;
            padding:35px;
            border-radius:28px;
            margin-top:20px;
            color:black;
            box-shadow:0 12px 35px rgba(0,0,0,0.35);
        ">

            <div style="
                text-align:center;
                margin-bottom:25px;
            ">

                <div style="
                    font-size:65px;
                ">
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
                    color:#777;
                    margin-top:5px;
                    font-size:15px;
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
                color:#555;
                font-size:15px;
            ">
                <span>Tanggal</span>
                <span>{waktu}</span>
            </div>

            {detail}

            <div style="
                margin-top:25px;
                padding-top:20px;
                border-top:2px dashed #ddd;
            ">

                <div style="
                    display:flex;
                    justify-content:space-between;
                    margin-bottom:12px;
                    font-size:22px;
                    font-weight:bold;
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
                    margin-bottom:10px;
                    color:green;
                    font-weight:bold;
                    font-size:19px;
                ">
                    <span>KEMBALIAN</span>
                    <span>Rp {kembalian:,}</span>
                </div>

            </div>

            <div style="
                text-align:center;
                margin-top:35px;
                color:#666;
                font-size:15px;
            ">
                Terima Kasih 🙏
                <br>
                Selamat menikmati bakpau 🥟
            </div>

        </div>
        """

        st.success("Struk berhasil dicetak")

        # PENTING
        st.markdown(
            receipt_html,
            unsafe_allow_html=True
        )
