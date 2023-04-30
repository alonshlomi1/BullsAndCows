"""
user game stats page
"""
import tkinter as tk
from tkinter import messagebox

FONT = "Arial"
FONT_SIZE = 12


class Gamer_Stats_View:
    """
    view for all the game stats functionality that user can change
    """

    def __init__(self, main_view, location):
        """
        init the game stats view
        :param main_view: tha main view that init it
        :param location: the parent root
        """
        self.frame = None
        self.digits_slider = None
        self.open_statistics_button = None
        self.clear_button = None
        self.game_button = None
        self.label_chosen_num = None
        self.label_num_of_games = None
        self.check_number_view = None
        self.check_colors_view = None
        self.var_number_view = None
        self.var_colors_view = None

        self.main_view = main_view
        self.set_frame(location)
        self.set_check_box()
        self.set_labels()
        self.set_buttons()
        self.set_slider()

    def set_frame(self, location):
        """
        set the main frame of the view
        :param location: the parent root
        :return: None
        """
        self.frame = tk.Frame(location, height=400, width=400, padx=10, pady=10)
        self.frame.grid(column=0, row=0, sticky='n,s')

    def set_check_box(self):
        """
        set all the checkboxes and their vars in tha game stats view
        :return: None
        """
        self.var_colors_view = tk.Variable()
        self.var_colors_view.set(True)
        self.var_number_view = tk.Variable()
        self.var_number_view.set(False)

        self.check_colors_view = tk.Checkbutton(self.frame,
                                                text="Colors View",
                                                variable=self.var_colors_view,
                                                onvalue=True,
                                                offvalue=False,
                                                command=self.update_colors_view,
                                                font=(FONT, FONT_SIZE))
        self.check_colors_view.grid(column=0, row=0)
        self.check_number_view = tk.Checkbutton(self.frame,
                                                text="Number View",
                                                variable=self.var_number_view,
                                                onvalue=True,
                                                offvalue=False,
                                                command=self.update_number_view,
                                                font=(FONT, FONT_SIZE))
        self.check_number_view.grid(column=1, row=0)

    def set_labels(self):
        """
        set all labels in the game stats view
        :return:  None
        """
        self.label_num_of_games = tk.Label(self.frame, width=15, text="Number of games:", pady=20,
                                           font=(FONT, FONT_SIZE))
        self.label_num_of_games.grid(column=0, row=2)

        self.label_chosen_num = tk.Label(self.frame, width=15, text="Number of digits:", pady=20,
                                         font=(FONT, FONT_SIZE))
        self.label_chosen_num.grid(column=0, row=4)

    def set_buttons(self):
        """
        set all tha buttons in tha game stats view
        :return:  None
        """
        self.game_button = tk.Button(self.frame, text="Start Game", font=(FONT, FONT_SIZE))
        self.game_button.grid(column=1, row=7, sticky='e')
        self.game_button.bind("<Button-1>", lambda event: self.start_game())

        self.open_statistics_button = tk.Button(self.frame, text="open statistics", font=(FONT, FONT_SIZE))
        self.open_statistics_button.grid(column=1, row=8, sticky='e', pady=5)
        self.open_statistics_button.bind("<Button-1>", lambda event: self.statistics_button())

        self.clear_button = tk.Button(self.frame, text="Clear", font=(FONT, FONT_SIZE))
        self.clear_button.grid(column=1, row=9, sticky='e', pady=5)
        self.clear_button.bind("<Button-1>", lambda event: self.main_view.clear())



    def set_slider(self):
        """
        set the digits slider it the game stats view
        :return:  None
        """
        self.digits_slider = tk.Scale(self.frame, from_=1, to=6, orient=tk.HORIZONTAL, state='normal', tickinterval=1,
                                      font=(FONT, FONT_SIZE))
        self.digits_slider.set(4)
        self.digits_slider.grid(columnspan=3, row=5, sticky='e,w')

        self.num_of_games_slider = tk.Scale(self.frame, from_=1, to=50, orient=tk.HORIZONTAL, state='normal',
                                            tickinterval=6, font=(FONT, FONT_SIZE))

        self.num_of_games_slider.set(5)
        self.num_of_games_slider.grid(columnspan=3, row=3, sticky='e,w')

    def update_colors_view(self):
        """
        update the current check/uncheck of the colors view checkbox
        update the rest of the view to be valid state
        updete the main view to switch to the current result view
        :return: None
        """
        if self.var_colors_view.get():
            self.var_number_view.set(False)
            self.main_view.set_to_colors()
        else:
            self.var_number_view.set(True)
            self.main_view.set_to_numbers()

    def update_number_view(self):
        """
        update the current check/uncheck of the numbers view checkbox
        update the rest of the view to be valid state
        updete the main view to switch to the current result view
        :return: None
        """
        if self.var_number_view.get():
            self.var_colors_view.set(False)
            self.main_view.set_to_numbers()
        else:
            self.var_colors_view.set(True)
            self.main_view.set_to_colors()

    def start_game(self):
        """
        func for start game button
        the func will read the specific vars from the entries depend on the checkboxes state
        :return: None
        """
        self.main_view.play_game(int(self.num_of_games_slider.get()), number_Of_digits=int(self.digits_slider.get()))

    def statistics_button(self):
        if self.open_statistics_button.cget('text') == "open statistics":
            self.main_view.open_statistics()
            self.open_statistics_button.configure(text="close statistics")
        else:
            self.main_view.close_statistics()
            self.open_statistics_button.configure(text="open statistics")

    def set_statistics_open(self):
        self.open_statistics_button.configure(text="open statistics")
