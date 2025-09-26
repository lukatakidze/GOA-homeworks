from turtle import *

#step 1 : draw a square 
speed(30)
width(7)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of square

#drawing a door

forward(70)
color("red")
begin_fill()
left(90)
forward(100)
right(90)
forward(60)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()
#drawing a roof

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a window
color("blue")
left(30)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
right(90)
forward(100)
right(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
color("green")
forward(100)
color("blue")
forward(50)
left(90)
forward(25)
left(90)
forward(50)
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(50)
penup()
goto(200, 200)
pendown()
forward(25)
right(90)
forward(50)
right(90)
forward(25)
right(90)
forward(25)
right(90)
forward(50)

exitonclick()
