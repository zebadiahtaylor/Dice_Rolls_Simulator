from datetime import datetime, timedelta
import time
from sys import argv, exit
import random
import csv
from statistics import mean, median, mode, multimode
"""
this program simulates x number of dice rolls and provides the time/roll and analysis in a CSV file.
It's based on a procedural programming paradigm.
It's a bit of a mess. An early program. Made no use of the stastitics library in first version.
written by zebadiah taylor 10/2020
"""

# Number of times the program rolls. Feel free to change. Overly large numbers can be challenging for computers. 
# Use whole numbers only. 
sim_count = 1000
# The type of die the program simulates. Use whole numbers only. 
dice_size = 20

"""for future iterations to take command line arguments"""
# try:
#     sim_count = argv[1]
#     dice_size = argv[2]
# except IndexError:
#     exit("You gave the incorrect number of arguments Try: py dice_role_sim.py ### #")
# try: 
#     int(sim_count)
#     int(dice_size)
# except TypeError, ValueError:
#     exit("All arguments must use whole numbers only. Try: py dice_role_sim.py 1000 20")


def dice_roll_sim_main(sim_count, dice_size):
    # this dict is used for counting the # of individual roll
    
    last_roll = 0
    list_of_all_rolls = []
    most_common_roll_count = 0
    most_common_rolls = {}
    roll_count = {}
    
    repeats = 0
    max_repeats = 0
    multiple_max_repeated_rolls = []

    # used for calculating averages later on
    sum_of_nums = 0

    # records when the program started to determine execution time
    start_time = time.time()

    # creates or overwrites CSV file
    with open("dice_roll_simulations.csv", 'w', newline='') as file:
        csv_output = csv.writer(file, delimiter=",")
        csv_output.writerow(["second", "microsecond", f"d{dice_size} roll"])

    # "Rolls" the dice sim_count number of times
    for x in range(int(sim_count) + 1):
        now = datetime.now()
        dice_roll = random.randint(1, dice_size)
        # counts how often each number was rolled in the roll_count dict
        if dice_roll in roll_count.keys():
            roll_count[dice_roll] += 1
        else:
            roll_count[dice_roll] = 1
        # writes the time and "rolled" number to the csv
        with open("dice_roll_simulations.csv", 'a', newline='') as file:
            csv_output = csv.writer(file, delimiter=",")
            csv_output.writerow([now.second, now.microsecond, dice_roll])
        sum_of_nums += dice_roll
        list_of_all_rolls.append(dice_roll)
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
        csv_output = csv.writer(file)
        csv_output.writerow([f"The program simulated {sim_count} dice rolls  in {time.time() - start_time} seconds."])
        csv_output.writerow([f"The mean average of these numbers is {round(sum_of_nums/x, 2)}"])
        csv_output.writerow([f"The mean roll is {round(sum_of_nums/x)} "])
        if len(multiple_max_repeated_rolls) > 1 and max_repeats > 1:
            csv_output.writerow([f"""The longest strings of repeats were rolls of {multiple_max_repeated_rolls}. Each were rolled {max_repeats} times in a row."""])
        elif max_repeats > 1:
            csv_output.writerow([f"The longest string of repeats was a roll of {max_repeated_roll}, which was rolled {max_repeats} times in a row."])
        csv_output.writerow([f"""Below are Most Common Roll(s) and Times that # was Rolled"""])
        csv_output.writerow([f"{most_common_rolls}"])
    
    # prints analysis to the terminal
    print(f"Hello! You have run a dice rolling simulation!")
    print(f"The program simulated {sim_count} dice rolls in {round(time.time() - start_time, 2)} second(s).")
    print(f"The average (mean) roll was {round(mean(list_of_all_rolls), 2)}")
    print(f"The mode was {mode(list_of_all_rolls)}")
    if len(multiple_max_repeated_rolls) > 1 and max_repeats > 2:
            print(f"The longest strings of repeats were rolls of {multiple_max_repeated_rolls}. Each were rolled {max_repeats} times in a row.")
    elif max_repeats > 1:
        print(f"The longest string of repeats was a roll of {max_repeated_roll}, which was rolled {max_repeats} times in a row.")
    
    """
    Prints out the mode. 
    """
    
    output_rolls = ""
    key_list = list(most_common_rolls.keys())
    times_rolled = list(most_common_rolls.values())
    times_rolled = times_rolled[0] # Number of times most common rolls occurred
    for key in key_list:    # 
        output_rolls += str(key) + " & "
    output_rolls = output_rolls[:-3]
    if len(output_rolls) <= 2:
        print(f"The most common roll (the mode) was {output_rolls}, "
        f"which was rolled {times_rolled} times.")
    else: 
        print(f"The most common rolls (the modes) were {output_rolls}, "
        f"each rolled {times_rolled} times")


    # print(f"""Below are Most Common Roll(s) and Times that # was Rolled""")
    # print(f"{most_common_rolls}")


dice_roll_sim_main(sim_count, dice_size)