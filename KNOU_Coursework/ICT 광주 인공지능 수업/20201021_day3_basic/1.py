#1, 2, 3 출력(sep 사용)

#1,2,3 출력(sep 사용)

#1920X1080 출력(SEP사용)

'''
1
2
3
식으로 출력하시요(SEP사용)
'''

#국어,영어,수학,과학 점수를 차례로 입력하세요
#힌트 : map,input,split



#개행===============================================================
#print('1\n2\n3')

#개행 금지처리======================================================
#print는 end의 기본설정이 '\n'이다. 이를 제거하니 개행이 안되는 것.
'''
print(1, end='')
print(2, end='')
print(3)

print('a', end='')
print('b')
print('c')
'''



#연습문제=====================================================
'''
year = 2019
month = 1
day= 31
hour = 10
minute = 33
second = 57

print("실행결과 1")
print(year, month, day, sep='/')
print(hour,minute,second, sep=':')

print("실행결과 2")
print(year, month, day,'  ', sep='/' ,end='')
print(hour,minute,second, sep=':')
'''

#참/거짓 연산자
True # 소문자 true이면 정의없다고 에러남.
False

print(3>1)

print(10==10)
print(10!=5)
print('Python' == 'Python')
print('Python' == 'python')
print('Python' != 'python')

print("구분선1---------------------")
print(10>20)
print(10<20)
print(10>=10)
print(10<=10)


print("구분선2 ---------------------")
print(1==1.0)
print(1 is 1.0)
print(1 is not 1.0)














