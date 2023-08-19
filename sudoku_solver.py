from grid import Grid


class SudokuSolver:
    ###################################################
    # Initialization
    ###################################################
    def __init__(self, num_of_rows=9, num_of_cols=9, square_size=3):
        self._grid = Grid(num_of_rows, num_of_cols, square_size)
        self._num_of_rows = num_of_rows
        self._num_of_cols = num_of_cols

    ###################################################
    # Getters & Setters
    ###################################################
    def get_grid(self):
        return self._grid

    ###################################################
    # Functions
    ###################################################
    def check_square(self, square_number):
        completed_numbers = []

        for row in range(1, self._num_of_rows + 1):
            for col in range(1, self._num_of_cols + 1):
                current_square = self._grid.get_grid()[row][col]

                if current_square.get_square() == square_number:
                    if current_square.get_value() != 0:
                        completed_numbers.append(current_square.get_value())

        return completed_numbers

    def check_row(self, row_number):
        completed_numbers = []

        for row in range(1, self._num_of_rows + 1):
            for col in range(1, self._num_of_cols + 1):
                current_square = self._grid.get_grid()[row][col]

                if current_square.get_row() == row_number:
                    if current_square.get_value() != 0:
                        completed_numbers.append(current_square.get_value())

        return completed_numbers

    def check_col(self, col_number):
        completed_numbers = []

        for row in range(1, self._num_of_rows + 1):
            for col in range(1, self._num_of_cols + 1):
                current_square = self._grid.get_grid()[row][col]

                if current_square.get_col() == col_number:
                    if current_square.get_value() != 0:
                        completed_numbers.append(current_square.get_value())

        return completed_numbers

    def find_possible_numbers(self, square_number, row_number, col_number):
        possible_numbers = list(range(1, self._num_of_rows + 1))

        square_completed_numbers = self.check_square(square_number)
        possible_numbers = [x for x in possible_numbers if x not in square_completed_numbers]

        row_completed_numbers = self.check_row(row_number)
        possible_numbers = [x for x in possible_numbers if x not in row_completed_numbers]

        col_completed_numbers = self.check_col(col_number)
        possible_numbers = [x for x in possible_numbers if x not in col_completed_numbers]

        return possible_numbers

    def solve(self):
        for loop_count in range(1, (self._num_of_rows * self._num_of_cols) + 1):
            all_solved = True
            for row in range(1, self._num_of_rows + 1):
                for col in range(1, self._num_of_cols + 1):
                    current_square = self._grid.get_grid()[row][col]

                    if current_square.get_value() == 0:
                        possible_numbers = self.find_possible_numbers(
                            current_square.get_square(),
                            current_square.get_row(),
                            current_square.get_col()
                        )

                        if len(possible_numbers) == 1:
                            current_square.set_value(possible_numbers[0])
                        else:
                            all_solved = False

            if all_solved:
                break


if __name__ == '__main__':
    solver = SudokuSolver()

    grid = solver.get_grid()

    # Row 1
    grid.update_square(1, 1, 3)
    grid.update_square(1, 3, 9)
    grid.update_square(1, 4, 4)
    grid.update_square(1, 6, 7)
    grid.update_square(1, 7, 5)
    grid.update_square(1, 9, 8)

    # Row 2
    grid.update_square(2, 1, 7)
    grid.update_square(2, 3, 6)
    grid.update_square(2, 6, 5)

    # Row 3
    grid.update_square(3, 1, 4)
    grid.update_square(3, 3, 2)
    grid.update_square(3, 4, 6)
    grid.update_square(3, 6, 3)
    grid.update_square(3, 7, 1)
    grid.update_square(3, 8, 9)

    # Row 4
    grid.update_square(4, 1, 9)
    grid.update_square(4, 2, 7)
    grid.update_square(4, 3, 4)
    grid.update_square(4, 4, 1)
    grid.update_square(4, 5, 3)

    # Row 5
    grid.update_square(5, 1, 2)
    grid.update_square(5, 7, 7)

    # Row 6
    grid.update_square(6, 1, 8)
    grid.update_square(6, 2, 3)
    grid.update_square(6, 4, 7)
    grid.update_square(6, 5, 6)
    grid.update_square(6, 8, 1)
    grid.update_square(6, 9, 9)

    # Row 7
    grid.update_square(7, 5, 7)
    grid.update_square(7, 8, 2)
    grid.update_square(7, 9, 6)

    # Row 8
    grid.update_square(8, 3, 7)
    grid.update_square(8, 8, 5)

    # Row 9
    grid.update_square(9, 1, 1)
    grid.update_square(9, 6, 6)
    grid.update_square(9, 7, 4)
    grid.update_square(9, 8, 7)
    grid.update_square(9, 9, 3)

    solver.solve()

    print(solver.get_grid())
