'''
x = int(input("숫자입력 : ") )
print("x : ", x)
if x-20 < 0 :
    print("min is 0")
else :
    print(x-20)
'''

'''
#[힌트] 문자열을 특정 위치 받기 위해 슬라이스를 사용합니다.
x = input("시간 입력(xx:xx식) :").split(':')
#난 스플릿으로 잘랐음;
#선생님은 약간 비추한 이유는 사용자가 ':'을 입력않을시(1300 식으로 입력시) 처리불가.

print(x) #입력값 저장 상태 확인.
print(x[1]) #분 부분 출력확인.

if(int(x[1]) == 00) :
    print("정각입니다")
else :
    print("정각 아닙니다")
'''

#슬라이스 활용법
#문자열[시작인덱스 : 끝인덱스]
#문자열[시작인덱스 : 끝인덱스 : 인덱스 증가폭]
#슬라이스 활용시 
'''
x = input("시간 입력(xx:xx식)")

print(x) #입력값 저장 상태 확인.
print(x[3:5]) #분 부분 출력확인.

if(int(x[3:5]) == 00) :
    print("정각입니다")
else :
    print("정각 아닙니다")
'''

'''
#선생님의 모범 답안
user_in = input("현재시간 : ")
if user_in[3:] == "00" : #3번째 자리부터 끝까지(분 단위 부분)
    print("정각 입니다.")
else :
    print("정각 아닙니다.")
'''


'''
fruit = ["사과","포도","홍시"]

rep = input("좋아하는 과일은?")

if rep =="사과" or rep =="포도" or rep =="홍시" :
    print("정답입니다!")
else :
    print("틀렸습니다")
'''

'''
모범 답안
#변수 in 자료구조를 활요하는 방식입니다
if user_in
'''

'''
warn_investment_list=["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]

user_stock=input("투자하실 종목 :")

if user_stock in warn_investment_list :
    print("투자 경고 종목입니다.")
else :
    print("위험 투자 아닙니다.")
'''

'''
fruit = {"봄":"딸기", "여름":"토마토", "가을":"사과" }

user_in = input("제가 좋아하는 계절은 : ")
#나의 답안(이렇게 작성해도 상관없는게 딕셔너리 기본적으로 key값을 비교한다.
if user_in in fruit :
    print("정답입니다!")
else :
    print("아쉽군요")
'''

'''#모범답안(.keys()를 활용하여 키값을 비교함)
fruit = {"봄":"딸기", "여름":"토마토", "가을":"사과" }
if user_in in fruit.keys() :
    print("정답입니다")
else :
    print("오답입니다")
'''

fruit = {"봄":"딸기","여름":"토마토","가을":"사과"}
#사용자가 입력한 값이 딕셔너리값(value)에 포함되었다면 정답, 아닐시 오답.
user_in = input("좋아하는 과일은?")
if user_in in fruit.values() :
    print("정답입니다")
else :
    print("오답입니다")
















