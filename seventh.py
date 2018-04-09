import turtle


def make_triangle():
	window = turtle.Screen()
	window.bgcolor("blue")
	triangle = turtle.Turtle()
	triangle.shape("turtle")
	triangle.color("yellow")
	triangle.speed(1)
	count = 0
	count1 = 0

	while count < 3 :
		triangle.forward(100)
		triangle.left(120)
		count+=1
	triangle.right(60)
	triangle.forward(100)
	triangle.left(120)
	triangle.forward(100)
		


	window.exitonclick()


make_triangle()