from models.board import Board
from models.game_symbol import GameSymbol
from strategies.winning_strategy import WinningStrategy


class RowWinningStrategy(WinningStrategy):
    def check_winner(self, board: Board, current_symbol: GameSymbol) -> bool:
        for row in board.board_cells:
            if all(cell.symbol == current_symbol for cell in row):
                return True
        return False

