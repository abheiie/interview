import random
from typing import Set

from exceptions.invalid_move_exception import InvalidMoveException
from exceptions.invalid_players_exception import InvalidPlayerException
from models.board import Board
from models.board_cell import BoardCell
from models.game_status import GameStatus
from models.game_symbol import GameSymbol
from models.player import Player
from strategies.column_winning_strategy import ColumnWinningStrategy
from strategies.diagonal_winning_strategy import DiagonalWinningStrategy
from strategies.row_winning_strategy import RowWinningStrategy


class Game:
    PLAYER_COUNT = 2
    DEFAULT_GAME_STATUS = GameStatus.IN_PROGRESS

    def __init__(self, board: Board = None, players: [Player] = []) -> None:
        self.board = board
        self.players = players
        self.status = Game.DEFAULT_GAME_STATUS
        self.next_player_index = 0
        self.winning_strategies = [
            RowWinningStrategy(),
            ColumnWinningStrategy(),
            DiagonalWinningStrategy(),
        ]
        self.winner: Player = None

    def get_next_move(self) -> BoardCell:
        # validate the move
        player: Player = self.players[self.next_player_index]
        move: BoardCell = player.make_move(self.board)
        self.validate_move(move)
        return move

    def start_game(self):
        self.status = GameStatus.IN_PROGRESS
        self.next_player_index = random.randint(0, Game.PLAYER_COUNT - 1)

    def get_next_player(self):
        return self.players[self.next_player_index]

    def validate_move(self, move: BoardCell):
        if not self.board.is_empty(move.row, move.column):
            raise InvalidMoveException("Cell is already filled")

    def make_move(self):
        # get the next move
        move: BoardCell = self.get_next_move()

        # update the board
        self.board.update(move)

        # check winner
        if self.check_winner(move.symbol):
            self.status = GameStatus.FINISHED
            self.winner = self.get_next_player()  # actually the current (:
            return

        # check draw
        if self.check_draw():
            self.status = GameStatus.DRAWN
            return

        # update the next player
        self.next_player_index = (self.next_player_index + 1) % Game.PLAYER_COUNT

    def check_winner(self, current_symbol: GameSymbol):
        for winning_strategy in self.winning_strategies:
            if winning_strategy.check_winner(self.board, current_symbol):
                return True
        return False

    def check_column_winner(self, current_symbol: GameSymbol):
        for col in range(len(self.board.board_cells[0])):
            if all(row[col].symbol == current_symbol for row in self.board.board_cells):
                return True
        return False

    def check_draw(self):
        for row in self.board.board_cells:
            for cell in row:
                if cell.symbol is None:
                    # If any cell is empty, the game is not a draw
                    return False
        # If no empty cells are found, and there is no winner, it's a draw
        return True

    @staticmethod
    def builder():
        return Game.Builder()

    class Builder:
        def __init__(self) -> None:
            self.game = Game()

        def with_size(self, size: int):
            self.game.board = Board(size)
            return self

        def with_player(self, player: Player):
            self.game.players.append(player)
            return self

        def build(self):
            is_valid: bool = self.validate()
            if not is_valid:
                raise InvalidPlayerException("Invalid players")
            new_game = Game()
            new_game.board = self.game.board
            new_game.players = self.game.players
            new_game.status = self.game.status
            return new_game

        def validate(self):
            players = self.game.players

            # check no of players
            if len(players) != Game.PLAYER_COUNT:
                return False

            # check if symbols are not unique
            game_symbol: Set[GameSymbol] = {player.game_symbol for player in players}
            if len(game_symbol) != Game.PLAYER_COUNT:
                return False

            return True
