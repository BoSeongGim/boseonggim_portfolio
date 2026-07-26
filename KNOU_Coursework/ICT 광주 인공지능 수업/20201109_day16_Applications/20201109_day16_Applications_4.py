#텍스트 계산기 만들기
#1.입력을 받는 2개의 텍스트 박스
#2.사칙연산은 라디오 버튼으로 선택.
#3.결과 버튼을 누르면 라벨에 결과가 표시
#4.0으로 나누는 예외 상황 처리
#5.표시는 소수점 2자리까지 표기.

#====================================================

#배치해보기
#좌표를 직접 정하여 라디오,라벨등의 배치위치등을 자신이 원하는 대로 할 수 있다.
import tkinter as tk
window = tk.Tk()
window.title("Educoding&IT")
window.geometry("320x400+100+100")
window.resizable(False, False)

b1 = tk.Button(window,text="(50,50)")
b2 = tk.Button(window,text="(50,100)")
b3 = tk.Button(window,text="(100,150)")
b4 = tk.Button(window,text="(0,200)" )
b5 = tk.Button(window,text="(0,300)" )
b6= tk.Button(window, text="(0,300)" )

b1.place(x=50,y=50)
b2.place(x=50,y=100,width=50,height=50) #버튼의 길이 및 높이도 설정.
b3.place(x=100, y=150, bordermode="inside")
b4.place(x=0, y=200, relwidth=0.5)
b5.place(x=0, y=300, relx=0.5)
b6.place(x=0, y=300, relx=0.5,width=50,height=50, anchor="s") #anchor:위젯의 기본조정위치를 변경함.(s는 남쪽(south)를 의미)

window.mainloop()



