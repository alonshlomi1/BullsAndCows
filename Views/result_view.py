"""
game results screen with numbers page
"""
import tkinter as tk
from App_data.info import FONT, FONT_SIZE, TITLE_FONT_SIZE



class Result_View:
    """
    the number result view
    """

    def __init__(self, main_view, location):
        """
        :param main_view: the view that init it
        :param location: the parent root
        """
        self.main_view = main_view
        self.frame = tk.Frame(location, width=500, height=500)
        self.frame.grid(column=1, row=0, sticky='n')
        self.scroll_bar = tk.Scrollbar(self.frame, width=20, orient='vertical')
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text = tk.Text(self.scroll_bar, width=55, font=(FONT, FONT_SIZE))
        self.text.pack(side=tk.LEFT)
        self.text.insert(tk.END, open("./App_data/bhOutput.txt", 'r').read())

    def update_result(self):
        """
        updates the view for update info
        :return: None
        """
        self.main_view.clear()
        self.text.insert(tk.END, open("./App_data/bhOutput.txt", 'r').read())
