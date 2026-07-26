

#모범답안 - 5개의 함수 연산자 입력형  모습.(문법에러 나오고 있음. 아직 수리중)
'''
def sum(a,b) :
    return a+b

def sub(a,b) :
    return a-b

def mul(a,b) :
    return a*b

def div(a,b) :
    return a/b

def rem(a,b) :
    return a%b

def allcal(a,b, type) :
    if type == 1:
        return sum(a,b)
    elif type == 2 :
        return sub(a,b)
    elif type == 3 :
        return mul(a,b)
    elif type == 4 :
        return div(a,b)
    elif type == 5 :
        return rem(a,b)
    


print("="*30)
print("1.더하기 \n 2.빼기 \n 3.곱하기 \n 4.나누기 \n 5.나머지구하기  \n 6.나가기 \n ")
print("="*30)

while True :
    menu = input("원하는 계산기 기능을 입력하세요.")

    if(menu == '+' or menu == '-' or menu == '*' or menu == '/' or menu == '%' ) :
        numberA = int(input("첫번째 숫자를 입력하세요.") )
        numberB = int(input("두번째 숫자를 입력하세요.") )

    if(menu == '+') :
        result = sum(numberA, numberB)
        print("더하기 결과는 %d 입니다." %result)

    elif(menu == '-') :
        result = sub(numberA, numberB)
        print("빼기 결과는 %d입니다." %result)

    elif(menu == '*') :
        result = mul(numberA, numberB)
        print("곱하기 결과는 %d입니다." %result)

    elif(menu == '/'):
        result = div(numberA, numberB)
        print("나누기 결과는 %d입니다." %result)

    elif(menu == '%'):
        result = allcal(numberA, numberB)
        print("나머지 결과는 %d입니다." %result)

    elif(menu == 'E') :
        break
    else :
        print("잘못입력하셨습니다. 다시 입력해주세요.")
'''

#계산 맞추기 게임 프로젝트 ====================================
import random

def sum(a,b) :
    return a+b
def sub(a,b) :
    return a-b
def mul(a,b) :
    return a*b

tryCount = 0 #5번 도전 카운트
userAnswelCount =0 #정답맞춘 횟수
userNoAnswelCount =0 #오답 횟수
def make_question() :
    randomNumber1 = random.randint(-99, 99)
    randomNumber2 = random.randint(-99, 99)
    randomCal     = random.randint(1, 3)
    
    if randomCal == 1 :
        selectCal = '+'
    elif randomCal == 2 :
        selectCal = '-'
    elif randomCal == 3 :
        selectCal = '*'

    quizString = str(randomNumber1) + selectCal + str(randomNumber2) #문제를 문자열로 작성.

    return quizString

def check(quiz,userAnswel) : 
    if(eval(quiz) == userAnswel) :
        print("축하합니다. 정답입니다!")
        return 1 #신호/ 정답카운트 1올림
    else :
        print("아쉽습니다. 오답입니다 ㅠㅠ")
        return 0 #신호/ 오답카운트 1올림


while tryCount < 5 :
    quiz = make_question() 
    print("문제",tryCount+1,": ", quiz)
    userAnswel = int(input("생각하시는 답을 입력해 주세요.") )
    if check(quiz,userAnswel) == 1 :
        userAnswelCount +=1  
        print("정답 카운트 현황 : ", userAnswelCount )
        print("오답 카운트 현황 : ", userNoAnswelCount )
    else :
        userNoAnswelCount +=1  
        print("정답 카운트 현황 : ", userAnswelCount )
        print("오답 카운트 현황 : ", userNoAnswelCount )

    tryCount+=1

print("최종 정답카운트 : ",userAnswelCount)
print("최종 오답카운트 : ",userAnswelCount)

"""
#천영성 씨의 답안 
import random
def make_question():
    operator = random.randint(1,3)
    num1 = random.randint(-99,99)
    num2 = random.randint(-99,99)
    if operator ==1:
        num1 = str(num1)
        num2 = str(num2)
        question = num1 + '+' + num2 
        return question
    elif operator ==2:
        num1 = str(num1)
        num2 = str(num2)
        question = num1 +'-'+ num2
        return question
    elif operator==3:
        num1 = str(num1)
        num2 = str(num2)
        question = num1 +'*'+ num2
        return question
correct = 0
fail = 0
i = 0
while i<5:
    result = make_question()
    print(result)
    answer =  int(input("계산 결과의 답은 무엇입니까?"))
    if eval(result) == answer:
        correct +=1
    else:
        fail+=1
    i+=1
print('맞은갯수:',correct , '틀린갯수:',fail)
"""
