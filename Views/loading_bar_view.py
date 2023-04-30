"""
loading bar page
"""
import tkinter as tk

class Loading_bar:
    """
    the loading bar view
    """

    def __init__(self, main_view, location):
        """
        :param main_view: the view that init it
        :param location: the parent root
        """
        self.current = None
        self.loading_bar = None
        self.main_view = main_view
        self.frame = tk.Frame(location)
        self.frame.grid(row=1, column=1)

    def set_loading_bar(self):
        """
        sets the starting loading bar
        :return:None
        """
        self.loading_bar = tk.ttk.Progressbar(self.frame, orient=tk.HORIZONTAL, length=200, mode="determinate", takefocus=True, maximum=100)
        self.loading_bar.pack()
        self.loading_bar.step()
        self.current = 1
        self.main_view.update()

    def delete_loading_bar(self):
        """
        delete the loading bar
        :return: None
        """
        self.frame.winfo_children()[0].destroy()

    def update(self, complete, total):
        """
        update loading bar to the current state
        :param complete: number of games already completed
        :param total: total number of games
        :return: None
        """
        for i in range(self.current, int((complete/total)*100)):
            self.current += 1
            self.loading_bar.step()
        self.main_view.update()



