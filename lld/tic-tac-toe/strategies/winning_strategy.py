from abc import ABC, abstractmethod
from models.board import Board
from models.game_symbol import GameSymbol

class WinningStrategy(ABC):
    @abstractmethod
    def check_winner(self, board: Board, current_symbol: GameSymbol) -> bool:
        pass