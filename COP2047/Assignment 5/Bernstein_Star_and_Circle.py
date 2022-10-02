#Author Name: Aiden Bernstein
#Date: 10/1/2022
#Program Name: Bernstein_Star_and_Circle.py
#Purpose: Draw stars and circles

import turtle

turt = turtle.Turtle()                                  #create turtle object called turtle

turt.speed(10)                                          #make this process slightly more bearable

def main(size, x = 3, y = 3):
    for i in range (y):
        turt.penup()
        turt.setposition(-500,250 - i * (size * 6))     #move turt to a suitable position to begin the row
        turt.pendown()
        for j in range (x):
            star(size)                                  #draw the star
            turt.penup()                                #move turt into position for the next star in the row
            turt.forward(size * 6)
            turt.pendown()

def star(size):                                         #draw the star
    for i in range(5):
        turt.forward(size * 2)
        turt.circle(size)
        turt.right(144)

main(50)                                                #call the main function
turtle.done()                                           #end the program