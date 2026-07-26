'''
#1.금액  입력
coin = int(input("금액을 입력하세여.(최대금액 10000원)"))

#1.1. 금액 부족한 경우

#
#drink = {1:700, 2:600, 3:800}#각버튼 마다 가격설정

if 600>= coin : #피드백 "제품금액따라 다양한데 무조건 600원은 좋지 않음."
    print("")
#1.2. 최대금액 초과 
elif coin >=10000 :
    print("최대 금액을 초과하였습니다.")
    print("10000원만 적용되며, 초과금액은 반환됩니다.")
    coin = 10000
    print("입금액 : ",coin)    

#1.3. 음료 설명
print("음료 설명"); print("1-사이다 700원"); print("2-콜라 600원"); print("3-오렌지쥬스 800원")

#2.음료 선택
choice = int(input("음료번호 : ") )

#3.잔액 출력
if choice == 1 and coin >= 700 :
    print("사이다 나왔습니다. 잔액:",coin-700)
elif choice == 2 and coin >= 600:
    print("콜라 나왔습니다. 잔액:",coin-600)
elif choice ==3 and coin >=800 :
    print("오렌지쥬스 나왔습니다. 잔액:",coin-800)
else :
    print("실시않음. 잔액:",coin)
    
'''

#텍스트 계산기 만들기

#사용자입력
user_in_1 = int(input("첫번째 숫자 :") )
user_in_2 = int(input("두번째 숫자 :") )
user_calcul = input("사용할 연산자(+,-,*,/ 중에서 택1) : ")


#연산자 체크
cal = ['+','-','*','/']
if user_calcul in cal :
    print("사용가능 연산자입니다.")
    if user_calcul == '+' : 
        print("+결과 : ", user_in_1+user_in_2)

    elif user_calcul == '-' : 
        print("-결과 : ", user_in_1-user_in_2)

    elif user_calcul == '*' :
        print("*결과 : ", user_in_1*user_in_2)

    elif user_calcul == '/' :
        if user_in_2 ==0 :
            print("0으로 나눌 수 없습니다!")
        else : 
            print("/결과 : ", user_in_1/user_in_2)    
#연산자 안될시 아예 종료처리.
else :
    print("사용불가 입력입니다")
    print("계산기 종료합니다.")




    
