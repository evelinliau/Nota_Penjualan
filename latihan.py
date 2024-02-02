print("<< \tTOKO PENJUALAN XYZ\t >>")
print("-"*35)
nama_brg = input("Nama Barang\t = ")
hrg_brg = int(input("Harga Barang\t = Rp. "))
jumlah_brg = int(input("Jumlah Barang\t = "))

sub_total = hrg_brg * jumlah_brg
print("subtotal\t = Rp.",sub_total)

diskon = int(sub_total * 0.2)
print("diskon 20%\t = Rp.",diskon)

total_akhir = sub_total - diskon
print("Harga total\t = Rp.",total_akhir)

besar_bayar = int(input("Besar Bayar\t = Rp. "))


kembalian = besar_bayar - total_akhir
print("Kembalian Anda\t = Rp.",kembalian)

print(f"Kembalian\t= {kembalian:>5}")
RincianKembalian1 = kembalian // 50000
kembalian2 = kembalian % 50000
RincianKembalian2 = kembalian2 % 50000 // 20000
RincianKembalian3 = kembalian2 % 50000 % 20000 // 10000
RincianKembalian4 = kembalian2 % 50000 % 20000 % 10000 // 5000
RincianKembalian5 = kembalian2 % 50000 % 20000 % 10000 % 5000 // 2000
RincianKembalian6 = kembalian2 % 50000 % 20000 % 10000 % 5000 % 2000 // 1000
print("-"*35)
print("Rincian Kembalian")
print("-"*35)
print(f"Rp.50.000\t= {RincianKembalian1:>5}")
print(f"Rp.20.000\t= {RincianKembalian2:>5}")
print(f"Rp.10.000\t= {RincianKembalian3:>5}")
print(f"Rp.5.000\t= {RincianKembalian4:>5}")
print(f"Rp.2.000\t= {RincianKembalian5:>5}")
print(f"Rp.1.000\t= {RincianKembalian6:>5}")


