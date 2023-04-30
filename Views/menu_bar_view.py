"""
top menu bar page
"""
import tkinter as tk
from tkinter import messagebox
from App_data.info import HELP_MSG
from App_data.info import ABOUT_MSG

class Menu_bar:
    """
    the top manu bar setting
    """
    def __init__(self, location):
        """
        init top menu bar
        :param location: the parent root
        """
        self.menu_bar = tk.Menu(location)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Exit", command=self.exit_func)
        self.menu_bar.add_cascade(menu=self.file_menu, label="File")

        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu.add_command(label="Help", command=self.help_func)
        self.help_menu.add_command(label="About", command=self.about_func)

        self.menu_bar.add_cascade(menu=self.help_menu, label="Help")

        location.config(menu=self.menu_bar)


    def help_func(self):
        """
        pop the help message
        """
        messagebox.showinfo(title="Help",message=HELP_MSG)


    def about_func(self):
        """
        pop the about message
        """
        messagebox.showinfo(title="About",message=ABOUT_MSG)

    def exit_func(self):
        """
        exit the program
        """
        exit()