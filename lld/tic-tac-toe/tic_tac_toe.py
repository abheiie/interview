from exceptions.invalid_symbol_exception import InvalidSymbolException
from models.bot_player import BotPlayer
from models.game import Game
from models.game_level import GameLevel
from models.game_status import GameStatus
from models.game_symbol import GameSymbol
from models.human_player import HumanPlayer
from models.user import User
from strategies.random_playing_strategy import RandomPlayingStrategy
import time


class TicTacToe:
    BOARD_SIZE = 3

    def __init__(self) -> None:
        pass

    def main(self) -> None:
        print("Welcome to Tic Tac Toe!")
        human_player = self.get_user_input()
        game = self.create_game(human_player)
        game.start_game()

        while game.status == GameStatus.IN_PROGRESS:
            next_player = game.get_next_player()
            if next_player.game_symbol == human_player.game_symbol:
                print("Your turn ", next_player.game_symbol.value," -" "\n")
            else:
                print("Bot is thinking...", next_player.game_symbol.value, " -", "\n")
                time.sleep(1)
                
            game.make_move()
            game.board.print_board()
            
        if game.status == GameStatus.DRAWN:
            print("=== Draw ===")
            
        if game.status == GameStatus.FINISHED:
            print(f" === Game won by player: {game.winner.game_symbol.value} ===")
            

    def create_game(self, human_player: HumanPlayer) -> Game:
        game = (
            Game.builder()
            .with_size(TicTacToe.BOARD_SIZE)
            .with_player(human_player)
            .with_player(
                BotPlayer(
                    self.decide_bot_symbol(human_player.game_symbol),
                    GameLevel.EASY,
                    RandomPlayingStrategy(),
                )
            )
            .build()
        )
        return game

    def decide_bot_symbol(self, human_symbol: GameSymbol) -> GameSymbol:
        if human_symbol == GameSymbol.X:
            return GameSymbol.O
        else:
            return GameSymbol.X

    def get_user_input(self) -> HumanPlayer:
        name = input("Enter name: ")
        email = input("Enter email: ")
        symbol = input("Enter a symbol (X, O): ").upper()
        try:
            user_symbol = GameSymbol[symbol]
        except KeyError:
            raise InvalidSymbolException(f"Invalid symbol input: {symbol}")

        user = User(name, email, "")
        human_player = HumanPlayer(user_symbol, user)
        return human_player


if __name__ == "__main__":
    tic_tac_toe_obj = TicTacToe()
    tic_tac_toe_obj.main()
