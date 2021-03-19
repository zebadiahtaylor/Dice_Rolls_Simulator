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
        mode_count = 0
        the_mode = self._modes()
        for x in self.rolls_simulation:
            if x == the_mode[0]: # Only needs to check 1st num
                mode_count += 1
        return mode_count            

    def pretty_modes(self):
        """
        For returning a "prettier" string
        of the mode(s). 
        """
        modes = self._modes()
        modes = ' & '.join([str(mode) for mode in modes])
        return modes

    def __repr__(self):
        return f"Session contained {self.roll_count} rolls w/ a d{self.die_type}"


"""
For testing purposes only
"""
# tuesday_night = DiceRollSimulation(20, 10000)
# # weds_night = DiceRollSimulation(6, 500)
# # print(f"the # of rolls: {len(tuesday_night.rolls_simulation)}")
# # print(f"the # of rolls: {len(weds_night.rolls_simulation)}")
# # print(tuesday_night.rolls_simulation)
# # print(tuesday_night.find_mean_average())
# print(f"the mode is {tuesday_night.find_modes()}, "
#       f"rolled {tuesday_night.find_mode_frequency()} times")
# # print(f"the mean is {mean(tuesday_night.rolls_simulation)}")

# print(f"the mode is {tuesday_night.pretty_modes()}, "
#       f"rolled {tuesday_night.find_mode_frequency()} times")