from models.board import Board
from models.board_cell import BoardCell
from models.game_level import GameLevel
from models.game_symbol import GameSymbol
from models.player import Player
from strategies.playing_strategy import PlayingStrategy


class BotPlayer(Player):
    def __init__(
        self,
        game_symbol: GameSymbol,
        game_level: GameLevel,
        playing_strategy: PlayingStrategy,
    ) -> None:
        super().__init__(game_symbol)
        self.game_level = game_level
        self.playing_strategy = playing_strategy

    def make_move(self, board: Board) -> BoardCell:
        move = self.playing_strategy.make_move(board)
        move.symbol = self.game_symbol
        return move