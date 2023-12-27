from typing import List

from models.board_cell import BoardCell


class Board:
    def __init__(
        self,
        size: int,
    ):
        self.__size = size
        self.__board_cells = self.initialize_board_cells(self.__size)

    @property
    def board_cells(self):
        return self.__board_cells

    def initialize_board_cells(self, size: int) -> List[List[BoardCell]]:
        return [[BoardCell() for column in range(size)]] * size
