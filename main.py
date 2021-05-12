import src.app.insertData as insertData
import src.app.helper as helper
import src.app.transaction as transaction

def initMainMenu():
    print("Selamat datang di simple kasir")
    print("Silahkan pilih menu dibawah ini:")
    print("1. Input data produk baru")
    print("2. Update data produk")
    print("3. Transaksi\n")
    menu = input("Silahkan masukan angka menu: ")
    if menu == "1":
        insertData.run()
    elif menu == "2":
        helper.clear()
        print("Menu", menu, "dalam tahap pengembangan\n")
        initMainMenu()
    elif menu == "3":
        transaction.run()
    else:
        val = input("Menu yang anda pilih tidak tersedia, tekan enter untuk memulai kembali...")
        if val == "":
            run()


def run():
    helper.clear()
    initMainMenu()


if __name__ == '__main__':
    run()
