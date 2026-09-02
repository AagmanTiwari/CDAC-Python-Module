'''
Exercise 2: Movie Night Playlist
Scenario: You are organizing a movie marathon. You start with a playlist: 
["Inception", "The Matrix", "Interstellar"]. Prompt the user to enter the name of a movie they want to add.

If the movie is already in the list, print "Already added!" and do not insert it.
If it is not in the list, append it to the end of the list. Finally, sort the movie list alphabetically and print the updated playlist.

Sample Input: "Interstellar"
Sample Output:Already added!
Alphabetical Playlist: ['Inception', 'Interstellar', 'The Matrix']

Sample Input: "Avatar"
Sample Output:
Added Avatar!
Alphabetical Playlist: ['Avatar', 'Inception', 'Interstellar', 'The Matrix']
'''


def main():
    movie_playlist = ["Inception", "The Matrix", "Interstellar"]
    while True:
        movie_name = input(
            "Enter the name of the movie to add (or type 'exit' to quit): ").strip().title()

        if movie_name.lower() == "exit":
            print("Exiting .....")
            break

        if movie_name == "":
            print("Please enter a valid movie name.")
            continue

        if movie_name in movie_playlist:
            print("Already added!")
        else:
            movie_playlist.append(movie_name)
            print(f"Added {movie_name}!")

        # Sort the playlist alphabetically
        movie_playlist.sort()
        print(f"Alphabetical Playlist: {movie_playlist}")


main()
