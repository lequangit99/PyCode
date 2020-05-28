if __name__ == "__main__":
    num1 = int(input("Nhập vào 1 số: "))

    if num1 % 2 == 0:
        print("{} là số chẵn".format(num1))
    else:
        print("{} là số lẻ".format(num1))

    if num1 % 4 == 0:
        print("{} là bội số của 4".format(num1))

    num2 = int(input("Nhập vào số thứ 1: "))
    num3 = int(input("Nhập vào số thứ 2: "))

    if num2 % num3 == 0:
        print("{} chia hết cho {}".format(num2,num3))
    else:
        print("{} không chia hết cho {}")
