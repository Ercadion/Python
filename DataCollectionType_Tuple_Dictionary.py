#Tuple
bases = ('A','C','G','T')
for base in bases:
    print(base)
#A
#C
#G
#T
type((8,)) #tuple
(x,) #a tuple with single element

life = (['Canada',76.5],['United States',75.5],['Mexico',72.0])
type(life) #tuple
type(life[0]) #list
life[0] = ['Korea',78.0] #error, tuple is immutable
life[0][1] = 80.0 #available, list is mutable

a=10,20
type(a) #tuple
type((10,20)) #tuple
x,y=10,20 #x=10, y=20
type(x) type(y) #both int
[[w,x],[[y],z]] =[{10,20},[(30,),40]] #w=10 x=20 y=30 z=40

#swap
s1 = 'first'
s2 = 'second'
s1,s2 = s2,s1

#Dictionary
obseration_file = open('observations.txt')
birds_count = []
for line in observations_files:
    bird = line.strip()
    found = False
    for entry in bird_counts:
        if entry[0] == bird:
            entry[1] = entry[1] +1
            found = True
    if not found:
        birds_counts.append([bird,1])
observations_file.close()
for entry in bird_counts:
    print(entry[0],entry[1])

#example
bird_to_observation = {'canada goose': 3, 'northern fulmar': 1}
#empty dictionary is {}
bird_to_observation['canada goose'] #3
bird_to_observation['canada goose'] = 9
bird_to_observation
#{'canada goose': 9, 'northern fulmar': 1}
del bird_to_observation['canada goose']
bird_to_observation
{'northern fulmar': 1}
'northern fulmar' in bird_to_observation #True

#method
D.clear() #remove all
D.keys() #dict_keys([])꼴로 key들 나옴, list(k)로 list로 활용가능
D.values() #dict_values([])꼴로 값들이 나옴, list(k)로 list로 활용가능
D.items() #dict_items([])꼴로 key, value 둘다 합쳐서 나옴, list(k)로 list로 활용가능
D.get(k) #value 가져온다, 없으면 None, 없는값에 value 넣어서 주면 그 값 반환
D.update(other) #D에 other 합친다

observation_file = open('observations.tst')
bird_to_observations = {}
for line in observations_file:
    bird = line.strip()
    if bird in bird_to_observations:
        bird_to_observations[bird] = bird_to_observations[bird]+1
    else:
        bird_to_observations[bird] = 1
observations_file.close()
for bird, observations in bird_to_observations.items():
    print(bird, obsercations)

observation_file = open('observations.tst')
bird_to_observations = {}
for line in observations_file:
    bird = line.strip()
    bird_to_observations[bird] = bird_to_observations.get(bird, 0) +1
observations_file.close()
for bird, observations in bird_to_observations.items():
    print(bird, obsercations)

sorted_birds = sorted(bird_to_observations.keys())
for bird in sorted_birds:
    print(bird, bird_to_observations[bird])

#inverting a dictionary, key -> value, value -> key
#bird_to_observations
observations_to_birds_list = {} #inverting
for bird, observations in bird_to_observations.item():
    if observations in observations_to_birds_list:
        observations_to_birds_list[observation].append(bird)
    else:
        observations_to_birds_list[observation] = [bird]
