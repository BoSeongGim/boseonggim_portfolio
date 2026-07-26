"""
import tkinter as tk
root = tk.Tk()

lbl = tk.Label(root,text="EduCoding",underline=3)
lbl.pack()

txt = tk.Entry(root)
txt.pack()

btn = tk.Button(root,text = "OK",activebackground="red",width=5)
btn.pack()

root.mainloop()
"""

'''
#Tkinter라이브러리 임포트(GUI가능하게 해줌) 
import tkinter as tk
#Tk 객체 인스턴스 생성.
root = tk.Tk()

#라벨 생성
label = tk.Label(root, text='Hello World!')
#변수 = Tk로만들어진 라벨(parent, text등의 옵션...)

#라벨배치
label.pack()

#root표시(윈도우창 생성)
root.mainloop()

#파이썬에서는 이걸 5줄로 하면 끝내는것이
#윈도우관련 프로그래밍에서 만들려하면 100줄은 걸린다고 하심... ㄷㄷ;
'''

"""
import tkinter as tk
root = tk.Tk()

#버튼을 눌렀을시의 작동. command옵션에 삽입되어 작동한다.
def func() :
    print('Pushed') #파이썬 셸에 출력된다.

button = tk.Button(root, text = 'push!', command=func) #push!는 라벨처럼 버튼위에 뜬다.

button.pack()

root.mainloop()
"""
'''
#Tkinter 라이브러리 임포트
import tkinter as tk
root= tk.Tk()       #Tk 객체 인스턴스 생성 

# 버튼을 눌렀을 때 처리.
def func() :
    label.config(text='Pushed')#1번 클릭하면 pushed로 바뀌며, 영원히 pushed로 유지된다.

#라벨 생성
label = tk.Label(root, text='Push Button')
#라벨 배치
label.pack()

#버튼 생성
button = tk.Button(root, text='Push!!',command=func)
#버튼 배치
button.pack()

#루트 표시(윈도우 팝업)
root.mainloop()
'''

#버튼 누를 때마다 라벨에 사과, 오렌지 번갈아 표시
import tkinter as tk
root = tk.Tk()

bAct = False
print(type(bAct))
def func() :
    global bAct
    if bAct :
        label.config(text="Apple")
        bAct = False
        print(bAct)
    else :
        label.config(text="Orange")
        bAct = True
        print(bAct)

label = tk.Label(root, text ="push!")
label.pack()

button = tk.Button(root,text="change",command=func)
button.pack()

root.mainloop()













