'''
a = [38,21,53,62,19]
print(min(a))
print(max(a))

a=[10,10,10,10,10]
x=0

for i in a:
    x += i

print(x)

a=[10,10,10,10,10]
print(sum(a))
'''

"""
numbers=[]
print("빈 numbers :", numbers)

for i in range(10):
    numbers.append(i+1)
print("1~10 numbers :", numbers)

#홀수제거
for index,value in enumerate(numbers) :
    if(value % 2 == 1):
        del numbers[index]
        print("중간 numbers :", numbers)        
print("최종 numbers :", numbers)

#numbers의 0번째 자리에 값 20 추가.
numbers.insert(0,20)
print("numbers :", numbers)

#numbers의 값 20 삭제.
numbers.remove(20)
print("numbers :", numbers)

##numbers의 값 4의 위치(인덱스)
print("4의 위치",numbers.index(4))

##numbers를 내림차순 정렬하여 출력

numbers.sort(reverse =True)
print(numbers)
print(numbers.sort(reverse=True)) #None이라는 결과가 나오는 이유는sort는 리턴값이 없기때문
"""

"""
#모범답안
numbers=[]
print("빈 numbers :", numbers)

i =1
while i <= 10 :
    numbers.append(i)
    i = i+1
print(numbers)

i = len(numbers) -1
if numbers[i] %2 ==1 :
    del numbers[i]
    i=i-1
print(numbers)
"""


#리스트 표현식 매우 매우 중요! 딥러닝의 수학시 많이씀
a = [i for i in range(10) ]
#   |③ |  ② | ①
# ① : 배열 0~9를 생성
# ② : 기존의 반복문처럼 0~9까지 하나씩 꺼냄.
# ③ : i라는 이름의 리스트를 생성
b = list(i for i in range(10))
print(a)
print(b)

#리스트 표현식으로 해보기
[i for i in range(5,15)]   #5~14까지
[i for i in range(0,20,2)] #0~18까지.


#리스트 표현식+if조건문
a=[i for i in range(10) if i %2 ==0 ]
#   | ④ |  ② | ①         |   ③
# ① : 배열 0~9를 생성
# ② : 기존의 반복문처럼 0~9까지 하나씩 꺼냄.
# ③ : 하나씩 꺼낸 값을 조건문따라 비교한다.
# ④ : i라는 이름의 리스트를 생성
print(a)


b=[i for i in range(6,15) if i %2 ==0 ]
print(b)

#모범답 : b=[i+5 for i in range(10) if i%2 ==1]
#

#리스트 표현식으로 구국단 만들기

a= [i * j for j in range(2,10) for i in range(1,10)]
#   | ④    | ② | ①            |   ③
#j는 메인 수 2단, 3단 ..9단담당.
# ① : 배열 1~9를 생성
# ② : 기존의 반복문처럼 1~9까지 하나씩 꺼냄.
# ③ : i는 곱해지는 수를 담당
# ④ : 출력될 구구단 값 저장.
print(a)










