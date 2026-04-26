"""
Program Name: settings.py
My name: Ishan Agarwal
Purpose: This file contains the settings for the game, including screen dimensions and speeds.
Starter Code: No
Date: 04/19/2026
"""

from pathlib import Path

class Settings:
    """
    This class contains the general setting for this game. 
    """

    def __init__(self) -> None:
        """
        This initializes the settings for the game
        """

        self.name: str = 'Alien Invasion'
        self.screen_w = 1000
        self.screen_h = 600
        self.FPS = 60
        #Background Image
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        #Ship image
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5
        self.starting_ship_count = 3

        #Bullet image
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullets_amount = 5

        #Alien image
        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png'
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 3
        self.fleet_direction = 1
        self.fleet_drop_speed = 18

        #Button settings
        self.button_w = 200
        self.button_h = 50  
        self.button_color = (0, 135, 50)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'Fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'