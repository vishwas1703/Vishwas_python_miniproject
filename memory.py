"""
Memory, puzzle game of number pairs
This program is checked for pylint
author - Vishwas
date -  22 aug 2021
time - 6:30 am
"""
from random import shuffle
import turtle
from freegames import path
def game_memory():
    print("Memory Game Instructions:")
    print("1) Tap on Tiles to reveal number hidden.")
    print("2) Tap on other tiles and match pair to reveal image hidden under tiles.")
    print("3) Click on X to close game.")
    pen=turtle.Turtle()
    india = path('car.gif')
    tiles = list(range(32)) * 2
    state = {'mark': None}
    hide = [True] * 64
    def square(x_axis, y_axis):
        "Draw white square with black outline at (x, y). starts from left bottom corner"
        pen.up() #turtle.up() function Pull the pen up – no drawing when moving.
        pen.goto(x_axis, y_axis)
        pen.down()
         #turtle.up() function Pull the pen up – no drawing when moving.
        #print("enter box colour and line color")
        #box,line=input().split(" ")
        pen.color('gray20','cyan2')
        pen.begin_fill()
        for _ in range(4):
            pen.forward(50) #400/8 =50
            pen.left(90) # angle
        pen.end_fill()
    def index(x_axis, y_axis):
        "Convert (x, y) coordinates to tiles index."
        return int((x_axis + 200) // 50 + ((y_axis + 200) // 50) * 8)
    def xy_coordinates(count):
        "Convert tiles count to (x, y) coordinates."
        return (count % 8) * 50 - 200, (count // 8) * 50 - 200
    try:
        def tap(x_axis, y_axis):
            "Update mark and hidden tiles based on tap."
            spot = index(x_axis, y_axis)
            mark = state['mark']
            if mark is None or mark == spot or tiles[mark] != tiles[spot]:
                state['mark'] = spot
            else:
                hide[spot] = False
                hide[mark] = False
                state['mark'] = None
    except IndexError:
        print("tap properly")
    def draw():
        "Draw image and tiles."
        pen.clear()
        pen.goto(0, 0)
        pen.shape(india)
        pen.stamp()

        for count in range(64):
            if hide[count]:
                x_axis, y_axis = xy_coordinates(count)
                square(x_axis, y_axis)

        mark = state['mark']

        if mark is not None and hide[mark]:
            x_axis, y_axis = xy_coordinates(mark)
            pen.up()
            pen.goto(x_axis + 2, y_axis)
            pen.color('black')
            pen.write(tiles[mark], font=('Arial', 30, 'normal'))
        turtle.update()
        turtle.ontimer(draw, 100)
    shuffle(tiles)
    # shuffle is random package objet
    turtle.Screen().title("Memory Game")
    turtle.Screen().setup(405, 405, 370, 0)
    turtle.addshape(india)
    # add shape is turtle
    turtle.hideturtle()
    # hide turtle is turtle module
    turtle.tracer(False)
    # turtle
    turtle.onscreenclick(tap)
    #turtle
    draw()
    turtle.done()
    turtle.Terminator()
    print("Thank you for playing Memory Game.")

