'''
print("A :", ord("A"))
print("1 :", ord("1"))
print("a :", ord("a"))
'''

'''
print(chr(45))
print(chr(97))
print(chr(75))

s1,s2 = input('두 수를 입력하세요:').split()
#.split() 을 통해 2개의 입력 수신 가능(스페이스를 통해 구분함)

i1 = int(s1)
i2 = int(s2)
print('두 수의 합은 : ', i1+i2)
'''

'''
a,b = input("문자열 2개를 입력해주세요 : ").split(':')
#.split()가 ':'를 통해 구분하도록 함.
#(스페이스 이외의 입력으로 구분이 가능하도록 설정이 가능하다)

print(a)
print(b)
'''

'''
a,b = map(int, input("2개의 숫자를 입력하세요 : ").split(':'))
print(a+b)
'''

'''
i1,i2,i3,i4,i5 = map(int, input("5개의 값 입력 : ").split())
print("합은",i1+i2+i3+i4+i5)
'''

'''
kor,eng,math,sience = map(int, input("국어, 영어, 수학, 과학 점수 입력 : ").split())
print("평균 : ",int((kor+eng+math+sience)/4)) 
'''

'''
kor,eng,math,sience = map(int, input("국어, 영어, 수학, 과학 점수 입력 : ").split())
print("평균 : ",float(kor+eng+math+sience)/4)#float 안써도 동일.
'''

'''
print(1,2,3)
print('Hello',"python")
'''

print(1,2,3, sep=', ') #sep를 통해 출력할 대상들 간격마다 ', '를 붙여줌.   
print(4,5,6, sep=',')
print('hello','Python',sep='')#sep=''는 공백없음이다.
print(1920,1080,sep='x')

