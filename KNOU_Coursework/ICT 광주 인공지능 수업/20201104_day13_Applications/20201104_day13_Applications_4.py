'''
def add(a,b) :
    return a+b

x = add(10,20)
print(x)

print(add(10,20))
'''

"""
def mul(a,b,c) :
    return a*b*c

x,y,z= map(int, input("정수로 곱할 숫자 3개 입력:").split() )
print("입력 값 : " ,x,y,z)
print("곱 결과 : ",mul(x,y,z))
"""

'''
#값을 여러개 반환해야 하는 경우
def add_sub(a,b) :
    return a+b, a-b


x,y = add_sub(10, 20)
print("add :",x)
print("sub :",y)


x = add_sub(10, 20)
print("x:",x)#튜플이 반환된다는 사실을 알 수 있따.

x,y=(30,-10)#튜플이 언패킹 되는 예제. 함수도 이를 이용한 것이다.

print(x)
print(y)
'''

"""
def cal(in1, in2) :
    return in1+in2, in1-in2,in1*in2,in1/in2,

in1, in2= map(int, input("사칙연산위해 숫자 2개 입력 :").split() )
print("+,-,*,/결과 : ", cal(in1,in2) )

#각각 출력(언패킹)
summ,sub,mul,exp = cal(in1,in2)
print("+ 결과 : ", summ )
print("- 결과 : ", sub )
print("* 결과 : ", mul )
print("/ 결과 : ", exp )

#서식지정자로 출력
print("+ 결과 : %f ,- 결과 : %f , * 결과 : %f, / 결과 : %f", summ,sub,mul,exp)


#모범답안(서식지정자까지 실시)

def cal(nD1, nD2) :
    return nD1+nD2, nD1-nD2, nD1*nD2, nD1/nD2

nin1, nin2= map(int, input().split() )

fR1,fR2,fR3,fR4 = cal(nin1, nin2)

print("+= %f    -= %f    *= %f    /= %f" %(fR1,fR2,fR3,fR4))
"""

def mul(a,b) :
    c = a*b
    return c

def add(a,b) :
    c = a+b
    print(c)
    d = mul(a,b) #다른 함수 mul()을 호출하여 곱하기도 실시.
    print(d)

x = 10
y = 20
add(x,y)




















