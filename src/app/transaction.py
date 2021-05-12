from typing import Any
import src.app.helper as helper
import time
import main

productLists = []

def initTransactionMenu():
    global productLists
    f = open("src/data/dataset.txt", "r")
    productLists = f.read().split(";")
    productLists.pop()

    print("Daftar produk:\n")
    idx = 1
    line = 1
    menu = ""
    dataLength = len(productLists)
    startNumberLeft = 1
    startNumberRight = 0
    if dataLength % 2 != 0:
        dataLength = (dataLength - 1) / 2
        startNumberRight = int(dataLength + 2)
    else:
        dataLength = dataLength / 2
        startNumberRight = int(dataLength + 1)

    for productList in productLists:
        products = productList.split(",")
        if line <= 2:
            if line == 1: # left
                if startNumberLeft < 10:
                    menu = menu + str(startNumberLeft) + ".  " + helper.addSpace(products[0]) + helper.currencyFormat(products[1]) + "     "
                else:
                    menu = menu + str(startNumberLeft) + ". " + helper.addSpace(products[0]) + helper.currencyFormat(products[1]) + "     "
                startNumberLeft += 1
            
            if line == 2: # right
                if startNumberRight < 10:
                    menu = menu + str(startNumberRight) + ".  " + helper.addSpace(products[0]) + helper.currencyFormat(products[1]) + "     "
                else:
                    menu = menu + str(startNumberRight) + ". " + helper.addSpace(products[0]) + helper.currencyFormat(products[1]) + "     "
                line = 0
                menu = menu + "\n"
                startNumberRight += 1

        idx += 1
        line += 1

    print(menu)
    addProduct()


def addProduct():
    global productLists
    print("\nKetik k dan tekan enter untuk membatalkan")
    val = input("Masukan nomor produk: ")
    productLength = len(productLists)

    leftSideLength = 0
    if productLength % 2 != 0:
        dataLength = (productLength - 1) / 2
        leftSideLength = int(dataLength + 1)
    else:
        leftSideLength = int(productLength / 2)

    if val == "k":
        main.run()
    else:
        val = int(val)
        if val > 0 and val <= productLength:
            if val <= leftSideLength:
                idx = val + (val - 1)
                addQty(productLists[idx - 1])
            else:
                idx = val + (val - (productLength + 1))
                addQty(productLists[idx - 1])
        else:
            helper.clear()
            print("Produk tidak tersedia, harap pilih kembali\n")
            initTransactionMenu()


def addQty(products):
    global productLists
    val = input("Masukan jumlah pesanan: ")
    if int(val) > 0:
        with open("src/data/transaction.txt", "a") as f:
            f.writelines(products + "," + val + "," + str(time.time()) +  ";")
    else:
        print("Qty harus lebih dari 0\n")
        addQty(products)
    
    returnToTransaction()


def run():
    helper.clear()
    initTransactionMenu()


def returnToTransaction():
    helper.clear()
    print("Simpan data berhasil!")
    initTransactionMenu()