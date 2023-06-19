import turtle as t

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
t.bgcolor(bg)

for x in range(350):
    if x%5:
        primary = not primary
    if primary:
        t.pencolor(pr)
    else:
        t.pencolor(sc)
    t.width(x / 100 + 1)
    t.forward(x)
    t.left(59)

t.hideturtle() 
t.done()