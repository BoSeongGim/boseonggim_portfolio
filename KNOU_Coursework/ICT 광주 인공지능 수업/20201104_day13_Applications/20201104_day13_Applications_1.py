
#print('apple pineapple'.count('pl'))

#======================================================
'''
연습문제 :'apple pineapple apple pineapple'에서 'pl'을 찾고
인덱스들을 모두 표시하도록 하시오.
'''
'''
text = 'apple pineapple apple pineapple'
index=[]
i=0

while i < len(text) :
    print("i :",i)
    print(text)
    if text.find('pl') != -1 :
        index = text.find('pl') 
        print(index)
        sliceCutPosition = text.find('pl')
        print(sliceCutPosition)
        text=text[sliceCutPosition:]
        i=0

    i+=1
    
print(index)
'''

"""
#힌트
strMy='apple pineaplle apple pineapple'

nFind1 = strMy.find('pl')
print(nFind1)

newNFind = nFind1+2 #두 글자를 찾아야 하므로 찾은 위치에 2를 더함.

strMy = strMy[newNFind:]
print(strMy)
nFind2 = strMy.find('pl')
nFind2 = (newNFind) + nFind2
print(nFind2)
"""

'''
#모범답안(간략화 전)
str1 = 'apple pineaplle apple pineapple'
str2 = 'pl'

cnt = str1.find(str2)

print("최초위치 : ",cnt)

print("str1[cnt+1:] : ",str1[cnt+1:]) 
print("str1[cnt+1:].find(str2) : ",str1[cnt+1:].find(str2)) 

while str1[cnt+1:].find(str2) != -1:
    cnt = str1[cnt+1:].find(str2) + cnt +1
    print(cnt)
'''
"""
#모범답안 간략화된 최종코드 
str1 = 'apple pineaplle apple pineapple'
str2 = 'pl'

cnt = 1
#cnt = 1인 이유 :0,1인 경우 while문이 조건문 만족으로 오해할 수 있기에 최초시작은 -1로 설정.
#                궁금해서 개인적으로 0,1 해보니 잘 작동함...

while str1[cnt+1:].find(str2) != -1:
    cnt = str1[cnt+1:].find(str2) + cnt +1
    print(cnt)
"""
#======================================================

#찾아낸 해법을 일반화 시키기
#가변적으로 입력되는 문자열에 대해 처리할 수 있는 방법 고민
#내가 할 수 있는 메소드들을 활용하여 만들기-> 일반화->최적화


import re
str1 = 'apple pineapple apple pineapple'
str2 = 'pl'

for a in re.finditer(str2,str1) :
    print(a.start(), a.end())














