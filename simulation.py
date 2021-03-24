"""
Mass dice roll simulator based on the OOP paradigm.  
"""
from datetime import datetime, timedelta
import time
from random import randint
from statistics import mean, median, mode, multimode

class DiceRollSimulation():
    """
    Takes # of rolls and the die size (type of die, like a d20, etc.)
    and upon initilization creates a simulation of X # of rolls.
    Provides tools for analysis of said simulation. 
    """
    # rolls_simulation = [] # A list containing all rolls in the simulation.

    def __init__(self, die_type, roll_count):
        self.die_type = int(die_type)
        self.roll_count = int(roll_count)
        self.rolls_simulation = [randint(1, self.die_type) for _ in range(self.roll_count)]

    def _mean(self):
        return round(mean(self.rolls_simulation), 2)

    def _median(self):
        return median(self.rolls_simulation)
 
    def _modes(self):
        """
        Returns as a list. Use "def pretty_modes"
        below for returning strings.
        """
        modes = multimode(self.rolls_simulation)
        return modes

    def _mode_frequency(self):
        """
        Returns frequency of the mode(s)
        """
        mode_count = 0
        the_mode = self._modes()
        for x in self.rolls_simulation:
            if x == the_mode[0]: # Only needs to check 1st num
                mode_count += 1
        return mode_count            

    def pretty_modes(self):
        """
        Returns modes as a string.
        """
        modes = self._modes()
        modes = ' & '.join([str(mode) for mode in modes])
        return modes

    def pretty_rolls(self):
        """
        Returns rolls as a string.
        """
        pretty_rolls = self.rolls_simulation
        pretty_rolls = ', '.join([str(roll) for roll in pretty_rolls])
        return pretty_rolls

    def __repr__(self):
        return f"Instance({self.die_type}, {self.roll_count})"

    def __str__(self):
        return f"This session rolled {self.die_type} {self.roll_count} times."

