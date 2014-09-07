"""
Clone of 2048 game.
"""

import poc_2048_gui        

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # replace with your code
    
    merge_line = line[:]
    line_flag = []
    line_len = len(merge_line)
    for i in range(0, line_len):
        line_flag += [False]
    for i in range(1, line_len):
        if merge_line != 0:
            k = i
            for j in range(i-1, -1, -1):
                if merge_line[j] == 0:
                    k = j
                else:
                    break
            merge_line[k], merge_line[i] = merge_line[i], merge_line[k]
            #print merge_line
            if k > 0 and merge_line[k] == merge_line[k-1] and line_flag[k-1] == False:
                merge_line[k-1], merge_line[k] = 2*merge_line[k-1], 0 
                line_flag[k-1] = True
            #print merge_line
            #print
    return merge_line

#print merge([2, 0, 2, 4])
#print merge([0, 0, 2, 2])
#print merge([2, 2, 0, 0])
#print merge([2, 2, 2, 2])
#print merge([8, 16, 16, 8])

import random
class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self.matrix = []
        for i in range(0, grid_height):
            row = []
            for j in range(0, grid_width):
                row += [0]
            self.matrix += [row]
        
    
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        # replace with your code
        self.__init__(self.get_grid_height(),self.get_grid_width())
    
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        print self.matrix

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return len(self.matrix)
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return len(self.matrix[0])
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        width = self.get_grid_width()
        height = self.get_grid_height()
        
        if direction == UP:
            for offset in range(width):
                line = []
                for i in range(height):
                    line += [self.matrix[i][offset]]
                merge_line = merge(line)
                for i in range(height):
                    self.matrix[i][offset] = merge_line[i]
        elif direction == DOWN:
            for offset in range(width):
                line = []
                for i in range(height-1, -1, -1):
                    line += [self.matrix[i][offset]]
                print line
                merge_line = merge(line)
                print merge_line
                print 
                for i in range(height):
                    self.matrix[height-i-1][offset] = merge_line[i]
        elif direction == LEFT:
            for offset in range(height):
                line = []
                for i in range(width):
                    line += [self.matrix[offset][i]]
                merge_line = merge(line)
                for i in range(width):
                    self.matrix[offset][i] = merge_line[i]                    
        elif direction == RIGHT:
            for offset in range(height):
                line = []
                for i in range(width-1, -1, -1):
                    line += [self.matrix[offset][i]]
                merge_line = merge(line)
                for i in range(width):
                    self.matrix[offset][width - i -1] = merge_line[i] 
        self.new_tile()
                    
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        #print self.matrix
        node = []
        for i in range(self.get_grid_height()):
            for j in range(self.get_grid_width()):
                if self.matrix[i][j] == 0:
                    node += [(i,j)]

        rand_node = random.choice(node)
        row = rand_node[0]
        col = rand_node[1]
        if self.matrix[row][col] == 0:
            if random.randrange(0, 10) == 9:
                self.matrix[row][col] = 4
            else:
                self.matrix[row][col] = 2
        #print self.matrix
        #print
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """        
        # replace with your code
        self.matrix[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        # replace with your code
        return self.matrix[row][col]
 
    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
