class GridSquare:
    ###################################################
    # Initialization
    ###################################################
    def __init__(self, square, row, col, value=0):
        self._square = square
        self._row = row
        self._col = col
        self._value = value

    ###################################################
    # Getters & Setters
    ###################################################
    def get_square(self):
        return self._square

    def set_square(self, square):
        self._square = square

    def get_row(self):
        return self._row

    def set_row(self, row):
        self._row = row

    def get_col(self):
        return self._col

    def set_col(self, col):
        self._col = col

    def get_value(self):
        return self._value

    def set_value(self, value):
        self._value = value

    ###################################################
    # Overrides
    ###################################################
    def __str__(self):
        return f"This is a grid square | " \
               f"Square Location: {self._square} | " \
               f"Row: {self._row} | " \
               f"Column: {self._col} | " \
               f"Value: {self._value}"
