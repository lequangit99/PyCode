import os

if __name__ == "__main__":
    pwd = os.getcwd()
    os.mkdir("ABC") #tạo thư mục
    os.chdir("ABC") #cd vào thư mục
    file = open("text1.txt", "w") # tạo file
    file.close()
    os.chdir(pwd)
    os.rename("ABC","XYZ")
    os.chdir("XYZ")
    question = input("Bạn có muốn xoá file text1.txt không? yes/no: ")
    if question == "yes":
        os.remove("text1.txt")