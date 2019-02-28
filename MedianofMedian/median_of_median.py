from time import time
from numpy.random import randint
from statistics import median

# o(len(arr)/5)
def pick_pivot(arr):
    medians = []
    pointer = 0
    while pointer < len(arr):
        _sarr = sorted(arr[pointer:pointer+5])
        medians.append(_sarr[len(_sarr)//2 - 1 + len(medians)%2])
        pointer += 5
    return medians[len(medians)//2-1 +len(medians)%2]
    
def find_median(arr,k,prev_pivot):
    pivot = pick_pivot(arr) #o(n/5)
    if len(arr) == 1:
        return arr[0]
    if pivot == prev_pivot:
        return prev_pivot
    less = []
    more = []
    for el in arr: #o(n)
        if (el<=pivot):
            less.append(el)
        else:
            more.append(el)
    l = len(less)
    if l == k:
        return pivot
    if l<k:
        m = find_median(more,k-l,pivot)
    if l>k:
        m = find_median(less,k,pivot)
    return m

def find_median_robust(arr):
    l = len(arr)
    if l%2:
        return find_median(arr,l//2+1,0)
    a = find_median(arr,l/2,0)
    b = find_median(arr,l/2 + 1,0)
    return (a+b)/2.0 

def time_func(func,arr):
    start = time()
    func(arr)
    end = time()
    print(f'{func.__name__} took {end-start}')


def get_median(arr):
    sarr = sorted(arr)
    l = len(sarr)
    if l % 2:
        return sarr[l//2]
    return (sarr[l//2]+sarr[l//2 + 1])/2

    
if __name__ == "__main__":
    # arr = [1,2,3,3,3]
    # print(find_median_robust(arr))

    arr = randint(0,1000000,size=(1,100000))[0]
    time_func(get_median,arr)
    time_func(find_median_robust,arr)
    time_func(median,arr)
   