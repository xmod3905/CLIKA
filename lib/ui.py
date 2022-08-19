import os, locale, platform
locale.setlocale(locale.LC_ALL, '')

def clearCli():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

def penambahNol(input):
    input = str(input)
    panjang_input = len(input)
    if(panjang_input%2):
        return "0"+input
    return input

def pembuatSepasi(banyaknya):
    return ' ' * banyaknya 

def rapikan(input, panjang_tempat, tipe = "tengah"):
    input = str(input)
    selisih = panjang_tempat - len(input)
    if tipe == 'kanan':
        return pembuatSepasi(selisih)+input
    if tipe == 'kiri':
        return input + pembuatSepasi(selisih)
    selisih = round(selisih/2)
    return pembuatSepasi(selisih)+input+pembuatSepasi(selisih)
    
def build(list_barang, yangDibayarkan = 0):
    clearCli()
    header = "||"+rapikan("No", 6)+"|"+rapikan("ID Barang", 13)+"|"+rapikan("Nama Barang", 25)+"|"+rapikan("Harga Satuan", 16)+"|"+rapikan("Kuantitas Barang", 20)+"|"+rapikan("Total Harga", 15)+"||"
    print(rapikan("MESIN KASIR BASIS CLI 'CLIKAS'", len(header)))
    print(rapikan("Dibuat oleh", len(header)))
    print(rapikan("Muhammad Iqbal", len(header)))
    print(rapikan("(5312421026)", len(header)))
    print("="*len(header))
    print(header)
    print("-"*len(header))
    totalBayar = 0
    banyakBarang = 0
    for i,x in enumerate(list_barang):
        kuantitas = x[3]
        i+=1
        konten = "||"+rapikan(penambahNol(i), 6)+"|"+rapikan(x[0], 13, 'kiri')+"|"+rapikan(x[1], 25, 'kiri')+"|"+rapikan(locale.format_string("%d", int(x[2]), grouping=True), 16, 'kanan')+"|"+rapikan(penambahNol(kuantitas), 20)+"|"+rapikan(locale.format_string("%d", x[2]*kuantitas, grouping=True), 15, 'kanan')+"||"
        totalBayar += x[2]*kuantitas
        banyakBarang += x[3]
        print(konten)
    print("="*len(header))
    yangDibayarkan = int(yangDibayarkan)
    if yangDibayarkan > 0:
        kembalian = yangDibayarkan - totalBayar
        totalBayar = locale.format_string("%d", totalBayar, grouping=True)
        yangDibayarkan = locale.format_string("%d", yangDibayarkan, grouping=True)
        print(rapikan("Banyak Jenis Barang",20,"kiri"),":",len(list_barang),"Jenis")
        print(rapikan("Banyaknya Barang",20,"kiri"),":", banyakBarang,"Barang")
        print(rapikan("Total bayar",20,"kiri"),":","Rp.", rapikan(totalBayar, 15, "kanan")+ ",-")
        print(rapikan("Dibayarkan", 20, "kiri"),":","Rp.", rapikan(yangDibayarkan, 15, "kanan")+ ",-")
        msg = "Kembalian"
        if kembalian<0:
            kembalian*=(-1)
            msg = "Hutang"
        print(rapikan(msg, 20, "kiri"),":", "Rp.",rapikan(locale.format_string("%d", kembalian, grouping=True), 15, "kanan")+ ",-")
        print(rapikan("==Transaksi Selesai==", len(header)))
    else:
        print("Total bayar sementara:","Rp.", locale.format_string("%d", totalBayar, grouping=True)+ ",-")