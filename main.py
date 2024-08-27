# import numpy as np
# from PIL import Image
from canvas import Canvas
from shapes import Rectangle
from shapes import Square

#Get canvas width and height from the user
canvas_width = int(input("Enter canvas width: "))
canvas_height =int(input("Enter canvas height: "))

#Make a dictionary of color codes and prompt for color
colors = {"white":(255, 255, 255), "black" : (0, 0, 0)}
canvas_color = input("Enter canvas color(white or black): ").lower()

#Create a canvas with the user data
canvas = Canvas(height = canvas_height, width = canvas_width, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw? Enter quit to quit.")
    #Ask for rectangle data and create rectangle if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter X of the rectangle: "))
        rec_y = int(input("Enter Y of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        rec_red = int(input("How much red should the rectangle have? "))
        rec_green = int(input("How much green should the rectangle have? "))
        rec_blue = int(input("How much blue should the rectangle have? "))

        #Create the rectangle
        rec1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(rec_red, rec_green, rec_blue))
        rec1.draw(canvas)

    #Ask for square data and create if user entered 'square'
    if shape_type.lower() == 'square':
        square_x = int(input("Enter X of the square: "))
        square_y = int(input("Enter Y of the square: "))
        square_side = int(input("Enter the side length of thr square: "))
        square_red = int(input("How much red should the square have? "))
        square_green = int(input("How much green should the square have? "))
        square_blue = int(input("How much blue should the square have? "))

        #Create the square
        square_1 = Square(x=square_x, y=square_y, side=square_side, color=(square_red, square_green, square_blue))
        square_1.draw(canvas)

        #Break the loop if the user entered 'quit'
    if shape_type == 'quit':
        break


canvas.make('canvas.png')


#


