#classes
#class 안에 포함된 함수를 method라 부른다
#모든 type들은 자기들만의 method가 있다

str.capitalize('trump') #Trump
str.upper('trump') #TRUMP
str.center('Center',26) #'          Center          '
str.count('The biggest snow of the season',s) #4
'trump'.capitalize() #Trump
'trump'.upper() #TRUMP
#이런식으로 문자열을 앞으로도 가능, 이게 객체지향적 프로그래밍

#string method
'trump'.capitalize() #Trump
'ATTGGG'.count('T') #2
'strange'.endswith('ge') #True
'strange'.startswith('st') #True
'strange'.find('an') #3, 시작하는 위치의 인덱스 출력
'strange'.find('an',4) #-1, 4번 인덱스 이후부터 탐색, 없으면 -1 출력
'strange'.find('an',2,5) #3, [2,5)에서 탐색
'trump'.islower() #True, isupper는 반대
'TRUMP'.lower() #trump
str.lstrip('          hello world     ') #왼쪽 공백 삭제, rstrip은 오른쪽 삭제
str.strip('     hello world      ') #양쪽 다 없애기
str.split() #spacebar 기준으로 문자열 쪼개서 list type으로 변환
str.swapcase() #대문자 -> 소문자, 소문자 -> 대문자
'{0} ate {1} apples {2}'.format('I','3','yesterday') #I ate 3 apples yesterday
#숫자를 쓰면 0부터 들어가고 안쓰면 앞에서부터 들어간다

my_pi = 3.141592
'Pi rounded to {0} decimal places is {1:.2f}'.format(2,my_ pi)
#Pi rounded to 2 decimal places is 3.14
sentence = 'Pi rounded to {} deciaml places is {:.2f}'
sentence.format(2,my_pi) #결과 같다

#Nesting(중첩사용)
'Computer Science'.swapcase().endswith('ENCE') #True, 중첩하여 사용할 수 있다

#class and object
#예를 들어 int의 경우 class int라는 프레임을 하나 만들어놓고 object를 찍어내는것
#이렇게 찍어낸 애들이 integer의 object다 즉 객체이다
#이들은 class int에 있는 모든 method들 사용 가능

#object-oriented programming(객체지향, 객체가 주체)
#imperative programming(함수가 주체)
