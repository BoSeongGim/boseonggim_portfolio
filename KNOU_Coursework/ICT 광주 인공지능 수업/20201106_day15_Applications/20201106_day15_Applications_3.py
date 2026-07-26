"""
inFp = None
InStr = ""
inFp = open("data1.txt","r",encoding="utf-8") #파일을 읽는 권한을 획득. int형 그런게 아니다.

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break
    print(inStr, end="")

inFp.close()
"""
'''
inFp = open("data1.txt","r",encoding="utf-8")
inList =[]
inList = inFp.readlines()
print(inList)
inFp.close()
'''
"""
inFp=None
inList=[]
inStr=""
inFp = open("data1.txt","r",encoding="utf-8")

inList = inFp.readlines()
for inStr in inList :
    print(inStr, end="")
inFp.close()
"""

'''
fileName = input("파일명을 입력하세요 : ")
inList=[]
inStr=""

inFp = open(fileName,"r",encoding="utf-8")

inList = inFp.readlines()

for inStr in inList :
    print(inStr, end="")
inFp.close()
'''
"""
outFp = None
outStr = ""

outFp = open("data2.txt","w", encoding='utf-8')

while True :
    outStr = input("내용 입력 :")
    if outStr != "" :
        outFp.writelines(outStr +"\n")
    else :
        break

outFp.close()
print("--------정상작동-------")
"""

inFp, outFp = None, None
inStr =""

inFp= open("data2.txt","r",encoding='utf-8')
outFp = open("data2_copy.txt","w",encoding='utf-8')

inList = inFp.readlines()
print(inList)
for inStr in inList :
    outFp.writelines(inStr)
inFp.close()
outFp.close()
print("-----정상적으로 파일이 복사되었음----")



















