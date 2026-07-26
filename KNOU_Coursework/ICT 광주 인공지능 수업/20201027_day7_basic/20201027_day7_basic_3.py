'''
count = int(input("반복할 횟수를 입력하세요 : "))

while count > 0 :
    print("count : ", count)
    count -= 1
'''

#카운트 한개만으로 1부터 시작
'''
nData = int(input("반복할 횟수를 입력하세요 : "))
nTotal = nData
while nData > 0 :
    print("count : ", (nTotal+1) -nData )
    nData -= 1
'''

'''
import random

print(random.random())
print(random.random())
print(random.random())
'''

'''
import random

i=1
while i < 10+1 :
    print(i,"회 :",random.random())
    i+=1
'''

'''
import random

i=0
while i <100 :
    print(i+1,"회 : ",random.randint(1,6) ) #1~6사이의 정수형 난수 생성.
    i+=1
'''

'''
#1~6난수 무한생성중 숫자3이 나오면 반복 종료.

import random

count=0
randomTemp=0

while count >= 0 :
    randomTemp = random.randint(1,6)
    count += 1
    if(randomTemp ==3 ) :
        print(count,"회차 랜덤값 :", randomTemp)
        print("랜덤값 3 나왔습니다. 종료합니다.")    
        break
    else :
        print(count,"회차 랜덤값 :", randomTemp)

#모법답안
import random

i =0
while i != 3:
    i = random.randint(1,6)
    print i

'''

'''
#무한루프 
while True : #ctrl +c를 누르면 무한루프 탈출가능.
    print("Hi")
'''



















