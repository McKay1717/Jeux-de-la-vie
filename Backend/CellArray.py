from __builtin__ import type
from math import sqrt


class CellArray:
    def __init__(self, number_of_cell):
        # Main array of cell, true = white, false=black
        self.__cell_array = []
        self.__len_of_cell_array = 0
        self.__row_size = 0
        try:
            self.__InitArray(number_of_cell)
        except Exception as v:
            raise v

    def GetRowSize(self):
        return self.__row_size

    def __ComputeRowSize(self, number_of_cell):
        if type(number_of_cell) is not int:
            raise TypeError(str(number_of_cell) + 'is not a integer')

        row_size = sqrt(number_of_cell)
        # Test if int cast is safe
        if row_size % 1 != 0:
            raise ValueError('Can\'t make a square with this number of cell :' + str(number_of_cell))

        row_size = int(row_size)
        self.__row_size = row_size
        return row_size

    def __InitArray(self, number_of_cell):
        try:
            row_size = self.__ComputeRowSize(number_of_cell)
        except ValueError as v:
            raise v
        # Init whole tab to white
        for x in range(0, row_size):
            y_array = []
            for y in range(0, row_size):
                y_array.append(True)
            self.__cell_array.append(y_array)
            self.__len_of_cell_array = number_of_cell

    def GetCell(self, x, y):
        try:
            current_cell = self.__cell_array[x][y]
        except Exception as e:
            raise e
        return current_cell

    def SetCell(self, x, y, state):
        if type(state) != bool:
            raise TypeError('Je veux un boolean putain !')
        try:
            self.__cell_array[x][y] = state
        except Exception as e:
            raise e

    def __iter__(self):
        self.__x = 0
        self.__y = 0
        return self

    def next(self):
        row_size = self.GetRowSize() - 1

        cell = self.GetCell(self.__x, self.__y)
        if self.__x == row_size and self.__y == row_size:
            raise StopIteration
            return cell

        if self.__x >= row_size:
            self.__y += 1
            self.__x = 0
        else:
            self.__x += 1

        return cell
