import turtle as t
  
pr, sc = None, None 

with open('config.json', 'r') as f:
    data = json.load(f)
    pr = data["primaryColor"]
    sc = data["secondaryColor"]
    
t.tracer(0)
t.bgcolor("black")  
t.pensize(2)  
t.speed(0)
  
for i in range(50):  
    for colors in [pr, sc]:  
        t.color(colors)  
        t.circle(100)  
        t.left(10)  
  
t.hideturtle()  
t.done()