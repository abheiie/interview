from typing import Set

from exceptions.invalid_players_exception import InvalidPlayerException
from models.board import Board
from models.game_status import GameStatus
from models.game_symbol import GameSymbol
from models.player import Player


class Game:
    PLAYER_COUNT = 2
    DEFAULT_GAME_STATUS = GameStatus.IN_PROGRESS

    def __init__(self) -> None:
        self.__board = None
        self.__players = []
        self.__status = Game.DEFAULT_GAME_STATUS

    @property
    def players(self):
        return self.__players

    @players.setter
    def players(self, players):
        self.__players = players

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, board):
        self.__board = board

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    def start_game(self):
        pass

    def make_move(self):
        pass

    def __check_winner(self):
        pass

    def __check_draw(self):
        pass

    @staticmethod
    def builder():
        return Game.Builder()

    class Builder:
        def __init__(self) -> None:
            self.__game = Game()

        def with_size(self, size: int):
            self.__game.board = Board(size)
            return self

        def with_player(self, player: Player):
            self.__game.players.append(player)
            return self

        def build(self):
            is_valid: bool = self.validate()
            if not is_valid:
                raise InvalidPlayerException("Invalid players")
            new_game = Game()
            new_game.board = self.__game.board
            new_game.players = self.__game.players
            new_game.status = self.__game.status
            return new_game

        def validate(self):
            players = self.__game.players

            # check no of players
            if len(players) != Game.PLAYER_COUNT:
                return False

            # check if symbols are not unique
            game_symbol: Set[GameSymbol] = {player.game_symbol for player in players}
            if len(game_symbol) != Game.PLAYER_COUNT:
                return False

            return True
