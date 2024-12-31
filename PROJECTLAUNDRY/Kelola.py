import streamlit as st

# Fungsi untuk mengelola pesanan
def manage_orders():
    st.title("Kelola Pesanan")

    # State untuk menyimpan daftar pesanan
    if "orders" not in st.session_state:
        st.session_state.orders = []

    # Form untuk membuat pesanan baru
    with st.form("form_order"):
        customer_name = st.text_input("Masukkan nama pelanggan:")
        submitted = st.form_submit_button("Tambah Pesanan")

        if submitted and customer_name:
            order_id = len(st.session_state.orders) + 1
            st.session_state.orders.append({"id": order_id, "name": customer_name})
            st.success(f"Pesanan #{order_id} untuk {customer_name} telah ditambahkan.")

    # Tampilkan daftar pesanan
    st.write("Daftar Pesanan:")
    if st.session_state.orders:
        for order in st.session_state.orders:
            st.write(f"ID Pesanan: {order['id']}, Nama Pelanggan: {order['name']}")
    else:
        st.write("Belum ada pesanan.")
