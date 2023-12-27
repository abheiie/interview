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
        self.__game_level = game_level
        self.__playing_strategy = playing_strategy

    def make_move(self, board: Board) -> BoardCell:
        return self.__playing_strategy.make_move(board)
