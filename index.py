import turtle
import random
bubble = turtle.Turtle()
bubble.shape("circle")
bubble.penup()
window = turtle.Screen()
window.bgcolor("sky blue")
window.tracer(0)
player = turtle.Turtle()
player.shape("turtle")
player.color("blue")
player.penup()
bubble.color("green")
my_colors = ["green", "blue", "purple", "pink", "yellow", "blue"]
def move_bubble():
  bubble.color(random.choice(my_colors))
  bubble.setx(random.randint(-100, 100))
  bubble.sety(random.randint(-100, 100))

score = 0
display = turtle.Turtle()
display.penup()
display.setposition(-130, 130)
display.write("Score")

def turn_right():
  player.right(15)
  player.color("blue")

def turn_left():
  player.left(15)
  player.color("yellow")
  
window.onkey(turn_left, "Left")
window.listen()

window.onkey(turn_right, "Right")
window.listen()



while True:
  player.forward(1)
  window.update()
  
  if player.distance(bubble) < 20:
    move_bubble()
    display.clear()
    display.write("Score: {}".format(score))
    score = score + 1
   
    
    
# if the player has left the screen
  if player.xcor() > 200:
    player.setx(-200)
  if player.xcor() < -200:
    player.setx(200)
  if player.ycor() > 200:
    player.sety(-200)
  if player.ycor() < -200:
    player.sety(200)

    
  
  
