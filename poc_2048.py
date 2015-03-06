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
    # replace with your code from the previous mini-project
    line_len = len(line)
    merge_line = line[:]
    line_flag = [False] * line_len

    for ptr_i in range(1, line_len):
        if merge_line != 0:
            ptr_k = ptr_i
            for ptr_j in range(ptr_i - 1, -1, -1):
                if merge_line[ptr_j] == 0:
                    ptr_k = ptr_j
                else:
                    break
            merge_line[ptr_k], merge_line[ptr_i] = merge_line[ptr_i], merge_line[ptr_k]
            if ptr_k > 0 and merge_line[ptr_k] == merge_line[ptr_k - 1] and line_flag[ptr_k - 1] == False:
                merge_line[ptr_k - 1], merge_line[ptr_k] = 2 * merge_line[ptr_k - 1], 0 
                line_flag[ptr_k - 1] = True
    return merge_line

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        # replace with your code
        self._grid_height = grid_height
        self._grid_width = grid_width
        self._matrix = [[0] * grid_width for _ in range(grid_height)]

    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        # replace with your code
        for ptr_i in range(self._grid_height):
            for ptr_j in range(self._grid_width):
	        self._matrix[ptr_i][ptr_j] = 0
        self.new_tile()
        self.new_tile()

    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # replace with your code
        return reduce(lambda x, y: x + "\n" + y, [str(self._matrix[ptr_i]) for ptr_i in range(self._grid_height)])

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        return len(self._matrix)

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        # replace with your code
        return len(self._matrix[0])

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # replace with your code
        width = self._grid_width
        height = self._grid_height
        
        if direction == UP:
            for offset in range(width):
                merge_line = merge([self._matrix[ptr_i][offset] for ptr_i in range(height)])
                for ptr_i in range(height):
                    self.set_tile(ptr_i, offset, merge_line[ptr_i])
        elif direction == DOWN:
            for offset in range(width):
                merge_line = merge([self._matrix[ptr_i][offset] for ptr_i in range(height - 1, -1, -1)])
                for ptr_i in range(height):
                    self.set_tile(height - ptr_i - 1, offset, merge_line[ptr_i])
        elif direction == LEFT:
            for offset in range(height):
                merge_line = merge([self._matrix[offset][ptr_i] for ptr_i in range(width)])
                for ptr_i in range(width):
                    self.set_tile(offset, ptr_i, merge_line[ptr_i])
        elif direction == RIGHT:
            for offset in range(height):
                merge_line = merge([self._matrix[offset][ptr_i] for ptr_i in range(width - 1, -1, -1)])
                for ptr_i in range(width):
                    self.set_tile(offset, width - ptr_i -1, merge_line[ptr_i])
        self.new_tile()

    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        node = []
        for ptr_i in range(self._grid_height):
            for ptr_j in range(self._grid_width):
                if self._matrix[ptr_i][ptr_j] == 0:
                    node += [(ptr_i, ptr_j)]
        if len(node) == 0:
            return
        import random
        rand_node = random.choice(node)
        row = rand_node[0]
        col = rand_node[1]
        if self._matrix[row][col] == 0:
            if random.randrange(0, 10) == 9:
                self.set_tile(row, col, 4)
            else:
                self.set_tile(row, col, 2)

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        # replace with your code
        self._matrix[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        # replace with your code
        return self._matrix[row][col]

poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
