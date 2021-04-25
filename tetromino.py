import random # each tetromino is created with a random x value above the grid
from tile import Tile # used for representing each tile on the tetromino
from point import Point # used for tile positions
import numpy as np # fundamental Python module for scientific computing
import pygame
import math

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
         n = 4  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino I in its initial orientation
         occupied_tiles.append((1, 0)) # (column_index, row_index)
         occupied_tiles.append((1, 1))
         occupied_tiles.append((1, 2))
         occupied_tiles.append((1, 3))
      elif type == 'O':
         n = 2  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino O in its initial orientation
         occupied_tiles.append((0, 0))
         occupied_tiles.append((1, 0))
         occupied_tiles.append((0, 1))
         occupied_tiles.append((1, 1))
      elif type == 'Z':
         n = 3  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino Z in its initial orientation
         occupied_tiles.append((0, 0))
         occupied_tiles.append((1, 0))
         occupied_tiles.append((1, 1))
         occupied_tiles.append((2, 1))
      elif type == 'S':
         n = 3  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino S in its initial orientation
         occupied_tiles.append((1, 0))
         occupied_tiles.append((2, 0))
         occupied_tiles.append((0, 1))
         occupied_tiles.append((1, 1))
      elif type == 'L':
         n = 3  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino S in its initial orientation
         occupied_tiles.append((1, 0))
         occupied_tiles.append((1, 1))
         occupied_tiles.append((1, 2))
         occupied_tiles.append((2, 2))
      elif type == 'J':
         n = 3  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino S in its initial orientation
         occupied_tiles.append((1, 0))
         occupied_tiles.append((1, 1))
         occupied_tiles.append((0, 2))
         occupied_tiles.append((1, 2))
      elif type == 'T':
         n = 3  # n = number of rows = number of columns in the tile matrix
         # shape of the tetromino S in its initial orientation
         occupied_tiles.append((0, 1))
         occupied_tiles.append((1, 1))
         occupied_tiles.append((2, 1))
         occupied_tiles.append((1, 2))


      # create a matrix of numbered tiles based on the shape of the tetromino
      self.tile_matrix = np.full((n, n), None)
      # initial position of the bottom-left tile in the tile matrix just before 
      # the tetromino enters the game grid
      self.bottom_left_corner = Point()
      # upper side of the game grid
      self.bottom_left_corner.y = grid_height
      # a random horizontal position 
      self.bottom_left_corner.x = random.randint(0, grid_width - n)
      # create each tile by computing its position w.r.t. the game grid based on 
      # its bottom_left_corner
      for i in range(len(occupied_tiles)):
         col_index, row_index = occupied_tiles[i][0], occupied_tiles[i][1]
         position = Point()
         # horizontal position of the tile
         position.x = self.bottom_left_corner.x + col_index
         # vertical position of the tile
         position.y = self.bottom_left_corner.y + (n - 1) - row_index
         # create the tile on the computed position 
         self.tile_matrix[row_index][col_index] = Tile(position)


   # Method for drawing the tetromino on the game grid
   def draw(self):
      n = len(self.tile_matrix)  # n = number of rows = number of columns
      for row in range(n):
         for col in range(n):
            # draw each occupied tile (not equal to None) on the game grid
            if self.tile_matrix[row][col] != None:
               # considering newly entered tetrominoes to the game grid that may 
               # have tiles with position.y >= grid_height
               position = self.tile_matrix[row][col].get_position()
               if position.y < self.grid_height:
                  self.tile_matrix[row][col].draw() 

   # Method for moving the tetromino in a given direction by 1 on the game grid
   def move(self, direction, game_grid):

      # check if the tetromino can be moved in the given direction by using the
      # can_be_moved method defined below
      if not(self.can_be_moved(direction, game_grid)):
         return False  # tetromino cannot be moved in the given direction
      # move the tetromino by first updating the position of the bottom left tile 
      if direction == "left":
         self.bottom_left_corner.x -= 1
      elif direction == "right":
         self.bottom_left_corner.x += 1
      else:  # direction == "down"
         self.bottom_left_corner.y -= 1
      # then moving each occupied tile in the given direction by 1
      n = len(self.tile_matrix)  # n = number of rows = number of columns
      for row in range(n):
         for col in range(n):
            if self.tile_matrix[row][col] != None:
               if direction == "left":
                  self.tile_matrix[row][col].move(-1, 0)
               elif direction == "right":
                  self.tile_matrix[row][col].move(1, 0)
               else: # direction == "down"
                  self.tile_matrix[row][col].move(0, -1)


      return True  # successful move in the given direction

   # "rotate method" rotates by -90 (right)
   def rotate_right(self, game_grid):
      n = len(self.tile_matrix)
      # tiles' initial coordinates
      first_pos_x = self.bottom_left_corner.x
      first_pos_y = self.bottom_left_corner.y

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

               self.tile_matrix[j][i].set_position(pos)

      # these are the operations to rotate the tile matrix array as needed
      reversed_tile_matrix = np.flipud(self.tile_matrix)
      transposed = np.transpose(reversed_tile_matrix)
      self.tile_matrix = transposed

      if is_occupied:
         return False

      return True  # successful move in the given direction

   # "rotate method" rotates by +90 (left)
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
            if self.tile_matrix[j][i] is not None:
               pos = self.tile_matrix[j][i].get_position()

               # subtract first positions
               pos.x -= first_pos_x
               pos.y -= first_pos_y

               temp = pos.x
               pos.x = (n - 1 - pos.y) + first_pos_x
               pos.y = temp + first_pos_y

               # Do tiles exceed the grid?
               # Was the tile occupied before?
               if pos.x < 0 or pos.y < 0 or pos.x > self.grid_width - 1 or game_grid.is_occupied(pos.y, pos.x):
                  is_occupied = True


               self.tile_matrix[j][i].set_position(pos)

      # these are the operations to rotate the tile matrix array as needed
      transposed = np.transpose(self.tile_matrix)
      reversed_tile_matrix = np.flipud(transposed)
      self.tile_matrix = reversed_tile_matrix

      if is_occupied:
         return False

      return True  # successful move in the given direction

   # Method to check if the tetromino can be moved in the given direction or not
   def can_be_moved(self, dir, game_grid):
      n = len(self.tile_matrix)  # n = number of rows = number of columns
      if dir == "left" or dir == "right":
         for row in range(n):
            for col in range(n): 
               # direction = left --> check the leftmost tile of each row
               if dir == "left" and self.tile_matrix[row][col] != None:
                  leftmost = self.tile_matrix[row][col].get_position()
                  # tetromino cannot go left if any leftmost tile is at x = 0
                  if leftmost.x == 0:
                     return False
                  # skip each row whose leftmost tile is out of the game grid 
                  # (possible for newly entered tetrominoes to the game grid)
                  if leftmost.y >= self.grid_height:
                     break
                  # tetromino cannot go left if the grid cell on the left of any 
                  # of its leftmost tiles is occupied
                  if game_grid.is_occupied(leftmost.y, leftmost.x - 1):
                     return False
                  break  # end the inner for loop
               # direction = right --> check the rightmost tile of each row
               elif dir == "right" and self.tile_matrix[row][n - 1 - col] != None:
                  rightmost = self.tile_matrix[row][n - 1 - col].get_position()
                  # tetromino cannot go right if any of its rightmost tiles is 
                  # at x = grid_width - 1
                  if rightmost.x == self.grid_width - 1:
                     return False
                  # skip each row whose rightmost tile is out of the game grid 
                  # (possible for newly entered tetrominoes to the game grid)
                  if rightmost.y >= self.grid_height:
                     break
                  # tetromino cannot go right if the grid cell on the right of 
                  # any of its rightmost tiles is occupied
                  if game_grid.is_occupied(rightmost.y, rightmost.x + 1):
                     return False
                  break  # end the inner for loop
      # direction = down --> check the bottommost tile of each column
      else:
         for col in range(n):
            for row in range(n - 1, -1, -1):
               if self.tile_matrix[row][col] != None:
                  bottommost = self.tile_matrix[row][col].get_position()
                  # skip each column whose bottommost tile is out of the grid 
                  # (possible for newly entered tetrominoes to the game grid)
                  if bottommost.y > self.grid_height:
                     break
                  # tetromino cannot go down if any bottommost tile is at y = 0
                  if bottommost.y == 0:
                     return False 
                  # or the grid cell below any bottommost tile is occupied
                  if game_grid.is_occupied(bottommost.y - 1, bottommost.x):
                     return False
                  break  # end the inner for loop
      return True  # tetromino can be moved in the given direction

   #drops tetrmino by num tiles on y axis.
   def drop_tetromino(self,num):
      self.bottom_left_corner.y -= num
      for i in range(len(self.tile_matrix)):
         for j in range(len(self.tile_matrix)):
            if self.tile_matrix[i][j] is not None:
               self.tile_matrix[i][j].move(0, -num)
               

   def move_mouse(self, grid):
     mouse_position = pygame.mouse.get_pos()


     mouse_x_coordinate = mouse_position[0]
     mouse_x_position_on_grid = mouse_x_coordinate / 40
     print(mouse_x_position_on_grid)

     if mouse_x_position_on_grid <= grid.current_tetromino.bottom_left_corner.x:
         a = 0
         while mouse_x_position_on_grid < grid.current_tetromino.bottom_left_corner.x or mouse_x_position_on_grid == 0:
             if not grid.current_tetromino.move("left", grid):
                 break
             if mouse_x_position_on_grid <= 0:
                 mouse_x_position_on_grid = 0
                 a += 1
                 if a == 2:
                     break


     elif mouse_x_position_on_grid >= grid.current_tetromino.bottom_left_corner.x:
         b = 0
         while mouse_x_position_on_grid > grid.current_tetromino.bottom_left_corner.x + len(
                 grid.current_tetromino.tile_matrix):

             if not grid.current_tetromino.move("right", grid):
                 break
             if mouse_x_position_on_grid >= 11:
                 mouse_x_position_on_grid = 11
                 b += 1
                 if b == 2:
                     break











