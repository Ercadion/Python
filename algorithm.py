L= [809, 834, 477, 478, 307, 122, 96, 102, 324, 476]
def find_two_smallest1(L):
    smallest = min(L) # 96
    min1 = L.index(smallest) # 6
    L.remove(smallest)
    next_smallest = min(L) # 102
    min2 = L.index(next_smallest) # 6 -> 7
    if min2 >= min1:
        min2 += 1
    return (min1,min2)

def find_two_smallest2(L):
    sort_list = sorted(L)
    min1 = L.index(sort_list[0])
    min2 = L.index(sort_list[1])
    return (min1,min2)

def find_two_smallest3(L):
    if L[0]>L[1]:
        min1, min2 = 1, 0
    else:
        min1, min2 = 0, 1
    for i in range(2,len(L)):
        if L[i] < L[min1]:
            min2 = min1
            min1 = i
        elif L[i] < L[min2]:
            min2 = i

#Timing the function
import time
import find_two_smallest1
import find_two_smallest2
import find_two_smallest3
def time_find_two_smallest(find_func,lst):
    t1 = time.perf_counter()
    find_func(lst)
    t2 = time.perf_couner()
    return (t2-t1)*1000
