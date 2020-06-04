from collections import Counter


class HocSinh():
    def __init__(self):
        self.maLop = ""
        self.tenLop = ""
        self.hoTen = ""
        self.ngaySinh = ""
        self.gioiTinh = ""

    def getMaLop(self):
        return self.maLop

    def getTenLop(self):
        return self.tenLop

    def getHoTen(self):
        return self.hoTen

    def getNgaySinh(self):
        return self.ngaySinh

    def getGioiTinh(self):
        return self.gioiTinh

    def setMaLop(self, maLop):
        self.maLop = maLop

    def setTenLop(self, tenLop):
        self.tenLop = tenLop

    def setHoTen(self, hoTen):
        self.hoTen = hoTen

    def setNgaySinh(self, ngaySinh):
        self.ngaySinh = ngaySinh

    def setGioiTinh(self, gioiTinh):
        self.gioiTinh = gioiTinh.lower()

    def AddHS(self):
        print("Nhập vào thông tin sinh viên\n")
        self.maLop = input("Nhập vào mã lớp: ")
        self.tenLop = input("Nhập vào tên lớp: ")
        self.hoTen = input("Nhập vào họ tên: ")
        self.ngaySinh = input("Nhập vào ngày sinh: ")
        self.gioiTinh = input("Nhập vào giới tính: ")

    def __str__(self):
        return "Mã lớp {} Tên lớp {} Họ tên {} Ngày sinh {}  Giới tính {}".format(self.maLop, self.tenLop, self.hoTen, self.ngaySinh, self.gioiTinh)


class QuanLyHocSinh():
    def __init__(self):
        self.arrHS = []

    def AddHS(self):
        while True:
            hocSinh = HocSinh()
            hocSinh.AddHS()
            self.arrHS.append(hocSinh)
            check = input("Bạn có muốn thêm sinh viên nữa không(y/n): ?")
            if check == "n":
                break

    def fileOutput(self):
        f = open("dshs.txt", "w")
        s = ""
        for i in range(len(self.arrHS)):
            s += "{} {} {} {} {}\n".format(self.arrHS[i].getMaLop(), self.arrHS[i].getTenLop(),
                                           self.arrHS[i].getHoTen(), self.arrHS[i].getNgaySinh(), self.arrHS[i].getGioiTinh())
        f.write(s)
        f.close()

    def fileInput(self):
        f = open("dshs0.txt", "r")
        fileData = f.readlines()
        for x in range(len(fileData)):
            data = fileData[x].split()
            hocSinh = HocSinh()
            hocSinh.setMaLop(data[0])
            hocSinh.setTenLop(data[1])
            hocSinh.setHoTen(data[2])
            hocSinh.setNgaySinh(data[3])
            hocSinh.setGioiTinh(data[4])
            self.arrHS.append(hocSinh)
        f.close()

    def thongKe(self):
        arrThongKe = []
        for x in range(len(self.arrHS)):
            arrThongKe.append(self.arrHS[x].getGioiTinh())
        c = Counter(arrThongKe)
        return "Nam : {} Nữ: {}".format(c["nam"], c["nu"])

    def thongKeLop(self):
        arrThongKeLop = []
        newList = []
        for x in range(len(self.arrHS)):
            arrThongKeLop.append(self.arrHS[x].getTenLop())
        [newList.append(x) for x in arrThongKeLop if x not in newList]
        c = Counter(arrThongKeLop)
        s = ""
        for x in newList:
            s += "{} {}\n".format(x, c[x])
        return s


if __name__ == "__main__":
    quanly = QuanLyHocSinh()
    while True:
        print("""1.Thêm
2.Đếm số học sinh nam nữ
3.Ghi file
4.Đọc file
5.Thống kê sĩ số lớp """)
        num = int(input("Chọn chức năng: "))
        if num == 1:
            quanly.AddHS()
        elif num == 2:
            print(quanly.thongKe())
        elif num == 5:
            print(quanly.thongKeLop())
        elif num == 3:
            quanly.fileOutput()
        elif num == 4:
            quanly.fileInput()
