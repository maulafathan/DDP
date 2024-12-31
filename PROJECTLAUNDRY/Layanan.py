import streamlit as st

# Fungsi untuk menampilkan layanan laundry
def display_services(services):
    st.title("Layanan Kami")
    st.write("Kami menyediakan layanan berikut:")

    for service in services:
        st.write(f"- {service.name}: Rp {service.price_per_kg}/kg")
