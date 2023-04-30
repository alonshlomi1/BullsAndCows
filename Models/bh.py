# author: itzhik aviv
import random
import sys

NumberOfGames = 10
NumberOfDigits = 4
Number = 2
Zero = True


class BH:
    def __createTable(self):
        self.__L = []
        for x in range(10 ** (self.__numberOfDigits - 1),
                       10 ** self.__numberOfDigits):
            s1 = str(x)
            s2 = set(s1)
            if not Zero and "0" in s1:
                continue
            else:
                if len(s1) == len(s2):
                    self.__L.append(s1)
        # random.shuffle(self.__L)

    def __createTheNumber(self):
        self.__Number = random.choice(self.__L)
        self.__number = self.__Number

    def __createGuess(self):
        self.__guess = random.choice(self.__L)

    def __findBH(self):
        self.__NH = 0
        self.__NB = 0
        for i in range(self.__numberOfDigits):
            c1 = self.__guess[i]
            j = self.__number.find(c1)
            if i == j:
                self.__NB += 1
            else:
                if j >= 0:
                    self.__NH += 1

    def __reduceTable(self):
        self.__L1 = []
        for self.__guess in self.__L:
            self.__findBH()
            if (self.__NB == self.__nb and \
                    self.__NH == self.__nh):
                self.__L1.append(self.__guess)
        self.__L.clear()
        self.__L = self.__L1.copy()
        # random.shuffle(self.__L)

    def __init__(self, number=0, numberOfDigits=4, data=None, i=0):
        self.__counter = 0
        self.data = data
        try:
            if not isinstance(number, int) \
                    or number < 0:
                raise ValueError("number = " \
                                 + str(number) \
                                 + ": must be int (not string or float) and >= 0.")
            if not isinstance(numberOfDigits, int) \
                    or numberOfDigits <= 0 or numberOfDigits >= 9:
                raise ValueError("mumberOfDigits = " \
                                 + str(numberOfDigits)
                                 + ": must be int (not string or float) and > 0" \
                                 + " and <= 9.")
            if number == 0:
                self.__numberOfDigits = numberOfDigits
                self.__createTable()
                self.__createTheNumber()
            else:
                self.__Number = str(number)
                self.__number = self.__Number
                self.__numberOfDigits = len(self.__number)
                if not Zero and "0" in self.__Number:
                    raise ValueError(self.__number + \
                                     ": number must not include 0.")
                for c in self.__number:
                    if self.__number.count(c) > 1:
                        raise ValueError(self.__number + \
                                         ": every digit must appears only one time.")
                self.__createTable()
        except ValueError as e:
            print(e)
            return
        print("number: ", self.__number,
              " table size: ", len(self.__L))
        self.data['games'][i]['number'] = self.__number
        self.data['games'][i]['table_size'] = len(self.__L)
        self.data['games'][i]['guess_list'] = []
        self.original_table_len = len(str(len(self.__L)))
        while True:
            self.__number = self.__Number
            self.__counter += 1
            self.__createGuess()
            self.__findBH()
            print("guess number", self.__counter, \
                  " is:", self.__guess, \
                  " table size:", len(self.__L), \
                  ("  " * (self.original_table_len - len(str(len(self.__L))))) +
                  " nb:", self.__NB, " nh:", self.__NH, end="\n")
            self.data['games'][i]['guess_list'].append({
                "guess_number": self.__counter,
                "is": self.__guess,
                "table_size": len(self.__L),
                "nb": self.__NB,
                "nh": self.__NH
            })
            if self.__NB == self.__numberOfDigits:
                break
            else:
                # self.__L.remove(self.__guess)
                self.__number = self.__guess
                self.__nb = self.__NB
                self.__nh = self.__NH
                self.__reduceTable()
        print("\n"+ str(self.__counter),"tries",  end='')
        self.data['games'][i]['number_of_tries'] = self.__counter
        self.data['total_guesses'] += self.__counter
        #print("\n")

    def getCounter(self):
        return self.__counter
