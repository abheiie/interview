import random

from models.board import Board
from models.board_cell import BoardCell
from strategies.playing_strategy import PlayingStrategy


class RandomPlayingStrategy(PlayingStrategy):
    def make_move(self, board: Board) -> BoardCell:
        # get list of empty indices
        empty_indices = board.get_empty_indices()

        # randomly select an empty index
        random_index = random.choice(empty_indices)

        # random board cell
        ramdom_board_cell = BoardCell(row=random_index[0], column=random_index[1])
        return ramdom_board_cell
