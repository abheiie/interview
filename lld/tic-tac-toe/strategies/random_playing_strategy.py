from models.board import Board
from models.board_cell import BoardCell
from strategies.playing_strategy import PlayingStrategy


class RandomPlayingStrategy(PlayingStrategy):
    def make_move(self, board: Board) -> BoardCell:
        pass
