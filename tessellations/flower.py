import turtle as t 
import colorsys as cs 

bg, pr, sc = None, None, None 
primary = True

with open('config.json', 'r') as f:
    data = json.load(f)
    bg = data["backgroundColor"]
    pr = data["primaryColor"]
    sc = data["secondaryColor"]

t.setup(800,800)
t.speed(0)
t.tracer(0)
t.width(2)
t.bgcolor(bg) 
for j in range(25):
    for i in range(15):
        if primary:
            t.color(pr)
        else:
            t.color(sc)
        primary = not primary
        t.right(90)
        t.circle(200-j*4,90)
        t.left(90)
        t.circle(200-j*4,90)
        t.right(180)
        t.circle(50,24)
t.hideturtle() 
t.done()