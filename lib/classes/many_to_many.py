from statistics import mean

class Game:
    def __init__(self, title):
        self.title = title
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if not hasattr(self, "_title"):
            if type(new_title) == str and len(new_title) > 0:
                self._title = new_title

    def results(self):
        return [result for result in Result.all if result.game == self]

    def players(self):
        return list({game.player for game in self.results()})

    def average_score(self, player):
        return mean([result.score for result in self.results()])

class Player:
    def __init__(self, username):
        self.username = username
    
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, new_username):
        if type(new_username) == str and 2 <= len(new_username) <= 16:
            self._username = new_username

    def results(self):
        return [result for result in Result.all if result.player == self]

    def games_played(self):
        return list({result.game for result in self.results()})

    def played_game(self, game):
        return game in self.games_played()

    def num_times_played(self, game):
        return len([result.game for result in self.results() if result.game == game])

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, new_score):
        if not hasattr(self, "_score"):
            if type(new_score) == int and 1 <= new_score <= 5000:
                self._score = new_score
    
    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, new_game):
        if isinstance(new_game, Game):
          self._game = new_game
        
    @property
    def player(self):
        return self._player
    
    @player.setter
    def player(self, new_player):
       if isinstance(new_player, Player):
           self._player = new_player