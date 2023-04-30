"""
game results with colors screen page
"""
from tkinter import ttk
import tkinter as tk
import json
from App_data.info import LINE_HEIGHT, colors_dict, FONT, FONT_SIZE, TITLE_FONT_SIZE


class Colors_View:
    """
    the colors result view
    using tk.Canvas for both display text and colors ovals
    """

    def __init__(self, main_view, location):
        """
        func for init colors result view
        :param main_view: the main view that init it
        :param location: the parent root
        """
        self.scroll_bar_frame = None
        self.scroll_bar = None
        self.canvas = None
        self.canvas_height = None
        self.colors_output = None
        self.main_view = main_view
        self.frame = tk.Frame(location, width=450, height=500)
        self.frame.grid(column=1, row=0, sticky="n,w")
        self.line = 20
        self.base = 110
        self.set_canvas()

    def set_canvas(self):
        """
        set the main canvas and scroll bar
        gets info from bhOutputColors.json and App_data.colors
        :return: None
        """
        # open json file for the data
        with open('./App_data/bhOutputColors.json.py') as file:
            self.colors_output = json.load(file)
        self.canvas_height = 400
        self.canvas = tk.Canvas(self.frame, width=450, height=600, bg="white",
                                scrollregion=(0, 0, 100, self.canvas_height))
        self.canvas.grid(column=0, row=0, sticky="ew")

        self.scroll_bar = tk.Scrollbar(self.frame, width=30, orient='vertical', command=self.canvas.yview)
        self.scroll_bar_frame = ttk.Frame(self.frame)

        self.scroll_bar.grid(column=1, row=0, sticky="ns")
        self.canvas.configure(yscrollcommand=self.scroll_bar.set)

    def set_games(self):
        """
        show all the games on the canvas using print_game func
        :return: None
        """
        self.line = 20
        self.base = 110
        # shows all the games
        for i in range(len(self.colors_output["games"])):
            self.print_game(i - 1)
        self.next_line()
        self.canvas.create_text(self.base + 125, self.line, font=(FONT, FONT_SIZE),
                                text="Average number of guesses for " + str(len(self.colors_output["games"]))
                                     + "  games is: " + str(self.colors_output["average_guesses"]))

    def print_game(self, i):
        """
        print the current game uses print_guess for all guesses
        :param i: the number of the current game
        :return: None
        """
        self.next_line()
        # print the game title
        self.canvas.create_text(self.base, self.line, font=(FONT, TITLE_FONT_SIZE, "underline"),
                                text="Game Number: " + str(i + 2))
        self.next_line()
        # print the game stats
        self.canvas.create_text(self.base, self.line, font=(FONT, FONT_SIZE), text="hidden sequence: ")
        self.print_colors(self.base + 90, self.line, number=self.colors_output["games"][i]["number"])

        # print all the game guesses
        for j in range(len(self.colors_output["games"][i]["guess_list"])):
            self.print_guess(i, j)
        self.next_line()
        self.next_line()
        # print game final stats
        self.canvas.create_text(self.base + 30, self.line, font=(FONT, FONT_SIZE),
                                text= str(len(self.colors_output["games"][i]["guess_list"]))+ " tries in game number " +str(i + 2))
        self.next_line()
        self.next_line()

    def print_guess(self, i, j):
        """
        print the current guess
        :param i: the current game number
        :param j: the current guess number
        :return: None
        """
        self.next_line()
        self.next_line()
        # print guess number
        self.canvas.create_text(self.base, self.line, font=(FONT, FONT_SIZE), text="guess number: " + str(j + 1))
        self.canvas.create_text(self.base + 120, self.line, font=(FONT, FONT_SIZE), text="is: ")
        # print the guess
        self.print_colors(self.base + 140, self.line, number=self.colors_output["games"][i]["guess_list"][j]["is"])

        self.next_line()
        self.canvas.create_text(self.base, self.line, font=(FONT, FONT_SIZE),
                                text="table size: " + str(
                                    self.colors_output["games"][i]["guess_list"][j]["table_size"]))
        self.canvas.create_text(self.base + 120, self.line, font=(FONT, FONT_SIZE),
                                text="nb: " + str(
                                    self.colors_output["games"][i]["guess_list"][j]["nb"]))
        self.canvas.create_text(self.base + 170, self.line, font=(FONT, FONT_SIZE),
                                text="nh: " + str(
                                    self.colors_output["games"][i]["guess_list"][j]["nh"]))

    def print_colors(self, base, line, number):
        """
        print the choose number with colored ovals
        uses info from  App_data.colors to switch numbers and colors
        :param base: base x position on the canvas
        :param line: y position on the canvas, the current line
        :param number: the hidden number
        :return: None
        """
        for ind, val in enumerate(str(number)):
            self.canvas.create_oval(base + (ind * 20), line - 10, base + (ind * 20) + 20, line + 10,
                                    fill=colors_dict[int(val)])

    def next_line(self):
        """
        set line to the next line
        :return: None
        """
        self.line += LINE_HEIGHT

    def update_result(self):
        """
        updates the view for update info
        :return: None
        """
        self.canvas.delete(tk.ALL)
        with open('./App_data/bhOutputColors.json.py') as file:
            self.colors_output = json.load(file)
            self.canvas_height = (self.colors_output["total_guesses"] * 4 + len(
                self.colors_output["games"] * 2)) * LINE_HEIGHT
            self.canvas.configure(scrollregion="0 0 100 " + str(self.canvas_height))
            self.set_games()
