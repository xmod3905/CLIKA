# from os import system, name 
import os 
import barang
import lib.ui as ui
YangDibeli = []

# Bug cek_duplikasi

os.system("clear")

# def cek_duplikasi(triger):
#     if len(triger) > 0:
#         hasil = barang.cari(triger[0],YangDibeli, True)
#         if hasil:
#             YangDibeli.pop(2)
#             triger.pop(3)
#             # triger.append(int(triger[3]) + int(hasil[3])) 
#             return triger
#     return triger

def handel_pilihan_kustom():
    dataKustom = ["===Kustom!==="]
    namaBarang = input("Apa nama barangnya?")
    hargaBarang = int(input("Berapa harga barangnya?"))
    kuantitasBarang = int(input("Berapa banyak yang dibeli?"))
    dataKustom.append(namaBarang)
    dataKustom.append(hargaBarang)
    dataKustom.append(kuantitasBarang)
    YangDibeli.append(dataKustom)

def handel_pilihan_basis_data():
    indeksPencarian = input("Masukan Nama Barang / ID-nya!")
    hasilPencarian = barang.cari(indeksPencarian)
    if hasilPencarian:
        kuantitasBarang = int(input("Berapa banyak yang dibeli?"))
        hasilPencarian.append(kuantitasBarang)
        # YangDibeli.append(cek_duplikasi(hasilPencarian))
        YangDibeli.append(hasilPencarian)
    else: 
        print("Maaf barang tidak terdaftar di basis data.")
        handel_pilihan_basis_data()

def penambahan_barang():
    tipeInput = input("Cari barang atau masukan kustom?\n(Cari isi 1, kustom isi 0)")
    if(int(tipeInput) == 1):
        handel_pilihan_basis_data()
    else: 
        handel_pilihan_kustom()
    ui.build(YangDibeli)

def utama():
    print("Selamat Datang!")
    print("MESIN KASIR BASIS CLI 'CLIKAS'")
    print("Dibuat Oleh:")
    print("Muhammad Iqbal")
    print("(5312421026)")
    print("="*30)
    penambahan_barang()
    kataTAA = "Lanjut menambahakan barang(1) atau akhiri(0)?"
    tambahAtauAkhiri = int(input(kataTAA))
    while tambahAtauAkhiri == 1:
        penambahan_barang()
        tambahAtauAkhiri = int(input(kataTAA))
    if len(YangDibeli) < 1:
        utama()
    uangYgDibayar = int(input("Berapa uang yang dibayarkan?"))
    ui.build(YangDibeli,uangYgDibayar)

utama()