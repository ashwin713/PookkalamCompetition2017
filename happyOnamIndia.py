import turtle

bharath = turtle.Turtle()
bharath.hideturtle()
bharath.penup()
bharath.speed(20)
bharath.pensize(3)

bharath.begin_fill()
bharath.color("#138808")
for i in range(1, 140, 20):
    bharath.right(90)    
    bharath.forward(i)   
    bharath.right(270)   
    bharath.pendown()    
    bharath.circle(i)    
    bharath.penup()      
    bharath.home()       
bharath.pendown()
bharath.end_fill()


bharath.begin_fill()
bharath.color("#ff9933")
for i in range(6):
    bharath.circle(100)
    bharath.right(60)
bharath.end_fill()     


bharath.begin_fill()
bharath.color("#0000ff")
for i in range(24):
    bharath.circle(20)
    bharath.right(15)     
bharath.pendown()
bharath.end_fill()


bharath.begin_fill()
bharath.color("white")
bharath.right(90)
bharath.forward(24)
bharath.right(270)
bharath.circle(25)
bharath.end_fill()


bharath.right(90)
bharath.forward(-25)
bharath.right(270)
bharath.color("#0000ff")
for i in range(24):
    for j in [0,1,2,3]:
        bharath.forward(25)
        bharath.left(90)
    bharath.right(30)

turtle.mainloop()     