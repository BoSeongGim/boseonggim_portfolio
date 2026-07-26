#if, elif, else 모두 사용하기 - elif,else 순서 주의하기
'''
#[주의] elif 앞에 else 가 오면 잘못된 문법이다.
if x == 10 :
    print('10입니다')
else :
    print('10도 20도 아닙니다.')
elif x == 20 : #elif 앞에 else 가 오면 잘못된 문법이다.
'''

'''
drink = input("마실 음료 : ") 

if( drink == '콜라' ) :
    print('콜라 내보낸다.')
elif(drink =='사이다' ) :
    print('사이다 내보낸다.')
elif(drink =='환타') :
    print('환타 내보낸다.')
else :
    print('해당 음료 없음')
'''

'''
#수업의 경우 음료들을 1,2,3번 버튼으로 표현.
button = int(input("마실 음료 : "))
if button == 1 :
    print('콜라')
elif button == 2 :
    print('사이다')
elif button == 3 :
    print('환타')
else :
    print('제공하지 않는 메뉴')
'''

'''
#1.금액 입력
#2.자판기의 음료 번호 선택
#3.잔액 계산

#1.금액 입력
money = int(input("자판기에 넣을 금액 : "))
print("money : ", money)


print("음료안내 :")
print(" 1번 : 콜라 : 600원")
print(" 2번 : 사이다 : 700원")
print(" 3번 : 환타 : 800원")

#2.자판기의 음료 번호 선택

select = int(input("음료 번호 : ") )

#3.잔액 계산
if (select == 1 ) :
    print("콜라", "잔액 :",money -600 )
elif(select ==2) :
    print("사이다", "잔액 :",money -700 )
elif(select == 3) :
    print("환타", "잔액 :",money -800 )
else :
    print("없는 음료 번호.", "잔액 : ",money)
'''

'''
x = int(input("숫자입력 : "))
#if( x>=11 and x<=20 ) :
if 11<= x <=20 : #[권고]이렇게 하는게 더 좋음.
    print("11~20")
#elif( x>=21 and x<=30 ) :
elif 21<= x <= 30 : #[권고]이렇게 하는게 더 좋음.
    print("21~30")
else :
    print("아무것도 해당하지 않습니다.")
'''

'''
age = int( input("나이 : ") )
balance = 9000 #교통카드 잔액

price_child = 650
price_middle = 1050
price_adult = 1250

# if (7<= age <= 12) : 
if 7<= age <= 12 : 
    print("초등생 요금 적용 : ", balance - price_child )
elif 13<= age <18 :
    print("청소년 요금 적용 : ", balance - price_middle )
elif age > 19 :
    print("성인요금 적용 : ", balance - price_adult)
'''

'''
x = int(input("입력 숫자 : "))
print("입력 : ",x)
if x%2 == 0 :
    print("짝수")
elif x%2 == 1 :
    print("홀수")
#나누기 연산자 % 써야 하는데 계속 mod쓰면서 삽질.... -_-;;
#아놔 divmod를 mod로 알아서 계속 안됬음... -ㅅ-;
'''

x = int(input("숫자 입력.(차후 +20처리) : "))
print("x+20 : ",x+20)

if 0<= x <= 255 :
    print("x : ",x)
else :
    print("max : 255(255초과시 무조건 255)")






















