import sys
import pygame
from time import sleep

from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from gamestats import GameStats
from scoreboard import Scoreboard
from highscore import Highscore

class AlienInvasion:
    """ Class to manage game assets and behavior """

    def __init__(self):
        """ Init game and create assets """
        pygame.init()
        pygame.mixer.init()
        self.settings = Settings()

        self.ship_sound_fire = pygame.mixer.Sound(self.settings.ship_sound_fire)
        self.alien_sound_explosion = pygame.mixer.Sound(self.settings.alien_sound_explosion)
        self.game_sound_gameover = pygame.mixer.Sound(self.settings.game_sound_gameover)
        self.game_sound_music = pygame.mixer.Sound(self.settings.game_sound_music)
        self.game_sound_levelup = pygame.mixer.Sound(self.settings.game_sound_levelup)
        self.game_sound_start = pygame.mixer.Sound(self.settings.game_sound_start)
        self.game_sound_mweh = pygame.mixer.Sound(self.settings.game_sound_mweh)
        self.game_sound_playmusic = pygame.mixer.Sound(self.settings.game_sound_playmusic)

        pygame.mixer.Sound.play(self.game_sound_music, -1)

        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        self.highscore = Highscore(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()

        self.just_started = False
        self.countdown = False
        self.onlyonce = True

    def run_game(self):
        """ Start the main loop for the game """
        clock = pygame.time.Clock()
        while True:
            if self.countdown == True:
                pygame.mixer.Sound.stop(self.game_sound_music)
                pygame.mixer.Sound.play(self.game_sound_start)
                sleep(3)
                pygame.mixer.Sound.play(self.game_sound_playmusic, -1)
                self.countdown = False

            if self.stats.game_active and self.just_started:
                self.countdown = True
                self.just_started = False

            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()
                self._check_collisions()

            self._update_screen()
            clock.tick(200)

    def _check_events(self):
        """ Respond to keyboard or mouse events """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_UP:
            if self.stats.game_active:
                self._fire_bullet()
            else:
                self._start_game()
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _start_game(self):
            self.stats.game_active = True

            self.settings.init_dynamic_settings()
            self.stats.reset_stats()

            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            for alien in self.aliens:
                alien.start_moving()
            self.ship.new_ship()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
            self.just_started = True

    def _fire_bullet(self):
        """ Create bullet and add to bullets group """
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            pygame.mixer.Sound.play(self.ship_sound_fire)

    def _clean_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """ Create fleet of aliens """
        # Make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * (alien_width))
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create rows of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):       
        # Create an alien and place in window
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number + 25
        self.aliens.add(alien)

    def _update_aliens(self):
        """ Update the positions of all aliens """
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_aliens_landed()

    def _ship_hit(self):
        """ Handle hitting ship """
        self.ship.explode()
        self.onlyonce = True
        for alien in self.aliens:
            alien.pause_moving()
        pygame.mixer.Sound.play(self.game_sound_mweh)
        if self.stats.ships_left > 1:
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
        else:
            self.stats.game_active = False
            self.stats.game_over = True
            self.stats.check_highscore()
            self.highscore.update()
            pygame.mixer.Sound.stop(self.game_sound_playmusic)
            pygame.mixer.Sound.play(self.game_sound_gameover)
            #sleep(4)
            pygame.mixer.Sound.play(self.game_sound_music)
            pygame.mouse.set_visible(True)

    def _check_aliens_landed(self):
        """ Check if any aliens have landed """
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break
    
    def _check_fleet_edges(self):
        """ Change fleet direction when reached edge of screen """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """ Drop fleet and change direction """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _update_bullets(self):
        """ Update bullets and clean old bullets """
        self.bullets.update()
        self._clean_bullets()
    
    def _check_collisions(self):
        """ Check for collisions between bullets and aliens """
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
                pygame.mixer.Sound.play(self.alien_sound_explosion)

            self.sb.prep_score()

        if not self.aliens:
            pygame.mixer.Sound.play(self.game_sound_levelup)
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.sb.prep_level()
            sleep(2)
    
    def _update_screen(self):
        """ Redraw screen and flip to new screen """

        # Redraw screen 
        self.screen.fill(self.settings.bg_color)

        self.ship.blitme()

        if self.stats.game_active:
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.aliens.draw(self.screen)
            self.sb.draw_score()

        if not self.stats.game_active:
            self.highscore.draw_highscore()

        if not self.ship.exploding:
            if self.onlyonce:
                for alien in self.aliens:
                    alien.start_moving()
                self.onlyonce = False

        # Make the last drawn screen visible
        pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
