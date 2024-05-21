from turtle import *

def catch1(x,y):
    print(1)
    
def catch2(x,y):
    print(2)

t1 = Turtle('turtle')
t2 = Turtle('turtle')

t1.fd(100)
t1.color('red')

t2.left(90)
t2.forward(100)

t1.onclick(catch1)
t2.onclick(catch2)


mainloop()