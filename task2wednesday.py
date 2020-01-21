favourite_movies =[
    "Joker",
    "Gentelments",
    "Jumanji",
    "Her",
    "Bin Jip"
]

print(favourite_movies)
#remove(),
favourite_movies.remove("Jumanji")

print(favourite_movies)

("\n")
#reverse(),

favourite_movies.reverse()

print(favourite_movies)

#sort(), 
#sort alphabetical
favourite_movies.sort()

#favourite movies - reversed
favourite_movies.sort(reverse=True)

print(favourite_movies)

# count(), 

x = favourite_movies.count("Her")

print(x)

print(favourite_movies.count("Her"))
# extend() 

more_movies = [
    "John Wick",
    "Mlode wilki"
]

favourite_movies.extend(more_movies)
print(favourite_movies)
