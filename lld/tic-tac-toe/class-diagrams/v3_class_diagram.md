    To solve problem no -4 and -5 we can use Flyweight desing pattern 
    Create 2 classes Intrinsic and Extrinsic 
    1. User(Intrinsic) - This class will not change (name, email, photo)
    2. Human(Extrinsic) - This class will have session_id, color 


```mermaid 
classDiagram
direction RL
class Game{
    -board : Board
    -players : [Player]
    -status : GameStatus
    -winner_id : int
    +start_game()
    +make_move()
    +check_winner()
}

class Player{
    <<abstract class>>
    -symbol : Symbol
    +play()
}

class Bot{
    -level : Level
    -strategy: PlayingStrategy
    +play()
}

class Human{
    -session_id : int
    -color : Color  
    -user : User
    +play()
}
class User{
    -name : string
    -email : string
    -photo : bytes
}
class PlayingStrategy{
    <<abstract class>>
    +make_move()
}

class Random{
    +make_move()
}

class MinMax{
    +make_move()
}

class Board{
    -size : int
    -Cells : [[Cell]]
}

class Cell{
    -symbol : Symbol
    -x : int
    -y : int 
}


class Color{
    <<enumeration>>
    RED
    BLACK
    BLUE
}

class GameStatus{
    <<enumeration>>
    IN_PROGRESS
    FINISHED
    DRAWN
}

class Level{
    <<enumeration>>
    EASY
    MEDIUM
    HARD
}

class Symbol{
    <<enumeration>>
    X
    Y
}

Player "M" *-- "1" Game : has
Human --|> Player : Inheritance
User "1" o-- "M" Human : has
Bot --|> Player: Inheritance
Board "1" *-- "1" Game : has
Random --|> PlayingStrategy : Inheritance
MinMax --|> PlayingStrategy : Inheritance
PlayingStrategy "1" *-- "1" Bot : has
Cell "M" *-- "1" Board : has

```
