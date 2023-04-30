"""
statistics page
"""
import os
import tkinter as tk
from tkinter import messagebox
import json
from Views.graph_view import Graph
from App_data.info import FONT, FONT_SIZE, TITLE_FONT_SIZE


class Statistics_view:
    """
    the total statistics
    """

    def __init__(self, main_view, location):
        """
        init the statistics view
        :param main_view: the main view that init i
        :param location: the parent root to display in
        """
        self.label_num_of_games = None
        self.set_button = None
        self.digits_slider = None
        self.buttons_frame = None
        self.graph = None
        self.graph_frame = None
        self.y = None
        self.x = None
        self.last_game_text = None
        self.stats_output = None

        self.main_view = main_view
        self.frame = tk.Frame(location)
        self.frame.grid(row=0, column=2)

    def set_statistics(self):
        """
        sest up the last game statistics and the graph
        """
        # read data to display
        if not os.path.isfile('./App_data/bhOutputStatistics.json.py'):
            tk.messagebox.showinfo("massage", "Creating new Data file, please wait a few minuts... ")
            self.main_view.set_json()
        with open('./App_data/bhOutputStatistics.json.py') as file:
            self.stats_output = json.load(file)
        self.set_buttons_bar()
        self.create_graph()

    def set_buttons_bar(self):
        self.buttons_frame = tk.Frame(self.frame)

        self.label_num_of_games = tk.Label(self.buttons_frame, width=15, text="Number of games:", pady=20,
                                           font=(FONT, FONT_SIZE))
        self.label_num_of_games.grid(column=0, row=0)

        self.digits_slider = tk.Scale(self.buttons_frame, from_=50, to=200, resolution=50, orient=tk.HORIZONTAL,
                                      state='normal', tickinterval=50, font=(FONT, FONT_SIZE), length=300)
        self.digits_slider.set(50)
        self.digits_slider.grid(column=1, row=0, sticky='e,w', padx=10)

        self.set_button = tk.Button(self.buttons_frame, text="Set", font=(FONT, FONT_SIZE))
        self.set_button.grid(column=2, row=0, sticky='e')
        self.set_button.bind("<Button-1>", lambda event: self.set_button_click())

        self.buttons_frame.grid(row=1, column=0)

    def set_button_click(self):

        for child in self.graph_frame.winfo_children():
            child.destroy()
        self.create_graph()


    def delete_statistics(self):
        """
        delete all statistics view
        """
        for child in self.frame.winfo_children():
            child.destroy()
        self.main_view.update()

    def create_graph(self):
        """
        create lists for the graph
        :return:
        """
        # x for the number of digits values
        self.x = []
        # z for the number of tries values
        # self.z = []
        # y for the average number of tries values
        self.y = []
        # sets the graph frame
        self.graph_frame = tk.Frame(self.frame, height=100, width=100)
        self.graph_frame.grid(row=0, column=0, pady=10, padx=10)
        # fill x,y,z values from data
        for i, bar in enumerate(self.stats_output[str(self.digits_slider.get())]["avr_per_digit"]):
            # self.z.append(bar["games_for_digit"])
            self.y.append(bar["avg"])
            self.x.append(i + 1)
        # create graph
        self.graph = Graph(self.graph_frame, self.x[:6], self.y[:6], "average number of tries")
        self.graph.renderer.get_tk_widget().grid(row=1, column=1)
        # option to add another graph
        # self.graph1 = Graph(self.graph_frame, self.x, self.z, "number of tries")
        # self.graph1.renderer.get_tk_widget().grid(row=1, column=2)
