#Modules
import math #math module 불러오기
type(math) #module
math.sqrt(9) #module명을 함수 앞에 적어주어야 해당 모듈 안의 함수 사용가능

from math import pi, sqrt #이렇게 import 하면 앞에 math. 필요없음
from math import * #모든 변수나 함수를 위의 방법처럼 사용가능 but 디버깅 힘듦
                   # 변수나 함수가 겹치면 오류 생길 수도 있다

#https://docs.python.org/release/3.3.0/py-modindex.html

#define own module
#하나의 파일이 곧 모듈, 파일명이 모듈명
import importlib
importlib.reload(exp) #다시 로드 exp에서의 수정사항 반영해서 반환

if run_directly:
    print("ran directly");
else:
    print("another module is importing me");

if __name__=="main":
    print("ran directly");
else:
    print("module name is",__name__);
#위 두개 모두 똑같은 거, 직접 run 시켜서 호출할 때와 모듈 형태로 끌어올때 차이를
#구분해야 할 때 사용 가능

#random
import random
x1 = random.random() #generates a random floating-point number in range [0,1)
x2 = random.uniform(a,b) # ~~~ in range [a,b)
x3 = random.randrange(stop) #chooses an integer in range [0,stop)
x4 = random.randrange(start,stop) # ~~ in range [start,stop)
x5 = random.randrange(start,stop,step) # ~~ [start,start+step,start+step*2,stop)
x6 = random.randint(start,stop) # ~~ in range [start,stop]

#Graphic(turtle)
import turtle
t = turtle.Pen()
t.forward(50)
t.left(90)
t.forward(50)
t.right(90)
t.backward(50)
t.up() #펜 들기, 이 상태에서 이동시 그림 안 그려짐
t.down() #펜 놓기
t.reset() #제자리로 돌아가기 + 다 지우기
t.clear() #다 지우기만

