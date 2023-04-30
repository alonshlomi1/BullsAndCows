"""
main model page
"""
import os
import random

from Models.bh import BH
import sys
import json


class Model:
    """
    main model of tha application
    """
    def __init__(self, controller):
        """
        :param controller: the controller that init it
        """
        self.statistics_data = None
        self.stats_data = None
        self.controller = controller

    def game(self, number_of_games=2, number_Of_digits=None):
        """
        tha func run number of games with help from BH and write in all at bhOutput.txt for the numbers view
        and bhOutputColors.json for the colors view

        :param number_of_games: the number of games the user choose
        :param number_Of_digits: the number of digits that the user choose to play with
        :return: Bool: if the game simulation succeed
        """
        orig_stdout = sys.stdout
        # set default print to file for the numbers view
        sys.stdout = open("./App_data/bhOutput.txt", 'w')
        l = []
        # data for the json file for the colors view
        data = {}
        # open stats_data to update the statistics view
        with open('./App_data/bhOutputStats.json.py') as file:
            self.stats_data = json.load(file)
        data['games'] = []
        data["average_guesses"] = 0
        data["total_guesses"] = 0

        # simulate the games and prints the results to all the data files
        for i in range(number_of_games):
            print("\nGame number ", str(i + 1))
            data['games'].append({})
            data['games'][i]['game_number'] = i + 1
            # generate random number
            rand_num = self.random_number(number_Of_digits)
            # simulate the game with BH
            bh = BH(number=rand_num, numberOfDigits=number_Of_digits, data=data, i=i)
            data = bh.data
            l.append(bh.getCounter())
            print(" in game number ",  str(i + 1), "\n")
            self.controller.update_loading_bar(i, number_of_games)
        # prints end results to the files
        print("average number of guesses for ", \
              str(number_of_games), " games is: ", \
              sum(l) / len(l))
        data["average_guesses"] = sum(l) / len(l)
        sys.stdout.close()
        sys.stdout = orig_stdout
        self.stats_data["last_game"]["avg"] = sum(l) / len(l)
        self.stats_data["last_game"]["number_of_digits"] = number_Of_digits
        self.stats_data["last_game"]["number_of_games"] = number_of_games
        self.stats_data["last_game"]["number_of_games"] = number_of_games
        temp = self.stats_data["all_games"]["games_for_digits"][number_Of_digits-1]
        self.stats_data["all_games"]["games_for_digits"][number_Of_digits-1]["avg_for_digit"] = (temp["avg_for_digit"]*temp["games_for_digit"] + ((sum(l) / len(l))* number_of_games))/(temp["games_for_digit"]+number_of_games)
        self.stats_data["all_games"]["games_for_digits"][number_Of_digits-1]["games_for_digit"] += number_of_games

        # write data to json files
        with open("./App_data/bhOutputColors.json.py", 'w') as j_f:
            json.dump(data, j_f)
        with open("./App_data/bhOutputStats.json.py", 'w') as j_f:
            json.dump(self.stats_data, j_f)

        if number_of_games in [50, 100, 150, 200] and os.path.isfile('./App_data/bhOutputStatistics.json.py'):
            with open('./App_data/bhOutputStatistics.json.py') as file:
                self.statistics_data = json.load(file)
            self.statistics_data[str(number_of_games)]["avr_per_digit"][number_Of_digits - 1]["avg"] = sum(l) / len(l)
            with open("./App_data/bhOutputStatistics.json.py", 'w') as j_f:
                json.dump(self.statistics_data, j_f)

        return True

    def random_number(self, number_of_digits):
        """
        generate a random var without repeating digits from the number_of_digits parm
        :param number_of_digits: int: number of digits to generate (1-9)
        :return: int: the new random var
        """
        rand_num = ""
        for i in range(number_of_digits):
            rand_digit = random.randint(1, 9)
            # check that the digit not already in the number
            while str(rand_digit) in rand_num:
                rand_digit = random.randint(0, 9)
            rand_num += str(rand_digit)
        return int(rand_num)

    def set_json(self):
        with open('./App_data/bhOutputStatistics.json.py', 'w') as file:
            json.dump({
    "50": {"avr_per_digit": [{"avg": 5.28}, {"avg": 4.84}, {"avg": 5.04}, {"avg": 5.38}, {"avg": 6.0}, {"avg": 6.56}]},
    "100": {
        "avr_per_digit": [{"avg": 5.21}, {"avg": 5.24}, {"avg": 5.08}, {"avg": 5.38}, {"avg": 5.91}, {"avg": 6.59}]},
    "150": {"avr_per_digit": [{"avg": 4.833333333333333}, {"avg": 5.153333333333333}, {"avg": 5.22}, {"avg": 5.46},
                              {"avg": 5.846666666666667}, {"avg": 6.586666666666667}]}, "200": {
        "avr_per_digit": [{"avg": 5.155}, {"avg": 5.29}, {"avg": 5.09}, {"avg": 5.415}, {"avg": 5.785},
                          {"avg": 6.535}]}}, file)
        for i in [50, 100, 150, 200]:
            for j in range(1, 6):
                self.game(i, j)