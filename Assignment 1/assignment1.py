
import csv
CSV_FILE = 'movies.csv'
MENU = """Menu:
L - List movies
A - Add new movie
W - Mark a movie as watched
Q - Quit"""


def main():
    print("Movie Tracker Program")
    movies = load_movies(CSV_FILE)
    choice = ''
    while choice.upper() != 'Q':
        print(MENU)
        choice = input("Choose an option: ").upper()
        if choice == 'L':
            list_movies(movies)
        elif choice == 'A':
            add_movie(movies)
        elif choice == 'W':
            mark_as_watched(movies)
        elif choice != 'Q':
            print("Invalid option.")
    save_movies(CSV_FILE, movies)
    print("Goodbye!")


def load_movies(filename):
    movies = []
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            movies.append(row)
    return movies


def save_movies(filename, movies):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(movies)


def list_movies(movies):
    movies.sort(key=lambda x: (x[2], x[0]))
    for i, movie in enumerate(movies, 1):
        watched_status = '*' if movie[3] == 'u' else ''
        print(f"{i}. {movie[0]} - {movie[1]} ({movie[2]}) {watched_status}")


def add_movie(movies):
    title = input("Title: ")
    category = input("Category: ")
    year = input("Year: ")
    # Basic error checking
    if not year.isdigit() or int(year) < 1900 or int(year) > 2024:
        print("Invalid year!")
        return
    movies.append([title, category, year, 'u'])


def mark_as_watched(movies):
    unwatched_movies = [movie for movie in movies if movie[3] == 'u']
    if not unwatched_movies:
        print("No more movies to watch!")
        return
    list_movies(movies)
    try:
        choice = int(input("Enter the number of the movie to mark as watched: "))
        if movies[choice-1][3] == 'u':
            movies[choice-1][3] = 'w'
            print(f"{movies[choice-1][0]} marked as watched")
        else:
            print("That movie is already watched.")
    except (ValueError, IndexError):
        print("Invalid selection.")


if __name__ == '__main__':
    main()
