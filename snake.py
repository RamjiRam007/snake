import turtle
import random

grass = turtle.Screen()
grass.bgpic("grass.gif")

grass.addshape("headfront.gif")
grass.addshape("headdown.gif")
grass.addshape("headleft.gif")
grass.addshape("headright.gif")
grass.addshape("body.gif")

snake=turtle.Turtle()
snake.penup()
snake.setheading(90)
snake.goto(0,0)
snake.shape("headfront.gif")

food=turtle.Turtle()
food.penup()
food.speed(500)
food.color("red")
food.shape("circle")
food.goto(100,10)

segment=[]

pen=turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(0,300)
pen.speed(500)
pen.write("Score : 0",font=("courier",27,"bold"))

#movement of snake
def move():
    snake.forward(20)
    
'''snake up side key'''
def up():
    if snake.heading() != 270 :
        snake.setheading(90)
        snake.shape("headfront.gif")
'''snake down side key'''
def down():
    if snake.heading() != 90 :
        snake.setheading(270)
        snake.shape("headdown.gif")


def right():
    if snake.heading() != 180 :
        snake.setheading(0)
        snake.shape("headright.gif")

def left():
    if snake.heading() != 0 :
        snake.setheading(180)
        snake.shape("headleft.gif")



turtle.onkeypress(up,"Up")
turtle.onkeypress(down,"Down")
turtle.onkeypress(left,"Left")
turtle.onkeypress(right,"Right")
score=0

turtle.listen()

while True:

    grass.update()

    if snake.xcor()>290 or snake.xcor()<-290 or snake.ycor()>290 or snake.ycor()<-290 :
        grass.bgpic("gameover.gif")
        food.hideturtle()

    for i in segment :
        if i.distance(snake)<10:
            grass.bgpic("gameover.gif")
            food.hideturtle()


    if snake.distance(food) < 20 :
        x=random.randint(-285,285)
        y=random.randint(-285,285)
        food.setpos(x,y)
        score= score + 1
        pen.clear()
        pen.write("score : {}".format(score),font=("courier",27,"bold"))
        body=turtle.Turtle()
        body.penup()
        body.speed(0)
        body.shape("body.gif")

        segment.append(body)


    for i in range(len(segment)-1,0,-1):
        x=segment[i-1].xcor()
        y=segment[i-1].ycor()
        segment[i].goto(x,y)


    if len(segment)>0:
        x=snake.xcor()
        y=snake.ycor()
        segment[0].goto(x,y)

    move()

turtle.done()