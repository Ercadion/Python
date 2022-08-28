#while loop
rabbits = 3
while rabbits >0:
    print(rabbits)
    rabbits = rabbits -1

#interactive program
text = ''
while text != 'quit':
    text = input("Please enter a chemical formula (or quit to exit) : ")
    if text =='quit':
        print("...exiting program")
    elif text =="H2O":
        print("Water")
    elif text =='NH3':
        print('Ammonia')
    elif text =='CH4':
        print('Methane')
    else:
        print("Unknown compound")

#break
text = ''
while True:
    text = input("Please enter a chemical formula (or quit to exit) : ")
    if text =='quit':
        print("...exiting program")
        break
    elif text =="H2O":
        print("Water")
    elif text =='NH3':
        print('Ammonia')
    elif text =='CH4':
        print('Methane')
    else:
        print("Unknown compound")

#continue
#skip immediately to the next iteration of the loop
s = 'C3H7'
total=0
count=0
for i in range(len(s)):
    if s[i].isalpha():
        continue
    total = total+int(s[i])
    count = count+1
print('total : ',total)
print('count : ',count)

