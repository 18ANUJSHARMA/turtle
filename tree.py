import turtle as t

size = int(input("Size: "))

t.bgcolor("black")
t.pensize(2)
t.color("green")
t.left(90)
t.backward(size)
t.speed(0)
t.hideturtle()
t.shape("turtle")

def tree(i):
    if i<10:
        return
    else:
        t.forward(i)
        t.color("orange")
        t.circle(2)
        t.color("brown")
        t.left(30)
        tree(3*i/4)
        t.right(60)
        tree(3*i/4)
        t.left(30)
        t.backward(i)
tree(size)
t.done()
