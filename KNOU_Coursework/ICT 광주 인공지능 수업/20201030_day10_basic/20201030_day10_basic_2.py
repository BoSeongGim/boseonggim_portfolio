#small project_1
#두 자연수 n,m 입력 받고 n~m까지의 합을 구하는 프로그램 작성
'''
start=int(input("시작하는 정수 입력 : "))
end = int(input("끝나는 정수 입력 : "))
total = 0
for i in range(start, end+1) :
    total += i
print(start,"부터",end,"까지의 합은 ",total,"입니다")
'''

'''
#small project_2
#두 자연수 n,m 입력 받고 n~m까지의 짝수들의 제곱의 합을 구하는 프로그램 작성
start=int(input("시작하는 정수 입력 : "))
end = int(input("끝나는 정수 입력 : "))
total = 0
for i in range(start, end+1) :
    if(i %2 ==0 ) : 
        total += i**2 #i의 제곱
        
print(start,"부터",end,"까지의 짝수 제곱의 합은 ",total,"입니다")
'''



#small project_3
#[목표] 학생의 5과목 최종 실 성적 입력후 평균을 계산.
scores=[]
scores = list( map(int, input("5개의 성적 : ").split() ) )
#list(map(int, input().split()))
#print(scores)


total =0; 
scoreMin = 100;
scoreMax = 0;
for score in scores :
    #1.모든 과목의 점수의 합을 구하세요.
    total += score    

    #2. 최고 점수를 구합니다.
    if score > scoreMax :
        scoreMax = score

    #3. 최저 점수를 구합니다.
    if score < scoreMin :
        scoreMin = score


#4. (모든 과목 점수의합) - (최고점수) - (최저점수) #최고/최저는 직접할 것.
print("scoreMax : ",scoreMax)
print("scoreMin : ",scoreMin)
print("최종 실기 평균 : ",(total - scoreMax -scoreMin)/len(scores)-2 ) #최고,최저점수 과목2개 제외.


        




































