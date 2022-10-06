import MemoryGame
import GuessGame
import CurrencyRouletteGame


def welcome(name):
    return "Hello " + name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play.\n"


def load_game():
    game_number = 0
    while game_number < 1 or game_number > 3:
        try:
            game_number = int(input("Please choose a game to play:\n1. Memory Game - a sequence of numbers will "
                                    "appear for 1 second and you have to guess it back\n2. Guess Game - guess a "
                                    "number and see if you chose like the computer\n3. Currency Roulette - try and "
                                    "guess the value of a random amount of USD in ILS\n"))
        except:
            pass

    difficulty = 0
    while difficulty < 1 or difficulty > 5:
        try:
            difficulty = int(input("Please choose game difficulty from 1 to 5:"))
        except:
            pass

    if game_number == 1:
        MemoryGame.play(difficulty)
    elif game_number == 2:
        GuessGame.play(difficulty)
    elif game_number == 3:
        CurrencyRouletteGame.play(difficulty)
