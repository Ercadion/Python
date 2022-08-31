#Function with no parameters
def say():
    return "Hello" #이후 say() 출력하면 Hello 반환

#Function with no return value
def say():
    print('Hello') #return 값 none으로 자동 설정
#즉 result = say() -> result 출력하면 값 없음 하지만 say()를 치면 Hello는 출력됨
def say():
    print('Hello')
result = say()
print(result) #Hello none 출력됨

#Docstring(Documentation string)
#규칙
#1.Types of (Parameters) -> Return value
#2.Function description
#3.Example calls
def days_differfence(day1,day2):
    """(int,int) -> int
    Return the number of days between day1 and day2,
    which are both in the range 1~365
    (thus inficating the day of the year)
    >>>days_difference(200,224)
    24
    >>>days_difference(50,50)
    0
    >>>days_difference(100,99)
    -1
    """
    return day2-day1
#이렇게 적어놓으면 help()를 통해서 확인가
