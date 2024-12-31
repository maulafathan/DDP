import streamlit as st

# Fungsi untuk menghitung biaya laundry
def calculate_order(services):
    st.title("Hitung Biaya Laundry")

    selected_service_name = st.selectbox("Pilih layanan", [service.name for service in services])
    selected_service = next(service for service in services if service.name == selected_service_name)

    weight = st.number_input("Masukkan berat pakaian (dalam kg):", min_value=1, step=1)

    if st.button("Hitung"):
        cost = selected_service.calculate_cost(weight)
        st.success(f"Total biaya untuk {selected_service_name} adalah: Rp {cost:.3f}")
