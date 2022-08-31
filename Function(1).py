#웹파이썬 Function(1)

abs(-9) #절댓값 변환

pow(3,2) #제곱 옆에 예제 같은 경우는 3^2로 9로 출력됨

round(4.3) #반올림
round(-3.5) # -4로 출력
round(3.141592,2) #소수점 둘째자리까지

#typecast 함수 자료형 바꿔주는 역할
int(34.6) #34
int(-4.3) #-4
float(21) #21.0

#함수 설명 필요할때
help(abs) #와 같은 help 안에 함수명

#memory address
id(-9)
id(-abs) #다음과 같은 값들의 메모리 주소를 출력

#function define
def convert_to_celsius(fahrenheit):
    return(fahrenheit - 32)*5/9 #convert_to_celsius 라는 함수를 정의해준 것

#local variables
def quadratic(a,b,c,x):
    first = a*x**2
    secnond = b*x
    third = c
    return first + second + third
#이 함수에서 first, sencond, third, a, b, c, x들은 지역변수로 함수 안에서만
#접근할 수 있음

