import tkinter as tk
from time import strftime


class App:

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Pomodoro Timer")
        self.root.minsize(600, 400)
        self.root.geometry("+650+300")
        self.root.config(bg='pink')

        # Labels
        self.label = tk.Label(self.root, text='Pomodoro Timer', padx=30, pady=20, font=('Georgia', 18), bg='crimson')
        self.label.pack()

        # Buttons
        tk.Button(self.root, text='Pomodoro', bg='pink', activebackground='lightgrey', font=('Georgia', 16)).place(x=40, y=100)
        tk.Button(self.root, text='Long Break', bg='pink', activebackground='lightgrey', font=('Georgia', 16)).place(x=230, y=100)
        tk.Button(self.root, text='Short Break', bg='pink', activebackground='lightgrey', font=('Georgia', 16)).place(x=430, y=100)
        tk.Button(self.root, text='START', foreground='crimson', padx=50, pady=0, font=('Georgia', 22)).place(x=200, y=300)


        self.root.mainloop()


App()
