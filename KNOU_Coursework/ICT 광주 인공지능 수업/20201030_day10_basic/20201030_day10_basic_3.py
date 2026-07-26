#small project_4 XX학교의 학점별 인원표 출력 
'''
(예)입력 : 86 72 98 60 45 식으로 학생 성적 입력시
          # A, B, C, D, F학점
    출력 : [2, 1, 1, 1, 0]
'''
"""
scores = list(map(int, input("학생들의 성적들 :").split() ))
grade_counter = [0,0,0,0,0]

for score in scores :
    if(100 >= score >=85) :    #A
        grade_counter[0] +=1
    elif(84 >= score > 70 ) :  #B
        grade_counter[1] +=1
    elif(69 >= score > 55 ) :  #C
        grade_counter[2] +=1
    elif(54 >= score > 40 ) :  #D
        grade_counter[3] +=1
    else :                     #F
        grade_counter[4] +=1        
        
print("grad_counter(등급별 인원표) : ", grade_counter)
"""

#small project_5[나의 풀이] 이름 중에 m 또는 h 포함된 사람 인원 카운트
name_list = ['matthew', 'mark', 'luke', 'john','paul','peter']
count_mORh =0

for name in name_list :
    if(name.find('m') != -1) : #m이 포함되었다면 -1이외의 숫자출력. 
        print(name)
        count_mORh +=1
    elif(name.find('h') != -1) : #h이 포함되었다면 -1이외의 숫자출력. 
        print(name)
        count_mORh +=1
        
#실행결과 
print("m또는 h가 이름에 포함된 사람은",count_mORh,"명 입니다")
#구분선---------------------------------------------------------------

#small project_5[모범 답안]
name_list = ['matthew', 'mark', 'luke', 'john','paul','peter']
count = 0

for name in name_list : # name_list 에서 'matthew'등의 이름을 꺼냄.
    for n in name :     #꺼낸 이름이 'matthew'라면 m,a,t,t,e,w순으로 1개씩 비교. 
        if n == 'm' or n == 'h' :
            count +=1
            break

print("[모범답안] m또는 h가 이름에 포함된 사람은",count,"명 입니다")









































