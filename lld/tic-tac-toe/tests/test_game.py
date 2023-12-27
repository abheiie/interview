import unittest

from models.board import Board
from models.bot_player import BotPlayer
from models.game import Game
from models.game_level import GameLevel
from models.game_symbol import GameSymbol
from models.human_player import HumanPlayer
from models.user import User
from strategies.random_playing_strategy import RandomPlayingStrategy


class TestGame(unittest.TestCase):
    BOARD_SIZE = 3

    def test_create_game(self):
        game = (
            Game.builder()
            .with_size(TestGame.BOARD_SIZE)
            .with_player(HumanPlayer(GameSymbol.X, User()))
            .with_player(
                BotPlayer(GameSymbol.O, GameLevel.EASY, RandomPlayingStrategy())
            )
            .build()
        )
        self.assertEqual(2, len(game.players), "The game should have 2 players")

    def test_create_board(self):
        self.board: Board = Board(TestGame.BOARD_SIZE)

        # Check board size
        row_size = len(self.board.board_cells)
        self.assertEqual(3, row_size, "The board size should be 3x3")

        column_size = len(self.board.board_cells[0])
        self.assertEqual(3, column_size, "The board size should be 3x3")
