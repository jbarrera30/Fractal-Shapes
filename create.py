import turtle
import random

def random_rgb():
    col = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if col == (0,0,0):
        random_rgb()
    return col

def spiral(length):
    if length < 800:
        turtle.color(random_rgb())
        turtle.forward(length)
        turtle.right(90)
        spiral(length +5 )

def tree(length):
    if length > 5:
        turtle.color(random_rgb())
        turtle.forward(length)
        turtle.right(20)
        tree(length-5)
        turtle.left(40)
        tree(length - 5)
        turtle.right(20)
        turtle.backward(length)

def sierpinskitriangle(length, detail):
    turtle.color(random_rgb())
    if detail == 0:
        for i in range(3):
            turtle.color(random_rgb())
            turtle.forward(length)
            turtle.left(120)
    else:
        sierpinskitriangle(length / 2, detail - 1)
        turtle.forward(length / 2)
        sierpinskitriangle(length / 2, detail - 1)
        turtle.penup()
        turtle.backward(length / 2)
        turtle.pendown()
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(60)
        sierpinskitriangle(length / 2, detail - 1)
        turtle.left(60)
        turtle.penup()
        turtle.backward(length/2)
        turtle.pendown()
        turtle.right(60)

def kochsnowflake(length, detail):
    turtle.color(random_rgb())
    if detail == 0:
        turtle.forward(length)
    else:
        length /= 3
        kochsnowflake(length, detail - 1)
        turtle.left(60)
        kochsnowflake(length, detail-1)
        turtle.right(120)
        kochsnowflake(length, detail -1)
        turtle.left(60)
        kochsnowflake(length, detail - 1)

def dragonDirections(detail):
    s = 'R'
    for i in range(detail-1):
        flip = ''
        add = s + 'R'
        rev = s[::-1]
        for char in rev:
            if char == 'R':
                flip += 'L'
            if char == 'L':
                flip += 'R'
        temp = add + flip
        s = temp
    return s

def dragonDraw(direction, length):

    for char in direction:
        turtle.color(random_rgb())
        if char == 'R':
            turtle.right(90)
            turtle.forward(length)
        else:
            turtle.left(90)
            turtle.forward(length)

def main():
    options = ['tree', 'spiral', 'snowflake', 'triangle', 'dragon']
    while True:
        shape = input('Choose a shape from the options(spiral, tree, snowflake, triangle, dragon):')
        if shape in options:
            break
        else:
            print('Not an option!')

    turtle.colormode(255)
    turtle.pensize(1)
    turtle.hideturtle()
    turtle.setup(width=1000, height=800, startx=500, starty=100)
    turtle.bgcolor("black")
    turtle.speed(10)
    if shape == 'tree':
        turtle.left(90)
        tree(50)
    if shape == 'spiral':
        turtle.left(90)
        spiral(5)
    if shape == 'snowflake':
        turtle.penup()
        turtle.setx(-150)
        turtle.sety(100)
        turtle.pendown()
        for i in range(3):
            kochsnowflake(300, 3)
            turtle.right(120)
    if shape == 'triangle':
        turtle.penup()
        turtle.setx(-100)
        turtle.sety(-50)
        turtle.pendown()
        sierpinskitriangle(200,4)
    if shape == 'dragon':
        turtle.sety(-150)
        dragonDraw(dragonDirections(13),5)
    window = turtle.Screen()
    window.exitonclick()

if __name__ == '__main__':
    main()
