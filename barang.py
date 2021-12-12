class list_barang:
    # list [nomor_id, nama_produk, harga]
    # range random 898000000000-899800000000
    list = [
        [893814795871,'Mie Instan', 2000], 
        [893317772299,'Minyak Goreng', 12000],
        [891661637357,'Sabun', 1500], 
        [893893929999,'Tepung Terigu', 7000],
        [893279211041,'Tepung Maizena', 8000],
        [890542936532,'Tepung Beras', 6000],
        [888817056135,'Telur Ayam', 20000], 
        [895576475144,'Telur Bebek', 21000],
        [888244474674,'Telur Asin', 3000],
        [888658144992,'Air Mineral L', 10000],
        [892227935562,'Air Mineral M', 6000],
        [888111558814,'Air Mineral S', 3000],
        [896461272156,'Buku Tulis', 1500],
        [893030280149,'Sampo Saset', 500],
        [891847933160,'Sampo Botol', 9000],
        [891903686090,'Pengaris Plastik', 1000],
        [895483399483,'Pengaris Metal', 5000],
        [897779460340,'Roti', 1000],
        [893700966595,'Pasta Gigi S', 2500],
        [891662091438,'Pasta Gigi M', 5000],
        [892920719459,'Pasta Gigi L', 8000],
        [895471550796,'Lanting S', 5000],
        [890216600245,'Lanting M', 9000],
        [892683501623,'Lanting L', 15000],
        [896501141509,'Keripik S', 6000],
        [897238282110,'Keripik M', 10000],
        [897862254807,'Keripik L', 16000],
        [895433283732,'Popok Bayi S', 3000],
        [892074736219,'Popok Bayi M', 150000],
        [892074736219,'Popok Bayi M', 150000],
        [888031051256,'Matrai 10.000', 11500],
        [888031051256,'Matrai 6.000', 7500],
    ]
def cari(input, list_yg_dicari = list_barang.list,printIndex = False):
    for i,x in enumerate(list_yg_dicari):
        if (str(x[0]) == input) or (x[1] == input) : 
            if(printIndex):
                return [i,x]
            return x
    return False
