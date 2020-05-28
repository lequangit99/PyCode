if __name__ == "__main__":
    file = open("quatmo.txt", "r+")
    while True:
        data = file.read()
        print(data)
        inputStr = str(input("Nhập thêm vào: "))
        file.write("\n"+inputStr)
