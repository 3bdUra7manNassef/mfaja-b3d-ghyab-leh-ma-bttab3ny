import turtle

# Creating a window
window = turtle.Screen()
window.bgcolor('gray')
window.title('n1sf llt15er 3la nshr alakwad l1nna shrk0 3bdo llt15er')

# Creating a pen ('abo_grgr')
abo_grgr = turtle.Turtle()
abo_grgr.pensize(3)
abo_grgr.speed(100)
abo_grgr.hideturtle()

motion = 1

# Drawing the spiral
for i in range(100):
    abo_grgr.fd(motion)
    abo_grgr.right(121)
    motion += 3

# Exiting the window
turtle.done()
