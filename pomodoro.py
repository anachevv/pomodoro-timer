import tkinter as tk
from time import strftime


class App:

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Pomodoro Timer")
        self.root.minsize(600, 400)
        self.root.geometry("+650+300")
        self.root.config(bg='pink')

        self.root.mainloop()


App()
