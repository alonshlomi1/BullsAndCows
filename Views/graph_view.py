"""
graph view page
"""
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Graph:

    def __init__(self,parent,  x, y, y_bar):
        """
        create  the Average tries for number of digits graph
        :param parent: the root patent to display in
        :param x: x value list
        :param y: y value list
        :param y_bar: y value title
        """
        xy = []
        for i in range(len(x)):
            xy.append(y[i]/x[i])
        self.fig, self.ax = plt.subplots()
        self.ax.bar(x, y)
        # shows all x values
        plt.xticks(x)
        # make graph titles
        self.ax.set_xlabel('number of digits')
        self.ax.set_ylabel(y_bar)
        self.ax.set_title('Average tries for number of digits Graph')
        self.ax.xaxis.set_label_coords(0.5,-0.055)

        self.ax2 = self.ax.twiny()
        self.ax2.plot(x, xy, 'r-')
        self.ax2.set_ylabel('average number of tries / number of digits', color='r', rotation=0)
        self.ax2.yaxis.set_label_coords(0.5,-0.1)
        for i, val in enumerate(xy):
            self.ax2.text(x[i], val, f'{val:.2f}', color='r', ha='center', va='bottom')
        # draw graph and close fig
        self.renderer = FigureCanvasTkAgg(self.fig, master=parent)
        self.renderer.draw()
        plt.close(self.fig)


