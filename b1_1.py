from datetime import date

if __name__ == "__main__":
    today = date.today()

    name = input("Nhập vào tên: ")
    age = int(input("Nhập vào tuổi: "))

    temp = int(today.year) + 100 - age
    loop = int(input("Nhập vào số bản sao: "))
    for x in range(loop):
        print("Năm {} {} sẽ 100 tuổi".format(temp,name))




