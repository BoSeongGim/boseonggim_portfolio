'''
hello = 'Hello, world!'
print(len(hello) )#스페이스도 문자로 취급한다.

hello_han = '안녕, 세계!'
print(len(hello_han))#바이트숫자가 아니라 실제로 표현되는 글자들의 숫자로 카운팅.

a = [38, 21, 53, 62, 19]
print( a[0] )
print( a[2] )
print( a[4] )

print(type(a) ) 
print( type(a[0]) )


b=(38,21,53,62,19)#튜플
print(b[0])


r = range(0,10,2)
print(r[2])


hello = "Hello, World!"
print(hello[7])



a=[38, 21, 53, 62, 19]
print(a[-1])
print(a[-5])


hello='Hello, World!'
print(hello[-4])


a=[38,21,53,62,19]
print(len(a))
#print(a[5])#에러예제,len(a)의 값은 갯수이기에 자리수에는 안맞다.
#C언어 경우 범위를 벗어나도 별도의 에러로 취급않지만 파이썬 경우 벗어남을 알려준다.
#len(a)로 하면 에러남. 갯수 센거와 시작 위치는 다르다.
print(a[len(a)-1])


#요소에 값을 할당하기
#리스트-요소에 접근하여 값변경 "가능"하다.
a=[0,0,0,0,0]
print(a)
a[0]=38
a[1]=21
a[2]=53
a[3]=62
a[4]=19

print(a)
print(a[0])
print(a[4])

#튜플,레인지,문자열은 변경불가  
b=(0,0,0,0,0)#튜플 = 리스트의 읽기 버전
print(b[0])
#b[0]=100

r=range(0,10,2)#메모리 할당 안되니까.
#r[0]=3

hello='Hello, World!'
#hello[4]="Q"

#요소 삭제

#리스트는 시퀀스 자료형 중 유일하게 삭제 가능.
a=[38,21,53,62,19]
del a[2]
print(a)

#튜플,레인지,문자열은 요소 삭제불가.
b=(38,21,53,62,19)
print(b[2])
#del b[2]
#print(b)

r=range(0,10,2)
#del r[2]

hello='Hello, World!'
#del hello[6]
'''

#슬라이스
#인공지능, 텐서플로우 할 때 슬라이스를 통해 자료의 일부를 자를 때 매우 중요!

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[0:4])
print(a[0:])
print(a[1:1]) #공란나옴 #인덱스에 1을 더 크게 지정해야 요소 1개를 가져온다.
print(a[0:1])
print(a[1:2])






































