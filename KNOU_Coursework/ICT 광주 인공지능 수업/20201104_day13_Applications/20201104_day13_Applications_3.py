"""
#연습문제
#힌트 : split활용 -> list 만들기

#나의 답안
path = 'C:\\Users\\Edu\\AppData\\Local\\Programs\\Python\\Python36-32\\data.txt'
pathList= path.split('\\')
print(pathList)
for i in pathList :
    print("i:",i)
    if  i.find('txt') != -1 :
        filename = i
        
print(filename)

#모범답안-1
x = path.split('\\')
filename = x[-1]
print(filename)

#모범답안-2
x = path.split('\\')
x.reverse()
filename= x[0]
print(filename)

#모범답안-3
filename = path[path.rfind('\\') +1 :] 
print(filename)
"""

#------------------------------------------------------------------------

#아래의 문자열에서 the의 개수를 출력.(them, there등은 카운트 하면 안됨.)
#원문 : the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the.
'''
text = "the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."
print(text.count('the')) #정답 : 6 

#모범답안
str = "the grown-ups' response, this time, was to advise me to lay aside my drawings of boa constrictors, whether from the inside or the outside, and devote myself instead to geography, history, arithmetic, and grammar. That is why, at the, age of six, I gave up what might have been a magnificent career as a painter. I had been disheartened by the failure of my Drawing Number One and my Drawing Number Two. Grown-ups never understand anything by themselves, and it is tiresome for children to be always and forever explaining things to the."
print(str.count('the ') + str.count('the,') + str.count('the.')) #정답 : 6 
'''


"""
def hello():
    print("Hello, by def!!!")

hello()  #def hello(): 실시
"""

def add(a,b) :
    print(a+b)

add(10,20)









  

