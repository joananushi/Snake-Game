import turtle
import time
import random

delay= 0.1

score= 0
high_score=0

#Set up the screen
screen= turtle.Screen()
screen.title('SnakeGame')
screen.bgcolor('black')
screen.setup(width=600, height=600)
screen.tracer(0)

#create a custum triangle shape for the snake head
screen.register_shape('triangle',((0,-10),(5,10),(-5,10)))

#Snake Head
head= turtle.Turtle()
head.speed(0)
head.shape('triangle')
head.color('green')
head.penup()
head.goto(0,0)
head.direction='stop'

#snake food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0,100)

segments=[]

#pen

pen= turtle.Turtle()
pen.speed(0)
pen.shape('square')
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write('Score:{} High Score:{}'.format(score,high_score),align='center', font={'Courier', 24, 'normal'})

#Functions
def go_up():
    if head.direction!='down':
        head.direction ='up'
def go_down():
    if head.direction!='up':
        head.direction ='down'
def go_left():
    if head.direction!='right':
        head.direction ='left'
def go_right():
    if head.direction!='left':
        head.direction ='right'
def move():
    if head.direction =='up':
        y=head.ycor()
        head.sety(y + 20)
        head.setheading(90)
    if head.direction =='down':
        y=head.ycor()
        head.sety(y - 20)
        head.setheading(270)
    if head.direction =='left':
        x=head.xcor()
        head.setx(x - 20)
        head.setheading(180)
    if head.direction =='right':
        x=head.xcor()
        head.setx(x + 20)
        head.setheading(0)

#keyboard bindings
screen.listen()
screen.onkeypress(go_up, 'w')
screen.onkeypress(go_down, 's')
screen.onkeypress(go_left, 'a')
screen.onkeypress(go_right, 'd')

#Main Game Loop

while True:
    screen.update()

    #check for a collision wih the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction='stop'
        
        #hide the segments
        for segment in segments:
            segment.goto(1000,1000)

        segments.clear()
        score=0
        delay=0.1
        pen.clear()
        pen.write('score:{} high score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))
    
    #check for collision with the food
    if head.distance(food)<20:
        #move the food to random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('green')
        new_segment.penup()
        segments.append(new_segment)
        #shorten the delay
        delay-=0.001
        #increase the score
        score+=10
        if score>high_score:
            high_score=score
        
        pen.clear()
        pen.write('Score:{} High score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))
    
    for index in range(len(segments) -1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)
    #,ove segment 0 to where the head is
    if len(segments)>0:
        x= head.xcor()
        y= head.ycor()
        segments[0].goto(x,y)

    move()
    #check for head collision with the body segments
    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            for segment in segments:
                segment.goto(1000,1000)
            segments.clear()

            score=0
            delay=0.1
            pen.clear()
            pen.write('Score:{} High score: {}'.format(score, high_score), align='center', font=('Courier', 24, 'normal'))
    time.sleep(delay)
#exit the program
screen.mainloop()

