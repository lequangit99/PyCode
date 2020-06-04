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
    sort_orders = sorted(c.items(), key=lambda x: x[1], reverse=True)
    for i in sort_orders:
        for x in chars:
            if i[0] == x:
                cotX.append(i[0])
                cotY.append(i[1])
    plt.bar(cotX[0:10],cotY[0:10])
    plt.show()