import turtle
import random
def tree(l,s):
    if l > 15:
        turtle.color("brown")
        turtle.pensize(s)
        turtle.forward(l)
        left_a=random.randint(10,30)
        right_a=random.randint(10,30)
        turtle.left(left_a)
        tree(l * 0.7, s/1.1)
        turtle.right(left_a + right_a)
        tree(l * 0.7, s/1.1)
        turtle.left(right_a)
        turtle.backward(l)
    else: 
        color = turtle.pencolor()
        turtle.pencolor("green")
        for i in range(4):
                turtle.circle(5-i)
                turtle.left(90)
                

        turtle.pencolor(color)
turtle.tracer(0)
turtle.setheading(90)
tree(100,5)
turtle.update()
turtle.mainloop()
