FavouiteGame = {
    "Name": "Undertale",
    "Rating": "10/10",
    "Genre": "RPG"
}

FavouiteGame["Sequel"] = "N/A"

try:
    Sequel = FavouiteGame["Sequel"]
    NumberOfSequels = "N/A" + 0
except KeyError:
    print("Could not find such a key in the dictionary")
except TypeError as error:
    print("Cannot add Strings to Integers")
    print("Error Description - " + str(error))