import tkinter as tk
from time import strftime


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Pomodoro Timer")
        self.minsize(600, 400)
        self.geometry("+650+300")
        self.config(bg='pink')

        # Labels
        self.label = tk.Label(self, text='Pomodoro Timer', padx=30, pady=20, font=('Georgia', 18), bg='crimson')
        self.label.pack()

        self.clock_label = tk.Label(text='', background='orangered', foreground='white', font=('Roboto', 25))
        self.clock_label.pack(anchor='center', padx=200, pady=100)
        self.display_time()

        # Buttons
        tk.Button(self, text='Pomodoro', bg='pink', activebackground='lightgrey', font=('Georgia', 16)).place(x=40, y=100)
        tk.Button(self, text='Long Break', bg='pink', activebackground='lightgrey', font=('Georgia', 16)).place(x=230, y=100)
        tk.Button(self, text='Short Break', bg='pink', activebackground='lightgrey', font=('Georgia', 16)).place(x=430, y=100)
        tk.Button(self, text='START', foreground='crimson', padx=50, pady=0, font=('Georgia', 22)).place(x=200, y=300)

    def display_time(self):
        string = strftime('%H:%M:%S %p')
        self.clock_label.config(text=string)
        self.clock_label.after(1000, self.display_time)


if __name__ == "__main__":
    app = App()
    app.mainloop()
