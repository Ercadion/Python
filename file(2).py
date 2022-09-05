import urllib.request
url = 'http://openapi.seoul.go.kr:8088/6773656176656c6c37395178796377/xml/TbKioskInfo/1/1000/'
webpage = urllib.request.urlopen(url)
line = webpage.readline()
webpage.close()

#line = line.strip()
#line = line.decode('utf-8') 위 line의 경우 type string이 아니라 bytes이라서
#print(line)                 decode를 통해 string으로 변환

#writing files
outfile = open('topics.txt','w') #write는 .txt 없으면 만들고 있으면 덮어쓴다
outfile.write('Computer science') 
outfile.close()

outfile = open('topics.txt','a') #append는 추가
outfile.write('Computer science') 
outfile.close()

def sum_number_pairs(input_file,output_filename):
    output_file = open(output_filename,'w')
    for numer_pair in input_file:
        number_pair = number_pair.strip()
        operands = number_pair.split()
        total = float(operands[0]) +float(operands[1])
        new_line = '{0} [1]\n'.format(numer_pair, total)
        output_file.write(new_line)
    output_file.close()
