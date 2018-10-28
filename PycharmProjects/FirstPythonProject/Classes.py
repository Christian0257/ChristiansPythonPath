FavGames = []

class Games:
    def addGame(self, name, genre, rating):
        game = {"name": name, "Genre": genre, "rating": rating}
        FavGames.append(game)


class Games2:
    def __init__(self, name, genre, rating):
        game = {"name": name, "Genre": genre, "rating": rating}
        FavGames.append(game)

    def __str__(self):
        return "Game"


game2 = Games2("Undertale", "RPG", "10/10")


class Games3:

    Gamer = "Christian Oliver"

    def __init__(self, name, genre, rating):
        self.name = name
        self.genre = genre
        self.rating = rating
        FavGames.append(self)

    def __str__(self):
        return "Game - " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_gamer(self):
        return self.Gamer


game = Games3("Undertale", "RPG", "10/10")

print(game)

print(FavGames)
