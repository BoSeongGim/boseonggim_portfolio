'''

import turtle as t
t.shape('turtle')

t.pencolor("BLUE")
t.fillcolor("RED")

t.begin_fill()

t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)
t.end_fill()

'''

'''
import turtle as t
t.pensize(3)

#삼각형 만들기
t.penup()
t.goto(-200,-50)
t.pendown()
t.circle(40, steps = 3)


#사각형 만들기
t.penup()
t.goto(-100,-50)
t.pendown()
t.circle(40,steps = 4)


#5각형 만들기
t.penup()
t.goto(0,-50)
t.pendown()
t.circle(40, steps = 5)


#6
t.penup()
t.goto(100,-50)
t.pendown()
t.circle(40, steps=6)

#원 만들기
t.penup()
t.goto(200,-50)
t.pendown()
t.circle(40)
'''

'''
#for문 활용하여 사각형 그리기.
import turtle as t
t.shape('turtle')
for i in range(4) :
    t.fd(100)
    t.rt(90)
'''

'''
#for문 활용하여 5각형 그리기.
import turtle as t
t.shape('turtle')
for i in range(5) :
    t.fd(100)
    t.rt(72)
'''

'''
import turtle as t
t.shape('turtle')

cur = int(input("원하는 각형의 숫자 : "))
ang = 360 / cur
print("cur : ",cur)

#t.shape('turtle')
for i in range(cur) :
    t.fd(100)
    t.rt(ang)
'''

'''
import turtle as t

n =6
t.shape('turtle')
t.color('red')
t.begin_fill()

for i in range(n) :
    t.forward(100)
    t.right(360 / n)
t.end_fill()
'''

'''
import turtle as t
t.shape('turtle')
t.speed('fastest')

deg= 5
cnt = int(360/deg) #그냥 하면 float->range()에서는 int형만 받기에 에러남.
print(type(cnt))
for i in range(cnt) :
    t.circle(100)
    t.rt(deg)
'''

'''
import turtle as t

t.shape('turtle')
t.speed('fastest')

for i in range(300) :
    t.forward(i)
    t.right(91)
'''

'''
import turtle as t
n =5
t.shape('turtle')
for i in range(n) :
    t.fd(100)
    t.rt(144)
    t.fd(100)
    t.rt(72)
'''

import turtle as t
n =5
t.shape('turtle')
for i in range(n) :
    t.fd(100)
    t.rt((360/n)*2)
    t.fd(100)
    t.rt(360/n)






























