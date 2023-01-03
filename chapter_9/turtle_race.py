from turtle import Turtle
import time
import random


turtle1 = Turtle()
turtle1.shape('turtle')
turtle1.color('red')
turtle1.penup()
turtle1.goto(-160,100)

turtle2 = Turtle()
turtle2.shape('turtle')
turtle2.color('green')
turtle2.penup()
turtle2.goto(-160,70)

turtle3 = Turtle()
turtle3.shape('turtle')
turtle3.color('blue')
turtle3.penup()
turtle3.goto(-160,40)

turtle4 = Turtle()
turtle4.shape('turtle')
turtle4.color('gray')
turtle4.penup()
turtle4.goto(-160,10)

time.sleep(1.5)

turtle1.pendown()
turtle2.pendown()
turtle3.pendown()
turtle4.pendown()

for i in range(100):
    value1 = random.randint(1,5)
    value2 = random.randint(1,5)
    value3 = random.randint(1,5)
    value4 = random.randint(1,5)

    bvalue1 = random.randint(1,5)
    bvalue2 = random.randint(1,5)
    bvalue3 = random.randint(1,5)
    bvalue4 = random.randint(1,5)

    turtle1.forward(value1)
    turtle2.forward(value2)
    turtle3.forward(value3)
    turtle4.forward(value4)

  
time.sleep(3)