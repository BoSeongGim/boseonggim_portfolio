
#quiz7
'''
userInPrice = int(input("제품가격 : "))
userInCash = input("캐시쿠폰 : ")
if userInCash == 'Cash3000' :
    print("지불금액 : ", userInPrice - 3000)
elif userInCash == 'Cash5000' : 
    print("지불금액 : ", userInPrice - 5000)
'''


'''
userIn = int(input("짝홀수 구분 :") )

if userIn % 2 == 0 :
    print(userIn,"는 짝수입니다.")
else :
    print(userIn,"는 홀수입니다.")
'''

#논리연산자 활용 
'''
written_test = 75
coding_test = True

if (written_test >=80 and coding_test == True) :
    print("합격")
else :
    print("불합...ㅠㅠ ")
'''

"""
#나의 버전 
kor,eng,math,sci = int(input("국어,영어,수학,과학 점수 : ").split() )
if kor >=0 and kor <=100 and eng >=0 and eng <=100 and math >=0 and math <=100 and sci >=0 and sci<=100 :
    total = kor+eng+math+sci
    avg = total / 4

    if avg >= 80 :
        print("합격")
    else :
        print("불합격")        

else :
    print("점수는 0~100 사이만!")


#모범 답안 

kor= int(input("국어 점수 : "))
eng= int(input("영어 점수 : "))
math= int(input("수학 점수 : "))
sci= int(input("과학 점수 : "))
if 0<=kor<=100 and eng >=0 and eng <=100 and math >=0 and math <=100 and sci >=0 and sci<=100 :
    total = kor+eng+math+sci
    avg = total / 4

    if avg >= 80 :
        print("합격")
    else :
        print("불합격")        

else :
    print("점수는 0~100 사이만!")
"""

'''
userIn = int(input("숫자 1 :"))

if 11 <= userIn <= 20 :
    print("11~20")
elif 21<= userIn <= 30 :
    print("21~30")
else :
    print("nothing")
'''

"""
age = int(input("너의 나이는 : "))
card =9000
if age <7 : 
    print("나이의 입력은 7이상이어야 합니다.")
elif 7<= age <=12 :
    print("card : ",card-650)
elif 13<=age <=18 :
    print("card : ",card-1050)    
else :
    print("card : ",card-1250)
"""

'''
userIn = int(input("number :") )

cal = userIn-20
if (cal<0) :
    print("0")
elif cal >255 :
    print("255")
else :
    print(cal)
'''

'''
userIn = input("time : ").split(':')
# print(userIn)
if(userIn[1] == '00' ) :
    print("정각입니다.")
else :
    print("정각아닙니다.")
'''
apple = int(input("사과 갯수 : "))
mikan = int(input("귤의 갯수 : "))

if apple >= 10 :
    print("총액 : ", (apple*150)-(apple*150*0.1) + mikan*30 )

else :
    print("총액 : ", apple*150 + mikan*30 )







































