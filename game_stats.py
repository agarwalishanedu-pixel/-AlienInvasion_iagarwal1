"""
Program Name: game_stats.py
My name: Ishan Agarwal
Purpose: This file contains the class for tracking game statistics
Starter Code: NO
Date: 04/19/2026
"""


#Volatile Game Stats

class GameStats():
    """
    This class is used to track the game stats, such as the number of ships left
    """

    def __init__(self, ship_limit)-> None:
        """
        This initializes the game stats"""

        self.ships_left = ship_limit