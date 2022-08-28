#loop
#for loop
#for <<variable>> in <<list>>:
#   <<block>>
velocities = [0.0, 9.81, 19.62, 29.43]
speed = 2
for speed in velocities:
    print('Metric: ',speed,'m/sec')
print('Final',speed,'m/sec')

country = 'United States of America'
for ch in country:
    if ch.isupper(): # USA
        print(ch)

for num in range(10): #0 1 2 3 4 5 6 7 8 9
    print(num)

list(range(3)) #[0,1,2]
list(range(1,5)) #[1,2,3,4]
list(range(1,10,2)) #[1,3,5,7,9]
list(range(5,0,-1)) #[5,4,3,2,1]

values = [4,10,3,8,-6]
for num in values: #8, 20, 6, 16, -12
    num = num*2
    print(num)
print(values) #[4, 10, 3, 8, -6]

values = [4,10,3,8,-6]
for i in range(len(values)):
    values[i] = values[i]*2
print(values)

#loop 중첩
positive = ['Li','Na','K']
negative = ['F','Cl','Br']
for metal in positive:
    for halogen in negative:
        print(metal+halogen) #print가 9번 실행됨

#ex:Print multiplication table
def print_table(n):
    a = list(range(1,n+1))
    for i in a:
        print('\t',i, end='')
    print()
    for i in a:
        print(i,end = '')
        for j in a:
            print('\t',(i)*(j),end='')
        print()

#중첩 list looping
elements = [['Li','Na','K'],['F','Cl','Br']]
for inner_list in elements:
    print(inner_list)
for inner_list in elements:
    for item in inner_list:
        print(inner_list)

#ragged list
#inner_list의 크기가 같지 않은 list들
elements = [['Li'],['Na','K']] #같이 크기 다른 것들. for문 돌리는데 아무 이상 없음

