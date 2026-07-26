
'''
price = int(input("가격 :"))
coupon = input("쿠폰종류 : ")


if coupon =="Cash3000" :
    print("지불금액 : ",price-3000)
if coupon =="Cash5000" :
    print("지불금액 : ",price-5000)

if price is not coupon : 
    print("if문에 is, isnot는 객체끼리 비교시에 사용 가능.")
'''

'''
헝가리안 표기법(자료형+변수명)대로 하면
nMoney, 
strCpn 이라고 할 수 있다.
10만, 100만 라인식으로 프로그램이 엄청 커지면 변수의 유형을 잊을 수 있다.

하지만 최근에 헝가리안 표기법은 쓰이지 않는다.
자료형이 다양하거나 복잡하면 표기가 힘들어 변수명을 알기힘들게 하는 약점,
또한 최근에는 개발툴들이 좋아서 커서 올리면 바로 자료형을 뜨는 등을
생각하면 헝가리안은 한번 생각해봐야 할 문제.
'''

'''
number = int(input("짝수?홀수? : "))#0은 짝수임.
if(number%2 == 0) :
    print("짝수입니다")
if(number%2 == 1) :
    print("홀수입니다")
'''


x =5
if x == 10 :
    print('10입니다')
else :
    print('10이 아닙니다.')



x=5

if x == 10 :
    print("10입니다")
else :
    print('x에 들어있는 숫자는 ')
    print('10이 아닙니다')


x =10
if x == 10 :
    print('10입니다')
else :
    print('x에 들어있는 숫자는')
print('10이 아닙니다.')


if True :
    print('참')
else:
    print('거짓')

if False:
    print('참')
else:
    print('거짓')

if None:
    print('참')
else:
    print('거짓')


























