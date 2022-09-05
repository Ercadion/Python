#searching a list
#linear search
list.index
['d','a','b','a'].index('a') # 1, 처음에 찾으면 그대로 종료

def linear_search1(lst, value):
    i=0
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1

def linear_search2(lst, value):
    i=0
    while i !=len(lst) and lst[i] != value:
        i += 1
    if i==len(lst):
        return -1
    else:
        return i

def linear_search3(lst, value):
    lst.append(value)
    i=0
    while lst[i] != value:
        i += 1
    lst.pop()
    if i==len(lst):
        return -1
    else:
        return i

def linear_search4(lst,value):
    lst.append(value)
    if lst.index(value) != len(lst)-1:
        return lst.index(value)
    else:
        return -1
def time_it(search, lst, value):
    t1 = time.perf_counter()
    search(lst, value)
    t2 = time.perf_counter()
    return (t2-t1)*1000

L=list(range(10000001)) #얘를 테스트에 사용

#binary search(정렬이 되어 있다는 전제)
def binary_search(L, v):
    i=0
    j=len(L)-1
    while i != j+1:
        m = (i+j)//2 #나누기 후 소수 있으면 없애기
        if L[m] < v:
            i = m + 1
        else:
            j = m + 1
    if 0<=i<len(L) and L[i] == v:
        return i
    else:
        return -1

#bisect라는 모듈에 binary search 구현해 놓음
