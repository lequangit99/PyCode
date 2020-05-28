if __name__ == "__main__":
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    c = [x for x in a if x % 2 == 0]
    print(c)
    years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
    d = []
    for x in years_of_birth:
        d.append(2020-x)
    print(d)
