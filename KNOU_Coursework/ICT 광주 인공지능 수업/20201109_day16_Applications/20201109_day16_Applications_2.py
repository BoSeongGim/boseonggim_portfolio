#파이썬-라디오버튼 그래픽 그리기.
'''
import tkinter as tk
def Action1():
    lbl.config(text="Option 1")

def Action2():
    lbl.config(text="Option 2")

root = tk.Tk()

lbl = tk.Label(root, text="EduCoding",underline =3)
lbl.pack()

rbvar = ""
rb1 = tk.Radiobutton(root, text="Option 1", variable=rbvar, value='a', indicatoron=0, command=Action1)
rb1.pack()

rb2 = tk.Radiobutton(root, text="Option 2", variable=rbvar, value='b', indicatoron=0, command=Action2)
rb2.pack()
'''

"""
import tkinter as tk
root = tk.Tk()

def func1() :
    label.config(text = 'Button 1')

def func2() :
    label.config(text= 'Button 2')

sel = tk.IntVar() #라디오 버튼 값을 저장하는 정수형 Variable 객체를 생성한다.

sel.set(1) #sel에 1을 할당.

label = tk.Label(root, text = 'Select Button')
label.pack()

rb1 = tk.Radiobutton(root, text = 'Button 1',variable = sel, value=1, command=func1)#value는 sel과 연결된다고 하심.
rb1.pack()

rb2 = tk.Radiobutton(root, text = 'Button 2',variable = sel, value=2, command=func2)
rb2.pack()

root.mainloop()
"""

'''
#문제-라디오 버튼 클릭시 라벨에는 옵션을, 셸에는 밸류값 출력 /나의작성 실패.
import tkinter as tk
root = tk.Tk()

def func_print_selectRB() :
    label.config(text =  )
    if sel.get == 2317523564032 : #라디오 버튼이 보내주는 값에 따라 if문 구별계획중 막힙니다.
        label.config(text = "Choice1" )
   # else :
   #     label.config(text="허참... -ㅅ-")

sel =tk.IntVar() #라디오 그룹설정.
sel.set(1)

label = tk.Label(root, text="EduCoding") ; label.pack()

#아래의 라디오버튼들은 1번이라는 그룹이다.
#라디오 버튼들의 그룹에 
rb1 = tk.Radiobutton(root, text='Choice1', variable =sel, value=1) ; rb1.pack()
rb2 = tk.Radiobutton(root, text='Choice2', variable =sel, value=2) ; rb2.pack()
rb3 = tk.Radiobutton(root, text='Choice3', variable =sel, value=3) ; rb3.pack()

button = tk.Button(root, text="Print Choice", command=func_print_selectRB) ; button.pack()

root.mainloop()
'''

#[모범답안] 문제-라디오 버튼 클릭시 라벨에는 옵션을, 셸에는 밸류값 출력
import tkinter as tk
def Action1() :
    lbl.config(text ="Option 1")
def Action2() :
    lbl.config(text ="Option 2")
def Action3() :
    lbl.config(text ="Option 3")

root = tk.Tk()

lbl = tk.Label(root, text="EduCoding", underline =3)
lbl.pack()

var =tk.IntVar(root, 0)

#group of radioButtons
rBtn1 = tk.Radiobutton(root, text='Choice 1', value =1, variable=var, command=Action1)
rBtn1.pack()
rBtn2 = tk.Radiobutton(root, text='Choice 2', value =2, variable=var, command=Action2)
rBtn2.pack()
rBtn3 = tk.Radiobutton(root, text='Choice 3', value= 3, variable=var, command=Action3)
rBtn3.pack()

btn1=tk.Button(root,text='Print choice', command=lambda:print(var.get()) )#셸에 출력실시.
btn1.pack()

root.mainloop()





























    



















