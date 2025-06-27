
def transaksi():
    produk = {"Laptop", "Smartphone", "Tablet" , "Smartwatch",
            "Headphone" }
    harga = {5500000 :"Laptop", 3000000:"Smartphone", 2000000 : "Tablet", 1500000 : "Smartwatch" , 500000 :"Headphone" }
    total_pembelian = 0
    while True:
        print("Masukin Data dulu masseh")
        nama = input("Masukkan nama :")
        umur = int(input("Masukkan Umur :"))
        member = input("Apakah mempunyai member(iya/tidak) :")
        gadget = input("Gadget yang ingin dibeli :")
        jumlah_unit = int(input("Masukkan jumlah unit yang ingin dibeli :"))
        nawar = input("Apakah ingin melakukan penawaran(iya/tidak)")
        total_pembelian = jumlah_unit * harga
        if umur <= 17 and  total_pembelian >= 3000000:
            print("Maaf anda belum cukup umur untuk membeli produk ini")
            break
        if gadget == "Laptop":
            gadget == produk[0] and harga[0] 

        def cek_penawaran():
            if nawar == "iya":
                terima = input("Terima tawaran?")
                if terima == "iya":
                    hasil_nawar = total_pembelian - nawar
                elif terima == "tidak":
                    print("Penawaran ditolak, Harga Asli digunakan")
                elif nawar >= 0.80:
                    print("Penawaran Ditolak, Harga Asli digunakan")
                else:
                    print("Penawaran tidak ditemukan")
            elif nawar == "tidak":
                pass
            else:
                print("yasudah")
        def hitung_diskon():
            if member == "iya" and total_pembelian > 10000000:
                
                total_pembelian * 0.10
            elif member == "iya" and total_pembelian >5000000:
                total_pembelian * 0.5
            elif member == "tidak":
                print("Maaf anda tidak punya member")
        print("====STRUK PEMBELIAN====")
        print("NAMA     :", nama)
        print("Usia     :", umur)
        print("Produk yang dibeli :", gadget)
        print("Jumlah unit  :", jumlah_unit)
        # print("Harga/Unit :",)
        # print("Diskon :")
        print("Total Akhir :", total_pembelian)
        print("==========================")
        cek = input("Apkah ingin melakukan pembelian lain(ya/tidak)")
        if cek == "ya":
            continue
        elif cek == "tidak":
            break
        else:
            print("Format tidak ditemukan!!")

transaksi()
        
    




