from turtle import*

# i want to draw a house

#step one i need to draw a square

speed(3)

color("blue")

begin_fill()

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)   #end of square
left(90)

end_fill()

color("yellow")

begin_fill()

forward(75)
left(90)
forward(100)  #height of door

right(90)
forward(60)

right(90)
forward(100)

end_fill()

color("blue")

begin_fill()

left(90)
forward(225)

left(90)
forward(200)

left(90)
forward(225)

end_fill()

color("red")

begin_fill()

penup()

goto(200, 200)

pendown()

left(320)
forward(140)

left(85)
forward(130)

end_fill()

begin_fill()

backward(130)

left(135)
forward(225)

right(65)
forward(110)

end_fill()

color("green")



penup()

goto(200, 100)

forward(50)

pendown()

begin_fill()

left(155)
forward(100)


right(90)
forward(125)

right(90)
forward(100)

right(90)
forward(125)

end_fill()

color("black")

penup()

goto(220, 100)

pendown()

left(180)
forward(125)

penup()

goto(290, 155)

pendown()

left(270)
forward(100)


exitonclick()