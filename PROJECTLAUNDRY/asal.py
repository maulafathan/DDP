# Program Python untuk menghitung atau memasukkan jumlah kilo

def main():
    print("=== Program Penghitung Kilo ===")
    
    # Meminta pengguna memasukkan jumlah kilo
    try:
        jumlah_kilo = float(input("Masukkan jumlah kilo: "))
        
        # Menampilkan hasil
        print(f"Jumlah kilo yang Anda masukkan adalah: {jumlah_kilo} kg")
        
        # Contoh perhitungan sederhana
        harga_per_kilo = 15000  # Contoh harga per kilo dalam Rupiah
        total_harga = jumlah_kilo * harga_per_kilo
        print(f"Total harga untuk {jumlah_kilo} kg adalah: Rp {total_harga:,.2f}")
        
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

if __name__ == "__main__":
    main()