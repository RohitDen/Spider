#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as spider,
# a less useful variable name spider is used
spider = trtl.Turtle()

def draw_big_circle(radius):
    spider.pensize(4)
    spider.color("Black")
    spider.begin_fill()
    spider.goto(0,-10)
    spider.circle(radius)
    spider.end_fill()

# Function implementation to draw legs
def draw_legs(radius, extent):
    for angle in range( 5 , 185, 15 ):
        spider.penup()
        spider.goto(0, 0)  
        spider.setheading(angle)  
        spider.forward(radius)  
        spider.pendown()
        if (angle < 65 or angle > 120):
            spider.circle(radius, extent )  # Draw the arc
    

def draw_small_circle(radius):
    spider.setheading(0)
    spider.pensize(4)
    spider.color("Black")
    spider.begin_fill()
    spider.goto(0,-30)
    spider.circle(radius)
    spider.end_fill()
    
def draw_eyes1(radius):
    spider.setheading(0)
    spider.pensize(4)
    spider.color("Red")
    spider.begin_fill()
    spider.circle(radius)
    spider.end_fill() 

# Draw Big Circle
draw_big_circle(25)

# Draw arcs around the main circle
draw_legs(25, 80)  # Radius of Big circle

spider.penup()
spider.goto(0, -10)  
spider.pendown()

# Draw Small Circle
draw_small_circle(20)

spider.penup()
spider.goto(10, -20)  
spider.pendown()


# Draw 1st eye of the spider
draw_eyes1(3)

spider.penup()
spider.goto(-10, -20)  
spider.pendown()

# Draw 2nd eye of the spider
draw_eyes1(3)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()
