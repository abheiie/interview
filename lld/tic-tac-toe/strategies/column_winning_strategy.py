from models.board import Board
from models.game_symbol import GameSymbol
from strategies.winning_strategy import WinningStrategy


class ColumnWinningStrategy(WinningStrategy):
    def check_winner(self, board: Board, current_symbol: GameSymbol) -> bool:
        for col in range(len(board.board_cells[0])):
            if all(row[col].symbol == current_symbol for row in board.board_cells):
                return True
        return False
        