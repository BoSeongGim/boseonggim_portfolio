'''
for i in range(5) :
    for j in range(5) :
        if j <= i :
            print('*',end='')
    print()
'''

'''
#대각선 그리
diagonal=0 #diagonal : 대각선 
for i in range(5) :
    for j in range(5) :
        if(j != diagonal) :
            print(' ',end='')
        
        elif(j == diagonal) :
            print('*',end='')
    # j END
    print()
    diagonal +=1        

for i in range(5) :
    for j in range(5) :
        if j == i:
            print('*', end='')
        else :
            print(' ',end='')
    print()
'''

'''
1개의 for문만으로
*
**
***
****
*****
를 그릴 수 있다.
힌트 : print('*' * 10)
출력 : ************
'''

'''
start =1
for start in range(5+1) :
    print('*'*start)

#모범답안
for i in range(5) :
    print('*' * (i+1) )
'''

'''
rowBlank=4
star=1
for i in range(4) : 
    for j in range(7) :
        if(j<rowBlank) :
            print(' ', end='')
            continue
        elif(star>0) :
            print('*', end='')
            star -=1
            continue
    #star등 값 재지정
    rowBlank -= 1
    star = 2*(i+2)-1
    print("star : ",star) #코딩 중 별 개수설정 확인용
    print()
'''
'''
#모범답안 ---------------
for i in range(1,5): #4줄에 맞춰 출력위함
    for j in range(5 - i) :
        print(' ', end='')
    for j in range(2 * i -1) :
        print('*', end='')
    print()
'''
#for 1개로만 해보기 모범답안
rows=4
for i in range(1,rows+1) :
    print('0'*(rows-i) + '*'*(2*i-1) )




















