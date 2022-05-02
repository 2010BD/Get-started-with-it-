import turtle #Import the turtle library

mypen = turtle.Pen()#Then, in the form of an assignment, name the brush. The name of the brush will do anything. But the Pen initials after the parentheses must be capitalized.
mypen.pencolor("green")#Setting colors can also be done in the form of assignments

color = "red"

mypen.pencolor(color)

#Code wrapped in "#" can be enclosed in the form of assignments in parentheses
mypen.pensize(20)#Sets the size of the brush, the value in parentheses can be modified, but only in numeric form.
mypen.forward(100)#Sets the number of advances before the brush, and the values in parentheses can be modified, but only in numeric form.
mypen.right(90)#Sets the rotation angle of the brush, and the values in parentheses can be modified, but only in numeric form. Right is the right turn and left is the
#

mypen.goto(0,0)#In the coordinate method, there are two numbers, the first being the "x" axis and the second being the "y" axis, separated by commas
mypen.clear()#Clear all traces of paintings
i = 0 #Create a count variable
while i < 4: #Loop if 1 is less than 4
    mypen.forward(100)
    mypen.right(90)

mypen.hideturtle()#A function that hides a brush to hide a brush
turtle.done()#Used to end the program and run the program, if it is drawing in the turtle library, you must use this code, otherwise the program will be packaged incorrectly.
