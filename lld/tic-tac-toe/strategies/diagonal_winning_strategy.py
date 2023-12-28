from models.board import Board
from models.game_symbol import GameSymbol
from strategies.winning_strategy import WinningStrategy


class DiagonalWinningStrategy(WinningStrategy):
    def check_winner(self, board: Board, current_symbol: GameSymbol) -> bool:
        if all(
            board.board_cells[i][i].symbol == current_symbol
            for i in range(len(board.board_cells))
        ):
            return True

        # Check reverse diagonal
        if all(
            board.board_cells[i][len(board.board_cells) - 1 - i].symbol
            == current_symbol
            for i in range(len(board.board_cells))
        ):
            return True

        return False
