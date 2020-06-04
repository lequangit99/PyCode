from collections import Counter
import matplotlib.pyplot as plt

if __name__ == "__main__":
    f = open("news.txt", "r")
    fileData = f.read()
    count={}
    s = fileData.lower()
    chars = "abcdefghijklmnopqrstuvwxyz"
    c = Counter(s)
    cotX = []
    cotY = []
    for x in chars:
        cotX.append(x)
        cotY.append(c[x])
    plt.bar(cotX,cotY)
    plt.show()