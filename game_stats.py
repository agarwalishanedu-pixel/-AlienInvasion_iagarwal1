"""
Program Name: game_stats.py
My name: Ishan Agarwal
Purpose: This file contains the class for tracking game statistics
Starter Code: NO
Date: 04/19/2026
"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

#Volatile Game Stats

class GameStats():

    def __init__(self, game: 'AlienInvasion')-> None:
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self):
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions) -> None:
        # update score
        self._update_score(collisions)

    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f"Max: {self.max_score}")

        # update max_score
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f"Basic: {self.score}")

        # update hi_score

    def update_level(self):
        self.level += 1
        #print(self.level)