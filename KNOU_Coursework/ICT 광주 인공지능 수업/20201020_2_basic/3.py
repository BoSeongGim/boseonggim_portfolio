'''
a=10
b=20
c=a+b
print(c)


a=10
a=a+20
print(a)


a=10
print(a+20)
print(a)
'''

'''
number = input("숫자를 입력하세요 : ") #input : 사용자의 입력을 받는 함수.(단, 문자열로 처리)       
print(number)
'''

'''
number1 =int(input("숫자를 입력하세요_1 : "))
#input만 쓰면 문자열임. #int()로 형변환 해야 비로소 숫자(정수)가능.
number2 = int(input("숫자를 입력하세요_2 : "))
#input의 ""는 사용고객들에게 안내를 위한 안내문 기입용이다. 
sum=number1+number2
print(sum)
'''

'''
name=input("이름을 입력하시오:")
print(name,"씨, 안녕하세요?")
print("파이썬에 오신것을 환영합니다.")
'''

'''
name=input("이름을 입력하시오:")
print(name,"씨, 안녕하세요?")
print("파이썬에 오신것을 환영합니다.")
number1=int(input("첫 번째 정수를 입력하시오:"))
number2=int(input("두 번째 정수를  입력하시오:"))
sum=number1+number2
print(number1,"과", number2,"의 합은",sum,"입니다.")
'''

place = input("경기장은 어디입니까? : ")
win = input("이긴 팀은 어디입니까? : ")
lose = input("진 팀은 어디입니까? : ")
mvp = input("우수 선수는 누구입니까? : ")
score = input("스코어는 몇대몇입니까? : " )

print("[기사내용]==================================")
print("오늘",place,"에서 야구 경기가 열렸습니다")
print(win,"과",lose,"은 치열한 공방전을 펼쳤습니다")
print(mvp,"이 맹활약을 하였습니다")
print("결국",win,"이",lose,"를",score,"로 이겼습니다")




















