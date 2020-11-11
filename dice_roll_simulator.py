from datetime import datetime, timedelta
import time
from sys import argv
import random
import csv
"""
this program simulates x number of dice rolls and provides the time/roll and analysis in a CSV file.
written by zebadiah taylor
"""

# Number of times the program rolls. Feel free to change.
# sim_count = 5000
# dice_size = 20


def dice_roll_sim_main(sim_count, dice_size):
    # this dict is used for counting the # of individual roll
    roll_count = {}
    most_common_roll_count = 0
    most_common_rolls = {}
    last_roll = 0
    repeats = 0
    max_repeats = 0
    multiple_max_repeated_rolls = []

    # used for calculating averages later on
    sum_of_nums = 0

    # records when the program started to determine execution time
    start_time = time.time()

    # creates or overwrites CSV file
    with open("dice_roll_simulations.csv", 'w', newline='') as file:
        rand_shit = csv.writer(file, delimiter=",")
        rand_shit.writerow(["second", "microsecond", f"d{dice_size} roll"])

    # "Rolls" the dice sim_count number of times
    for x in range(sim_count + 1):
        now = datetime.now()
        dice_roll = random.randint(1, dice_size)
        # counts how often each number was rolled in the roll_count dict
        if dice_roll in roll_count.keys():
            roll_count[dice_roll] += 1
        else:
            roll_count[dice_roll] = 1
        # writes the time and "rolled" number to the csv
        with open("dice_roll_simulations.csv", 'a', newline='') as file:
            rand_shit = csv.writer(file, delimiter=",")
            rand_shit.writerow([now.second, now.microsecond, dice_roll])
        sum_of_nums += dice_roll
        # records repeated rolls, highest string of repeats
        if dice_roll != last_roll:
            if repeats > max_repeats:
                max_repeats = repeats
                max_repeated_roll = last_roll
                multiple_max_repeated_rolls.clear()
            if repeats == max_repeats:
                multiple_max_repeated_rolls.append(last_roll)
            repeats = 0
            last_roll = dice_roll
        if dice_roll == last_roll:
            repeats += 1

    # calculates most frequent roll(s)
    for each_key in roll_count.keys():
        if roll_count[each_key] == most_common_roll_count:
            most_common_rolls[each_key] = roll_count[each_key]
        if roll_count[each_key] > most_common_roll_count:
            most_common_rolls.clear()
            most_common_roll_count = roll_count[each_key]
            most_common_rolls[each_key] = roll_count[each_key]

    # ends the CSV file with useful information for the user
    with open("dice_roll_simulations.csv", 'a', newline='') as file:
        rand_shit = csv.writer(file)
        rand_shit.writerow([f"The program simulated {sim_count} dice rolls  in {time.time() - start_time} seconds."])
        rand_shit.writerow([f"The mean average of these numbers is {round(sum_of_nums/x, 2)}"])
        rand_shit.writerow([f"The mean roll is {round(sum_of_nums/x)} "])
        if len(multiple_max_repeated_rolls) > 1 and max_repeats > 1:
            rand_shit.writerow([f"""The longest strings of repeats were rolls of {multiple_max_repeated_rolls}. Each were rolled {max_repeats} times in a row."""])
        elif max_repeats > 1:
            rand_shit.writerow([f"The longest string of repeats was a roll of {max_repeated_roll}, which was rolled {max_repeats} times in a row."])
        rand_shit.writerow([f"""Below are Most Common Roll(s) and Times that # was Rolled"""])
        rand_shit.writerow([f"{most_common_rolls}"])


# dice_roll_sim_main(argv[1], argv[2])

# print(f"{argv[0]} is done. Find the dice_roll_simulations.csv file. Statistical analysis is at the very bottom/end.")
print(f"{argv[0]}{argv[1]}{argv[2]}")
