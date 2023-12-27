from models.game_symbol import GameSymbol


class BoardCell:
    def __init__(self) -> None:
        self.__row = None
        self.__column = None
        self.__symbol = None
