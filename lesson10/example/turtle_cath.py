from turtle import *
from random import random, randint, shuffle


t_list = []
points = 0

def catch(n, frequency=3):
    catch_count = 0
    def wrapper(x, y):
        t_list[n].penup()
        t_list[n].goto(random()*50,random()*50)
        t_list[n].left(random()*360)
        t_list[n].pendown()   
        global points
        points += 1
        if points % frequency == 0:
            create_t()
    return wrapper

def create_t(a=None):
    if a == None:
        a = random()*360
    t = Turtle('turtle')    
    t.speed(0)
    t.left(a)    
    t.color(*[round(random(),1) for _ in range(3)])
    t.onclick(catch(len(t_list)))
    t_list.append(t)
    
    
create_t(0)
create_t(120)    
create_t(240)        


while True:
    for t in t_list:
        t.fd(3)
    

mainloop()


