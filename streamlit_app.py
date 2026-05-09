# =========================================================
# PRODUK
# =========================================================

st.write("")
st.markdown("## 🛒 Pilih Produk")

produk_terpilih = []

for nama_produk, data in produk_data.items():

    st.markdown("""
    <div style="
        background:rgba(255,255,255,0.08);
        padding:20px;
        border-radius:20px;
        margin-bottom:25px;
        border:1px solid rgba(255,255,255,0.1);
    ">
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([3,1])

    # =====================================================
    # KOLOM GAMBAR
    # =====================================================

    with col1:

        st.image(
            data["gambar"],
            use_container_width=True
        )

        st.markdown(
            f"### {nama_produk}"
        )

        st.markdown(
            f"## Rp {data['jual']:,}"
        )

    # =====================================================
    # KOLOM QTY
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

    st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # SIMPAN PRODUK
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
