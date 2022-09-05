#fi;e I/O
#text files, music files, videos 등등 많을 종류 존재 but text file 만을 다룰 것임

#text files
#take up little disk space
#easy to process
#only letters in a file

#opening a file
#1) make a directory, file_examples
#2)open notepad and type the following
First line of text
Second line of text
Thrid line of text
#3)save this file in your file_examples directory as file_example.txt
#4)in IDLE, select File -> New Window and type this program
file = open('file_example.txt','r') #'r':read 만일 쓰기다 그럼 'w':write
contents = file.read(12) #12번째까지 읽어라
contentss = file.read() #앞에서 12번째까지 읽었으므로 13번째부터 시작
print(contents)
file.close() #열면 닫아줘야된다

with open('file_example.txt','r') as file: #close 자동으로 된다
    contents = file.read()
print(contents)

file = open('C:\\Users\\~~\\','r') #파일 주소를 넣을 수도 있다. 이때 \두번써야지 인식됨
file = open('C:/Users/~~/','r') #\\대신 그냥 /써도 된다
#파이썬 파일과 가지고 오려는 파일이 같은 폴더 내에 있으면 주소값 필요없고
#파일명만 있어도 된다
 import os
 os.getcwd() #current working diretory를 알 수 있게 해준다
 os.chdir('D:\\temp\\') #cwd 바꾸기

file = open('data/data1.txt','r') #해당 위치에 서브폴더 안에 있는 file 가지고 오기
file = open('../data/data1.txt','r') #../이 상위폴더 하나 올라가는 것

planets.txt
Mercury
Venus
Earth
file = open("Planets.tst",'r')
planets = file.readlines() #읽어서 하나의 list로 반환
file.close()
#['Mercury\n','Venus\n','Earth\n']
for p in planets:
    print(p) #두칸씩 띄워져서 출력된다
for p in planets:
    print(p.strip()) #여백 없애고 출력 즉 칸 안 띄워지고 출력

file = open('planets.txt','r')
for line in file:
    print(len(line))
file.close() #8 6 6 5
for line in file:
    print(len(line.strip()))
file.close() #7 5 5 4
