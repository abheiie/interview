from abc import ABC, abstractmethod

from models.board import Board
from models.board_cell import BoardCell


class PlayingStrategy(ABC):
    @abstractmethod
    def make_move(self, board: Board) -> BoardCell:
        pass
