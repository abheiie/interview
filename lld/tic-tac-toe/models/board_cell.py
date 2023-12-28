from models.game_symbol import GameSymbol


class BoardCell:
    def __init__(self, row = None, column = None, symbol = None) -> None:
        self.row = row
        self.column = column
        self.symbol = symbol

