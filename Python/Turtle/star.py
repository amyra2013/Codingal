import turtle

turtle.Screen().bgcolor("grey")
star=turtle.Turtle()

#first triangle for star
star.forward(100) # draw base

star.left(120)
star.forward(100)

star.left(120)
star.forward(100)

star.penup()
star.right(150)
star.forward(50)

#second triangle for star

star.pendown()
star.right(90)
star.forward(100)

star.right(120)
star.forward(100)

star.right(120)
star.forward(100)

turtle.done()
