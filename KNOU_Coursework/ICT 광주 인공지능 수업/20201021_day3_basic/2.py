#궁금사항
print("구분선3 ---------------------")

a=10
b=10
c=3333

print("a==b       : ", a==b)
print("a!=b       : ", a!=b)
print("a is b     : ", a is b)
print("a is not b : ", a is b)
# ==, != : 값 자체를 비교한다.
# is, is not : object(객체)를 비교한다. 
#=========================================

#논리연산자
#1)and
'''
print(True and True)
print(True and False)
print(False and True)
print(False and False)
'''

#2)or
'''
print("OR")
print(True or True)
print(True or False)
print(False or True)
print(False or False)
'''

#3)not
'''
print("not")
print(not True)
print(not False)
'''


#4)복합연산
print("연산자들 복합연산 ")
print(((not True) and False) or (not False))


print( (10==10) and (10 !=5) )
print( (10>5) or (10<3) )
print( not(10>5) )
print( not(1 is 1.0) )




# bool
# 0만 거짓이고, 0이외는 참이다(#힘내라 0... ㅠ)
print("bool---------------------------")
print( bool(1) )
print( bool(0) )
print( bool(1.5) )
print( bool( 'False' ) ) 
print( bool('') )
print( bool(' ') )



# *중요* 단락평가
print("단락평가=======================================")
print("단락평가-AND-------")
print( True and 'Python' )


print( 'Python' and True )
print( 'Python' and False )

print( False and 'Python' )
print( 0 and 'Python' )


print("단락평가-OR -------")
print( True or 'Python' )
print( 'Python' or True )

print( False or 'Python' )
print( 0 or False )

#연습문제

korean =92
english = 47
mathematics  =86
science = 81
print("연습문제")
print((korean >=50) and english >=50 and mathematics >=50 and science>=50 )


print("연습문제2")
korean, english, mathematics, science = map(int, input("국어,영어,수학,과학 입력 : ").split())
print(korean >=90 and english >80 and mathematics >85 and science >= 80)












