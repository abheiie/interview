from models.board import Board
from models.board_cell import BoardCell
from models.game_symbol import GameSymbol
from models.player import Player
from models.user import User


class HumanPlayer(Player):
    def __init__(self, game_symbol: GameSymbol, user: User) -> None:
        super().__init__(game_symbol)
        self.user = user

    def make_move(self, board: Board) -> BoardCell:
        pass
