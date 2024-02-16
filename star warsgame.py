import turtle
import math
import random

window = turtle.Screen()
window.setup(width=600, height=600)
window.title("Star Wars Game by Pankaj")
window.bgcolor("black")
window.tracer(0)

vertex = ((0,15),(-15,0),(-18,5),(-18,-5),(0,0),(18,-5),(18, 5),(15, 0))
window.register_shape("player", vertex)

asVertex = ((0, 10), (5, 7), (3,3), (10,0), (7, 4), (8, -6), (0, -10), (-5, -5), (-7, -7), (-10, 0), (-5, 4), (-1, 8))
window.register_shape("chattan", asVertex)

class Pankaj(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.penup()

def calculate_angle(t1, t2):
    x1 = t1.xcor()
    y1 = t1.ycor()
    
    x2 = t2.xcor()
    y2 = t2.ycor()
    
    angle = math.atan2(y1 - y2, x1 - x2)
    angle = angle * 180.0 / math.pi
    
    return angle

player = Pankaj()
player.color("white")
player.shape("player")
player.score = 0

missiles = []
for _ in range(3):
    missile = Pankaj()
    missile.color("red")
    missile.shape("arrow")
    missile.speed = 1
    missile.state = "ready"
    missile.hideturtle()
    missiles.append(missile)

pen = Pankaj()
pen.color("white")
pen.hideturtle()
pen.goto(0, 250)
pen.write("Score: 0", False, align="center", font=("Arial", 24, "normal"))

chattans = []
for _ in range(5):   
    chattan = Pankaj()
    chattan.color("brown")
    chattan.shape("arrow")
    chattan.speed = random.randint(2, 3)/50
    chattan.goto(0, 0)
    angle = random.randint(0, 260)
    distance = random.randint(300, 400)
    chattan.setheading(angle)
    chattan.fd(distance)
    chattan.setheading(calculate_angle(player, chattan))
    chattans.append(chattan)

def turn_left():
    player.lt(20)
    
def turn_right():
    player.rt(20)
    
def fire_missile():
    for missile in missiles:
        if missile.state == "ready":
            missile.goto(0, 0)
            missile.showturtle()
            missile.setheading(player.heading())
            missile.state = "fire"
            break

window.listen()
window.onkey(turn_left, "Left")
window.onkey(turn_right, "Right")
window.onkey(fire_missile, "space")

game_over = False
while not game_over:
    window.update()
    player.goto(0, 0)
    
    for missile in missiles:
        if missile.state == "fire":
            missile.fd(missile.speed)
        
        if abs(missile.xcor()) > 300 or abs(missile.ycor()) > 300:
            missile.hideturtle()
            missile.state = "ready"

    for chattan in chattans:    
        chattan.fd(chattan.speed)
        
        for missile in missiles:
            if chattan.distance(missile) < 20:
                angle = random.randint(0, 260)
                distance = random.randint(600, 800)
                chattan.setheading(angle)
                chattan.fd(distance)
                chattan.setheading(calculate_angle(player, chattan))
                chattan.speed += 0.01
                
                missile.goto(600, 600)
                missile.hideturtle()
                missile.state = "ready"
                
                player.score += 10
                pen.clear()
                pen.write("Score: {}".format(player.score), False, align="center", font=("Arial", 24, "normal"))

        if chattan.distance(player) < 20:
            angle = random.randint(0, 260)
            distance = random.randint(600, 800)
            chattan.setheading(angle)
            chattan.fd(distance)
            chattan.setheading(calculate_angle(player, chattan))
            chattan.speed += 0.005
            game_over = True
            player.score -= 30
            pen.clear()
            pen.write("Score: {}".format(player.score), False, align="center", font=("Arial", 24, "normal"))
            break

player.hideturtle()
for missile in missiles:
    missile.hideturtle()
for chattan in chattans:
    chattan.hideturtle()
pen.clear()

window.mainloop()
