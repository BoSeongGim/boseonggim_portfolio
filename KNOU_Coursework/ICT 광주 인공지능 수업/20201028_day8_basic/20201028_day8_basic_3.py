'''
for i in range(5) :
    for j in range(5) :
        if i>j :
            print('0',end='')
        else :
            print('*',end='')
    print()
#모범 답안
for i in range(5) :
    for j in range(5):
        if j < i :
            print(' ', end='')
        else :
            print('*', end='')
    print()
'''

'''
#역 이등변 삼각형
for i in range(5) :
    for j in range(9) :
        if(i>j) : 
            print(' ',end='')
        elif(i<=j and j<=(9-i-1) ) :
            print('*',end='')
            
    print()

'''

#입력한 숫자만 정삼각형 출력(20.10.28 오전11:27)
'''
nValue = int(input("숫자입력(정삼각출력)") )

for j in range(nValue) :
    for i in range(nValue -j) :
        print(' ',end='')
    for i in range(2*(j+1) - 1) :
        print('*', end='')
    print("")
'''

#FizzBuzz 내 작성문
for i in range(1, 100+1) : 
    if(i % 3 ==0 and i % 5 ==0 and i!= 0) :
        print("FizzBuzz")
    elif(i % 3 ==0 and i!= 0 ) :
        print("Fizz")
    elif(i % 5 == 0 and i!= 0) :
        print("Buzz")
    else :
        print(i)

#모범답안
for i in range(1, 101) :
    if i % 3== and i% 5 == 0 :
        print('FizzBuzz')
    elif i%3 == 0 :
        print('Fizz')
    elif i%5 ==0 :
        print('Buzz')

#참고모범답안-3의배수일때 /5의 배수일때 처리문
for i in range(1, 101) :
    if i % 3 == 0 :
        print('Fizz')
    if i % 5 == 0 :
        print('Buzz')
    else :
        print(i)



























