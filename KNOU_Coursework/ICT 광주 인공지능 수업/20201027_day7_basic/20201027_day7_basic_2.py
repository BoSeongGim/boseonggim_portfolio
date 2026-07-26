#문자열을 뒤집어서 출력할 때 resersed
'''
for letter in reversed("Python") :
    print(letter, end=' ')
print("")#개행 용도  
    
letter = 'Python'
for i in reversed(letter) :
    print(i, end=" " )
print("")#개행 용도  

x = [49, -17, 25, 102, 8, 62, 21]
for i in x :             #x리스트에서 i번째 셀을 꺼낸다.
    print(i*10, end=" ") #꺼낸 i번째 셀을 10곱하여 출력.
print("")#개행 용도  
'''

'''
gugudan = int(input("출력할 구구단 : ") )

for i in range(1,10) : # 2*1=2 ...2*9=18 식으로 뒤의 숫자는 1~9이니까 range실시.
    print(gugudan," * ", i , " = ", gugudan*i)
'''

'''
print("0부터 입력한 정수까지의 합계를 출력.")
user_in = int(input("정수 1개 입력 : ") )
total = 0

for i in range(0,user_in+1) : #사용자는 입력한 숫자까지의 합계를 원할것이기에 마지막 숫자까지 계산에 포함하도록 user_in에 +1함.
    total = total+ i
print("total :", total)
'''

'''
i=0                         #while초기식 / for은 않는 방식.
while i < 100 :             #while조건식 / for i in range(100) : 
    print("Hello World",i)  #반복할 코드(이건 동일) 
    i += 1                  #변화식(증감식) /for은 생략. range등에서 알아서 증감하니까.
'''

'''
초기식
while 조건식 :
    반복할 코드
    변화식(증감식)
'''

'''
#1~100출력 
i=1
while i < 101 :
    print("Hello world", i)
    i+=1
'''

#100~1 출력 
'''
k=100
while k>0 :
    print("Hello World",k)
    k-=1
'''

repeat = int(input("반복할 횟수를 입력하세요 : ")) #초기값 역할
count = 1
while count <repeat+1  :
    print("count : ",count)
    count += 1
















































