def instruksi(): 
    print("Selamat datang di program kalkulator sederhana!") 
    print("Masukkan dua angka dan pilih operasi perhitungannya!")

instruksi()    
angka1 = float(input("Masukkan angka pertama: ")) 
angka2 = float(input("Masukkan angka kedua: "))
    
def penjumlahan(angka1, angka2): 
    return angka1 + angka2

def pengurangan(angka1, angka2): 
    return angka1 - angka2

def perkalian(angka1, angka2): 
    return angka1 * angka2

def pembagian(angka1, angka2): 
    return angka1 / angka2

operasi = int( 
    input( 
        "Pilih operasi yang anda inginkan. (1) Penjumlahan, (2) Pengurangan, (3) Perkalian, (4) Pembagian:"
    ))

if operasi == 1: 
    print("Hasil penjumlahan dari", angka1, "dan", angka2, "adalah", penjumlahan (angka1, angka2))
elif operasi == 2: 
    print("Hasil pengurangan dari", angka1, "dan", angka2, "adalah", pengurangan (angka1, angka2))
elif operasi == 3:
    print("Hasil perkalian dari", angka1, "dan", angka2, "adalah", perkalian (angka1, angka2))
elif operasi == 4:
    print("Hasil pembagian dari", angka1, "dan", angka2, "adalah", pembagian (angka1, angka2))
else:
    print("Operasi yang anda pilih tidak tersedia!")