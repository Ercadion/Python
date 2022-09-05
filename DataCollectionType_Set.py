#Data_collection_type1
#Set, Tuple, Dictionary

#Set
vowels = {'a','e','i','o','u'}
vowels = {'a','e','i','o','u','a','e','i','o','u'}
#{'a','e','i','o','u'} 중복되는것 제외, 순서 상관 없음
{'a','e','i','o','u','a','e','i','o','u'} == {'a','e','i','o','u'}
#True

#empty set is not {} -> set()
set([2,3,2,5]) #{2,3,5}, set 안에 안 넣거나 하나만 넣어야한다

#method
S.add(v) #S에 v 더하기 이미 있으면 효과 없음
S.clear() #전체 제거
S.difference(other) #비교해서 다른거 출력, S - other
S.intersection(other) #비교해서 같은거 출력, S & other
S.issubset(other) #S가 other의 부분집합이면 True, S <= other
S.issuperset(other) #other가 S의 부분집합이면 True, S >= other
S.remove(v) #v를 S에서 제거
S.symmetric_difference(other) #둘이 서로 같은 거만 뺴고 양쪽꺼 다 출력, S ^ other
S.union(other) #둘의 합집합 출력, S | other

#set exmaple
observations_file = open('observation.txt') #.txt에는 관찰된 새 종류
birds_observed = set()
for line in observation_file:
    bird = line.strip()
    birds_observed.add(bird)

print(birds_observed)

for species in birds_observed:
    print(species)
