str a #변수 a를 string으로 선
len("Hello") #문자열의 길이 반환
"Hello"+"World" #출력값 HelloWorld
"Hello" * 2 #출력값 HelloHello

#escape sequence
#\'(single quote) \"(double quote) \\(backslash)
#\t(tab) \n(new line) \r(carriage return)

#print()
print(1,"1",'1',1.0)
a=5
print("Hello",a*2,"World")
print('a','b','c') #a b c
print('a','b','c',sep='-') #a-b-c
print('a','b','c',sep='-',end='r') #a-b-cr

#input
a = input() #a 값을 사용자가 입력한다. string의 형태로 입력받음

#slicing string
a="Hello World"
a[2] #e
b = a[4]+a[5]+a[6]+a[7] #lo w
c = a[1:4] #Hel
d = a[1:] #Hello World
e = a[:5] #Hell
a[-1] #d
a[-0] #H
b = a[7:-2] #Wor
c = a[1:6:2] #Hll
d = a[::-1] #dlroW olleH
