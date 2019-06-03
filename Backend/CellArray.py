from __builtin__ import type
from math import sqrt


class CellArray:
    def __init__(self):
        # Main array of cell, true = white, false=black
        self.__cell_array = []
        self.__len_of_cell_array = 0

    def InitArray(self, number_of_cell):
        if type(number_of_cell) is not int:
            raise Exception(str(number_of_cell) + 'is not a integer')

        row_size = sqrt(number_of_cell)
        # Test if int cast is safe
        if row_size % 1 != 0:
            raise Exception('Can\'t make a square with this number of cell :' + str(number_of_cell))

        row_size = int(row_size)
        #Init whole tab to white
        for x in range(0, row_size):
            y_array = []
            for y in range(0, row_size):
                y_array.append(True)
            self.__cell_array.append(y_array)
        self.__len_of_cell_array = number_of_cell