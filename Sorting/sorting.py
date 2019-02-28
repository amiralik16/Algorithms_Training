from time import time
from numpy.random import randint

def bubblesort(arr, debug=False):
    _flag = True
    _rep = 0
    while(_flag):
        _rep += 1
        _flag = False
        if debug: print(f'rep number: {_rep}') 
        for i in range(1,len(arr)):
            if arr[i-1]>arr[i]:
                arr[i],arr[i-1] = arr[i-1],arr[i]
                _flag = True
            if debug: print(i,arr)
    return arr

def selectionsort(arr, debug=False):
    for i in range(len(arr)):
        m = i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[m]:
                m = j
        arr[i],arr[m] = arr[m],arr[i]
        if debug: print(i,arr)
    return arr

def mergesort(arr, debug=False):
    if len(arr)<2: return arr
    cut = len(arr) // 2
    left = mergesort(arr[:cut])
    right = mergesort(arr[cut:])
    return merge(left,right)

def merge(left,right):
    helperarr = [0] * (len(left) + len(right))
    li = ri = 0
    current = 0
    while li<len(left) and ri<len(right):
        if left[li] <= right[ri]:
            helperarr[current] = left[li]
            li += 1
            current += 1
            continue
        if right[ri] <= left[li]:
            helperarr[current] = right[ri]
            ri += 1
            current += 1
            continue
    if(li<len(left)):
        helperarr[current:] = left[li:]
    elif ri<len(right): 
        helperarr[current:] = right[ri:]
    return helperarr

def quicksort(arr):
    start = 0
    end = len(arr)-1
    quicksort_r(arr,start,end)
    return arr

def quicksort_r(arr,start,end):
    if start>=end:
        return
    idx = partition(arr,start,end)
    quicksort_r(arr,start,idx-1)
    quicksort_r(arr,idx,end)

def partition(arr,start,end):
    pivot = arr[(start+end) // 2]
    while start<=end:
        while(arr[start]<pivot): start += 1
        while(arr[end]>pivot): end -= 1
        if start<=end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1
    return start


def time_func(func,arr):
    start = time()
    func(arr)
    end = time()
    print(f'{func.__name__} took {end-start}')
        

if __name__ == "__main__":
    arr = [1,5,2,4,3,8,6,6]
    # #bubblesort
    # sarr = bubblesort(arr)
    # print(f'\nbubble sort = {sarr}')

    # #selection sort
    # sarr = selectionsort(arr,True)
    # print(f'\nselection sort = {sarr}')

    #merge sort
    sarr = mergesort(arr)
    print(f'\nmerge sort = {sarr}')

    # #quick sort
    # sarr = quicksort(arr)
    # print(f'\nquick sort = {sarr}')

    # arr = randint(0,1000000,size=(1,10000))[0]
    # time_func(bubblesort,arr)
    # time_func(selectionsort,arr)
    # time_func(mergesort,arr)
    # time_func(quicksort,arr)
    # time_func(sorted,arr)
