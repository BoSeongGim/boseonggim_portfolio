'''
def plus_ten(x) :
    return x +10

print(list(map(plus_ten, [1,2,3]) ) )

print( list(map(lambda x : x +10, [1,2,3] ) ) )
'''
"""
a=[1,2,3,4,5,6,7,8,9,10]

print(list(map(lambda x: str(x) if x % 3 == 0 else x, a) ) )

a=[1,2,3,4,5,6,7,8,9,10]
print( list(map(lambda x : str(x) if x == 1 else float(x) if x ==2 else x +10, a) ) )

"""

'''
def f(x) :
    if x == 1 :
        return str(x)
    elif x ==2 :
        return float(x)
    else :
        return x +10

a= [1,2,3,4,5,6,7,8,9,10]
print(list(map(f,a) ) )
'''
"""
a = [1,2,3,4,5]
b = [2,4,6,8,10]

print(list(map(lambda x, y : x*y, a,b) ) ) 

"""

'''
def f(x) :
    return x > 5 and x <10

a=[8,3,2,10,15,7,1,9,0,11]
print(list(filter(f,a) ) )
'''
"""
a=[8,3,2,10,15,7,1,9,0,11]
print(list(filter(lambda x: x>5 and x<10, a) ) ) 
"""

'''
def f(x,y) :
    return x +y

a = [1,2,3,4,5]
from functools import reduce

print( reduce(f,a) )
'''

"""
a = [1,2,3,4,5]
from functools import reduce

print(reduce(lambda x, y: x+y , a ) )
"""
'''
x =10
def foo() :
    print(x)
print(x)

def foo() :
    x = 10
    print(x)

foo()
# print(x)#에러 #지역변수이므로 사라져서 출력 불가.
'''

x =10
def foo() :
    x = 20
    print(x)

foo()
print(x)























