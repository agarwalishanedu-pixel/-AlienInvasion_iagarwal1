"""
Program Name: game_stats.py
My name: Ishan Agarwal
Purpose: This file contains the class for tracking game statistics
Starter Code: NO
Date: 04/19/2026
"""
from pathlib import Path
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

#Volatile Game Stats

class GameStats():

    def __init__(self, game: 'AlienInvasion')-> None:
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_score()
        self.reset_stats()

    def init_saved_score(self):
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
            #save the file

    def save_scores(self):
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"File Not Found: {e}")

    def reset_stats(self):
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions) -> None:
        # update score
        self._update_score(collisions)

        # update max score
        self._update_max_score()

        # update hi score
        self._update_hi_score()

    def _update_score(self, collisions):
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f"Basic: {self.max_score}")

    def _update_max_score(self):
        # update max_score
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f"Max: {self.score}")

    def _update_hi_score(self):
        # update hi_score
        if self.score > self.hi_score:
            self.hi_score = self.score
        #print(f"Hi: {self.score}")
        

    def update_level(self):
        self.level += 1
        #print(self.level)