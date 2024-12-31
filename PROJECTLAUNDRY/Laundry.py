import streamlit as st
import Home
import Layanan
import Menghitung
import Kelola

# Class untuk Layanan Laundry
class LaundryService:
    def __init__(self, name, price_per_kg):
        self.name = name
        self.price_per_kg = price_per_kg

    def calculate_cost(self, weight):
        return self.price_per_kg * weight

# Data layanan contoh
services = [
    LaundryService("Cuci kering (Dry Cleaning)", 4000),
    LaundryService("Setrika (Iron)", 5000),
    LaundryService("Cuci & Setrika (Wash & Iron)", 10000)
]

# Navigasi aplikasi
st.sidebar.title("Navigasi Aplikasi Laundry")
pages = ["Beranda", "Layanan", "Hitung Biaya", "Kelola Pesanan"]
selected_page = st.sidebar.radio("Pilih Halaman", pages)

# Routing halaman
if selected_page == "Beranda":
    Home.display_home()
elif selected_page == "Layanan":
    Layanan.display_services(services)
elif selected_page == "Hitung Biaya":
    Menghitung.calculate_order(services)
elif selected_page == "Kelola Pesanan":
    Kelola.manage_orders()
