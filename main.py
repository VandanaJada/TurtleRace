from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=800, height=600)
user_bet = screen.textinput(title='Your bet', prompt='Choose a color')
colors = ['red', 'green', 'orange', 'yellow', 'purple', 'blue', 'indigo', 'black', 'beige', 'SpringGreen']
all_turtles = []

#creating 10 turtles for the race
for i in range(10):
    turtle = Turtle(shape='turtle')
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-380,-200+50*i)
    all_turtles.append(turtle)
is_raceon = True
while is_raceon:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            turtle.speed(0)
            winning_color = turtle.pencolor()
            is_raceon = False
        turtle.forward(random.randint(0,10))
if winning_color == user_bet:
    print(f"You won the bet! {winning_color} turtle was the winner")
else:
    print(f"You lost the bet! {winning_color} turtle was the winner")
screen.exitonclick()
