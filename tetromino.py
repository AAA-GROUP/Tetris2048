from point import Point # used for tile positions
import numpy as np # fundamental Python module for scientific computing
import math
<<<<<<< HEAD
#asd
# Class used for representing tetrominoes with 3 out of 7 different types/shapes 
# as (I, O and Z)
#Hello, world!
=======
>>>>>>> parent of a5decee (Revert "Update tetromino.py")

# Class used for representing tetrominoes with 7 different types/shapes

class Tetromino:
   # Constructor to create a tetromino with a given type (shape)
   def __init__(self, type, grid_height, grid_width):
      # set grid_height and grid_width from input parameters
      self.grid_height = grid_height
      self.grid_width = grid_width

      # set the shape of the tetromino based on the given type
      occupied_tiles = []
      if type == 'I':
@@ -21,52 +21,52 @@ def __init__(self, type, grid_height, grid_width):
         occupied_tiles.append((1, 0)) # (column_index, row_index)
         occupied_tiles.append((1, 1))
         occupied_tiles.append((1, 2))
<<<<<<< HEAD
         occupied_tiles.append((1, 3))           
=======
>>>>>>> parent of a5decee (Revert "Update tetromino.py")
         occupied_tiles.append((1, 3))
      elif type == 'O':
         n = 2  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino O in its initial orientation
<<<<<<< HEAD
         occupied_tiles.append((0, 0)) 
         occupied_tiles.append((0, 0))
         occupied_tiles.append((1, 0))
         occupied_tiles.append((0, 1))
         occupied_tiles.append((1, 1)) 
=======
         occupied_tiles.append((0, 0))
         occupied_tiles.append((1, 0))
         occupied_tiles.append((0, 1))
>>>>>>> parent of a5decee (Revert "Update tetromino.py")
         occupied_tiles.append((1, 1))
      elif type == 'Z':
         n = 3  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino Z in its initial orientation
<<<<<<< HEAD
         occupied_tiles.append((0, 0)) 
=======
>>>>>>> parent of a5decee (Revert "Update tetromino.py")
         occupied_tiles.append((0, 0))
         occupied_tiles.append((1, 0))
         occupied_tiles.append((1, 1))
         occupied_tiles.append((2, 1))
      elif type == 'S':
<<<<<<< HEAD
         n = 3
         occupied_tiles.append((2, 0))
         n = 3  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino S in its initial orientation
         occupied_tiles.append((1, 0))
         occupied_tiles.append((1, 1))
         occupied_tiles.append((2, 0))
         occupied_tiles.append((0, 1))

         occupied_tiles.append((1, 1))
      elif type == 'L':
         n = 3
         occupied_tiles.append((0, 0))
         occupied_tiles.append((0, 1))
         occupied_tiles.append((0, 2))
=======
         n = 3  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino S in its initial orientation
         occupied_tiles.append((1, 0))
         occupied_tiles.append((2, 0))
         occupied_tiles.append((0, 1))
         occupied_tiles.append((1, 1))
      elif type == 'L':
>>>>>>> parent of a5decee (Revert "Update tetromino.py")
         n = 3  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino S in its initial orientation
         occupied_tiles.append((1, 0))
         occupied_tiles.append((1, 1))
         occupied_tiles.append((1, 2))
<<<<<<< HEAD

         occupied_tiles.append((2, 2))
      elif type == 'J':
         n = 3
=======
         occupied_tiles.append((2, 2))
      elif type == 'J':
>>>>>>> parent of a5decee (Revert "Update tetromino.py")
         n = 3  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino S in its initial orientation
         occupied_tiles.append((1, 0))
         occupied_tiles.append((1, 1))
         occupied_tiles.append((0, 2))
<<<<<<< HEAD

         occupied_tiles.append((1, 2))
      elif type == 'T':
         n = 3  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino T in its initial orientation
=======
         occupied_tiles.append((1, 2))
      elif type == 'T':
         n = 3  # n = number of rows = number of columns in the tile matrix
>>>>>>> parent of a5decee (Revert "Update tetromino.py")
         # shape of the tetromino S in its initial orientation
         occupied_tiles.append((0, 1))
         occupied_tiles.append((1, 1))
         occupied_tiles.append((2, 1))
         occupied_tiles.append((1, 2))

<<<<<<< HEAD
         # create a matrix of numbered tiles based on the shape of the tetromino
=======
>>>>>>> parent of a5decee (Revert "Update tetromino.py")

      # create a matrix of numbered tiles based on the shape of the tetromino
      self.tile_matrix = np.full((n, n), None)
      # initial position of the bottom-left tile in the tile matrix just before 
      # the tetromino enters the game grid
@@ -86,7 +86,8 @@ def __init__(self, type, grid_height, grid_width):
         position.y = self.bottom_left_corner.y + (n - 1) - row_index
         # create the tile on the computed position 
         self.tile_matrix[row_index][col_index] = Tile(position)


<<<<<<< HEAD

