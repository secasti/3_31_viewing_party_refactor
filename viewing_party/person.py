class Person:
    def __init__(self, name):
        self.name = name
        self.friends = []
        self.watchlist = []
        self.watched = []

    def add_friend(self, new_friend):
        if new_friend not in self.friends:
            self.friends.append(new_friend)

    def add_movie_to_watchlist(self, movie):
        if movie not in self.watched and movie not in self.watchlist:
            self.watchlist.append(movie)
    