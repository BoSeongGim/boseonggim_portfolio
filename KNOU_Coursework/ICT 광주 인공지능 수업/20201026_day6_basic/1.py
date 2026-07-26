#2020.10.26 AM09:00(도서관 휴관으로 수업수강에 차질 발생)
#book 14.1
x = 5
if x == 10 :
    print('10입니다.')
else : #[주의] else : 이외 형태는 불가.
    print('10이 아니므니다.')

x = 5
#print("y : ",y) #실행시 에러남.(y값 미정의)

if x == 10: #신기하게 에러 안남(y값 미정의)
    y=x 
else :
    y=0
    print("y : ",y)

#2020.10.26 AM09:15부터 ==========================================================================
'''
x = 10
if x > 0 :
    if x < 20 :
        print("20보다 작은 양수입니다. if 2번 ")

if x > 0 and x < 20 :
    print("20보다 작은 양수입니다. 중첩 if ")


written_test = 75
coding_test = True

if written_test >=80 and coding_test==True :
    print("경축! 합격!!!")
else :
    print("불합 재도전 ㅠㅠ")
    

kor, eng, math,sci = map(int, input("국,영,수,과 점수 입력 : ").split())
print("kor, eng, math,sci : ",kor, eng, math,sci)
if kor <0 or kor > 100 or  eng <0 or eng > 100 or math <0 or math > 100 or sci <0 or sci > 100 :
    print("0~100만 입력!")
else :
    avg = (kor+eng+math+sci) /4
    print("평균 : ", avg)
    if avg >= 80 :
        print("경축! 합격!!! >ㅂ<")
    else :
        print("불합 재도전 ㅠ_ㅠ")
'''
#15.1 elif 사용하기

x = 20
if x == 10 :
    print('10입니다.')
elif x == 20 :
    print('20입니다.')


x= 30
if x == 10 :
    print('10입니다')
elif x ==20 :
    print('20입니다')
else :
    print('10도 20도 아닙니다.')



        
