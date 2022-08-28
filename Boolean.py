#Boolean
#True, False 값을 가진다
#and, or, not 연산자를 이용
#exclusive or -> True, True 일때에도 False가 되게 하는 or, a!=b

#relational operators
#<, >, <=, >=, ==, !=

#numbers and strings with Booleans
1 == True
not 0 #True
not 1 #False
#0을 제외한 모든 수는 True 하지만 not을 붙였을 때만
#비교연산자를 사용할 경우 즉 5 == True, 5 == False는 둘 다 False로 나온다.
#근데 왠만해서는 Boolean을 숫자로 대체해서 사용하지 말자
not ''
not "" #empty string은 False로 취급 나머지 string들은 True
#함수에서 반환값을 지정해주지 않을 경우 반환되는 None도 False로 취급

#or에서 첫번째 시행이 True라면 두번째를 계산하지 않고 True를 내보낸다
#and에서 첫번째 시행이 False라면 두번째를 계산하지 않고 False를 내보낸다
>>>(2<3) or (1/0)
True
#원래 (1/0)은 ZeroDivisionError가 뜨지만 위에서 보다시피 안 뜨고 True가 나온 모습

#Comparing Strings
'A'<'a' #True
'A'<'z' #True
'abc'<'acd' #True
'abc'<'abcd' #True
'가'<'나' #True
'가나'<'가다' #True
'가나다'<'가나' #False
'가'>'거' #False
'Jan' in '01 Jan 1838' #True
'Feb' in '01 Jan 1838' #False
#대문자끼리 비교
'C++'<'Python' #True
'Javascript'>'Python' #False

#연산 우선 순위
#and는 or보다 먼저 시행
