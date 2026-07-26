"""
def add(x,y) :
    return x+y

def sub(x,y) :
    return x-y

def mul(x,y) :
    return x*y

def nanum(x,y) :
    return x/y

def namuzi(x,y) :    
    return x%y

def mainCal(x,y) : 
    print("함수 mainCal 실시. 실시.")
    if select ==1 :
        print("add 결과 : ", add(userIn_1,userIn_2) )
    elif select ==2 :
        print("sub 결과 : ", sub(userIn_1,userIn_2) )
    elif select ==3 :
        if x == 0 or y == 0 :
            print("[경고!] 0이 있는 경우는 연산할 수 없습니다!")
            print("[안내] 곱하기 연산은 실시않고 초기메뉴로 이동합니다.")
        else :
            print("mul 결과 : ", mul(userIn_1,userIn_2) )
    elif select ==4 :
        if x == 0 or y == 0 :
            print("[경고!] 0이 있는 경우는 연산할 수 없습니다!")
            print("[안내] 나누기 연산은 실시않고 초기메뉴로 이동합니다.")
        else :
            print("nanum 결과 : ", nanum(userIn_1,userIn_2) )
    elif select ==5 :
        if x == 0 or y == 0 :
            print("[경고!] 0이 있는 경우는 연산할 수 없습니다!")
            print("[안내] 나머지 연산은 실시않고 초기메뉴로 이동합니다.")
        else :
            print("namuzi 결과 : ", namuzi(userIn_1,userIn_2) )


print("===============================")
print("1.더하기")
print("2.빼기")
print("3.곱하기")
print("4.나누기")
print("5.나머지구하기")
print("6.나가기")
print("=================================")

exeSelect=1 #유저가 계속 실행여부
while exeSelect == 1 :
    select = int(input("원하는 연산자(계산)을 입력하세요. : ") )
    
    if 0>=select or select>6 : #연산자 코드부터 확인.
        print("1~6이내만 입력해주세요!")
    elif select == 6 :
        print("6.나가기 실행. 프로그램 종료입니다.")
        break
    else :
        userIn_1 = int(input("첫 번째 숫자를 입력하세요. : ") )
        userIn_2 = int(input("두 번째 숫자를 입력하세요. : ") )

        mainCal(userIn_1,userIn_2)
"""    

'''
#모범답안 - 5개의 함수 통합하기 전모습.

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

print("="*30)
print("1.더하기 \n 2.빼기 \n 3.곱하기 \n 4.나누기 \n 5.나머지구하기  \n 6.나가기 \n ")
print("="*30)

while True :
    menu = int(input("원하는 계산기 기능을 입력하세요.") )

    if(menu <= 5) :
        numberA = int(input("첫번째 숫자를 입력하세요.") )
        numberB = int(input("두번째 숫자를 입력하세요.") )

    if(menu == 1) :
        result = sum(numberA, numberB)
        print("결과는 %d 입니다.", %result)

    elif(menu == 2) :
        result = sub(numberA, numberB)
        print("결과는 %d입니다.", %result)

    elif(menu == 3) :
        result = mul(numberA, numberB)
        print("결과는 %d입니다.",%result)

    elif(menu ==4 ):
        result = div(numberA, numberB)
        print("결과는 %d입니다.",%result)

    elif(menu ==5 ):
        result = rem(numberA, numberB)
        print("결과는 %d입니다.", %result)

    elif(menu == 6) :
        break
    else :
        print("잘못입력하셨습니다. 다시 입력해주세요.")
'''


#모범답안 - 5개의 함수 통합 후 모습.

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
    menu = int(input("원하는 계산기 기능을 입력하세요.") )

    if(menu <= 5) :
        numberA = int(input("첫번째 숫자를 입력하세요.") )
        numberB = int(input("두번째 숫자를 입력하세요.") )

    if(menu == 1) :
        result = allcal(numberA, numberB,1)
        print("더하기 결과는 %d 입니다.", %result)

    elif(menu == 2) :
        result = allcal(numberA, numberB,2)
        print("빼기 결과는 %d입니다.", %result)

    elif(menu == 3) :
        result = allcal(numberA, numberB,3)
        print("곱하기 결과는 %d입니다.",%result)

    elif(menu ==4 ):
        result = allcal(numberA, numberB,4)
        print("나누기 결과는 %d입니다.",%result)

    elif(menu ==5 ):
        result = allcal(numberA, numberB,5)
        print("나머지 결과는 %d입니다.", %result)

    elif(menu == 6) :
        break
    else :
        print("잘못입력하셨습니다. 다시 입력해주세요.")



















