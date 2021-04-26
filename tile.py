import stddraw  # the stddraw module is used as a basic graphics library
from color import Color  # used for coloring the tile and the number on it
from point import Point  # used for representing the position of the tile
import copy as cp  # the copy module is used for copying tile positions
import random
import math  # math module that provides mathematical functions


# Class used for representing numbered tiles as in 2048
class Tile:
    # Class attributes shared among all Tile objects
    # ---------------------------------------------------------------------------
    # value used for the thickness of the boxes (boundaries) around the tiles
    boundary_thickness = 0.006
    # font family and size used for displaying the tile number
    font_family, font_size = "Arial", 16

    # Constructor that creates a tile at a given position with 2 as its number
    def __init__(self, position=Point(0, 0)):  # (0, 0) is the default position
        # assign the number on the tile
        self.number = 2 ** random.randint(1, 3)
        self.foreground_color = Color(255, 238, 214)  # foreground (number) color
        # Coloring algorithm
        if self.number == 2:
            self.foreground_color = Color(130, 114, 92)
            c1 = 247
            c2 = 238
            c3 = 228

        if self.number == 4:
            self.foreground_color = Color(130, 114, 92)
            c1 = 240
            c2 = 208
            c3 = 170
        if self.number == 8:
            c1 = 237
            c2 = 187
            c3 = 153

        # set the colors of the tile
        self.background_color = Color(c1, c2, c3)  # background (tile) color

        self.boundary_color = Color(173, 164, 149)  # boundary (box) color
        # set the position of the tile as the given position
        self.position = Point(position.x, position.y)

    # Setter method for the position of the tile
    def set_position(self, position):
        # set the position of the tile as the given position
        self.position = cp.copy(position)

    # Getter method for the position of the tile
    def get_position(self):
        # return the position of the tile
        return cp.copy(self.position)

    def set_color(self, c1, c2, c3):
        self.background_color = Color(c1, c2, c3)  # background (tile) color

    def set_foreground_color(self, c1, c2, c3):
        self.foreground_color = Color(c1, c2, c3)  # background (tile) color

    def set_number(self, number):
        self.number = number

    def get_number(self):
        return self.number

    # Method for moving the tile by dx along the x axis and by dy along the y axis
    def move(self, dx, dy):
        self.position.translate(dx, dy)

    # Method for drawing the tile
    def draw(self):
        # draw the tile as a filled square
        stddraw.setPenColor(self.background_color)
        stddraw.filledSquare(self.position.x, self.position.y, 0.5)
        # draw the bounding box of the tile as a square
        stddraw.setPenColor(self.boundary_color)
        stddraw.setPenRadius(Tile.boundary_thickness)
        stddraw.square(self.position.x, self.position.y, 0.5)
        stddraw.setPenRadius()  # reset the pen radius to its default value
        # draw the number on the tile
        stddraw.setPenColor(self.foreground_color)
        stddraw.setFontFamily(Tile.font_family)
        stddraw.setFontSize(Tile.font_size)
        stddraw.boldText(self.position.x, self.position.y, str(self.number))
        # print(self.position.x, self.position.y)

    # draw the next tetromino (first incoming)
    def draw_next(self, xa, yb):

        # draw the tile as a filled square
        stddraw.setPenColor(self.background_color)
        stddraw.filledSquare(14 + self.position.x - xa, 12 + self.position.y - yb, 0.5)
        # draw the bounding box of the tile as a square
        stddraw.setPenColor(self.boundary_color)
        stddraw.setPenRadius(Tile.boundary_thickness)
        stddraw.square(14 + self.position.x - xa, 12 + self.position.y - yb, 0.5)
        stddraw.setPenRadius()  # reset the pen radius to its default value
        # draw the number on the tile
        stddraw.setPenColor(self.foreground_color)
        stddraw.setFontFamily(Tile.font_family)
        stddraw.setFontSize(Tile.font_size)
        stddraw.boldText(14 + self.position.x - xa, 12 + self.position.y - yb, str(self.number))

    # draw the second incoming tetromino
    def draw_next_second(self, xa, yb):

        # draw the tile as a filled square
        stddraw.setPenColor(self.background_color)
        stddraw.filledSquare(14 + self.position.x - xa, 6 + self.position.y - yb, 0.5)
        # draw the bounding box of the tile as a square
        stddraw.setPenColor(self.boundary_color)
        stddraw.setPenRadius(Tile.boundary_thickness)
        stddraw.square(14 + self.position.x - xa, 6 + self.position.y - yb, 0.5)
        stddraw.setPenRadius()  # reset the pen radius to its default value
        # draw the number on the tile
        stddraw.setPenColor(self.foreground_color)
        stddraw.setFontFamily(Tile.font_family)
        stddraw.setFontSize(Tile.font_size)
        stddraw.boldText(14 + self.position.x - xa, 6 + self.position.y - yb, str(self.number))
