class Movie:
    def __init__(self, name, type, rating=0.0, comment=""):
        # Create a function with name, type, rating, and comment as movie object.
        # If rating or comment not given, will use default value.
        self.name = name
        self.type = type
        self.rating = rating
        self.comment = comment

    def to_file_string(self):
        # Turn movie data into one line string, use | to separate each part.
        # And save movie to file.
        return f"{self.name}|{self.type}|{self.rating}|{self.comment}"

    @staticmethod
    def from_file_string(line):
        # Read one line from file and make it to Movie object.
        # If data not complete, or rating not a number.
        parts = line.strip().split("|")
        if len(parts) != 4:
            return None
        name, type, rating, comment = parts
        try:
            rating = float(rating)
        except ValueError:
            rating = 0.0
        return Movie(name, type, rating, comment)