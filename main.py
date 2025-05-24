from user import User


def main():
    print("Welcome to Movie Night Planner!")
    username = input("Enter username: ")
    user = User.load_user(username)

    if not user:
        print("User not found. Please create a new account.")
        password = input("Create a password: ")
        user = User(username, password)
        user.save_user()

    while True:
        print("\nMenu:")
        print("1. Add movie to wishlist")
        print("2. View wishlist")
        print("3. Delete movie")
        print("4. Update movie info")
        print("5. Check movie existence")
        print("6. Clear wishlist")
        print("7. Add friend")
        print("8. Unfollow friend")
        print("9. List friends")
        print("10. Clear all friends")
        print("11. View suggestions from friends")
        print("12. Change password")
        print("13. Save and exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Movie name: ")
            type = input("Movie type (e.g., Action, Comedy): ")
            try:
                rating = float(input("Rating (0-10): "))
            except ValueError:
                rating = 0.0
            comment = input("Any comments?: ")
            user.add_movie(name, type, rating, comment)

        elif choice == "2":
            user.show_wishlist()

        elif choice == "3":
            name = input("Enter movie name to delete: ")
            user.delete_movie(name)

        elif choice == "4":
            name = input("Enter movie name to update: ")
            user.update_movie(name)

        elif choice == "5":
            name = input("Enter movie name to check: ")
            user.check_movie(name)

        elif choice == "6":
            user.clear_wishlist()

        elif choice == "7":
            friend = input("Friend username: ")
            user.add_friend(friend)

        elif choice == "8":
            friend = input("Friend username to unfollow: ")
            user.unfollow_friend(friend)

        elif choice == "9":
            user.list_friends()

        elif choice == "10":
            user.clear_friends()

        elif choice == "11":
            suggestions = user.suggest_movies()
            if suggestions:
                print("Movie suggestions from friends:")
                for movie in suggestions:
                    print(f"- {movie}")
            else:
                print("No new suggestions.")

        elif choice == "12":
            new_password = input("Enter new password: ")
            user.change_password(new_password)

        elif choice == "13":
            user.save_user()
            print("User saved. Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
