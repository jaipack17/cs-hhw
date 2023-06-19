import turtle

bg, pr, sc = None, None, None 
primary = True

with open('config.json', 'r') as f:
    data = json.load(f)
    bg = data["backgroundColor"]
    pr = data["primaryColor"]
    sc = data["secondaryColor"]

wn = turtle.Screen()                      
wn.bgcolor(bg)                       
wn.setworldcoordinates(0, 1000, 1000, 0)  
t = turtle.Turtle()
t.speed(0)      
t.color(pr)                           
t.shape("circle")                        
t.shapesize(0.1, 0.1, 0.1)

wn.tracer(0)

def triangle(x, y, length, turtle, primary):
    if primary:
        turtle.color(pr)
        primary = False
    else:
        turtle.color(sc)
        primary = True

    primary = not primary
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.begin_fill()
    turtle.goto(x+length, y)
    turtle.goto(x+length/2, y-length)
    turtle.goto(x, y)
    turtle.end_fill()

def fractal(x, y, length, turtle, deg, primary):
    if deg > 0:
        fractal(x+length/2, y, length/2, turtle, deg-1, primary)
        fractal(x+length/4, y-length/2, length/2, turtle, deg-1, primary)
        fractal(x, y, length/2, turtle, deg-1, primary)
    if deg == 0:
        triangle(x, y, length, turtle, primary)

fractal(250, 700, 500, t, 5, primary)

wn.exitonclick()