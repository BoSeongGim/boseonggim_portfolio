'''
#small project7 구구단
for i in range(9) :
    print("2*",i+1,"=", 2*(i+1), end='  ' )
    print("3*",i+1,"=", 3*(i+1), end='  ' )
    print("4*",i+1,"=", 4*(i+1), end='  ' )
    print("5*",i+1,"=", 5*(i+1), end='  ' )
    print("6*",i+1,"=", 6*(i+1), end='  ' )
    print("7*",i+1,"=", 7*(i+1), end='  ' )
    print("8*",i+1,"=", 8*(i+1), end='  ' )    
    print("9*",i+1,"=", 9*(i+1), end='  ' )
    print()

#모범답안
for i in range(1,10) :
    for j in range(2, 10) :
        print(j, "x", i, "=", j*i, end="",)
'''

'''
votes = [2,5,3,4,1,5,1,5,5,3]
candidates= ["","전정국","김남준","박지민","정호석","김태형"]
result =[0,0,0,0,0,0]
for vote in votes :
    result[vote] += 1
print("result :",result)
print("Max :",max(result))
print("maxIndex",max(result))
#실행결과
print("후보가 총",max(result),"표를 얻어 당선되었습니다.")
'''


#초기값
votes = [2,5,3,4,1,5,1,5,5,3]
candidates= ["","전정국","김남준","박지민","정호석","김태형"]
counter =[0]*6

#투표집계
for x in votes :
    counter[x] +=1


#최대표 후보 찾기
max = 0
i =1
while(i <len(counter)) :
    if counter[i] > max :
        max = counter[i]
        elected = i
    i += 1

#실행결과
print(candidates[elected],"후보가 총",counter[elected],"표를 얻어 당선되었습니다.")




















