#FizzBuzz 한 줄로 출력(내가 작성, 반타작)
'''
for i in range(1,101) :
    print("FizzBuzz" if (i%3 == 0 and i%5==0) 
#          elif(i%3 == 0) "Fizz"  #작동에러 ㅠ
#          elif(i%5 == 0)  "Buzz" #작동에러 ㅠ
          else i
          )
'''
# Python - inline if 문
# https://jhproject.tistory.com/125

'''
FizzBuzz - 한줄로 표기법
단락평가를 통해 평가한다.(#문자열 곱셈&덧셈을 통해 print내에서 처리)
'''

'''
for i in range(1,101): #[참고] 책-파이썬 코딩도장 20.5 코드 단축하기
    print('Fizz'*(i%3==0) +'Buzz'*(i%5==0) or i)
    #(i%3==0)
'''

'''
for i in range(1,101) :
    if (i%2 ==0 and i%11 ==0) :
        print('FizzBuzz')
    elif(i%2 ==0) :
        print('Fizz')
    elif(i%11 ==0) :
        print('Buzz')
    else :
        print(i)
'''

import turtle as t
t.shape('turtle')
'''
t.forward(100)#-> 방향으로 이동

t.right(90); t.forward(100)
t.right(90); t.forward(100)
t.right(90); t.forward(100) #사각형 완료.
'''

'''
#한 개의 사각형을 그린 후 오른쪽으로 이동하여 2번째 사각형 그리기.
t.forward(100)#-> 방향으로 이동

t.right(90); t.forward(100)
t.right(90); t.forward(100)
t.right(90); t.forward(100) #사각형 완료.

t.penup(); t.right(90); t.forward(200) #이동

t.pendown() #이동후 그리기 작업재개
t.forward(100)#-> 방향으로 이동

t.right(90); t.forward(100)
t.right(90); t.forward(100)
t.right(90); t.forward(100) #사각형 완료.
'''


'''
#4개의 사각형 그리기

t.forward(100)#-> 방향으로 이동

t.right(90); t.forward(100)
t.right(90); t.forward(100)
t.right(90); t.forward(100) #사각형-1 완료.

#이동 사각형-2
t.penup(); t.right(90); t.forward(200)

t.pendown() #이동후 그리기 작업재개
t.forward(100)#-> 방향으로 이동

t.right(90); t.forward(100)
t.right(90); t.forward(100)
t.right(90); t.forward(100) #사각형-2 완료.(좌표 : 200,0)


t.penup();t.goto(300,-200) ; t.pendown() #이동후 그리기 작업재개

t.right(180); t.forward(100)
t.right(90); t.forward(100)
t.right(90); t.forward(100)
t.right(90); t.forward(100) #사각형-3 완료.(좌표 : 200,0)

t.right(180); #그리기 편하게 머리방향 조정
t.penup();t.goto(100,-300) ; t.pendown() #goto는 거북이의 머리방향이 중요한게 아니 원점좌표(0,0)을 기준으로 함.... 

t.forward(100)
t.right(90); t.forward(100)
t.right(90); t.forward(100)
t.right(90); t.forward(100) #사각형-4 완료.(좌표 : 200,0)
'''































