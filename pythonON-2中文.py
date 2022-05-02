import turtle #导入turtle库

mypen = turtle.Pen()#然后以赋值的形式，命名画笔。画笔的名称什么都行。但是再括号后面的Pen首字母必须大写。
mypen.pencolor("green")#设置颜色也可以通过赋值的形式

color = "red"

mypen.pencolor(color)

#用“#”号包起来的代码括号中都可以用赋值的形式
mypen.pensize(20)#设置画笔的大小，括号内数值可修改，但只能是数字形式。
mypen.forward(100)#设置画笔的前进步数，括号内数值可修改，但只能是数字形式。
mypen.right(90)#设置画笔的旋转角度，括号内数值可修改，但只能是数字形式。right是右转，left是左转。
#

mypen.goto(0,0)#坐标方法，中有两个数字第一个是“x”轴，第二个是“y”轴，中间由逗号隔开
mypen.clear()#清除所有画的痕迹
i = 0 #创建计数变量
while i < 4: #循环如果1 小于4
    mypen.forward(100)
    mypen.right(90)

mypen.hideturtle()#隐藏画笔的函数，用于隐藏画笔
turtle.done()#用于结束程序和运行程序，在turtle库中如果是画图，必须使用这个代码，不然程序会包错。

