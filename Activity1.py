import turtle

turtle.Screen().bgcolor("white")
turtle.Screen().setup(400,400)

hexagon = turtle.Turtle()

num_of_sides = 6

side_length = 80

angle = 360 / num_of_sides

for x in range(num_of_sides):
    hexagon.forward(side_length)
    hexagon.right(angle)

turtle.done()