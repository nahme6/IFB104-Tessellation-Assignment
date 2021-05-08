
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10470433
#    Student name: NAVID AHMED
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  TESSELLATION
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "tessellate".  You are required to
#  complete this function so that when the program is run it fills
#  a rectangular space with differently-shaped tiles, using data
#  stored in a list to determine which tiles to place and where.
#  See the instruction sheet accompanying this file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

cell_size = 100 # pixels (default is 100)
grid_width = 10 # squares (default is 10)
grid_height = 7 # squares (default is 7)
x_margin = cell_size * 2.75 # pixels, the size of the margin left/right of the grid
y_margin = cell_size // 2 # pixels, the size of the margin below/above the grid
window_height = grid_height * cell_size + y_margin * 2
window_width = grid_width * cell_size + x_margin * 2
small_font = ('Arial', 18, 'normal') # font for the coords
big_font = ('Arial', 24, 'normal') # font for any other text

# Validity checks on grid size - do not change this code
assert cell_size >= 80, 'Cells must be at least 80x80 pixels in size'
assert grid_width >= 8, 'Grid must be at least 8 squares wide'
assert grid_height >= 6, 'Grid must be at least 6 squares high'

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas(bg_colour = 'light grey',
                          line_colour = 'slate grey',
                          draw_grid = True, mark_legend = True):
    
    # Set up the drawing canvas with enough space for the grid and
    # legend
    setup(window_width, window_height)
    bgcolor(bg_colour)

    # Draw as quickly as possible
    tracer(False)

    # Get ready to draw the grid
    penup()
    color(line_colour)
    width(2)

    # Determine the left-bottom coords of the grid
    left_edge = -(grid_width * cell_size) // 2 
    bottom_edge = -(grid_height * cell_size) // 2

    # Optionally draw the grid
    if draw_grid:

        # Draw the horizontal grid lines
        setheading(0) # face east
        for line_no in range(0, grid_height + 1):
            penup()
            goto(left_edge, bottom_edge + line_no * cell_size)
            pendown()
            forward(grid_width * cell_size)
            
        # Draw the vertical grid lines
        setheading(90) # face north
        for line_no in range(0, grid_width + 1):
            penup()
            goto(left_edge + line_no * cell_size, bottom_edge)
            pendown()
            forward(grid_height * cell_size)

        # Draw each of the labels on the x axis
        penup()
        y_offset = 27 # pixels
        for x_label in range(0, grid_width):
            goto(left_edge + (x_label * cell_size) + (cell_size // 2), bottom_edge - y_offset)
            write(chr(x_label + ord('A')), align = 'center', font = small_font)

        # Draw each of the labels on the y axis
        penup()
        x_offset, y_offset = 7, 10 # pixels
        for y_label in range(0, grid_height):
            goto(left_edge - x_offset, bottom_edge + (y_label * cell_size) + (cell_size // 2) - y_offset)
            write(str(y_label + 1), align = 'right', font = small_font)

        # Mark centre coordinate (0, 0)
        home()
        dot(15)

    # Optionally mark the spaces for drawing the legend
    if mark_legend:
        # Left side
        goto(-(grid_width * cell_size) // 2 - 75, 50)
        write('Minecraft Diamond', align = 'right', font = small_font)
        goto(-(grid_width * cell_size) // 2 - 75, -250)
        
        write('Minecraft Creeper', align = 'right', font = small_font)
        
        # Right side
        goto((grid_width * cell_size) // 2 + 75, 50)
        write('Minecraft Spider', align = 'left', font = small_font)
        goto((grid_width * cell_size) // 2 + 75, -250)
        write('Minecraft House', align = 'left', font = small_font) 

    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(False) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the "tesselate" function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the "random_pattern" function appearing below.
# Your program must work correctly for any data set that can be
# generated by the random_pattern function.
#
# Each of the data sets is a list of instructions, each specifying
# where to place a particular tile.  The general form of each
# instruction is
#
#     [squares, mystery_value]
#
# where there may be one, two or four squares in the grid listed
# at the beginning.  This tells us which grid squares must be
# filled by this particular tile.  This information also tells
# us which shape of tile to produce.  A "big" tile will occupy
# four grid squares, a "small" tile will occupy one square, a
# "wide" tile will occupy two squares in the same row, and a
# "tall" tile will occupy two squares in the same column.  The
# purpose of the "mystery value" will be revealed in Part B of
# the assignment.
#
# Note that the fixed patterns below assume the grid has its
# default size of 10x7 squares.
#

# Some starting points - the following fixed patterns place
# just a single tile in the grid, in one of the corners.

# Small tile
fixed_pattern_0 = [['A1', 'O']] 
fixed_pattern_1 = [['J7', 'X']]

# Wide tile
fixed_pattern_2 = [['A7', 'B7', 'O']] 
fixed_pattern_3 = [['I1', 'J1', 'X']]

# Tall tile
fixed_pattern_4 = [['A1', 'A2', 'O']] 
fixed_pattern_5 = [['J6', 'J7', 'X']]

# Big tile
fixed_pattern_6 = [['A6', 'B6', 'A7', 'B7', 'O']] 
fixed_pattern_7 = [['I1', 'J1', 'I2', 'J2', 'X']]

# Each of these patterns puts multiple copies of the same
# type of tile in the grid.

# Small tiles
fixed_pattern_8 = [['E1', 'O'],
                   ['J4', 'O'],
                   ['C5', 'O'],
                   ['B1', 'O'],
                   ['I1', 'O']] 
fixed_pattern_9 = [['C6', 'X'],
                   ['I4', 'X'],
                   ['D6', 'X'],
                   ['J5', 'X'],
                   ['F6', 'X'],
                   ['F7', 'X']]

# Wide tiles
fixed_pattern_10 = [['A4', 'B4', 'O'],
                    ['C1', 'D1', 'O'],
                    ['C7', 'D7', 'O'],
                    ['A7', 'B7', 'O'],
                    ['D4', 'E4', 'O']] 
fixed_pattern_11 = [['D7', 'E7', 'X'],
                    ['G7', 'H7', 'X'],
                    ['H5', 'I5', 'X'],
                    ['B3', 'C3', 'X']]

# Tall tiles
fixed_pattern_12 = [['J2', 'J3', 'O'],
                    ['E5', 'E6', 'O'],
                    ['I1', 'I2', 'O'],
                    ['E1', 'E2', 'O'],
                    ['D3', 'D4', 'O']] 
fixed_pattern_13 = [['H4', 'H5', 'X'],
                    ['F1', 'F2', 'X'],
                    ['E2', 'E3', 'X'],
                    ['C4', 'C5', 'X']]

# Big tiles
fixed_pattern_14 = [['E5', 'F5', 'E6', 'F6', 'O'],
                    ['I5', 'J5', 'I6', 'J6', 'O'],
                    ['C2', 'D2', 'C3', 'D3', 'O'],
                    ['H2', 'I2', 'H3', 'I3', 'O'],
                    ['A3', 'B3', 'A4', 'B4', 'O']] 
fixed_pattern_15 = [['G2', 'H2', 'G3', 'H3', 'X'],
                    ['E5', 'F5', 'E6', 'F6', 'X'],
                    ['E3', 'F3', 'E4', 'F4', 'X'],
                    ['B3', 'C3', 'B4', 'C4', 'X']]

# Each of these patterns puts one instance of each type
# of tile in the grid.
fixed_pattern_16 = [['I5', 'O'],
                    ['E1', 'F1', 'E2', 'F2', 'O'],
                    ['J5', 'J6', 'O'],
                    ['G7', 'H7', 'O']]
fixed_pattern_17 = [['G7', 'H7', 'X'],
                    ['B7', 'X'],
                    ['A5', 'B5', 'A6', 'B6', 'X'],
                    ['D2', 'D3', 'X']]

# If you want to create your own test data sets put them here,
# otherwise call function random_pattern to obtain data sets
# that fill the entire grid with tiles.
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a
# tessellation to draw.  Your program must work for any data set that
# can be returned by this function.  The results returned by calling
# this function will be used as the argument to your "tessellate"
# function during marking.  For convenience during code development
# and marking this function also prints the pattern to be drawn to the
# shell window.  NB: Your solution should not print anything else to
# the shell.  Make sure any debugging calls to the "print" function
# are disabled before you submit your solution.
#
# This function attempts to place tiles using a largest-to-smallest
# greedy algorithm.  However, it randomises the placement of the
# tiles and makes no attempt to avoid trying the same location more
# than once, so it's not very efficient and doesn't maximise the
# number of larger tiles placed.  In the worst case, only one big
# tile will be placed in the grid (but this is very unlikely)!
#
# As well as the coordinates for each tile, an additional value which
# is either an 'O' or 'X' accompanies each one.  The purpose of this
# "mystery" value will be revealed in Part B of the assignment.
#
def random_pattern(print_pattern = True):
    # Keep track of squares already occupied
    been_there = []
    # Initialise the pattern
    pattern = []
    # Percent chance of the mystery value being an X
    mystery_probability = 8

    # Attempt to place as many 2x2 tiles as possible, up to a fixed limit
    attempts = 10
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 2)
        # Try to place the tile there, provided the spaces are all free
        if (not [column, row] in been_there) and \
           (not [column, row + 1] in been_there) and \
           (not [column + 1, row] in been_there) and \
           (not [column + 1, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1],
                                       [column + 1, row], [column + 1, row + 1]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            chr(column + ord('A') + 1) + str(row + 2),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1

    # Attempt to place as many 1x2 tiles as possible, up to a fixed limit
    attempts = 15
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 1)
        row = randint(0, grid_height - 2)
        # Try to place the tile there, provided the spaces are both free
        if (not [column, row] in been_there) and \
           (not [column, row + 1] in been_there):
            been_there = been_there + [[column, row], [column, row + 1]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A')) + str(row + 2),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1
        
    # Attempt to place as many 2x1 tiles as possible, up to a fixed limit
    attempts = 20
    while attempts > 0:
        # Choose a random bottom-left location
        column = randint(0, grid_width - 2)
        row = randint(0, grid_height - 1)
        # Try to place the tile there, provided the spaces are both free
        if (not [column, row] in been_there) and \
           (not [column + 1, row] in been_there):
            been_there = been_there + [[column, row], [column + 1, row]]
            # Append the tile's coords to the pattern, plus the mystery value
            pattern.append([chr(column + ord('A')) + str(row + 1),
                            chr(column + ord('A') + 1) + str(row + 1),
                            'X' if randint(1, 100) <= mystery_probability else 'O'])
        # Keep track of the number of attempts
        attempts = attempts - 1
        
    # Fill all remaining spaces with 1x1 tiles
    for column in range(0, grid_width):
        for row in range(0, grid_height):
            if not [column, row] in been_there:
                been_there.append([column, row])
                # Append the tile's coords to the pattern, plus the mystery value
                pattern.append([chr(column + ord('A')) + str(row + 1),
                                'X' if randint(1, 100) <= mystery_probability else 'O'])

    # Remove any residual structure in the pattern
    shuffle(pattern)
    # Print the pattern to the shell window, nicely laid out
    print('Draw the tiles in this sequence:')
    print(str(pattern).replace('],', '],\n'))
    # Return the tessellation pattern
    return pattern

#
#-----Student's Solution: Tile Function Definitions---------------------------------------------#
# Function for Small Tile
def smallTile(coordinate, broken):
    # Define varibables and set to null
    x = None
    y = None
    gotoDraw = None

    penup()

    # If statement to use numerical inputs or coordinates given and place tile in relative location
    if type(coordinate[0][0]) == str:
        x = ord(coordinate[0])
        y = int(coordinate[1])

        #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
        gotoDraw = goto((x - 64) * cell_size - 600, (y * cell_size) - 450)    
    elif type(coordinate[0][0]) == int:
        x = int(coordinate[0][0])
        y = int(coordinate[0][1])

        #---- Goto these coordinates using the varibles above ---#
        gotoDraw = goto(x,y)

    # Draw Border
    pensize(5)
    color("black")
    fillcolor('navy')
    
    gotoDraw
    
    pendown()
    
    begin_fill()
    setheading(0)
    forward(cell_size)
    setheading(90)
    forward(cell_size)
    setheading(180)
    forward(cell_size)
    setheading(270)
    forward(cell_size)

    end_fill()

    # Draw Minecraft Diamond
    corner = 90

    penup()
    setheading(45)
    forward(15)
    setheading(0)
    forward(20)

    color('royal blue')
    fillcolor('deep sky blue')
    
    begin_fill()
    pendown()
    
    forward(40)
    left(corner)
    forward(10)
    right(corner)
    forward(10)
    left(corner)
    forward(15)
    right(corner)
    forward(10)
    left(corner)
    forward(20)
    left(corner)
    forward(10)
    right(corner)
    forward(15)

    for i in range(2):
        left(corner)
        forward(10)
        right(corner)
        forward(10)
    
    left(corner)
    forward(20)

    for i in range(2):
        left(corner)
        forward(10)
        right(corner)
        forward(10)
            
    left(corner)
    forward(15)
    right(corner)
    forward(10)
    left(corner)
    forward(20)
    left(corner)
    forward(10)
    right(corner)
    forward(15)
    left(corner)
    forward(10)
    right(corner)
    forward(10)

    end_fill()
    penup()

    left(corner)
    forward(5)
    setheading(90)
    forward(35)

    fillcolor('light cyan')
    pendown()
    
    forward(15)
    begin_fill()
    
    for i in range(4):
        right(90)
        forward(30)
    end_fill()

    penup()
    setheading(-45)
    forward(20)

    color('cyan')
    pendown()
    
    dot(14)

    penup()
    
    # Draw Broken Tile
    if broken == 'X':

        pencolor('black')
        fillcolor('light grey')
        tileSize=100

        #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
        goto((x - 64) * cell_size - 600, (y * cell_size) - 450)  
        pendown()
        
        setheading(45)
        forward(tileSize//2)

        begin_fill()
        circle(-15)
        end_fill()

        begin_fill()
        setheading(90)
        forward(tileSize - 60)

        setheading(-20)
        forward(tileSize - 80)

        setheading(-75)
        forward(tileSize - 60)
        end_fill()

        setheading(65)
        forward(75)

        penup()
        
# Function for Tall Tile
def tallTile(coordinate, broken):

    # Take the relative input from the Tessellate Function, calculate the numerical value of the letter given and set the number to a integer value.
    # Place both set of coordinates given respectively:
    x1 = ord(coordinate[0][0])
    y1 = int(coordinate[0][1])

    x2 = ord(coordinate[1][0])
    y2 = int(coordinate[1][1])

    # Statement to swap coordinates if given in wrong order
    if y1 > y2:
        temp =  y2
        y2 = y1
        y1 = temp

    penup()

    # Draw bottom border
    pensize(5)
    color("black")
    fillcolor('red')

    #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
    goto((x1 - 64) * cell_size - 600, (y1 * cell_size) - 450)
    
    pendown()
    
    begin_fill()
    setheading(0)
    forward(cell_size)
    setheading(90)
    forward(cell_size)
    
    penup()

    # Leave a space
    setheading(180)
    forward(cell_size)
    #-------------#
    
    pendown()
    
    setheading(270)
    forward(cell_size)
    
    penup()

    # Draw top border #
    
    #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
    goto((x2 - 64) * cell_size - 600, (y2 * cell_size) - 450)
    
    setheading(0)
    forward(cell_size)
    
    pendown()
    
    setheading(90)
    forward(cell_size)
    setheading(180)
    forward(cell_size)
    setheading(270)
    forward(cell_size + 10)
    end_fill()
    
    penup()

    # Draw Minecraft Creeper

    setheading(0)
    forward(35)
    
    fillcolor('lime green')
    pendown()

    begin_fill()
    setheading(90)
    forward(50)
    setheading(180)
    forward(10)
    setheading(90)
    forward(40)
    setheading(0)
    forward(50)
    setheading(270)
    forward(40)
    setheading(180)
    forward(10)
    setheading(270)
    forward(90)
    end_fill()

    fillcolor('dim gray')
    
    begin_fill()
    setheading(0)
    forward(10)
    setheading(270)
    forward(25)
    setheading(180)
    forward(50)
    setheading(90)
    forward(25)
    setheading(0)
    forward(25)
    end_fill()
    
    setheading(270)
    forward(25)
    setheading(90)
    forward(25)
    setheading(0)
    forward(25)
    setheading(180)
    forward(10)

    fillcolor('lime green')
    
    begin_fill()
    setheading(180)
    forward(30)
    setheading(90)
    forward(40)
    end_fill()

    penup()

    forward(70)

    fillcolor('black')
    begin_fill()

    pendown()

    right(90)
    forward(5)
    left(90)
    forward(5)
    left(90)
    forward(5)
    left(90)
    forward(5)

    penup()

    left(90)
    forward(30)

    pendown()
    left(90)
    forward(5)
    left(90)
    forward(5)
    left(90)
    forward(5)
    left(90)
    forward(5)
    end_fill()
    
    penup()
    
    setheading(270)
    forward(5)
    setheading(180)
    forward(14)
    pendown()
    begin_fill()
    forward(5)
    setheading(270)
    forward(5)
    setheading(180)
    forward(5)
    setheading(270)
    forward(10)
    setheading(0)
    forward(5)
    setheading(90)
    forward(5)
    setheading(0)
    forward(8)
    setheading(270)
    forward(5)
    setheading(0)
    forward(5)
    setheading(90)
    forward(10)
    setheading(180)
    forward(5)
    setheading(90)
    forward(5)
    end_fill()

    penup()
    
    # Draw Broken Tile
    if broken == 'X':
        tileSize = 100
        pencolor('black')
        fillcolor('light grey')

        #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
        goto((x1 - 64) * cell_size - 600, (y1 * cell_size) - 450)
        pendown()
        
        setheading(65)
        forward(tileSize)

        begin_fill()
        circle(-15)
        end_fill()

        begin_fill()
        setheading(90)
        forward(tileSize - 60)
        setheading(-20)
        forward(tileSize - 80)
        setheading(-75)
        forward(tileSize - 60)
        end_fill()

        setheading(78)
        forward(115)
        
        penup()

# Function for Wide Tile
def wideTile(coordinate, broken):

    # Take the relative input from the Tessellate Function, calculate the numerical value of the letter given and set the number to a integer value.
    # Place both set of coordinates given respectively:
    x1 = ord(coordinate[0][0])
    y1 = int(coordinate[0][1])

    x2 = ord(coordinate[1][0])
    y2 = int(coordinate[1][1])

    penup()

    # Draw left border
    pensize(5)
    color("black")
    fillcolor('Gold')

    #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
    goto((x1 - 64) * cell_size - 600, (y1 * cell_size) - 450)

    pendown()
    
    begin_fill()
    setheading(0)
    forward(cell_size)

    penup()
    
    # Leave a space
    setheading(90)
    forward(cell_size)
    #-------------#
    
    pendown()
    
    setheading(180)
    forward(cell_size)
    setheading(270)
    forward(cell_size)
    end_fill()
    
    penup()

    # Draw right border #
    #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
    goto((x2 - 64) * cell_size - 600, (y2 * cell_size) - 450)

    pendown()

    begin_fill()
    setheading(0)
    forward(cell_size)
    setheading(90)
    forward(cell_size)
    setheading(180)
    forward(cell_size)
    end_fill()

    penup()

    # Draw Minecraft Spider

    penup()
    
    setheading(-90)
    forward(15)

    fillcolor('black')

    pendown()
    
    begin_fill()
    setheading(180)
    forward(25)
    setheading(-90)
    forward(20)
    setheading(-150)
    forward(70)
    setheading(-50)
    forward(10)
    setheading(30)
    forward(45)
    setheading(-120)
    forward(40)
    setheading(-30)
    forward(10)
    setheading(60)
    forward(50)
    setheading(-90)
    forward(20)
    setheading(0)
    forward(50)
    setheading(90)
    forward(20)
    setheading(-60)
    forward(50)
    setheading(30)
    forward(10)
    setheading(120)
    forward(42)
    setheading(-30)
    forward(50)
    setheading(60)
    forward(10)
    setheading(150)
    forward(70)
    setheading(90)
    forward(20)
    setheading(180)
    forward(50)
    setheading(-90)
    forward(55)
    setheading(0)
    forward(50)
    setheading(90)
    forward(50)
    setheading(180)
    forward(50)
    setheading(270)
    forward(50)
    setheading(0)
    forward(50)
    setheading(90)
    forward(50)
    end_fill()

    setheading(-135)
    forward(10)
    setheading(-90)

    # Draw Eyes
    fillcolor('red')
    begin_fill()
    for i in range(4):
        forward(15)
        right(90)
    end_fill()

    setheading(180)
    forward(20)
    setheading(-90)

    begin_fill()
    for i in range(4):
        forward(15)
        right(90)
    end_fill()
    
    penup()
    setheading(-90)
    forward(35)

    # Draw Fangs
    fillcolor('Midnight Blue')
    begin_fill()
    for i in range(4):
        forward(20)
        right(90)
    end_fill()
    
    penup()

    setheading(0)
    forward(5)

    begin_fill()
    for i in range(4):
        forward(20)
        right(90)
    end_fill()
    penup()

    # Draw Broken Version
    if broken == 'X':
        tileSize = 200
        pencolor('black')
        fillcolor('light grey')
        
        #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
        goto((x1 - 64) * cell_size - 600, (y1 * cell_size) - 450)
        
        pendown()
        
        setheading(45)
        forward(tileSize // 4)
        setheading(0)
        forward(50)
        
        begin_fill()
        circle(-15)
        end_fill()

        begin_fill()
        setheading(90)
        forward(tileSize // 6)
        setheading(-20)
        forward(tileSize // 8)
        setheading(-75)
        forward(tileSize // 6)
        end_fill()

        setheading(41)
        forward(103)

        penup()

# Function for Big Tile
def bigTile(coordinate, broken):

    # Take the relative input from the Tessellate Function, calculate the numerical value of the letter given and set the number to a integer value.
    # Place all set of coordinates given respectively:
    x1 = ord(coordinate[0][0])
    y1 = int(coordinate[0][1])

    x2 = ord(coordinate[1][0])
    y2 = int(coordinate[1][1])

    x3 = ord(coordinate[2][0])
    y3 = int(coordinate[2][1])

    x4 = ord(coordinate[3][0])
    y4 = int(coordinate[3][1])

    penup()

    # Bottom Left Square
    pensize(5)
    pencolor("black")
    fillcolor('green')
    
    # Draws Border
    #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
    goto((x1 - 64) * cell_size - 600, (y1 * cell_size) - 450)
    
    pendown()
    
    begin_fill()
    setheading(0)
    forward(cell_size)
    setheading(90)
    forward(cell_size)
    setheading(180)
    forward(cell_size)
    setheading(270)
    forward(100)

    penup()
    
    # Bottom Right Square
    pensize(5)
    pencolor("black")
    
    #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
    goto((x2 - 64) * cell_size - 600, (y2 * cell_size) - 450)

    pendown()

    # Draws Border
    setheading(0)
    forward(cell_size)  
    setheading(90)
    forward(cell_size)
    setheading(180)
    forward(cell_size)
    end_fill()
    
    penup()


    # Top Left Square
    pensize(5)
    pencolor("black")
    fillcolor('sky blue')
    
    #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
    goto((x3 - 64) * cell_size - 600, (y3 * cell_size) - 450)
    
    # Draws Border

    penup()
    
    setheading(0)
    forward(cell_size)
    setheading(90)
    forward(cell_size)

    pendown()

    begin_fill()
    setheading(180)
    forward(cell_size)
    setheading(270)
    forward(cell_size)

    penup()

    # Top Right Square
    pensize(5)
    pencolor("black")
    
    #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
    goto((x4 - 64) * cell_size - 600, (y4 * cell_size) - 450)

    # Draws Border

    penup()
    
    setheading(0)
    forward(cell_size)

    pendown()
    
    setheading(90)
    forward(cell_size)
    setheading(180)
    forward(cell_size)
    end_fill()

    penup()

    # Draw Minecraft House
    
    fillcolor("Dark Goldenrod")
    
    setheading(270)
    forward(30)

    pendown()

    begin_fill()
    setheading(180)
    forward(70)
    setheading(270)
    forward(170)
    setheading(0)
    forward(140)
    setheading(90)
    forward(170)
    setheading(180)
    forward(70)
    end_fill()

    penup()

    #-------------------------#
    # Draw Window #

    fillcolor("Deep Sky Blue")
    
    setheading(270)
    forward(20)

    pendown()
    
    begin_fill()
    setheading(180)
    forward(50)
    setheading(270)
    forward(40)
    setheading(0)
    forward(100)
    setheading(90)
    forward(40)
    setheading(180)
    forward(50)
    end_fill()
    
    penup()

    #-------------------------#
    # Draw Window Glare Streaks #

    pencolor('white')
    
    setheading(270)
    forward(10)

    pendown()

    setheading(225)
    forward(30)

    penup()

    setheading(45)
    forward(30)
    setheading(0)
    forward(20)

    pendown()
    
    setheading(225)
    forward(30)

    penup()
    
    #-------------------------#
    
    setheading(270)
    forward(50)

    pencolor('Black')
    
    pendown()
    
    begin_fill()
    setheading(180)
    forward(30)
    setheading(270)
    forward(30)
    setheading(0)
    forward(60)
    setheading(90)
    forward(30)
    setheading(180)
    forward(60)
    end_fill()

    # Draw Doors
    for i in range(2):

        setheading(270)
        forward(70)

        penup()
        
        setheading(0)
        forward(30)
        
        pendown()        
        setheading(90)
        forward(40)
        setheading(180)
        forward(30)
        setheading(0)
        forward(15)
        setheading(90)
        forward(15)
        setheading(180)
        forward(15)
        setheading(0)
        forward(30)
        setheading(180)
        forward(15)
        setheading(90)
        forward(15)
        setheading(0)
        forward(15)

    setheading(270)
    forward(70)
    setheading(90)
    forward(70)
    setheading(180)
    forward(30)
    setheading(270)
    forward(40)
    setheading(0)
    forward(10)
    setheading(180)
    forward(20)

    penup()

    # Draw Broken Tile
    if broken == 'X':
        tileSize=200
        pencolor('black')
        fillcolor('light grey')

        #---- Using the respective variables, goto these coordinates in ratio to the grid ---#
        goto((x1 - 64) * cell_size - 600, (y1 * cell_size) - 450)
        
        pendown()
        setheading(45)
        forward(tileSize//2)

        begin_fill()
        circle(-15)
        end_fill()

        begin_fill()
        setheading(90)
        forward(tileSize - 80)
        setheading(-45)
        forward(60)
        setheading(-90)
        forward(tileSize - 60)
        end_fill()

        setheading(66)
        forward(205)

        penup()

#-----Student's Solution: Tesselate---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "tessellate" function.
#
# Fill the grid with tiles as per the provided dataset
# Function Definition for Tessellation
def tessellate(coordinates):
    # Using for loop to sort through random_pattern list and determaine number of elements
    for coordinate in random_pattern():

        #---- Tessellation Code for Small Tiile ----#
        # If current position is random_pattern has 2 elements draw a Small Tile using the first element within the list for coordinates and the other to determaine wheather the tile is broken or not #
        if len(coordinate) == 2 and coordinate[1] == 'O':
            smallTile(coordinate[0], coordinate[1])
        elif len(coordinate) == 2 and coordinate[1] == 'X':
            smallTile(coordinate[0], coordinate[1])

        #---- Tessellation Code for Tall Tiile ----#
        # If current position is random_pattern has 3 elements and the y-coordinates are equal, draw a Tall Tile using the first 2 element within the list for coordinates and the other to determaine wheather the tile is broken or not #
        if len(coordinate) == 3 and coordinate[0][0] == coordinate[1][0] and coordinate[2] == 'O':
            tallTile([coordinate[0], coordinate[1]], coordinate[2])
        elif len(coordinate) == 3 and coordinate[0][0] == coordinate[1][0] and coordinate[2] == 'X':
            tallTile([coordinate[0], coordinate[1]], coordinate[2])

        #---- Tessellation Code for Wide Tiile ----#
        # If current position is random_pattern has 3 elements and the x-coordinates are equal, draw a Tall Tile using the first 2 element within the list for coordinates and the other to determaine wheather the tile is broken or not #
        if len(coordinate) == 3  and coordinate[0][1] == coordinate[1][1] and coordinate[2] == 'O':
            wideTile([coordinate[0], coordinate[1]], coordinate[2])
        elif len(coordinate) == 3  and coordinate[0][1] == coordinate[1][1] and coordinate[2] == 'X':
            wideTile([coordinate[0], coordinate[1]], coordinate[2])

        #---- Tessellation Code for Big Tiile ----#
        # If current position is random_pattern has 5 elements draw a Big Tile using the first 4 element within the list for coordinates and the other to determaine wheather the tile is broken or not #
        if len(coordinate) == 5 and coordinate[4] == 'O':
            bigTile([coordinate[0], coordinate[1], coordinate[2], coordinate[3]], coordinate[4])
        elif len(coordinate) == 5 and coordinate[4] == 'X':
                bigTile([coordinate[0], coordinate[1], coordinate[2], coordinate[3]], coordinate[4])
pass 

#
#-----Student's Solution: Legend Function Definitions---------------------------------------------#
def leftLegend(x = -725):
    #---- Small Tile ----#
    smallTile([[x,100]],'O')
    
    #---- Tall Tile ----#
    pensize(5)
    color("black")
    fillcolor('red')

    goto(x, -200)
    
    pendown()
    
    begin_fill()
    setheading(0)
    forward(100)
    setheading(90)
    forward(200)
    setheading(180)
    forward(100)
    setheading(270)
    forward(200)
    end_fill()

    penup()

    setheading(90)
    forward(90)

    # Draw Minecraft Creeper
    
    setheading(0)
    forward(35)
    
    fillcolor('lime green')
    pendown()

    begin_fill()
    setheading(90)
    forward(50)
    setheading(180)
    forward(10)
    setheading(90)
    forward(40)
    setheading(0)
    forward(50)
    setheading(270)
    forward(40)
    setheading(180)
    forward(10)
    setheading(270)
    forward(90)
    end_fill()

    fillcolor('dim gray')
    
    begin_fill()
    setheading(0)
    forward(10)
    setheading(270)
    forward(25)
    setheading(180)
    forward(50)
    setheading(90)
    forward(25)
    setheading(0)
    forward(25)
    end_fill()
    
    setheading(270)
    forward(25)
    setheading(90)
    forward(25)
    setheading(0)
    forward(25)
    setheading(180)
    forward(10)

    fillcolor('lime green')
    
    begin_fill()
    setheading(180)
    forward(30)
    setheading(90)
    forward(40)
    end_fill()

    penup()

    forward(70)

    fillcolor('black')
    begin_fill()

    pendown()

    right(90)
    forward(5)
    left(90)
    forward(5)
    left(90)
    forward(5)
    left(90)
    forward(5)

    penup()

    left(90)
    forward(30)

    pendown()
    left(90)
    forward(5)
    left(90)
    forward(5)
    left(90)
    forward(5)
    left(90)
    forward(5)
    end_fill()
    
    penup()
    
    setheading(270)
    forward(5)
    setheading(180)
    forward(14)
    pendown()
    begin_fill()
    forward(5)
    setheading(270)
    forward(5)
    setheading(180)
    forward(5)
    setheading(270)
    forward(10)
    setheading(0)
    forward(5)
    setheading(90)
    forward(5)
    setheading(0)
    forward(8)
    setheading(270)
    forward(5)
    setheading(0)
    forward(5)
    setheading(90)
    forward(10)
    setheading(180)
    forward(5)
    setheading(90)
    forward(5)
    end_fill()

    penup()

def rightLegend(x = 550):

    #---- Wide Tile ----X
    pensize(5)
    color("black")
    fillcolor('Gold')
    goto(x,100)
    
    pendown()
    
    begin_fill()
    setheading(0)
    forward(200)
    setheading(90)
    forward(100)
    setheading(180)
    forward(200)
    setheading(270)
    forward(100)
    end_fill()

    penup()

    setheading(90)
    forward(100)
    setheading(0)
    forward(100)

    # Draw Minecraft Spider
    
    penup()
    
    setheading(-90)
    forward(15)

    fillcolor('black')

    pendown()
    
    begin_fill()
    setheading(180)
    forward(25)
    setheading(-90)
    forward(20)
    setheading(-150)
    forward(70)
    setheading(-50)
    forward(10)
    setheading(30)
    forward(45)
    setheading(-120)
    forward(40)
    setheading(-30)
    forward(10)
    setheading(60)
    forward(50)
    setheading(-90)
    forward(20)
    setheading(0)
    forward(50)
    setheading(90)
    forward(20)
    setheading(-60)
    forward(50)
    setheading(30)
    forward(10)
    setheading(120)
    forward(42)
    setheading(-30)
    forward(50)
    setheading(60)
    forward(10)
    setheading(150)
    forward(70)
    setheading(90)
    forward(20)
    setheading(180)
    forward(50)
    setheading(-90)
    forward(55)
    setheading(0)
    forward(50)
    setheading(90)
    forward(50)
    setheading(180)
    forward(50)
    setheading(270)
    forward(50)
    setheading(0)
    forward(50)
    setheading(90)
    forward(50)
    end_fill()

    setheading(-135)
    forward(10)
    setheading(-90)

    fillcolor('red')
    begin_fill()
    for i in range(4):
        forward(15)
        right(90)
    end_fill()

    setheading(180)
    forward(20)
    setheading(-90)

    begin_fill()
    for i in range(4):
        forward(15)
        right(90)
    end_fill()
    
    penup()
    setheading(-90)
    forward(35)
    
    fillcolor('Midnight Blue')
    begin_fill()
    for i in range(4):
        forward(20)
        right(90)
    end_fill()
    
    penup()

    setheading(0)
    forward(5)

    begin_fill()
    for i in range(4):
        forward(20)
        right(90)
    end_fill()
    penup()

    #---- Big Tile ----#
    penup()

    # Bottom Left Square
    pensize(5)
    pencolor("black")
    fillcolor('green')
    goto(x, -200)

    # Draws Border
    pendown()
    
    begin_fill()
    setheading(0)
    forward(cell_size)
    setheading(90)
    forward(cell_size)
    setheading(180)
    forward(cell_size)
    setheading(270)
    forward(100)

    penup()
    
    # Bottom Right Square
    pensize(5)
    pencolor("black")
    goto((x + 100), -200)

    # Draws Border
    pendown()
    
    setheading(0)
    forward(cell_size)
    setheading(90)
    forward(cell_size)
    setheading(180)
    forward(cell_size)
    end_fill()
    
    penup()

    # Top Left Square
    pensize(5)
    pencolor("black")
    fillcolor('sky blue')
    goto(x, -100)

    # Draws Border
    penup()
    
    setheading(0)
    forward(cell_size)
    setheading(90)
    forward(cell_size)

    pendown()
    
    begin_fill()
    setheading(180)
    forward(cell_size)
    setheading(270)
    forward(cell_size)

    penup()

    # Top Right Square
    goto((x + 100), -100)
    pencolor("black")
    pensize(5)

    pendown()

    # Draws Border

    penup()
    
    setheading(0)
    forward(cell_size)

    pendown()
    
    setheading(90)
    forward(cell_size)
    setheading(180)
    forward(cell_size)
    end_fill()

    penup()

    # Draw Minecraft House

    fillcolor("Dark Goldenrod")
    
    setheading(270)
    forward(30)

    pendown()

    begin_fill()
    setheading(180)
    forward(70)
    setheading(270)
    forward(170)
    setheading(0)
    forward(140)
    setheading(90)
    forward(170)
    setheading(180)
    forward(70)
    end_fill()

    penup()

    ####

    fillcolor("Deep Sky Blue")
    
    setheading(270)
    forward(20)

    pendown()
    
    begin_fill()
    setheading(180)
    forward(50)
    setheading(270)
    forward(40)
    setheading(0)
    forward(100)
    setheading(90)
    forward(40)
    setheading(180)
    forward(50)
    end_fill()
    
    penup()

    ####

    pencolor('white')
    
    setheading(270)
    forward(10)

    pendown()

    setheading(225)
    forward(30)

    penup()

    setheading(45)
    forward(30)
    setheading(0)
    forward(20)

    pendown()
    
    setheading(225)
    forward(30)

    penup()
    
    ####
    setheading(270)
    forward(50)

    pencolor('Black')
    
    pendown()
    
    begin_fill()
    setheading(180)
    forward(30)
    setheading(270)
    forward(30)
    setheading(0)
    forward(60)
    setheading(90)
    forward(30)
    setheading(180)
    forward(60)
    end_fill()

    for i in range(2):

        setheading(270)
        forward(70)

        penup()
        
        setheading(0)
        forward(30)
        
        pendown()        
        setheading(90)
        forward(40)
        setheading(180)
        forward(30)
        setheading(0)
        forward(15)
        setheading(90)
        forward(15)
        setheading(180)
        forward(15)
        setheading(0)
        forward(30)
        setheading(180)
        forward(15)
        setheading(90)
        forward(15)
        setheading(0)
        forward(15)

    setheading(270)
    forward(70)
    setheading(90)
    forward(70)
    setheading(180)
    forward(30)
    setheading(270)
    forward(40)
    setheading(0)
    forward(10)
    setheading(180)
    forward(20)

    penup()

#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
# ***** You can change the background and line colours, and choose
# ***** whether or not to draw the grid and mark the places for the
# ***** legend, by providing arguments to this function call
create_drawing_canvas()

# Control the drawing speed
# ***** Change the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves slowly around the screen
tracer(False)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tiles
title("Minecraft Elements")

### Call the student's function to follow the path
### ***** While developing your program you can call the tessellate
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_pattern()" as the
### ***** argument.  Your tessellate function must work for any data
### ***** set that can be returned by the random_pattern function.
# tessellate(fixed_pattern_0) # <-- used for code development only, not marking
tessellate(random_pattern()) # <-- used for assessment
leftLegend()
rightLegend()

# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
