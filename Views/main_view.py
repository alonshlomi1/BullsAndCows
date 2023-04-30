"""
main view page
"""
import tkinter as tk
from Views.result_view import Result_View
from Views.game_stats_view import Gamer_Stats_View
from Views.menu_bar_view import Menu_bar
from Views.colors_view import Colors_View
from Views.loading_bar_view import Loading_bar
from Views.statistics_view import Statistics_view


class Main_View:
    """
    The main view window of the application
    """

    def __init__(self, controller):
        """
        func for init main view
        :param controller: is the controller that init it
        :var is_colors: bool: let the main view know to display color or number result page
        :var root: Tk: tha main UI root
        :var game_stats_view: view that shows all the user game stats functionality
        :var game_color_view: view that shows the game result with colors
        :var result_view: view that shows the game result with numbers
        :var menu_bar_view: init the top menu bar
        """
        self.result_view = None
        self.is_colors = True
        self.controller = controller

        # create main root
        self.root = tk.Tk()
        self.root.config(height=600)
        self.root.title("BullsAndCows Game")
        self.root.wm_attributes("-topmost", 1)
        self.root.eval('tk::PlaceWindow . center')

        # create all root children
        self.menu_bar_view = Menu_bar(self.root)
        self.game_stats_view = Gamer_Stats_View(self, self.root)
        self.game_color_view = Colors_View(self, self.root)
        self.loading_bar = None#Loading_bar(self, self.root)
        self.statistics_view = Statistics_view(self, self.root)

    def start_view(self):
        """
        statrt the main view
        :return:
        """
        self.root.mainloop()

    def play_game(self, number_of_games, number_Of_digits=None):
        """
        func that connect between pressing button on the UI to the model
        if the games succeed it wil update the current view
        :param number_of_games: number of games that the user want to play
        :param number_Of_digits: if tha user want to play with specific number of digits it will be here
        :return: None:
        """
        self.loading_bar = Loading_bar(self, self.root)
        self.loading_bar.set_loading_bar()
        self.erase()
        if self.controller.play_game(number_of_games, number_Of_digits):
            if self.is_colors:
                self.game_color_view.update_result()
            else:
                self.result_view.update_result()
        self.loading_bar.delete_loading_bar()
        self.loading_bar = None
#        if len(self.statistics_view.frame.winfo_children()) > 0:
#            self.statistics_view.delete_statistics()
#            self.statistics_view.set_statistics()

    def set_to_colors(self):
        """
        switch to color results view
        :return:None
        """
        self.result_view.frame.grid_remove()
        self.game_color_view = Colors_View(self, self.root)
        self.game_color_view.update_result()
        self.is_colors = True

    def set_to_numbers(self):
        """
        switch to number results view
        :return:None
        """
        self.game_color_view.frame.grid_remove()
        self.result_view = Result_View(self, self.root)
        self.is_colors = False

    def clear(self):
        """
        clear the current result view
        :return: None
        """
        if self.is_colors:
            self.game_color_view.canvas.delete(tk.ALL)
        else:
            self.result_view.text.delete('1.0', tk.END)
        self.close_statistics()

    def erase(self):
        """
        clear the current result view
        :return: None
        """
        if self.is_colors:
            self.game_color_view.canvas.delete(tk.ALL)
        else:
            self.result_view.text.delete('1.0', tk.END)

    def update(self):
        self.root.update()

    def update_loading_bar(self, complete, total):
        if self.loading_bar is not None:
            self.loading_bar.update(complete, total)

    def open_statistics(self):
        self.statistics_view.set_statistics()

    def close_statistics(self):
        self.statistics_view.delete_statistics()
        self.game_stats_view.set_statistics_open()

    def set_json(self):
        self.controller.set_json()