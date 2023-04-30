"""
main controller page
"""
from Models.model import Model
from Views.main_view import Main_View


class Controller:
    """
    the controller is initialized from the main app
    """

    def __init__(self):
        """
        :var model: is the connection to the main model
        :var view: is the connection to the main view
        """
        self.model = Model(self)
        self.view = Main_View(self)
        self.view.start_view()

    def play_game(self, number_of_games, number_Of_digits=None):
        """
        func that connect between pressing button on the UI to the model
        :param number_of_games: the number of games the user choose
        :param number: the number that the user choose to play with
        :param number_Of_digits: the number of digits that the user choose to play with
        :return: Bool: if the game simulation succeed
        """
        return self.model.game(number_of_games, number_Of_digits)

    def update_loading_bar(self, complete, total):
        """
        connect between the model and the view to update the current state of the loading bar
        :param complete: number of games completed
        :param total: total number of games
        """
        self.view.update_loading_bar(complete, total)


    def set_json(self):
        self.model.set_json()