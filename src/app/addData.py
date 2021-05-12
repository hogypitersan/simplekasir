import src.app.helper as helper
import main

def addData(productLists):
    helper.clear()
    datas = []

    with open('src/data/dataset.txt', 'a') as f:
        for list in productLists:
            data = list["productName"] + "," + list["productPrice"] + ";"
            datas.append(data)

        f.writelines(datas)
    returnToMain()


def returnToMain():
    print("Simpan data berhasil!")
    main.initMainMenu()