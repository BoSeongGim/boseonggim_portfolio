#2차원리스트에서 for반복문 1번만 사용하여 출력해보기
'''
a =[[10,20], [30,40], [50,60] ]

for x,y in a :
    print(x,y)
'''

'''
a=[ [10,20], [30,40], [50,60] ]

for i in range(len(a)) :        #가로크기   
    for j in range(len(a[i])):  #세로크기
        print(a[i][j], end=' ')
    print()

'''

"""
#while반복문으로 출력.
a = [[10,20], [30,40], [50,60] ]

i=0
while i <len(a):
    x,y = a[i]
    print(x,y)
    i +=1
"""

'''
a = [ [10,20], [30,40], [50,60] ]

i = 0
while i < len(a) :                  #가로 크기
    j =0
    while j <len(a[i]) :            #세로크기
        print(a[i][j], end=' ')     
        j+=1                        #가로인덱스를 1증가.(동일행의 오른쪽으로 이동)
    print()
    i +=1                           #세로인덱스를 1증가.(새로운 행으로 시작하도록 함)
'''

"""
a=[[1,2,3], [5,6,7], [8,9,10], [12,13,14] ]

print("for문으로 실시.")
for x,y,z in a :
    print (x,y,z)

print("while문으로 실시.")

i=0
while i <len(a) :
    x,y,z = a[i]
    print(x,y,z)
    i +=1
    

#모범답안
#for문
a=[[1,2,3], [5,6,7], [8,9,10], [12,13,14] ]
for aa in a :
    for aaa in aa :
        print(aaa, end=' ')
    print()

#while
i=0
while i len(a):
    j=0
    while j < len(a[i]) :
        print(a[i][j], end=' ')
        j+=1
    print()
    i+=1
"""

'''
a = []

for i in range(10) :
    a.append(0) #append로 요소 0을 추가함.
print(a)
'''

"""
all=[]

for x in range(3) :
    line=[]
    for y in range(2) :
        line.append(0)
    all+=[line]
print(all)
"""

'''
#리스트 응용문으로 [[0, 0], [0, 0], [0, 0]] 만들기 
a = [ [0 for j in range(2)] for i in range(3) ]
print(a)

a= [[0]*2 for i in range(3)]
print(a)
'''

"""
#톱니형 [[0, 0, 0], [0], [0, 0, 0], [0, 0], [0, 0, 0, 0, 0]] 만들기-1
questLen = [3,1,3,2,5]
lineAll =[]

for i in questLen :
    line =[]
    for j in range(i) :
        line.append(0)
    lineAll.append(line)

print(lineAll)


#톱니형 [[0, 0, 0], [0], [0, 0, 0], [0, 0], [0, 0, 0, 0, 0]] 만들기-2
a = [[0] * i for i in [3,1, 3,2,5]]
print(a)
"""

a=[ [10,20], [30,40] ]
b=a
b[0][0] = 500
print(a)
print(b)

a=[[10,20], [30,40] ]
b=a.copy()  #2차원 리스트 복사는 deepcopy를 해야 비로소 제대로 복사됨...
b[0][0] =500
print(a)
print(b)

a=[[10,20], [30,40] ]
import copy
b = copy.deepcopy(a)
b[0][0] = 500
print(a)
print(b)




































