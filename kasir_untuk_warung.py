import csv
from datetime import datetime

def simpan_transaksi(nama, harga, jumlah, diskon, subtotal):
    with open("transaksi.csv", "a", newline="", encoding="utf-8") as f:
        csv.writer(f).writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            nama, harga, jumlah, diskon, subtotal
        ])

print("=== KASIR MINI ===")

total_harga = 0
lanjut = "y"

while lanjut.lower() == "y":
    nama_barang = input("Masukkan nama barang: ")
    harga = float(input("Masukkan harga satuan (Rp): "))
    jumlah = int(input("Masukkan jumlah yang dibeli: "))

    subtotal = harga * jumlah

    diskon_persen = float(input("Masukkan diskon (%) untuk barang ini: "))
    
    if diskon_persen < 0: 
        print("Diskon tidak boleh negatif. Dianggap 0%.")
        diskon_persen = 0
    elif diskon_persen > 100:
        print("Diskon terlalu besar! Dianggap 100%.")
        diskon_persen = 100

    diskon = diskon_persen / 100
    total_diskon = subtotal * diskon
    total = subtotal - total_diskon
    total_harga += total

    simpan_transaksi(nama_barang, harga, jumlah, diskon, subtotal)

    print(f"Barang : {nama_barang}")
    print(f"Subtotal : Rp{subtotal:,.0f}")
    print(f"Diskon ({diskon_persen:.0f}%) : Rp{total_diskon:,.0f}")
    print(f"Total setelah diskon : Rp{total:,.0f}")

    lanjut = input("Apakah ingin menambah barang lagi? (y/n): ")

print("=== STRUK BELANJA ===")
print(f"Total yang harus dibayar: Rp{total_harga:,.0f}")
print("Terima kasih telah berbelanja!")