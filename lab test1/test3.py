def recommend_movies(movies, preferred_genre):
    recommended = [movie['title'] for movie in movies if movie['genre'].lower() == preferred_genre.lower()]
    return recommended

if __name__ == "__main__":
    # Example movie list
    movies = [
        {'title': 'The Dark Knight', 'genre': 'Action'},
        {'title': 'Pulp Fiction', 'genre': 'Crime'},
        {'title': 'Inception', 'genre': 'Action'},
        {'title': 'The Godfather', 'genre': 'Crime'},
        {'title': 'Forrest Gump', 'genre': 'Drama'},
        {'title': 'The Matrix', 'genre': 'Action'}
    ]

    user_genre = input("Enter your preferred genre: ")
    recommendations = recommend_movies(movies, user_genre)
    if recommendations:
        print(f"Recommended movies in the genre \"{user_genre}\":")
        for idx, title in enumerate(recommendations, 1):
            print(f"{idx}: {title}")
    else:
        print(f"No movies found in the genre \"{user_genre}\".")
