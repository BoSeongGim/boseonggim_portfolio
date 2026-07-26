"""
def counter() :
    i = 0
    
    def count() :
        nonlocal i
        i = i+1
        return i
    return count

c = counter()

for i in range(10) :
    print(c(),end=' ')
"""


#텍스트 파일내의 문장이 3라인이라는 전제하에 작동하는 코드임.
inFp = None
inStr = ""
inFp = open("data1.txt","r",encoding="utf-8")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

inStr = inFp.readline()
print(inStr, end="")

InStr = inFp.readline()
print(inStr, end="")

inFp.close()





















