'''
a = (38,21, 53,62,19)
print(a)

a=38, 21, 53, 62, 19
print(a)
'''

'''
a = tuple(range(10))
print(a)

b = tuple(range(5,12))
print(b)

c = tuple(range(-4,10,2))
print(c)


a = [1, 2, 3]
print("list a :", a)
print("tuple a :",tuple(a))

b= tuple(a)
print("tuple b by a",b)


b=(4,5,6)
print("change b tuple->list : "list(b))
'''

#print(list('Hello'))  # ['H', 'e', 'l', 'l', 'o'] 출력됨.
#print(tuple('Hello')) # ('H', 'e', 'l', 'l', 'o')

'''
a,b,c = [1, 2, 3]
print(a,b,c)
print(type(a))

d,e,f = (4,5,6)
print(d,e,f)



x=[1,2,3]
a,b,c = x
print(a,b,c)

y = (4,5,6)
d,e,f = y
print(d,e,f)



print(input().split())
x= input().split()
print("x : ",x)
a,b=x
print(a,b)
'''

#연습문제
#a = list(range(5,-9-1,-2) )
#print(a)


repeat = input("반복할 개수 : ")#증가폭 숫자 입력
print("repeat : ", repeat) #개인적 확인용

b=list(range(-10, 10+1,int(repeat)) )
print(b)










