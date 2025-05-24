from media import Movie


class User:
    def __init__(self, username, password):
        # Set the basic user info. Create empty list to store user's movie wishlist and friends.
        self.username = username
        self.password = password
        self.wishlist = []
        self.friends = []

    def add_movie(self, name, type, rating=0.0, comment=""):
        # Add movie to wishlist if it is not already added.
        # It will create a new Movie object and add it to the list.
        if not any(movie.name == name for movie in self.wishlist):
            self.wishlist.append(Movie(name, type, rating, comment))
            print(f"'{name}' has been added to your wishlist.")
        else:
            print("This movie is already in your wishlist.")

    def delete_movie(self, name):
        # Try to remove the movie with given name from wishlist.
        # If found and removed, show delete message. If not, show "movie not found".
        original_length = len(self.wishlist)
        self.wishlist = [m for m in self.wishlist if m.name != name]
        print("Movie deleted." if len(self.wishlist) < original_length else "Movie not found.")

    def update_movie(self, name):
        # Let user update rating and comment for a movie already in wishlist.
        # If rating input is not number, use 0.0 as default.
        for movie in self.wishlist:
            if movie.name == name:
                try:
                    movie.rating = float(input("New rating (0-10): "))
                except ValueError:
                    movie.rating = 0.0
                movie.comment = input("New comment: ")
                print("Movie updated.")
                return
        print("Movie not found.")

    def clear_wishlist(self):
        # Remove all movies from wishlist.
        self.wishlist.clear()
        print("Your wishlist has been cleared.")

    def check_movie(self, name):
        # Check if movie name exists in wishlist.
        exists = any(movie.name == name for movie in self.wishlist)
        print("Movie exists in wishlist." if exists else "Movie not found.")

    def show_wishlist(self):
        # Print all movies in wishlist. If no movies, show empty message.
        if not self.wishlist:
            print("No movies in your wishlist.")
        else:
            print("Your movie wishlist:")
            for movie in self.wishlist:
                print(f"- {movie}")

    def add_friend(self, friend_username):
        # Add a new friend to the friend list. Only add if it is not already added.
        if friend_username not in self.friends:
            self.friends.append(friend_username)
            print(f"You are now following {friend_username}.")
        else:
            print(f"You're already following {friend_username}.")

    def unfollow_friend(self, friend_username):
        # Remove friend from the list. If not found, nothing happen.
        self.friends = [f for f in self.friends if f != friend_username]
        print(f"Unfollowed {friend_username}.")

    def clear_friends(self):
        # Clear all friends from the list.
        self.friends.clear()
        print("You have unfollowed everyone.")

    def list_friends(self):
        # Print all friend usernames in list. If list is empty, then show 'You have no friends added'.
        print("Your friends:")
        print("\n".join(self.friends) if self.friends else "You have no friends added.")

    def suggest_movies(self):
        # Suggest movies that user's friends added but user did not added.
        # Will load each friend's data and collect unique movie names.
        suggestions = set()
        for friend_name in self.friends:
            friend = User.load_user(friend_name)
            if friend:
                for movie in friend.wishlist:
                    if movie.name not in [m.name for m in self.wishlist]:
                        suggestions.add(movie.name)
        return list(suggestions)

    def change_password(self, new_password):
        # Change user's password to a new one .
        self.password = new_password
        print("Password updated.")

    def save_user(self):
        # Save user infomation to file. And save wishlist and friend list to separate files.
        with open(f"{self.username}.txt", "w") as file:
            file.write(f"{self.username}\n{self.password}\n")

        with open(f"{self.username}_wishlist.txt", "w") as file:
            for movie in self.wishlist:
                file.write(movie.format_for_file() + "\n")

        with open(f"{self.username}_friends.txt", "w") as file:
            for friend in self.friends:
                file.write(friend + "\n")

    @classmethod
    def load_user(cls, username):
        # Load user data from file. If any file not exist, skip the part.
        # Will return a User object if load successful. Return None if main file not found.
        try:
            with open(f"{username}.txt", "r") as f:
                lines = [line.strip() for line in f.readlines()]
            if len(lines) < 2:
                return None
            user = cls(lines[0], lines[1])

            try:
                with open(f"{username}_wishlist.txt", "r") as f:
                    user.wishlist = [Movie.from_file_string(line)
                                     for line in f if Movie.from_file_string(line)]
            except FileNotFoundError:
                pass

            try:
                with open(f"{username}_friends.txt", "r") as f:
                    user.friends = [line.strip() for line in f.readlines()]
            except FileNotFoundError:
                pass

            return user
        except FileNotFoundError:
            return None
