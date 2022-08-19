# from os import system, name 
import os 
import barang
import lib.ui as ui
YangDibeli = []

# Bug cek_duplikasi

ui.clearCli()

def cek_duplikasi(triger):
    if int(len(YangDibeli)) > 0 :
        hasil = barang.cari(str(triger[0]),YangDibeli, True)
        if hasil:
            YangDibeli.pop(hasil[0])
            kuntitas = triger[3]
            triger.pop(3)
            kuntitas = int(kuntitas) + int(hasil[1][3])
            triger[3] = kuntitas
            return triger
    return triger

def handel_pilihan_kustom():
    dataKustom = ["===Kustom!==="]
    namaBarang = input("Apa nama barangnya?\n")
    hargaBarang = int(input("Berapa harga barangnya?\n"))
    kuantitasBarang = float(input("Berapa banyak yang dibeli?\n"))
    dataKustom.append(namaBarang)
    dataKustom.append(hargaBarang)
    dataKustom.append(kuantitasBarang)
    YangDibeli.append(dataKustom)

def handel_pilihan_basis_data():
    indeksPencarian = input("Masukan Nama Barang / ID-nya!\n")
    hasilPencarian = barang.cari(indeksPencarian)
    if hasilPencarian:
        kuantitasBarang = float(input("Berapa banyak yang dibeli?\n"))
        hasilPencarian.append(kuantitasBarang)
        YangDibeli.append(cek_duplikasi(hasilPencarian))
        # YangDibeli.append(hasilPencarian)
    else: 
        print("Maaf barang tidak terdaftar di basis data.")
        handel_pilihan_basis_data()

def penambahan_barang():
    tipeInput = input("Cari barang atau masukan kustom?\n(Cari isi 1, kustom isi 0)\n")
    if(int(tipeInput) == 1):
        handel_pilihan_basis_data()
    else: 
        handel_pilihan_kustom()
    ui.build(YangDibeli)
def tambahAkhiri():
    kataTAA = "Lanjut menambahakan barang(1) atau akhiri(0)?\n"
    tambahAtauAkhiri = int(input(kataTAA))
    while tambahAtauAkhiri == 1:
        penambahan_barang()
        tambahAtauAkhiri = int(input(kataTAA))
    if len(YangDibeli) < 1:
        utama()
    dihapus = int(input("Apa yang mau dihapus?\n(masukan 0 bila tidak ada)\n"))
    if dihapus > 0:
        YangDibeli.pop(dihapus-1)
        ui.build(YangDibeli)
        return tambahAkhiri()
    uangYgDibayar = int(input("Berapa uang yang dibayarkan?\n"))
    ui.build(YangDibeli,uangYgDibayar)
    return 0

def utama():
    print("Selamat Datang!")
    print("MESIN KASIR BASIS CLI 'CLIKAS'")
    print("Dibuat Oleh:")
    print("Muhammad Iqbal")
    print("(5312421026)")
    print("="*30)
    penambahan_barang()
    tambahAkhiri()

utama()