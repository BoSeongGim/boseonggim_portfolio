#리스트와 튜플 응용하기

#리스트, 튜플은 모두 객체에 해당하며 다양한 기본제공 기능들이 있다.
#요소를 추가/삭제/조회 하는 메서드를 제공


# append : 요소 하나를 추가.
# extend : 리스트를 확장

'''
a= [10,20,30]

a.append(500)

print(a)
print(len(a))
'''

'''
a=[]
a.append(10)
print(a)

#append 응용(선생님 한줄평 : 꼭! 어펜드 기억해주세요!)
#0~9의 요소를 가지는 리스트
a=[]
for i in range(10) :
    a.append(i)
print(a)
    
b=[]
#10~100의 요소를 가지는 리스트
for i in range(10,110,10) :
    b.append(i)
print(b)

#1~100에서 짝수만 넣기.
c=[]
for i in range(1,101) : 
    if i % 2 == 0 :
        c.append(i)

print(c)

#if문 안쓰고도 가능함.
tc=[]
for i in range(51) :
    tc.append(i*2)
print(tc)
'''
'''

#리스트 안에 리스트 추가하기.

a= [10,20,30]

a.append([500,600])

print(a)
print(len(a)) #리스트속의 리스트도 1개의 요소로 취급된다.
'''
'''
a = [10,20,30]

a.extend([500,600])

print(a)
print(len(a))
'''

'''
#insert - 추가인데 내가 원하는 포인트(요소)에 추가 할 수 있따.
a=[10,20,30]

a.insert(2,500) #맨 앞자리는 0부터 시작함.

print(a)
print(len(a))


#있는 위치에 insert하면?->밀어내기 실시.

a=[10,20,30]

a.insert(0,600)
print(a)
print(len(a))

#리스트 끝에 추가하고 싶다면?->요소 위치를 len(a)로 하면 된다.
a=[10,20,30]
a.insert(len(a), 500)
print(a)
'''

'''
a=[10,20,30]
a.insert(1,[500,600]) #insert넣을 요소가 리스트면 append처럼 리스트 속의 리스트 넣기 가능.
print(a)
print(len(a))

a=[10,20,30]
a[1:1]=[500,600]
print(a)
'''


#
a=[10,20,30]
print(a.pop())#a.pop()=특정 요소지정없음=마지막 요소를 자동삭제함.
print(a)
























