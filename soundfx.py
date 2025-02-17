import pygame
from time import sleep

class SoundFX:
    """ Class to implement soundeffects """
    def __init__(self) -> None:
        # Init pygame mixer
        pygame.mixer.init()

        # Load sounds
        self.sounds = dict()
        self.sounds['fire'] = pygame.mixer.Sound("assets/sounds/laser.mp3")
        self.sounds['explosion'] = pygame.mixer.Sound("assets/sounds/explosion.mp3")
        self.sounds['levelup'] = pygame.mixer.Sound("assets/sounds/levelup.mp3")
        self.sounds['fail'] = pygame.mixer.Sound("assets/sounds/fail.mp3")
        self.sounds['gameover'] = pygame.mixer.Sound("assets/sounds/gameover.mp3")
        
        # Load music
        self.musics = dict()
        self.musics['music_start'] = pygame.mixer.Sound("assets/sounds/music_start.mp3")
        self.musics['music_play'] = pygame.mixer.Sound("assets/sounds/music_play.mp3")

        # Open dedicated channel for music
        self.music_channel = pygame.mixer.Channel(1)
    
    def sound(self, sound, pausemusic=False, wait=False):
        """ Play sound """
        # Pause music before playing sound if True
        if pausemusic:
            self.music_channel.pause()
        pygame.mixer.Sound.play(self.sounds[sound])
        # Wait for sound to end before continuing game
        if wait:
            sleep(self.sounds[sound].get_length())
        # Unpause music before playing sound if True
        if pausemusic:
            self.music_channel.unpause()

    def music(self, music):
        """ Play music (infinite) """
        self.music_channel.play(self.musics[music], -1)




