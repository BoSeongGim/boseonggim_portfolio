'''
a=[10,20,30]
a.pop(1) #pop(인덱스)는 요소를 삭제한 뒤 삭제한 요소를 반환한다고 한다.
print(a)

a=[10,20,30]
del a[1] #pop() 대신 del을 사용해도 된다.
print(a)
'''

'''
#remove
a= [10,20,30]
a.remove(20)
print(a)

#똑같은 값이 여러개 있어도 remove는 맨처음 발견만 삭제후 종료.
a=[10,20,30,20]
a.remove(20)
print(a)
'''

'''
#리스트로 스택 만들기
a = [10,20,30] # 기존스택에 보관데이터

a.append(40) #스택에 40추가
print(a) #결과확인

a.pop(3) #스택의 40을 다시 꺼냄.
print(a) #결과확인

#요구하신 답.(처음부터 빈 리스트에서 시작.&모두 빼낼것.)
a=[]

a.append(10)
print(a)
a.append(20)
print(a)
a.append(30)
print(a)
a.append(40)
print(a)

a.pop() ; print(a)
a.pop() ; print(a)
a.pop() ; print(a)
a.pop() ; print(a)


for i in range(4) :
    i += 1
    a.append(i*10)
    print(a)
for i in range(4) :
    a.pop()
    print(a)

'''

#큐 구조 만들기->추가는 동일, 추출만 pop(0)으로 다름.(스택이랑 동일하니 생략..)

'''
#index(찾을 값)->결과물 : 찾을 값의 위치.
a=[10,20,30,15,20,40]
print(a.index(20)) #동일 값이 여러개 있어도 맨첨에 찾은애만 알려줌... -_-;
#print(a.index(100)) # ValueError: 100 is not in list 식으로 없는 값이라고 에러.
'''
'''
a=[10,20,30,40,20,50,20,30,60,70,20]
print(a)
#length=len(a)
saveIndex=[] #찾은 위치값 저장.

for i in a :
    saveIndex.append(a.index(20))
    print("saveIndex:",saveIndex)
    a.pop(a.index(20))
    a.insert(i,100)
    print(a)
print("실행결과 : ",saveIndex)
'''


#모범답안
nAdd = 0
a=[10,20,30,40,20,50,20,30,60,70,20]

result=[]

while True :
    if 20 in a :
        ni = a.index(20)        #; print("a.index(20) : ",a.index(20)) #값20이 있는 인덱스 위치 확인 
        result.append(ni+nAdd)  # pop을 통해 빼내지 않으면 최초의 20만 계속 검색.
        #print("result.append(ni+nAdd) : ",result.append(ni+nAdd))
        print(a) #개인적으로 확인위해 추가.

        a.pop(ni)              # ; print("a.pop(ni) : ",a.pop(ni))
        nAdd += 1
    else :
        break
print("20이 있는 인덱스 : ",result)
    

#다른 분들의 경우

for i in a :
    if i ==20 :
        b.append(a.index(i))
        del a[a.index(i)]
        a.insert(0,1)
    else :
        continue
        











































