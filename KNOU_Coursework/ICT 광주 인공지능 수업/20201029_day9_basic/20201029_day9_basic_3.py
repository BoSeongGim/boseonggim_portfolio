#quiz_1
'''
print("print for")
for i in range(10) :
    print(i+1, end='  ')
print()

print("print while")
j=0                         #1.초기식
while j < 10 :              #2.조건식
    print(j+1, end='  ')    #3.반복코드
    j+=1                    #4.변화식(증감값)
'''

'''
#quiz_2
sumByFor=0
for i in range(11) :
    sumByFor+=i
print("sumByFor 1부터 10까지의 합 : ",sumByFor)

sumByWhile = 0
j=0
while j<11 :
    sumByWhile +=j
    j+=1
print("sumByWhile 1부터 10까지의 합 : ",sumByWhile)
'''

'''
#quiz3
x=[49, -17, 25, 102, 8, 62, 21]
for i in range(len(x) ):
    print(x[i]*10)

lenX = len(x)
j=0
while j <lenX :
    print(x[j]*10)
    j+=1
'''

'''
#quiz4
gugu = int(input("구구단 숫자 : "))

for i in range(1,9+1) :
    print(gugu, "x", i, "=",gugu*i )

j=1
while j < 10 :
    print(gugu, "x", j, "=",gugu*j )
    j+=1
'''

'''
#quiz5
marks =[90, 25, 67, 45, 80]

print("quiz5_for")
for i in range(len(marks)):
    print("점수:",marks[i])
    if(marks[i] >60) :
        print("합격입니다!")
    else :
        print("불합격... ㅠ")

print("------------------------------")

print("quiz5_while")
j=0
while j<len(marks):
    print("점수:",marks[j])
    if(marks[j] >60) :
        print("합격입니다!")
    else :
        print("불합격... ㅠ")
    j+=1
'''

#quiz6 (#continue활용)
'''
marks =[90, 25, 67, 45, 80]

print("quiz6_for")
for i in range(len(marks)):
    print("점수:",marks[i])
    if(marks[i] >60) :
        print("합격입니다!")
        continue
    print("불합격... ㅠ")

print("------------------------------")
'''


Kor =[ 70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

total = 0
for i in range(len(Kor) ) :
    total += Kor[i]
print("학급 총점 : ", total)    
print("학급 인원 : ", len(Kor) )
print("학급 평균 : ", total /len(Kor) )
















