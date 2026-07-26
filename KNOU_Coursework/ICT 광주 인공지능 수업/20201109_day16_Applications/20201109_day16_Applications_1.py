'''
#버튼 누를 때마다 라벨의 사과/오렌지 표기를 번걸아 실시.
#아래와 같은 3-Step으로 실시.

#Step1.기초설정(임포트/객체인스턴스 생성/변수)---------------
import tkinter as tk    #1.1. 임포트
root = tk.Tk()          #1.2. 객체 생성
bAct=False              #1.3. 변수 생성
#------------------------------------------------------------

#Step2.함수설정.---------------------------------------------
def func() :
    global bAct
    if bAct :
        label.config(text="Apple")
        bAct=False
    else :
        label.config(text="Orange")
        bAct= True
#------------------------------------------------------------

#Step3.윈도우 구성&실시--------------------------------------
label = tk.Label(root, text = "push")#3.1.라벨생성&배치
label.pack()

button = tk.Button(root, text="change",command=func)#3.2.버튼생성&배치
button.pack()

root.mainloop() #3.3. root표시(윈도우실시)
#------------------------------------------------------------
'''

"""
#버튼을 누른 다름에 특정 동작을 하면 표시가 돌아오도록 프로그램을 변경.
#step1.
import tkinter as tk
root = tk.Tk()

#step2. 함수 선언
def func() :
    label.config(text ='pushed')

def func_event(ev) : 
    label.config(text='Push Button') #라벨의 표시를 변경.

#step3.윈도우의 
label = tk.Label(root, text = 'Push Button')
label.pack()

button = tk.Button(root, text = 'Push!',command=func)
button.pack()

#step4. 이벤트 추가(step3앞에 배치시 선언X라고 에러남...)-------------------
#이벤트 추가는 의미가 있는 것이 지금까지의 '절차적프로세스'를 벗어나서 실시.

button.bind('<Leave>',func_event)#마우스커서가 버튼을 벗어날시 이벤트 추가.
#bind : 특정 이벤트가 발생시, 지정한 함수를 실시함.
#Leave : 마우스커서가 위젯밖을 벗어날때 발생하는 이벤트 

#step5. 윈도우 실시.
root.mainloop()
"""

'''
#1.임포트&객체 인스턴스 선언
import tkinter as tk
root = tk.Tk()

#2.함수선언 버튼 클릭시명령/마우스위치 이벤트 발생2건
def func_push() :
    label.config(text='Pushed') #마우스 버튼 클릭시
def func_event_exit(ev) :
    label.config(text='Leaved') #라벨의 표시를 변경.(마우스 버튼밖)
def func_event_inter(ev) :
    label.config(text='Enterd') #라벨의 표시를 변경.(마우스 버튼 안)


#3윈도우 구성물 배치.
label = tk.Label(root, text="ButtonButton")
label.pack()
button = tk.Button(root, text="pushed",command=func_push)#클릭명령(command)를 func_push로 하겠다.
button.pack()

#4이벤트 추가
button.bind('<Leave>',func_event_exit)#마우스커서가 버튼을 벗어날시 이벤트 추가.
button.bind('<Enter>',func_event_inter)


root.mainloop()
'''

import tkinter as tk
root = tk.Tk()

def func() :
    label.config(text = 'Pushed')

def func_event_click(ev) : #ev는 이벤트발생시 x,y좌표등 온갖 정보를 갖고 있다.
    disp =str("x좌표:")+ str(ev.x) + '/'+str("y좌표:") +str(ev.y) 
    label.config(text = disp)

label =tk.Label(root, text="P B")
label.pack()

button = tk.Button(root, text="Push", command = func() )
button.pack()

button.bind('<Button-1>',func_event_click) # <Button-1> : 마우스 왼쪽버튼클릭시 이벤트. 

root.mainloop()

















