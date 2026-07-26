'''
연습문제 로또 번호 생성기

규칙
1. 번호는 1~50이내 생성
2. 총 7개의 숫자 추출.
3. 축출한 번호는 오름 차순으로 정리.
4. 10번을 반복 생성하기

'''

"""
import random
#1.랜덤생성기 정의
#print(random.randrange(1,50)) #2번에서 리스트 응용문에서 실시

#2.랜덤 숫자 추출(7회)
randomLotto = [random.randrange(1,50) for i in range(7)]
print("정렬전:",randomLotto)

#3.오름차순정리
randomLotto.sort()
print("정렬후:",randomLotto)
"""

'''
#모범답안-1기본형
import random

for i in range(10) :
    lotto_numbers = []
    while len(lotto_numbers) != 7 :
        lotto_number = random.randint(1,51)
        if lotto_number not in lotto_numbers : #로또 번호는 중복하지 않습니다.
            lotto_numbers.append(lotto_number)
        print(lotto_numbers)
        lotto_numbers.sort()
        print(lotto_numbers)
'''

"""
#모범답안-2응용형
#선생님이 구글에서 찾으신 더 심플하게 작성한 코드.
import random

for i in range(10):
    lotto_numbers = random.sample(range(1,51), 7)
    lotto_numbers.sort()
    print(lotto_numbers)

'''
random.sample(seq or set, N)
첫번째 매개 변수 : 시퀀스 데이터 타입(튜플, 문자열, range,리스트)
두번째 매개 변수 :ㅣ 랜덤하게 뽑을 인자의 개수

첫 번째 인자로 받은 시퀀스데이터 or set에서 N개의 랜덤하고,
유니크하고, 순서상관없이 인자를 뽑아서 리스트로 만들어서 반
'''

"""

'''
#2차원 리스트 
a =[[10,20], [30,40], [50,60] ]
print(a)
'''
"""
a = [ [10,20],
      [30,40],
      [50,60] ]

print("a[0][0]:",a[0][0])
print("a[1][1]:",a[1][1])
print("a[2][1]:",a[2][1])
a[0][1] = 1000
print("a[0][1]:",a[0][1])
print(a)
"""


a=[[10,20],[30,40],[50,60]]
for i in a :
    print(i)

#모범답안
a=[[10,20],[30,40],[50,60]]

for aa in a :               #[10,20]식으로 가져옴.
    for aaa in aa :         #리스트내의 10, 20을 각각 가져옴.
        print(aaa, end=' ')
    print()
    








        
