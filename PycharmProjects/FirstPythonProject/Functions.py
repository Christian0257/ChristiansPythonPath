FavGames = []


def add_game(game):
    FavGames.append(game)


def print_fav_games():
    for game in FavGames:
        print(game)


def read_file():
    file = open("AllFavouriteGames", "r")
    for game in file:
        add_game(game)
    file.close()


def save_file():
    file = open("AllFavouriteGames", "w")
    file.write(str(FavGames))
    file.close()


read_file()
print("Your Favourite Games are: " + str(FavGames))

AddAnotherGame = input("\nWould you like to add a new game?\n")

if AddAnotherGame[0] == "Y":
    AddAnotherGame = True
    while AddAnotherGame:
        NewGameTitle = input("What is the name of your game?\n")
        NewGameRating = input("On a scale from 1 to 10, how would you rate the game?\n")
        NewGameGenre = input("Finally, what is the genre of the game?\n")

        add_game({NewGameTitle, NewGameRating, NewGameGenre})
        print_fav_games();

        FinalChoice = input("Would you like to add another?")

        if FinalChoice[0] == "N":
            print("Thanks for your contribution(s)")
            save_file()
            break
