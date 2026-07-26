#small project6 리스트 순서 뒤집기
'''
arr = [1, 4, 2, 3]
arrReverse = []
reversePoint=len(arr)

#for i in range(len(arr),0,-1) :
for i in arr:
    arrReverse[i] += i


print("arr 뒤집기 결과 : ",arrReverse)
'''

"""
#small project6[모범답안]
arr = [1,4,2,3]
left, right = 0, len(arr)-1
#print("left :", left ,", right :",right) #개인적 변수 정상입력 확인용.

while left < (len(arr) //2 ) :
    arr[left], arr[right] = arr[right], arr[left]
    left += 1
    right -= 1

print("변환된 arr은",arr,"입니다.")
""""
