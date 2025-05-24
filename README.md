# Movie Night Planner

**Movie Night Planner** is a tool designed for small friend groups or roommates to coordinate weekly movie nights. It also serves as a personal tool for each user to manage their long-term movie watchlist. The system reduces decision fatigue, improves shared planning, and makes tracking movies more fun and social.

## Project Goals

- Help users plan weekly movie nights together
- Provide each user with a personalized movie wishlist
- Enable social features to suggest what to watch together
- Use Python classes and file I/O for simulating persistent data

## Features

### 👤 1. User System
- User registration and login using username and password
- Data is stored in local files to simulate user accounts

### 🎬 2. Personal Movie Wishlist
- Users can add, remove, and view movies on their wishlist
- Serves as a long-term "To-Watch" list

### 👥 3. Social Functionality
- Users can follow each other
- Only **mutual followers** can:
  - View each other’s wishlists
  - See who added which movies
  - Get suggestions for what to watch together

### 🎲 4. Weekly Movie Suggestion Generator
- Weekly or on-demand movie suggestions:
  - Recommends movies appearing on multiple mutual wishlists
  - If no overlap exists, suggests a random movie from available lists

## File Structure (Key Modules)

- `user.py`: Handles user system, friends, and wishlist logic
- `movie.py`: Defines the `Movie` class for movie details (type, rating, comment)
- `main.py`: (Optional) Entry point for running the program
- User data files: Like `username.txt`, `username_wishlist.txt`, `username_friends.txt` (simulate a database)

## Technologies Used

- Language: Python 3
- Object-Oriented Programming (OOP)
- File I/O for saving and loading data

##  How to Use

Run the program from the command line or integrate it with a GUI or web interface. Currently, this is a CLI-based version.
