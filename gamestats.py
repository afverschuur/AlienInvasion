import json

class GameStats:
    """ Track statistics for Alien Invasion """

    def __init__(self, ai_game):
        """ Init """
        self.settings = ai_game.settings
        self.highscores = self.load_highscores()
        self.reset_stats()
    
    def reset_stats(self):
        """ Init stats """
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

    def check_highscore(self):
        top3 = self.highscores.copy()
        new = False
        for place, (name, highscore) in enumerate(self.highscores):
            name = "New"
            if self.score > highscore:
                top3.insert(place, (name, self.score))
                new = True
                break
        self.highscores = top3[:3]
        if new:
            self.save_highscores(self.highscores)
        return new

    def load_highscores(self):
        highscores = []
        file = "highscores.json"
        try:
            with open(file) as f:
                highscores = json.load(f)
        except:
            highscores = [("Noname", 0), ("Noname", 0), ("Noname", 0)]

        return highscores
    
    def save_highscores(self, highscores):
        file = "highscores.json"
        try:
            with open(file) as f:
                json.dump(highscores, f)
        except:
            with open(file, 'w') as f:
                json.dump(highscores, f)