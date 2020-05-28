# 1. chuan hoa ho ten dssv trong tep tin dssv.txt (chi viet hoa chu cai dau), sap xep theo thu tu sau do ghi ra tep moi dssv_2.txt
# 2. thong ke co bao nhieu sinh vien ho "Nguyen", co bao nhieu sv ten "Anh"

# xay dung ham chuan hoa ten
def ChuanHoaTen(hoten):
    x = hoten.split()
    for i in range(len(x)):
        x[i] = x[i].capitalize()
    ten = x[len(x)-1]
    del x[len(x)-1]
    return " ".join(x), ten

f = open("dssv.txt")
dssv = []
for sv in f:
    hodem, ten = ChuanHoaTen(sv)
    dssv.append((ten, hodem))
dssv.sort()
f = open("dssv_2.txt", "w")
for x in dssv:
    f.write(x[1] + " " + x[0]+"\n")
f.flush()
f.close()
dem1 = 0
dem2 = 0
for x in dssv:
    if x[0] == "Anh":
        dem2 = dem2+1
    if x[1].find("Nguyen") == 0:
        dem1 = dem1+1
print("so sv co ho Nguyen: ", dem1)
print("so sv ten Anh: ", dem2)
