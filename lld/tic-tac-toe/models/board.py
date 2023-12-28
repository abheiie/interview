from typing import List

from models.board_cell import BoardCell


class Board:
    def __init__(
        self,
        size: int,
    ):
        self.size = size
        self.board_cells = self.initialize_board_cells(self.size)

    def initialize_board_cells(self, size: int) -> List[List[BoardCell]]:
        board_cells = []
        for i in range(size):
            board_cells.append([])
            for j in range(size):
                board_cells[i].append(BoardCell(row=i, column=j))
        return board_cells

    def is_empty(self, row: int, column: int) -> bool:
        return self.board_cells[row][column].symbol is None

    def update(self, move: BoardCell):
        self.board_cells[move.row][move.column].symbol = move.symbol

    def print_board(self):
        for i in range(len(self.board_cells)):
            for j in range(len(self.board_cells[i])):
                symbol = self.board_cells[i][j].symbol
                print(f" {symbol.value} " if symbol else " - ", end="")
                if j < len(self.board_cells[i]) - 1:
                    print("|", end="")
            print()
            if i < len(self.board_cells) - 1:
                print("-----------")
        print()

    def get_empty_indices(self):
        empty_indices = []
        for i in range(len(self.board_cells)):
            for j in range(len(self.board_cells[i])):
                if self.is_empty(i, j):
                    empty_indices.append((i, j))
        return empty_indices
