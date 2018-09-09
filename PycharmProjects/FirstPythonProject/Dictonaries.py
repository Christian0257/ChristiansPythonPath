AFavouiteGame = {
    "name": "Undertale",
    "rating": "10/10",
    "Genre" : "RPG"
}

print(AFavouiteGame.get("name"))


AllFavouriteGames = [
    {"name": "Undertale", "Rating": "10/10", "Genre": "RPG"},
    {"name": "Night in the Woods", "Rating": "10/10", "Genre": "Story Rich"},
    {"name": "Edith Finch", "Rating": "10/10", "Genre": "Walking Simulator"},
]

print(str(AllFavouriteGames[2].items()))

print(str(AllFavouriteGames[-1].get("Idiotic People Who Didn't like it", "Does not exist")))