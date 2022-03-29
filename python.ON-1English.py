import turtle #Start by importing the turtle library

mypen = turtle.Pen()#Then, in the form of an assignment, name the brush. The name of the brush will do anything. But the Pen initials after the parentheses must be capitalized.

mypen.pensize(20)#Sets the size of the brush, the value in parentheses can be modified, but only in numeric form.
mypen.forward(100)#Sets the number of advances before the brush, and the values in parentheses can be modified, but only in numeric form.
mypen.right(90)#Sets the rotation angle of the brush, and the values in parentheses can be modified, but only in numeric form. Right is the right turn and left is the left turn.

turtle.done()#Used to end the program and run the program, if it is drawing in the turtle library, you must use this code, otherwise the program will be packaged incorrectly.