=======
>>>>>>> parent of a5decee (Revert "Update tetromino.py")
   # Method for drawing the tetromino on the game grid
   def draw(self):
      n = len(self.tile_matrix)  # n = number of rows = number of columns
@@ -102,6 +103,7 @@ def draw(self):

   # Method for moving the tetromino in a given direction by 1 on the game grid
   def move(self, direction, game_grid):

      # check if the tetromino can be moved in the given direction by using the
      # can_be_moved method defined below
      if not(self.can_be_moved(direction, game_grid)):
@@ -124,48 +126,91 @@ def move(self, direction, game_grid):
                  self.tile_matrix[row][col].move(1, 0)
               else: # direction == "down"
                  self.tile_matrix[row][col].move(0, -1)


<<<<<<< HEAD
   # "rotate method" rotates by +90 (left)
   def rotate(self):
=======
>>>>>>> parent of a5decee (Revert "Update tetromino.py")
      return True  # successful move in the given direction

# "rotate method" rotates by -90 (right)
   def rotate_right(self, game_grid):
      n = len(self.tile_matrix)
      # tiles' initial coordinates
      first_pos_x = self.bottom_left_corner.x
      first_pos_y = self.bottom_left_corner.y

<<<<<<< HEAD
      # first transpose the matrix,
      # then reverse rows to arrange the tile matrix as rotated by +90
=======
>>>>>>> parent of a5decee (Revert "Update tetromino.py")
      # a boolean variable to check if the new position after rotation was occupied before
      # it also checks whether the tiles exceed the game grid
      is_occupied = False

      # update the tiles' positions
      for i in range(n):
         for j in range(n):
            if self.tile_matrix[j][i] is not None:
               pos = self.tile_matrix[j][i].get_position()

               # subtract first positions
               pos.x -= first_pos_x
               pos.y -= first_pos_y

               temp = pos.y
               pos.y = (n - 1 - pos.x) + first_pos_y
               pos.x = temp + first_pos_x

               # Do tiles exceed the grid?
               # Was the tile occupied before?
               if pos.x < 0 or pos.y < 0 or pos.x > self.grid_width - 1 or game_grid.is_occupied(pos.y, pos.x):
                  is_occupied = True

<<<<<<< HEAD
      # this tranposes the matrix
               self.tile_matrix[j][i].set_position(pos)

      # these are the operations to rotate the tile matrix array as needed
      reversed_tile_matrix = np.flipud(self.tile_matrix)
      transposed = np.transpose(reversed_tile_matrix)
      self.tile_matrix = transposed

=======
               self.tile_matrix[j][i].set_position(pos)

      # these are the operations to rotate the tile matrix array as needed
      reversed_tile_matrix = np.flipud(self.tile_matrix)
      transposed = np.transpose(reversed_tile_matrix)
      self.tile_matrix = transposed

>>>>>>> parent of a5decee (Revert "Update tetromino.py")
      if is_occupied:
         return False

      return True  # successful move in the given direction

   def rotate_left(self, game_grid):
      n = len(self.tile_matrix)
      first_pos_x = self.bottom_left_corner.x
      first_pos_y = self.bottom_left_corner.y
      # a boolean variable to check if the new position after rotation was occupied before
      # it also checks whether the tiles exceed the game grid
      is_occupied = False

      # update the tiles' positions
      for i in range(n):
         for j in range(n):
<<<<<<< HEAD
            if self.tile_matrix[i][j] is not None:
               pos = self.tile_matrix[i][j].get_position()
               #print(pos.x, pos.y)
=======
>>>>>>> parent of a5decee (Revert "Update tetromino.py")
            if self.tile_matrix[j][i] is not None:
               pos = self.tile_matrix[j][i].get_position()

               # subtract first positions
               pos.x -= first_pos_x
               pos.y -= first_pos_y

               temp = pos.x
               pos.x = (n - 1 - pos.y) + first_pos_x
               pos.y = temp + first_pos_y

<<<<<<< HEAD
               self.tile_matrix[i][j].set_position(pos)
=======
>>>>>>> parent of a5decee (Revert "Update tetromino.py")
               # Do tiles exceed the grid?
               # Was the tile occupied before?
               if pos.x < 0 or pos.y < 0 or pos.x > self.grid_width - 1 or game_grid.is_occupied(pos.y, pos.x):
                  is_occupied = True

<<<<<<< HEAD

               self.tile_matrix[j][i].set_position(pos)

=======

               self.tile_matrix[j][i].set_position(pos)

>>>>>>> parent of a5decee (Revert "Update tetromino.py")
      # these are the operations to rotate the tile matrix array as needed
      transposed = np.transpose(self.tile_matrix)
      reversed_tile_matrix = np.flipud(transposed)
      self.tile_matrix = reversed_tile_matrix

<<<<<<< HEAD
      return True  # successful move in the given direction
=======
>>>>>>> parent of a5decee (Revert "Update tetromino.py")
      if is_occupied:
         return False

      return True  # successful move in the given direction

   # Method to check if the tetromino can be moved in the given direction or not
   def can_be_moved(self, dir, game_grid):