#print(divmod(5,2))

#print(float(5))
#print(float(1+2))
#print(float('5.3'))

#print(13+(22-3)*4)
#print(13+(((22-3)*4)/5) )


#연습문제 국립환경과학원 도로거리
#doro=12
#print(int(0.2467*doro+4.159))
#print("가장 시끄러운 층은=",int(0.2467*doro+4.159),"층")

# "," 대신에 "+"를 사용하면 에러가 납니다. 
#print("가장 시끄러운 층은="+int(0.2467*doro+4.159)+"층")
#TypeError: can only concatenate str (not "int") to str
#유정협9:31 AM "+는 문자열과 수열조합이여서 오류납니다"


a=2
b=3.14
c=a+b
print(a)
print(b)
print(c)
#"5.140000000000001"로 나온다.
#부동소수점으로 표현을 하는데 정밀도를 포기하고 메모리의 효율성을 높인것.
#정규화 또는 %.2f식으로 표현 소수점을 제한하면 조정가능.
#1970년대의 메모리 하나하나는 매우 중요했기에 어떻게든 아껴쓰려했던 문화에 유래함.
#C언어의 경우에는 %.2f식으로 깐깐히 해야 한다.
#현대에도 이는 매우 중요하다. 로봇제어등에서 소수점 하나로 울고 웃고 난리남...

print(round(c,2))
print("%.2f" % c)
print(a+b)
print(a,b,a+b,c)
a=10
print("a에 저장된 값은 ",a,"입니다.")


