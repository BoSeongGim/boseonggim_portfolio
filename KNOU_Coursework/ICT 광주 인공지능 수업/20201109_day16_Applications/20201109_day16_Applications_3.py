#슬라이드
"""
import tkinter as tk
root = tk.Tk()

val= tk.IntVar() 
val.set(0)

def func(scl) : #슬라이드의 컨트롤러를 움직였을 때 처리.
    label.config(text='value = %d' % int(scl) )

label = tk.Label(root, text = 'Value = %d' % val.get() ) #슬라이드 바의 값을 표시하는 라벨 생성.
#                       라벨 텍스         /슬라이드 값 가져오는/
label.pack()

s=tk.Scale(root, label = 'Scale', orient ='h', from_ =0, to= 100, showvalue=True ,variable=val, command=func)
#                 scale라벨표시 /수평으로 숫자/  범위 : 0~100   /  showvalue통해 컨트롤러 위에 숫자값표시가능/
s.pack()

root.mainloop()
"""

'''
#텍스트 박스만들기
import tkinter as tk
root = tk.Tk()

def func(ev) :
    label.config(text = textBox.get() )

label = tk.Label(root, text = 'Input Text')
label.pack()

textBox = tk.Entry(root) #tk.Entry(root) : 텍스트 박스 생성하는 명령/ textBox는 내가 정한 변수명임.
textBox.pack()

textBox.bind('<Return>',func) #엔터키에 대한 입력을 <Return>으로 처리. 

root.mainloop()
'''

#1.입력을 받는 두개 의 텍스트 박스
#2.사칙연산은 라디오 버튼으로 선택.
#3.결과 버튼을 누르면 라벨에 결과가 표시.

import tkinter as tk
root = tk.Tk()

def cal_main() :
    value1 = int(textBox1.get() ) 
    value2 = int(textBox2.get() )

    if var.get() == 1 : 
        label.config(text = value1+value2)
    elif var.get() == 2 : 
        label.config(text = value1-value2)
    elif var.get() == 3 : 
        label.config(text = value1*value2)

    #나누기 연산 0으로 나누기에 대한 예외처리 작성.
    if var.get() == 4 and value1 !=0 and value2 !=0 : 
        label.config(text = value1/value2)
    else :
        label.config(text = "[예외처리] 나누기에 0이 입력시 불가합니다.")        
        

#1.입력을 받는 두개 의 텍스트 박스
textBox1 = tk.Entry(root)
textBox1.pack()
textBox2 = tk.Entry(root)
textBox2.pack()

#2.사칙연산은 라디오 버튼으로 선택.
var = tk.IntVar(root,0)#라디오 버튼들을 0번 그룹으로 묶음.
rBtn1_add = tk.Radiobutton(root, text="add", value=1, variable=var)
rBtn1_add.pack()
rBtn2_sub = tk.Radiobutton(root, text="sub", value=2, variable=var)
rBtn2_sub.pack()

rBtn3_mul = tk.Radiobutton(root, text="mul", value=3, variable=var)
rBtn3_mul.pack()

rBtn4_exp = tk.Radiobutton(root, text="exp", value=4, variable=var)
rBtn4_exp.pack()


#3.결과 버튼을 누르면 라벨에 결과가 표시.
bt = tk.Button(root, text="연산결과" ,command=cal_main)
bt.pack()

label = tk.Label(root, text="연산결과 출력됩니다.")
label.pack()
root.mainloop()








