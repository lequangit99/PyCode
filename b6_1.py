import numpy as np
arr = np.random.randint(int(10e3), size=int(10e5))
size = len(arr)

def buble_sort(arr):
    for i in range (0,size-1):
        for j in range (i+1, size):
            if(arr[i] > arr[j]):
                arr[i],arr[j] = arr[j],arr[i]

buble_sort(arr)

def patition(arr,l,h):
    i = l-1
    p = arr[h]
    for j in range(l,h):
        if arr[j] < p:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[h] = arr[h],arr[i+1] 
    return (i + 1) 

def quicksort(arr,l,h): 
    if l < h: 
        p = patition(arr,l,h) 
        quicksort(arr, l, p-1) 
        quicksort(arr, p+1, h) 

quicksort(arr, 0, size-1)