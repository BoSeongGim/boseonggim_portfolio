#for 시퀀스 자료&횟수 확정시 주로 사용
#while 횟수가 확정않고 때마다 다를 경우

'''
i=2
j=5

while i<=32 or j >=1 : 
    print(i, j)
    i=i*2
    j-=1    
'''

'''
money = int(input("금액을 입력하세요! : "))

while money >= 1350 :
    money -= 1350
    print("money : ", money)
'''

'''
i = 0
while True :
    print(i)
    i += 1
    if  i == 100 :
        break
'''

'''
for i in range(10000) : #무한루프처럼 무한반복 목적.
    print(i)
    if i == 100 : #종료조건 
        break
'''

'''
#break=완전탈출
#continue= 해당 턴에서만 자기 밑 코드 실행 않음
#continue는 사용하는 경우가 적지만 코드를 간단하게 만들어 주는 경우가 있다.
#딥러닝에서 break,continue를 활용하는 경우들 많습니다1

for i in range(100) :
    if i%2 == 0 :
        continue
    print(i) #짝수는 미실행된다.
'''


'''
i = 0
while i < 100 :
    i += 1
    if i % 2 == 0 :
        continue
    print(i)
'''

'''
count = int(input("반복할 횟수를 입력하세요 : "))

i = 0
while True :
    print(i)
    i += 1
    if i == count :
        break
'''

'''
count = int(input("반복할 횟수를 입력하세요 : "))
 
for i in range(count +1 ) : #0부터 증가하면서count까지 반복(count +1)
    if i % 2 == 0 :
        continue
    print(i)
'''

#0~73까지 실시.
i = 0 
while True :
    i +=1
    if i%10==3 :  #힌트 : 나머지 연산자 활용.
        print(i, end=' ') #3으로 끝나는 숫자만 출력
    if i >= 73 : #73 이상 인가 체크
        break

#실행결과 : 3 13 23 33 43 53 63 73 

# 모범답안 

i=0
while True:
    if i % 10 !=3 :
        i += 1
        continue
    if i>73 :
        break
    print(i, end=' ')
    i += 1










































