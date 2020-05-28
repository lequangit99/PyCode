if __name__ == "__main__":
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = []
    for x in a:
        if x < 5:
            print(x)
    for x in a:
        if x < 5:
            b.append(x)
    print(b)
    check = int(input("Nhập vào 1 số: "))
    for x in a:
        if x < check:
            print(x)
