from abc import ABC, abstractmethod

from models.board import Board
from models.board_cell import BoardCell
from models.game_symbol import GameSymbol


class Player(ABC):
    def __init__(self, game_symbol: GameSymbol) -> None:
        self.game_symbol = game_symbol

        @abstractmethod
        def make_move(self, board: Board) -> BoardCell:
            pass
