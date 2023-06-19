import json

tessellations = ["honeycomb.py", "sirpinski_triangle.py", "flower.py", "spiral.py", "circles.py"]
colors = ["red", "blue", "magenta", "green", "yellow", "orange", "white"]

primaryColor = input("Choose a primary color [\"red\", \"blue\", \"magenta\", \"green\", \"yellow\", \"orange\", \"white\"]: ")
secondaryColor = input("Choose a secondary color [\"red\", \"blue\", \"magenta\", \"green\", \"yellow\", \"orange\", \"white\"]: ")
toDisplay = int(input("Choose a tessellation to display by entering the corresponding serial number:\n\t1. Honeycomb\n\t2. Sirpinski's Triangle\n\t3. Flower\n\t4. Spiral\n\t5. Circles"))

if primaryColor in colors and secondaryColor in colors:
    data = None
    with open('config.json', 'r') as f:
        data = json.load(f)
        data["primaryColor"] = primaryColor
        data["secondaryColor"] = secondaryColor
    with open("config.json", "w") as f:
        json.dump(data, f)

if tessellations[toDisplay-1]:
    exec(open('tessellations/'+tessellations[toDisplay-1]).read())