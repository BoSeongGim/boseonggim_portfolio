#24.2 문자열 서식 지정자(%s)와 포매팅 사용하기
"""
# %s
print('I am %s.' %'james')


name = 'maria'
print('I am %s.' % name)

# %d
print('I am %d years old.' % 20)

#일부러 형을 안 맞추면?
print('I am %s' % 20) #걍 스트링형 처리한거 같다.
#print('I am %d' % 'mariya') #형 안맞는다고 에러.


# %f ( '%f' % 실수형숫자)

print('%f' % 2.3)   #출력결과 : 2.300000
print('%.2f' %2.3)  #출력결과 : 2.30
print('%.3f' %2.3)  #출력결과 : 2.300


#%뒤에 숫자를 작성=문자열을 숫자만큼의 길이로 만든 후 우측정렬.(#좌측에 빈칸나는 이유)
print('%10s' % 'python')

#왼쪽 정렬
print('%-10s' % 'python')
"""

#서식지정자로 문자열 안에 여러 개 값 넣기.
print('Today is %d %s.' % (3, 'April') )

print('Today is %d%s.'%(3,'April') )



#format매서드 사용하기
#'{인덱스}'.format(값)
print('Hello, {0}'.format('World!') )
print('Hello, {0}'.format(100) )


print('Hello, {0} {2} {1}'.format('Python','Script',3.6))
print('{0} {0} {1} {1}'.format('Python', 'Script') )

print('Hello, {} {} {}'.format('Python', 'Script', 3.6))

print('Hello, {language} {version}'.format(language='Python', version=3.6))

print('TEST, {language} {version}'.format(language='Java',
                                          version=7.7))


language='Python'
version = 3.6

#맨 앞의 f는 포매팅이라는 뜻으로 f를 붙임.
print(f'Hello, {language} {version}') #파이썬 3.6미만시 지원않아서 에러남...


print('{0:<10}'.format('python')) #{0:<10} :길이를 10으로 정하고, 왼쪽정렬한다.
print('{0:>10}'.format('python')) #우측정렬.
print('{0:<10} {2:>10} {1:<10}'.format('python','abc',123))

print('%03d' % 1)
print('{0:03d}'.format(35) )


print('%08.2f' % 3.6)
print('{0:08.2f}'.format(150.37))

print('{0:0<10}'.format(15)) #길이10, 왼쪽으로 정렬하고 남는 공간은 0으로 채움.
print('{0:0>10}'.format(15) )#길이10, 오른쪽으로 정렬하고 남는 공간은 0으로 채움.
print('{0:0>10.2f}'.format(15))#길이 10, 오른쪽으로 정렬, 소수점 자릿수는 2자리.

print('{0:10}'.format(15) )
print('{0:>10}'.format(15) )
print('{0:x>10}'.format(15))











