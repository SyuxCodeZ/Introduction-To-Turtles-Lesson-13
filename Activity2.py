import turtle

turtle.Screen().bgcolor("white")
turtle.Screen().setup(600,700)

star = turtle.Turtle()

# intialized variables

star.forward(100)
star.right(120)
star.forward(100)
star.right(120)
star.forward(100)

star.penup()

star.left(150)
star.forward(65)

star.pendown()

star.left(90)
star.forward(110)
star.left(120)
star.forward(110)
star.left(120)
star.forward(110)

turtle.done()