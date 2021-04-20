import stddraw # the stddraw module is used as a basic graphics library
from color import Color # used for coloring the game grid
import numpy as np # fundamental Python module for scientific computing
from point import Point
from tile import Tile
# Class used for modelling the game grid
class GameGrid:
	# Constructor for creating the game grid based on the given arguments
   def __init__(self, grid_h, grid_w):
      # set the dimensions of the game grid as the given arguments
      self.grid_height = grid_h
      self.grid_width = grid_w
      # create the tile matrix to store the tiles placed on the game grid
      self.tile_matrix = np.full((grid_h, grid_w), None)
      # the tetromino that is currently being moved on the game grid
      self.current_tetromino = None
      # the next tetromino that is draw next tetromino
      self.next_tetromino = None
      # game_over flag shows whether the game is over/completed or not
      self.game_over = False
      # set the color used for the empty grid cells
      self.empty_cell_color = Color(247, 237, 213)
      # set the colors used for the grid lines and the grid boundaries
      self.line_color = Color(0, 100, 200) 
      self.boundary_color = Color(0, 100, 200)
      # thickness values used for the grid lines and the grid boundaries 
      self.line_thickness = 0.002
      self.box_thickness = 8 * self.line_thickness

   # Method used for displaying the game grid
   def display(self,score, next_tetromino):
      # clear the background canvas to empty_cell_color
      stddraw.clear(self.empty_cell_color)
      # draw the game grid
      self.draw_grid(score, next_tetromino)
      # draw the current (active) tetromino
      if self.current_tetromino != None:
         self.current_tetromino.draw()

      # draw a box around the game grid 
      self.draw_boundaries()
      # show the resulting drawing with a pause duration = 250 ms
      stddraw.show(300)
         
   # Method for drawing the cells and the lines of the grid
   def draw_grid(self,score, next_tetromino):
      # draw each cell of the game grid
      for row in range(self.grid_height):
         for col in range(self.grid_width):
            # draw the tile if the grid cell is occupied by a tile
            if self.tile_matrix[row][col] != None:
               self.tile_matrix[row][col].draw()

      # draw the inner lines of the grid
      stddraw.setPenColor(self.line_color)
      stddraw.setPenRadius(self.line_thickness)
      # x and y ranges for the game grid
      start_x, end_x = -0.5, self.grid_width - 0.5
      start_y, end_y = -0.5, self.grid_height - 0.5
      for x in np.arange(start_x + 1, end_x, 1):  # vertical inner lines
         stddraw.line(x, start_y, x, end_y)
      for y in np.arange(start_y + 1, end_y, 1):  # horizontal inner lines
         stddraw.line(start_x, y, end_x, y)
      stddraw.setPenRadius()  # reset the pen radius to its default value
      stddraw.setPenRadius()  # reset the pen radius to its default value
      stddraw.setFontFamily("Arial")
      stddraw.setFontSize(25)
      stddraw.setPenColor(Color(31, 160, 239))
      a = score
      stddraw.boldText(14.1, 17, str(a))
      stddraw.text(14, 18, "Score")
      stddraw.text(14, 14, "Next Shape")
      # draw each cell of the game grid
      xa =-1
      yb =-1
      for row in range(len(next_tetromino.tile_matrix)):
         for col in range(len(next_tetromino.tile_matrix)):
            # draw the tile if the grid cell is occupied by a tile

            if next_tetromino.tile_matrix[row][col] != None:
               if(xa == -1):
                  xa = next_tetromino.tile_matrix[row][col].position.x
               if (yb == -1):
                  yb = next_tetromino.tile_matrix[row][col].position.y

               next_tetromino.tile_matrix[row][col].drawNext(xa, yb)
      
   # Method for drawing the boundaries around the game grid 
   def draw_boundaries(self):
      # draw a bounding box around the game grid as a rectangle
      stddraw.setPenColor(self.boundary_color)  # using boundary_color
      # set the pen radius as box_thickness (half of this thickness is visible 
      # for the bounding box as its lines lie on the boundaries of the canvas)
      stddraw.setPenRadius(self.box_thickness)
      # coordinates of the bottom left corner of the game grid
      pos_x, pos_y = -0.5, -0.5
      stddraw.rectangle(pos_x, pos_y, self.grid_width, self.grid_height)
      stddraw.setPenRadius()  # reset the pen radius to its default value

   # Method used for checking whether the grid cell with given row and column 
   # indexes is occupied by a tile or empty
   def is_occupied(self, row, col):
      # return False if the cell is out of the grid
      if not self.is_inside(row, col):
         return False
      # the cell is occupied by a tile if it is not None
      return self.tile_matrix[row][col] != None
      
   # Method used for checking whether the cell with given row and column indexes 
   # is inside the game grid or not
   def is_inside(self, row, col):
      if row < 0 or row >= self.grid_height:
         return False
      if col < 0 or col >= self.grid_width:
         return False
      return True

   # Method for updating the game grid by placing the given tiles of a stopped 
   # tetromino and checking if the game is over due to having tiles above the 
   # topmost game grid row. The method returns True when the game is over and
   # False otherwise.
   def update_grid(self, tiles_to_place):
      # place all the tiles of the stopped tetromino onto the game grid 
      n_rows, n_cols = len(tiles_to_place), len(tiles_to_place[0])
      for col in range(n_cols):
         for row in range(n_rows):            
            # place each occupied tile onto the game grid
            if tiles_to_place[row][col] != None:
               pos = tiles_to_place[row][col].get_position()
               if self.is_inside(pos.y, pos.x):
                  self.tile_matrix[pos.y][pos.x] = tiles_to_place[row][col]
               # the game is over if any placed tile is out of the game grid
               else:
                  self.game_over = True
      # return the game_over flag
      return self.game_over

   def clean_row(self,score):
      ctr = 0
      scr = score # to keep score
      for row in range(self.grid_height):
         for col in range(self.grid_width):
            # Counts filled tiles.
            if self.is_occupied(row,col):
               ctr += 1

         # Check if row is full
         if ctr == self.grid_width:
            # Delete full row and add to score
            for y in range(self.grid_width):
               scr += self.tile_matrix[row][y].get_number()
               self.tile_matrix[row][y] = None

               # Update grid and tile matrix in that particular column
               for x in range(row, self.grid_height-1):
                  if self.tile_matrix[x+1][y] is not None:
                     temp = self.tile_matrix[x+1][y]
                     self.tile_matrix[x+1][y].move(0, -1)
                     self.tile_matrix[x+1][y] = None
                     self.tile_matrix[x][y] = temp

         ctr = 0

      return scr

   def merge_tetrominos(self, score):

      # height and width
      height = self.grid_height
      width = self.grid_width

      # to check if two tiles are merged
      did_merged: bool

      # searches in column
      for col in range(width):
         # searches in row
         for row in range(height-1):
            did_merged = False # sets to false in the start of each loop

            # if initial and up-adjacent tile is not empty and numbers are equal, merges them
            if self.tile_matrix[row+1][col] is not None and self.tile_matrix[row][col] is not None:
               can_merged = self.tile_matrix[row][col].get_number() == self.tile_matrix[row+1][col].get_number()
               if can_merged:
                  new_num = self.tile_matrix[row][col].get_number() * 2 # update tile number
                  score += new_num  # update score

                  # update color
                  c1 = int(256 / (new_num - 1) + 90) % 256
                  c2 = int(256 / (new_num + 1) + 90) % 256
                  c3 = int(256 / new_num + 90) % 256

                  # update in matrix
                  self.tile_matrix[row][col].set_number(new_num)
                  self.tile_matrix[row][col].set_color(c1,c2,c3)

                  # set up-adjacent tile to zero
                  self.tile_matrix[row+1][col] = None
                  did_merged = True

            # moves entire row down by 1 if a merging happens
            if did_merged:
               for x in range(row, height-1):

                  if self.tile_matrix[x+1][col] is not None:
                     temp = self.tile_matrix[x+1][col]
                     self.tile_matrix[x+1][col].move(0, -1)
                     self.tile_matrix[x+1][col] = None
                     self.tile_matrix[x][col] = temp


      return score


   def four_connected(self):
      height = self.grid_height
      width= self.grid_width
      labeled_grid = np.zeros(shape=(height+2, width+2))
      new_tile_matrix = np.full(shape=(height+2 ,width+2), fill_value=None)
      for col in range(width):
         for row in range(height):
            new_tile_matrix[row+1][col+1] = self.tile_matrix[row][col]

      height += 2
      width += 2

      k = 0
      for i in range(1,height-1):
         for j in range(1, width-1):
            if new_tile_matrix[i][j] is not None:
               if new_tile_matrix[i-1][j] is None and new_tile_matrix[i][j - 1] is None:
                  k += 1
                  labeled_grid[i][j] = k

               elif new_tile_matrix[i - 1][j] is not None and new_tile_matrix[i][j - 1] is None:
                  labeled_grid[i][j] = labeled_grid[i - 1][j]

               elif new_tile_matrix[i - 1][j] is None and new_tile_matrix[i][j - 1] is not None:
                  labeled_grid[i][j] = labeled_grid[i][j - 1]

               elif new_tile_matrix[i - 1][j] is not None and new_tile_matrix[i][j - 1] is not None:
                  if labeled_grid[i - 1][j] == labeled_grid[i][j - 1]:
                     labeled_grid[i][j] = labeled_grid[i][j - 1]

                  else:
                     labeled_grid[i][j] = labeled_grid[i-1][j]
                     self.__change_label(labeled_grid, labeled_grid[i - 1][j], labeled_grid[i][j - 1], i, j)


      return labeled_grid

   def __change_label(self,label ,up_lbl, left_lbl, i, j):
      for x in range(i):
         for y in range(j):
            if label[x][y] == left_lbl:
               label[x][y] = up_lbl


      for n in range(j):
         if label[i][n] == left_lbl:
            label[i][n] = up_lbl

   def find_different_labels(self, labeled_grid):

        coordinates_array = np.zeros((10,2), dtype=np.int8)
        num_of_single_labels = 0
        for x in range(1, self.grid_height + 1):
            for y in range(1, self.grid_width + 1):
                a = labeled_grid[x][y]
                count = 0
                for j in range(1, self.grid_height + 1):
                    for k in range(1, self.grid_width + 1):
                        if labeled_grid[j][k] == a:
                            count += 1
                # assigning the corresponding coordinates of the tiles that have
                # a different label from the others
                if count == 1:
                    row_and_column = np.where(labeled_grid == a)
                    # do not include the tiles with the coordinate y = 0
                    if row_and_column[0] - 1 != 0:
                        coordinates_array[num_of_single_labels] = (row_and_column[1] - 1, row_and_column[0] - 1)
                        num_of_single_labels += 1

        coordinates_array.resize((num_of_single_labels, 2), refcheck=False)

        return coordinates_array

   def move_single_tile(self):

        single_labeled_tiles = self.find_different_labels(self.four_connected())
        if len(single_labeled_tiles) != 0:
            for k in range(len(single_labeled_tiles)):
                i = 0
                if single_labeled_tiles[k][1] - i > 0:
                    while self.tile_matrix[single_labeled_tiles[k][1] - i + -1][single_labeled_tiles[k][0]] == None:
                        if self.tile_matrix[single_labeled_tiles[k][1] - i][single_labeled_tiles[k][0] + 1] is not None:
                            break
                        if self.tile_matrix[single_labeled_tiles[k][1] - i][single_labeled_tiles[k][0] - 1] is not None:
                            break

                        temp = self.tile_matrix[single_labeled_tiles[k][1] - i][single_labeled_tiles[k][0]]
                        self.tile_matrix[single_labeled_tiles[k][1] - i][single_labeled_tiles[k][0]].move(0, - 1)
                        self.tile_matrix[single_labeled_tiles[k][1] - i][single_labeled_tiles[k][0]] = None
                        self.tile_matrix[single_labeled_tiles[k][1] - i - 1][single_labeled_tiles[k][0]] = temp
                        i += 1
