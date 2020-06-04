from collections import Counter


class ConVat:
    def __init__(self):
        self.ho = ""
        self.namSinh = 0
        self.moiTruongSong = ""

    def getHo(self):
        return self.ho

    def getNamSinh(self):
        return self.namSinh

    def getMoiTruongSong(self):
        return self.moiTruongSong

    def setHo(self, ho):
        self.ho = ho

    def setNamSinh(self, namSinh):
        self.namSinh = namSinh

    def setMoiTruongSong(self, moiTruongSong):
        self.moiTruongSong = moiTruongSong

    def inputData(self):
        print("Nhập vào thông tin con vật")
        self.ho = input("Nhập vào Họ: ")
        self.namSinh = input("Nhập vào Năm Sinh: ")
        self.moiTruongSong = input("Nhập vào môi trường sống: ")

    def __str__(self):
        return "Ho: {} Năm Sinh: {} Môi Trường Sống: {}".format(self.ho, self.namSinh, self.moiTruongSong)


class ThuCung(ConVat):
    def __init__(self):
        self.ma = 0
        self.ten = ""
        self.giong = ""

    def getMa(self):
        return self.ma

    def getTen(self):
        return self.ten

    def getGiong(self):
        return self.giong

    def setMa(self, ma):
        self.ma = ma

    def setTen(self, ten):
        self.ten = ten

    def setGiong(self, giong):
        self.giong = giong

    def inputData(self):
        print("Nhập vào thông tin con vật")
        self.ma = input("Nhập vào Mã: ")
        self.ten = input("Nhập vào Tên: ")
        self.giong = input("Nhập vào Giống: ")
        self.ho = input("Nhập vào Họ: ")
        self.namSinh = input("Nhập vào Năm Sinh: ")
        self.moiTruongSong = input("Nhập vào môi trường sống: ")

    def setData(self, ho, namSinh, moiTruongSong, ma, ten, giong):
        self.ho = ho
        self.namSinh = namSinh
        self.moiTruongSong = moiTruongSong
        self.ma = ma
        self.ten = ten
        self.giong = giong

    def __str__(self):
        return """Mã: {}
Tên: {}
Giống: {}
Ho: {}
Năm Sinh: {}
Môi Trường Sống: {}
""".format(self.ma, self.ten, self.giong, self.ho, self.namSinh, self.moiTruongSong,)


class QuanLy():
    def __init__(self):
        self.arrThuCung = []

    def them(self):
        thucung = ThuCung()
        thucung.inputData()
        self.arrThuCung.append(thucung)

    def xoa(self, ma):
        for x in self.arrThuCung:
            if x.getMa() == ma:
                self.arrThuCung.remove(x)

    def xem(self, ma):
        for x in self.arrThuCung:
            if x.getMa() == ma:
                print(x)

    def thongKe(self):
        arr = []
        for x in self.arrThuCung:
            arr.append(x.getHo())
        print(Counter(arr))

    def ghiFile(self):
        file = open("thucung1.txt", "w+", encoding="utf-8")
        strGhiFile = "STT,  Ma, Ten,    Giong,  Ho, Nam sinh,   Moi truong"
        file.write(strGhiFile)
        for x in range(len(self.arrThuCung)):
            strData = "\n{} {} {} {} {} {} {}".format(x+1, self.arrThuCung[x].getMa(), self.arrThuCung[x].getTen(), self.arrThuCung[
                x].getGiong(), self.arrThuCung[x].getHo(), self.arrThuCung[x].getNamSinh(), self.arrThuCung[x].getMoiTruongSong())
            file.write(strData)
        file.close()

    def docFile(self):
        file = open("thucung.txt", "r")
        fileData = file.readlines()
        for x in range(1, len(fileData)):
            data = fileData[x].split(" ")
            thucung = ThuCung()
            thucung.setData(data[0], data[1], data[2],
                            data[3], data[4], data[5])
            self.arrThuCung.append(thucung)


if __name__ == "__main__":
    quanly = QuanLy()
    while True:
        print("""1.Thêm
2.Xoá
3.Xem thú theo mã
4.Thông kê số lượng theo họ
5.Ghi file
6.Đọc file """)
        num = int(input("Chọn chức năng: "))
        if num == 1:
            quanly.them()
        elif num == 2:
            num = input("Nhập mã thú muốn xoá: ")
            quanly.xoa(num)
        elif num == 3:
            num = input("Nhập mã thú muốn xem: ")
            quanly.xem(num)
        elif num == 4:
            quanly.thongKe()
        elif num == 5:
            quanly.ghiFile()
        elif num == 6:
            quanly.docFile()
