from __builtin__ import type
from random import randint

class CellArray:
    def __init__(self, row_size):
        # Main array of cell, true = white, false=black
        self.__cell_array = []
        self.__row_size = row_size
        try:
            self.__InitArray(row_size)
        except Exception as v:
            raise v

    # Fill line with True and add it to main array
    def StartNextIteration(self):
        self.__cell_array.append(self.__InitLine())

    # Get size of line
    def GetRowSize(self):
        return self.__row_size

    # Return the ID of current iteration
    def GetCurrentIterID(self):
        return len(self.__cell_array)

    # Fill a line with True and return it
    def __InitLine(self):
        y_array = []
        for x in range(0, self.GetRowSize()):
            y_array.append(True)
        return y_array

    # Check if input is good and init the first line with a black pixel
    def __InitArray(self, row_size):
        if type(row_size) is not int:
            raise TypeError(str(row_size) + 'is not a integer')
        # Init whole tab to white
        y_array = self.__InitLine()
        self.__cell_array.append(y_array)
        self.__cell_array[0][randint(0, row_size - 1)] = False

    # Return the boolean for the iterd_id at the postion y
    def GetCell(self, iterd_id, y):
        try:
            current_cell = self.__cell_array[iterd_id][y]
        except Exception as e:
            raise e
        return current_cell

    # Set the boolean for the iterd_id at the postion y
    def SetCell(self, x, y, state):
        if type(state) != bool:
            raise TypeError('Je veux un boolean putain !')
        try:
            self.__cell_array[x][y] = state
        except Exception as e:
            raise e

    # Iterate over the line of the current iteration
    def __iter__(self):
        self.__x = self.GetCurrentIterID()-1
        self.__y = 0
        return self

    def next(self):
        row_size = self.GetRowSize() - 1

        cell = self.GetCell(self.__x, self.__y)
        if self.__y == row_size:
            raise StopIteration
            return cell
        else:
            self.__y += 1
        return cell
