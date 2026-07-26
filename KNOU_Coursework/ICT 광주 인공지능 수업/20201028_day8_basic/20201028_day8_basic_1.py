'''
start, stop = map(int, input("시작값, 종료값 숫자 2개입력 : ").split() )

if(start < stop) : #예외1 체크(시작값>종료값 여부 체크)
    print("start < stop 체크 : 정상 ")

    if(start>0 and stop<200) : #예외2 체크(입력값 1~200이내 체크)
        i = start
        while True :
            if  i % 10 ==3 :    #3으로 끝나는 숫자를 검증
                i += 1          #3으로 끝나도 일단 증가. continue 만나면 다시 첨부터 하니까.
                continue
        
            if i > stop :       #종료값까지 들어오면 종료.
                break
        
            print(i, end=' ')
            i += 1
            
    else : #예외2 처리
        print("[실행 불가] 시작값<0 또는 종료값>200이면 실행할 수 없습니다")
     #   break  #궁금부분-왜 break
        
else : #예외1 처리 
    print("[실행 불가] 시작값 > 종료값이면 실행할 수 없습니다")
    #   break #
'''

'''
for i in range(5) :
    for j in range(5) :
        print('j :', j , sep='', end=' ')
    print('i :', i,'\\n', sep='')
'''

'''
for i in range(5) :
    for j in range(5) :
        print("*", end='')
    print('', sep='')

print("")
'''

'''
for i in range(3) : 
    for j in range(7) :
        print("*", end='')
    print('', sep='')

print("")
'''


star=1
starMax=5
for i in range(5) :
    for j in range(starMax) :
        if j<star :    
            print("*", end='')
    star +=1
         
    print("") #개행





