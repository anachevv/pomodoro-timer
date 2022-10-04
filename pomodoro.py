import tkinter as tk
from time import strftime


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Pomodoro Timer")
        self.minsize(600, 400)
        self.maxsize(600, 400)
        self.geometry("+650+300")
        self.config(bg='pink')

        # Labels
        self.label = tk.Label(self, text='Pomodoro Timer', bg='crimson', padx=30, pady=20, font=('ArialRounded', 18, 'bold'))
        self.label.pack()
        # Pomodoro
        self.pomodoro_label = tk.Label(bg='pink', fg='white', font=('calibri', 60))
        # Long Break
        self.long_label = tk.Label(bg='pink', fg='white', font=('calibri', 60))
        # Short Break
        self.short_label = tk.Label(bg='pink', fg='white', font=('calibri', 60))

        # Buttons
        tk.Button(self, text='Pomodoro', bg='pink', activeforeground='crimson', activebackground='lightgrey', font=('ArialRounded', 16), command=self.pomodoro_time).place(x=40, y=100)
        tk.Button(self, text='Long Break', bg='pink', activeforeground='crimson', activebackground='lightgrey', font=('ArialRounded', 16), command=self.long_time).place(x=230, y=100)
        tk.Button(self, text='Short Break', bg='pink', activeforeground='crimson', activebackground='lightgrey', font=('ArialRounded', 16), command=self.short_time).place(x=430, y=100)
        tk.Button(self, text='START', bg='#ffffff', activebackground='lightgrey', activeforeground='crimson', fg='#D95550', padx=50, pady=0, font=('ArialRounded', 22)).place(x=190, y=300)

    def pomodoro_time(self):
        self.long_label.forget()
        self.short_label.forget()
        string = '25:00'
        self.pomodoro_label.pack(anchor='center', padx=200, pady=100)
        self.pomodoro_label.config(text=string, bg='pink', fg='white', font=('ArialRounded', 60))

    def long_time(self):
        self.pomodoro_label.forget()
        self.short_label.forget()
        string = '15:00'
        self.long_label.pack(anchor='center', padx=200, pady=100)
        self.long_label.config(text=string, bg='pink', fg='white', font=('ArialRounded', 60))

    def short_time(self):
        self.pomodoro_label.forget()
        self.long_label.forget()
        string = '5:00'
        self.short_label.pack(anchor='center', padx=200, pady=100)
        self.short_label.config(text=string, bg='pink', fg='white', font=('ArialRounded', 60))


if __name__ == "__main__":
    app = App()
    app.mainloop()
