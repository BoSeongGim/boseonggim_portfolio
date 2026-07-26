"""
x= 10
y= 3

def get_quotient_remainder(x,y) :
    quotient = int(x/y) #출력결과 :3 나오기위해 형변환 실시.
    remainder = x%y
    return quotient, remainder

quotient, remainder, = get_quotient_remainder(x,y)
print('몫: {0}, 나머지: {1}'.format(quotient, remainder) )
"""

'''
x,y = map(int, input("숫자 2개 입력 : ").split() )

def calc(x,y) :
    add = x+y
    sub = x-y
    mul = x*y
    div = x/y
    return add, sub, mul, div

a,s,m,d = calc(x,y)
print("덧셈:{0}, 뺄셈:{1}, 곱셈:{2}, 나눗셈{3}".format(a,s,m,d) )
'''

"""
def plus_ten(x) :
    return x +10

print(plus_ten(1) )

lambda x : x+10
print(lambda x : x+10)
"""

"""
#람다표현식 호출 - 변수할당 
plus_ten = lambda x : x+10
print(plus_ten(1))
"""

"""
print( (lambda x: x + 10)(1) )

y=10
print( (lambda x: x+y)(1) )
"""

"""
def plus_ten(x) :
    return x +10
print(list(map(plus_ten, [1,2,3] ) ) )

print(list(map(lambda x: x +10, [1,2,3] ) ) )
"""



















