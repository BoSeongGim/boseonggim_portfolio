'''
repeat = input("반복할 개수 : ")#증가폭 숫자 입력
print("repeat : ", repeat) #개인적 확인용

b=list(range(-10, 10+1,int(repeat)) )
print(b)
'''

start = input("시작할 숫자 : ",)
end = input("종료할 숫자 : ",)
repeat = input("반복할 개수 : ")#증가폭 숫자 입력
print("repeat : ", repeat) #개인적 확인용

b=list(range(int(start), int(end)+1,int(repeat)) )
print(b)
