from turtle import*
from colorsys import*
setposition(50,-50)
speed(0)
bgcolor('black')
pensize(4)
n=200
h=0
for i in range(140):
    for i in range(2):
        color(hsv_to_rgb(h,1,1))
        h+=0.004
        circle(40+i*5,90)
        forward(250)
        left(90)
    rt(20)
    hideturtle()
done()