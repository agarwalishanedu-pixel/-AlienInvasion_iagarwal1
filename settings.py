"""
Program Name: settings.py
My name: Ishan Agarwal
Purpose: This file contains the settings for the game, including screen dimensions and speeds.
Starter Code: No
Date: 04/12/2026
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
        self.screen_w = 1200
        self.screen_h = 800
        self.FPS = 60
        #Background Image
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        #Ship image
        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5

        #Bullet image
        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullets_amount = 5