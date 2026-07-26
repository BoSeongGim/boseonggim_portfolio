'''
#Enumerate를 사용하여 구할 수도 있다.
a=[10,20,30,40,20,50,20,30,60,70,20]
result = []

for i in range(len(a)):   #나의 경우  for i in a :로 했음.
    if a[i] == 20 :
        result.append(i)
print(result)


#count(값)을 통해 구하는 방법도 있찌.
a=[10,20,30,15,20,40]
print(a.count(20))


a = [10,20,30,15,20,40]
a.reverse()
print(a)
'''

'''
a = [10,20,30,15,20,40]

a.sort()
print(a)

a.sort(reverse=True) #a.reverse()와 같은 결과를 보여준다.
print(a)
'''

'''
#초기화 급으로 클리어 시키기.
a=[10,20,30]
a.clear()
print(a)

a=[10,20,30]
del a[:]
print(a)
'''

'''
#리스트를 슬라이스로 조작하기.
a=[10,20,30]
a[len(a):] = [500] #a[len(a):]는 "리스트 끝에서 하겠다"라는 의미.
print(a)

a=[10,20,30]
a[len(a):] = [1000,2000] #a.extend([500,600])과 같음.
print(a)
'''

'''
a=[0,0,0,0,0]
b=a #c언어의 포인터, 자바의 주소개념과 비슷하다. 별도의 배열이 만들어지는게 아니라,
    #하나의 동일한 주소를 가리키는 셈.(한 마디로 같은객체, 같은 주소인것.)

print(a is b) #True인 이유 : 하나의 동일한 주소를 가리키는 셈.(한 마디로 같은객체, 같은 주소인것.)

b[2] = 99
print("a : ",a)
print("b : ",b)
'''

'''
a = [0,0,0,0,0]
b = a.copy() #copy명령을 실시하면 별개의 배열을 생성하여 가리키는 주소가 다르다.

print(a is b)
b[2] = 999
print("a :",a)
print("b :",b)
'''

'''
a=[38,21,53,62,19]
for i in a :
    print(i)
print()

for i in [38,21,53,62,19] :
    print(i)
'''

'''
#index와 요소를 함께 출력하기 -enumerate()
a = [38,21,53,62,19]
for index, value in enumerate(a):
    print(index, value) #enumerate()는 요소값과 인덱스를 알려주니 매우 요긴함!!
print()
'''

'''
#enumerate(리스트,start=숫자) 'start=숫자'를 통해 인덱스 출력값을 설정할 수 있다.
a= [38,21,53,62,19]
for index,value in enumerate(a, start=1) :
    print(index, value)
print()
'''
"""
a=[10,20,30,40,20,50,20,30,60,70,20]
result=[]
for index,value in enumerate(a) :
    if(value == 20) :
        result.append(index)
        print("중간결과 : ",result)
print()

print("최종결과 : ",result)
"""

'''
a = [38,21,53,62,19]
i=0
while i <len(a): # while i <=len(a)로 리스트 범위를 벗어나기에 IndexError: list index out of range
    print(a[i])
    i+=1
'''


a=[38,21,53,62,19]

smallest= a[0]
for i in a :
    if i < smallest:
        smallest = i
print(smallest)


a=[38,21,53,62,19]

largest= a[0]
for i in a :
    if i > largest:
        largest = i

print(largest)


"""
a=[38,21,53,62,19]

a.sort()
print(a[0])

a.sort(reverse=True)
print(a[0])
"""






































































