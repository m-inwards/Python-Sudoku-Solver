from grid_square import GridSquare
from math import ceil


class Grid:
    ###################################################
    # Initialization
    ###################################################
    def __init__(self, num_of_rows=9, num_of_cols=9, square_size=3):
        self._grid = {}
        self._num_of_rows = num_of_rows
        self._num_of_cols = num_of_cols

        if num_of_cols != num_of_rows or num_of_cols % square_size != 0:
            raise Exception("Invalid Row/Column/Square Size configuration")

        for row_num in range(1, num_of_rows+1):
            self._grid[row_num] = {}

            for col_num in range(1, num_of_cols+1):
                row_index = ceil(row_num/square_size) - 1
                col_index = ceil(col_num/square_size)

                self._grid[row_num][col_num] = GridSquare((row_index * 3) + col_index, row_num, col_num)

    ###################################################
    # Getters & Setters
    ###################################################
    def get_grid(self):
        return self._grid

    ###################################################
    # Overrides
    ###################################################
    def __str__(self):
        print_str = ""

        for row in range(1, self._num_of_rows+1):
            for col in range(1, self._num_of_cols + 1):
                print_str += str(self._grid[row][col].get_value()) + " | "

            print_str += "\n"

        return print_str

    ###################################################
    # Functions
    ###################################################
    def update_square(self, row, col, value):
        self._grid[row][col].set_value(value)
