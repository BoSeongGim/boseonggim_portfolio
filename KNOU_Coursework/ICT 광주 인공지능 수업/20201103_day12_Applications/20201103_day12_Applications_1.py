#리스트에 map사용하기

"""
a=[1.2, 2.5, 3.7, 4.6]

for i in range(len(a)):
    a[i] = int(a[i])#형변환을 실시. int(1.2) => 1을 받는식으로 소수점이상만 받음.
    
print(a)
"""

'''
a=[1.2, 2.5, 3.7, 4.6]
a = list(map(int, a))
print(a)
'''

"""
a=list(map(str, range(10) ))#map을 통해 0~9가 str형으로 변경되어 list에 입력된다.
print(a)
"""

'''
print("map을 사용해서 정수로 변환해보기(input()썼으니 숫자값 입력하세요))"
a=map(int, input().split())
print(a)
print(list(a))
'''

"""
x = input().split()
m = map(int,x)     #문법적으로 실수->정수형으로 변경은 불허..?
a,b = m

print(a, b)
"""

"""
a=(38, 21, 53, 62, 19, 53)
print(a.index(53))
"""

'''
a=(10, 20, 30, 15, 20, 40)
print(a.count(20))
'''

"""
a=(38, 21, 53, 62, 19)

for i in a :
    print(i, end=' ')
print()

i=0#궁금해서 초기값 않으니 19로 임의들어가더라.
while i <len(a) :
    print(a[i], end=' ')
    i=i+1
"""

'''
a = tuple(i for i in range(10) if i % 2 ==0 )
print(a)

print( (i for i in range(10) if i % 2 ==0 ))
'''

"""
a = (1.2, 2.5, 3.7, 4.6)
a = tuple(map(int, a) )
print(a)
"""
'''
a = (38, 21, 53, 62, 19)
print(min(a))
print(max(a))
print(sum(a))
'''

"""
a = ['alpha', 'bravo', 'chalie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india']
b = [i for i in a if len(i) ==5 ]
print(b)
"""

"""
#참고 - 리스트 표현식+if조건문
a=[i for i in range(10) if i %2 ==0 ]
#   | ④ |  ② | ①         |   ③
# ① : 배열 0~9를 생성
# ② : 기존의 반복문처럼 0~9까지 하나씩 꺼냄.
# ③ : 하나씩 꺼낸 값을 조건문따라 비교한다.
# ④ : i라는 이름의 리스트를 생성
print(a)
"""

'''
inputNum1 = int(input("첫 번째 입력 정수(1~20) : "))
inputNum2 = int(input("두 번째 입력 정수(10~30) : "))

if( 1<=inputNum1 <=20 and 10<=inputNum2<=30) :
    result1 = [ 2**(i+1) for i in range(inputNum1) ]
    del result1[1] ; result1.pop(-2)
    print("result1 : ",result1)
    
    result2 = [ 2**(i+1) for i in range(10, inputNum2) ]
    del result2[1] ; result2.pop(-2)
    print("result2 : ",result2)
else :
    print("입력값이 범위를 벗어났습니다.")
'''

#모범답안
nData1, nData2 = map(int, input().split() )

if(nData1 < 1 and nData1 >20 ) :
    printf("1st data range error")
elif(nData2<10 and nData2>30 ):
    printf("2nd data range error")

else :
    MyList = [2**i for i in range(nData1, nData2+1) ]
    del MyList[1]
    del MyList[len(MyList)-2]
print(MyList)























