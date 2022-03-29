import turtle #首先导入turtle库

mypen = turtle.Pen()#然后以赋值的形式，命名画笔。画笔的名称什么都行。但是再括号后面的Pen首字母必须大写。

mypen.pensize(20)#设置画笔的大小，括号内数值可修改，但只能是数字形式。
mypen.forward(100)#设置画笔的前进步数，括号内数值可修改，但只能是数字形式。
mypen.right(90)#设置画笔的旋转角度，括号内数值可修改，但只能是数字形式。right是右转，left是左转。

turtle.done()#用于结束程序和运行程序，在turtle库中如果是画图，必须使用这个代码，不然程序会包错。
