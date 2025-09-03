import turtle, math

def koch(t, l, d): 
    if d == 0: t.forward(l); return
    l /= 3; [koch(t,l,d-1), t.left(60), koch(t,l,d-1), t.right(120), koch(t,l,d-1), t.left(60), koch(t,l,d-1)]

sides = int(input("sides: "))
length = float(input("Side Length: "))
depth = int(input("Depth: "))

screen = turtle.Screen(); screen.setup(900,900); screen.bgcolor("black")
t = turtle.Turtle(visible=False); t.speed(0); t.color("Cyan"); turtle.tracer(False)

margin = 0.85
growth = (4/5) ** depth
max_side = 900 * margin / sides 
scale = min(1.0, max_side / (length * growth))
length *= scale 

angle_step = 2*math.pi/sides
R = length/(2*math.sin(math.pi/sides))
v0 = (R*math.cos(-math.pi/2), R*math.sin(-math.pi/2))
v1 = (R*math.cos(-math.pi/2+2*math.pi/sides), R*math.sin(-math.pi/2+2*math.pi/sides))
t.penup(); t.goto(v0); t.setheading(t.towards(v1)); t.pendown()

for _ in range(sides): koch(t,length,depth); t.left(360/sides)
turtle.update(); screen.mainloop()