import turtle
import math
import json

bg, pr, sc = None, None, None 

with open('config.json', 'r') as f:
    data = json.load(f)
    bg = data["backgroundColor"]
    pr = data["primaryColor"]
    sc = data["secondaryColor"]
    
def hexagon(ttl, x, y, l):
    ttl.penup()
    ttl.goto(x, y)
    ttl.pendown()
    ttl.begin_fill()
    for _ in range(0, 6):
        ttl.forward(l)
        ttl.left(60)
    ttl.end_fill()


wn = turtle.Screen()
t = turtle.Turtle()

wn.tracer(0)
wn.bgcolor(bg)

side = 20          
dx = side * 3      
dy = -int(side / 2 * math.sqrt(3))

shift = False
shift_amount = side * 3 // 2

t.color(sc)
t.fillcolor(pr)
t.pensize(2)

for y in range(150, -150, dy):
    offset = 0 if shift else shift_amount
    for x in range(-150 + offset, 150 + offset, dx):
        hexagon(t, x, y, 20)
    shift = not shift

t.penup()
t.hideturtle()
wn.exitonclick()