import src.app.helper as helper
import src.app.addData as addData
import main

productLists = []

def insertProductName():
    print("Ketik k dan tekan enter untuk membatalkan\n")
    productName = input("Nama produk: ")
    if productName != "":
        if productName == "k":
            main.run()
        else:
            insertProductPrice(productName)


def insertProductPrice(productName):
    productPrice = input("Harga product: ")
    if productPrice != "":
        productLists.append({
            "productName": productName,
            "productPrice": productPrice
        })
        showOption()


def showOption():
    val = input("Tekan s untuk simpan, t untuk tambah data baru dan tekan enter: ")
    if val == "s":
        addData.addData(productLists)
    elif val == "t":
        insertProductName()
    else:
        print("Pilihan yang anda masukan tidak ditemukan")
        showOption()


def run():
    productLists = []
    helper.clear()
    print("Silahkan masukan data produk anda!")
    insertProductName()