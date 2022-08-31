#list
#list는 새로운 type, 여러가지 변수를 다룰 수 있다.
whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
#각각의 요소들을 element, item이라고 부른다.
whales[0] #5
whales[13] #3
whales[-1] #3
#list 다른 타입 다 혼용 가능
krypton = ['Krypton','Kr',-157.2,-153.4]

#lists are mutable
x = L[i]
L[i] = x #list는item을 교환하는 것 가능, string은 안됨

#operations on lists
a = [2,4,1,7,3]
len(a) #5
max(a) #7
min(a) #1
sum(a) #17
sorted(a) #[1,2,3,4,7]
sorted(a,reverse=True) #[7,4,3,2,1]

#+, *, del
original = ['H','He','Li']
final = original + ['Be'] #['H','He','Li','Be']
metals = ['Fe','Ni']
metals*3 #['Fe','Ni','Fe','Ni','Fe','Ni']
del metals[0] #['Ni']

#in operator
nobles = ['helium','neon','argon','krypton','xenon','radon']
gas = input('Enter a gas: ')
if gas in nobles:
    print('{} is noble.'.format(gas))
else:
    print('{} is not noble gas'.format(gas))

#slicing list
L[0:4] #0~3까지의 list내 item 출력
L[::2] #0 2 4~ 의 간격으로 출력
L[::-1] #역순으로 정렬 가능

#copying list
x = L[:] #원래의 list랑 복사된 list랑 다른 메모리주소를 가진다. 변화 반영 X
x = L #원래의 list랑 복사된 list랑 같은 메모리주소를 가진다. 변화 반영 O, Aliasing
x = [1,2,3,4,5]
y = x
z = x[:]
x[4] = 7
x #[1,2,3,4,7]
y #[1,2,3,4,7]
z #[1,2,3,4,5]

#함수에서 list
#함수에서는 aliasing 해서 나오게 된다.

#list methods
L.append(v) #v를 list L의 가장 마지막에 넣어준다
L.clear() #모든 요소 지우기
L.count(v) #v의 개수 세기
L.index(v,beg,end) #v가 몇번째 index에 있는지 찾기, beg~end 범위에서
L.insert(i,v) #i 번째 index에 v 넣어주기
L.pop() #list L의 마지막을 반환하고 list에서 제거
L.remove(v) #v값을 list L에서 제거
L.sort() #정렬, 원래꺼 없애고 정렬된거 반환

#list of list
life = [['Canada',76.5],['United States',75.5],['Mexico',72.0]]
life[0] #'Canada',76.5
life[0][1] #76.5
canada = life[0]
canada[1] = 80.0
canada #['Canada',80.0]
life #[['Canada',80.0],['United States',75.5],['Mexico',72.0]]
