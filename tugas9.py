def celcius_ke_fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

print(celcius_ke_fahrenheit(0))
print(celcius_ke_fahrenheit(100))


print('\n--- Mencari bilangan genap ---')
def is_genap(bil_genap):
    return bil_genap %2 == 0
# untuk mencetak value
print(is_genap(4))
print(is_genap(7)) 

print()
print('\n--- Mencari nilai rata rata ---')
# rata rata nilai 70
def nilai_kelulusan(nilai):
    if nilai >= 80:
       return 'Lulus'
    else :
       return 'Gagal'

# Untuk mencetak value
print(nilai_kelulusan(80))
print(nilai_kelulusan(60))

print('\n---- Cetak Bilangan Ganjil ---')
def bil_ganjil(angka):
    for i in range(1, angka, 2):
        print(i,end=" ")
# untuk memasukkan value
bil_ganjil(20)