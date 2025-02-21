import pygame

from classes.game_loop_interface import GameLoopInterface

from game_assets.ship import Ship
from game_assets.bullet import Bullet
from game_assets.alien import Alien

from .scoreboard import Scoreboard

class PlayGame(GameLoopInterface):

    ######################################
    # INIT
    ######################################

    def __init__(self, game_base) -> None:
        """ Init """
        super().__init__(game_base)

        # Init scoreboard
        self.sb = Scoreboard(game_base)
        
        # Init game assets
        self.ship = Ship(game_base)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Create fleet of alien
        self._create_fleet()

    def _create_fleet(self):
        """ Create fleet of aliens """
        # Make an alien
        alien = Alien(self.game_base)
        # Get size
        alien_width, alien_height = alien.rect.size

        # Calculate max aliens in row
        available_space_x = self.game_base.settings.screen_width - (2 * (alien_width))
        number_aliens_x = available_space_x // (2 * alien_width)

        # Calculate max rows of aliens
        ship_height = self.ship.rect.height
        available_space_y = (self.game_base.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create rows of aliens
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):       
        # Create an alien and place in window
        alien = Alien(self.game_base)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien.rect.height * row_number + 25
        self.aliens.add(alien)
    
    ######################################
    # CHECK EVENTS
    ######################################

    def check_events(self, event) -> None:
        """ Respond to keyboard events """
        if event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        # Key up events
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)
    
    def _check_keydown_events(self, event):
        """ Respond to keydown events (keyboard)"""
        # RIGHT
        if event.key == pygame.K_RIGHT:
            # Start moving ship to the right
            self.ship.moving_right = True
        # LEFT (no elif to hold still when right key and left key are both down)
        if event.key == pygame.K_LEFT:
            # Start moving ship to the left
            self.ship.moving_left = True
        # UP
        elif event.key == pygame.K_UP:
            # Fire laserbullet!
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """ Respond to keydup events (keyboard)"""
        # RIGHT
        if event.key == pygame.K_RIGHT:
            # Stop moving ship to the right
            self.ship.moving_right = False
        # LEFT
        if event.key == pygame.K_LEFT:
            # Stop moving ship to the left
            self.ship.moving_left = False

    def _fire_bullet(self):
        """ Create bullet and add to bullets group """
        # If more bullets allowed
        if len(self.bullets) < self.game_base.settings.bullets_allowed:
            # Create bullet
            new_bullet = Bullet(self.game_base)
            self.bullets.add(new_bullet)
            # Play sound
            self.game_base.soundfx.sound('fire')

    ######################################
    # UPDATE ASSETS
    ######################################

    def update_assets(self) -> None:
        """ Update assets """
        # Update ship
        self.ship.update()

        # Update aliens
        self._update_aliens()

        # Update bullets and cleanup bullets off screen
        self.bullets.update()
        self._clean_bullets()

        # Update collisions
        self._check_bullet_alien_collisions()
        self._check_ship_alien_collision()
        self._check_aliens_landed()

        # Update scoreboard
        self.sb.update()


    def _update_aliens(self):
        """ Update the positions of all aliens """
        self._check_fleet_edges()
        self.aliens.update()

    def _check_fleet_edges(self):
        """ Change fleet direction when reached edge of screen """
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    
    def _change_fleet_direction(self):
        """ Drop fleet and change direction """
        for alien in self.aliens.sprites():
            alien.rect.y += self.game_base.settings.fleet_drop_speed
        self.game_base.settings.fleet_direction *= -1

    def _clean_bullets(self):
        """ Clean up bullets when off screen """
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self):
        """ Check for collisions between bullets and aliens """
        # Check for collisions (last booleans: True asset dissapears)
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        # If collisions update score and play sound
        if collisions:
            for aliens in collisions.values():
                self.game_base.stats.score += self.game_base.settings.alien_points * len(aliens)
                # Play sound
                self.game_base.soundfx.sound('explosion')

        # If no aliens left, level up
        if not self.aliens:
            self._levelup()

    def _levelup(self):
        """ Level up the game """
        # Level up
        self.game_base.stats.level += 1

        # Increase speed
        self.game_base.settings.increase_speed()

        # Play sound
        self.game_base.soundfx.sound('levelup', wait=True)

        # Clear all bullets
        self.bullets.empty()

        # Create new fleet
        self._create_fleet()

    def _check_ship_alien_collision(self):
        """ Check for collisions between ship and alien """
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _check_aliens_landed(self):
        """ Check if any aliens have landed """
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.game_base.screen_rect.bottom:
                self._ship_hit()
                break
    
    def _ship_hit(self):
        """ Handle hitting ship """
        # Play sound
        self.game_base.soundfx.sound('fail')

        # When ships left, try again
        if self.game_base.stats.ships_left > 1:
            # Minus 1 ship
            self.game_base.stats.ships_left -= 1

            # Cleanup bullets and create new fleet
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()

        # No ships left: Game over!
        else:
            # Play sound
            self.game_base.soundfx.sound('gameover', pausemusic=True, wait=True)

            # If new highscore, switch to New Highscore loop
            if self.game_base.stats.is_highscore():
                self.game_base.switch_loop_to(self.game_base.new_highscore)
            # Else, switch Loop to Game Over loop
            else:
                self.game_base.switch_loop_to(self.game_base.game_over)

    ######################################
    # UPDATE SCREEN
    ######################################

    def update_screen(self) -> None:
        """ Redraw assets and flip the screen"""
        # Background
        self.game_base.screen.fill(self.game_base.settings.bg_color)

        # Draw ship, bullets and aliens
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.game_base.screen)
        
        # Draw scoreboard
        self.sb.draw()

    ######################################
    # HOOKS
    ######################################

    def start(self) -> None:
        self.game_base.soundfx.music('music_play')

        # Reset stats and dynamic settings
        self.game_base.settings.init_dynamic_settings()
        self.game_base.stats.reset_stats()

        # Update scoreboard 
        self.sb.update()

        # Clear aliens, bullets and create new fleet
        self.aliens.empty()
        self.bullets.empty()
        self._create_fleet()

        # Init new ship en center
        self.ship.new_ship()
        self.ship.center_ship()