import json

class GameStats:
    """ Track statistics for Alien Invasion """

    def __init__(self, ai_game):
        """ Init """
        self.settings = ai_game.settings
        self.highscores = self._load_highscores()
        self.reset_stats()
    
    def reset_stats(self):
        """ Init stats """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def is_highscore(self):
        new = False
        for place, (name, highscore) in enumerate(self.highscores):
            if self.score > highscore:
                new = True
                break
        return new
    
    def insert_and_save_highscore(self, new_name):
        top3 = self.highscores.copy()
        for place, (x, highscore) in enumerate(self.highscores):
            if self.score > highscore:
                top3.insert(place, [new_name, self.score])
                self.highscore = self.score
                break
        self.highscores = top3[:3]
        self._save_highscores()
    
    def _load_highscores(self):
        highscores = []
        file = "highscores.json"
        try:
            with open(file) as f:
                highscores = json.load(f)
        except:
            highscores = [("No name", 0), ("No name", 0), ("No name", 0)]

        return highscores
    
    def _save_highscores(self):
        file = "highscores.json"
        try:
            with open(file) as f:
                json.dump(self.highscores, f)
        except:
            with open(file, 'w') as f:
                json.dump(self.highscores, f)