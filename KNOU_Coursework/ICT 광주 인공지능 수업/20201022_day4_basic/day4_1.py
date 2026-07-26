# 시퀀스 객체 안에 특정값이 있는지를 확인하기
# 시퀀스 : 
'''
a=[0,10,20,30,40,50,60,70,80,90]
#값이 있으면 트루 없음 펄스
print(30 in a)
print(100 in a)

#특정 값이 없다면 트루, 없다면 펄스
print(100 not in a)
print(30 not in a)
print(43 not in (38, 76, 43, 62, 19) )
print(1 not in range(10) )
print('P' not in 'Hello, Python' )
'''

'''
aa = [1,3,5,7,9,11,13,15,17,19] #range리스트 못해서 일일 기입 -ㅅ-;;;
# a = list( range(1,20,2) )
#내가 만들때  a = range(1,20,2) 해서 리스트 형이 안되었다.
 
print(aa)
print(13 not in aa)
print(4 not in aa)
'''


'''
a = [0, 10, 20, 30]
b = [9, 8, 7, 6]
print(a+b)

a = [1,2,3]
b = (4,5)
print( a+list(b) ) 


a = [1,2]#내부값 1,2는 정수이다. 문자열1,2로 선언하려면 A=["1","2"]
b = [3,4]
c = a+b

print("c:",c)
print(a)
print(b)
print(c)

#range값을 연결시키고 싶다면 list,튜로 만들어야 한다.
#같은 시퀀스 계열이어도 예외가 있는것.
#range(0,10) +range(10,20)

print(list(range(0,10)) + list(range(10,20)))
print(tuple(range(0,10) ) + tuple(range(10,20)) )

print(str(range(0,10) ) + str(range(10,20)) )

print([0, 10, 20, 30]*3)
print(list(range(0,5,2))*3)
print(tuple(range(0,5,2))*3)
print('Hello, ' *3)
'''

a=[0,10, 20,30,40,50,60,70,80,90]
print(len(a))


b=(38, 76, 43, 62, 19)

print(len(b) )


print(type(a))
#아쉽게도 리스트 a내의 자료형은 확인 안되네..
#문의결과 리스트내의 인덱스에 직접 접근해야 한다고 하심.

print(len(range(0, 10, 2) ))




