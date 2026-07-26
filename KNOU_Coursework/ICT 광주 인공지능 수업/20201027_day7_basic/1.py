#반복문
'''
#반복문 기본형
1. for 변수 in range(횟수) :
2. for 변수 in range(시작, 끝) :
3. for 변수 in range(시작, 끝, 증가폭) :

#반복문-숫자순서 반대형
1. for 변수 in reversed(range(횟수)) :
2. for 변수 in reversed(range(시작, 끝)) :
3. for 변수 in reversed(range(시작, 끝, 증가폭)) : 

'''

#1.for 변수명 in range(횟수) :
#[주의] 카운팅은 0부터 시작함.
'''
for i in range(100) :
    print('Hello World!', i)
'''
'''
for count in range(100) :
    print("counting:",count)
'''

#2. 0이외의 시작하는 숫자, 끝나는 숫자를 지정할 수 있음.
'''
for i in range(5,12) :
    print("0외에서 시작 :",i)
'''

#3. 0이외 시작점 + 증감값 설정
'''
for i in range(0, 10, 2) : #짝수만 출력하게 됨 
    print("hello, world!",i)
'''

#10부터 1까지 -1씩 감소(10,9,8...)
'''
for i in range(10,0,-1):
    print("Hello world",i)
'''

#reversed 사용하여 감소하는 방식으로 실시.
'''
for i in reversed(range(10)) :
    print("reversed :",i)
'''

'''
repeat = int(input("반복할 횟수를 입력하세요 : "))
for i in range(repeat):
    print("repeat : ",i)
'''

#시퀀스 객체(리스트/튜플/문자열/)로 반복하기 
#딥러닝시 시퀀스 객체에서 꺼내는 경우가 많습니다

#리스트
'''
a = [10,20,30,40,50]
for i in a: #a라는 리스트의 i번째 셀을 꺼낸다.
    print(i)
'''

'''
fruits = ('apple','orange','grape')
for fruit in fruits : #fruit
    print(fruit)    
'''

for i in 'Python' :
    print(i, end=' ')
    



'''

r = range(5)

for i in r :
    print

'''
