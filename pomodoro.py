import threading
import tkinter as tk
from time import sleep
from tkinter import messagebox


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Pomodoro Timer")
        self.minsize(600, 400)
        self.maxsize(600, 400)
        self.geometry("+650+300")
        self.config(bg='pink')

        # App Title Label
        tk.Label(self, text='Pomodoro Timer', bg='crimson', padx=30, pady=20, font=('ArialRounded', 18, 'bold')).pack()
        # Pomodoro
        self.pomodoro_label = tk.Label(bg='pink', fg='white', font=('calibri', 60))
        # Long Break
        self.long_label = tk.Label(bg='pink', fg='white', font=('calibri', 60))
        # Short Break
        self.short_label = tk.Label(bg='pink', fg='white', font=('calibri', 60))

        self.time_label = tk.Label(bg='pink', fg='white', font=('calibri', 60))

        # Buttons
        self.pomodoro = tk.Button(self, text='Pomodoro', bg='pink', activebackground='lightgrey',
                                  font=('ArialRounded', 16), command=self.pomodoro_time)
        self.pomodoro.place(x=40, y=100)
        self.new_pomodoro = None

        self.long_break = tk.Button(self, text='Long Break', bg='pink', activeforeground='crimson',
                                    font=('ArialRounded', 16), command=self.long_time)
        self.long_break.place(x=230, y=100)
        self.new_long_break = None

        self.short_break = tk.Button(self, text='Short Break', bg='pink', activeforeground='crimson',
                                     font=('ArialRounded', 16), command=self.short_time)
        self.short_break.place(x=430, y=100)
        self.new_short_break = None

        tk.Button(self, text='STOP', bg='white', activeforeground='crimson',
                  fg='#D95550', padx=50, pady=0, font=('ArialRounded', 22), command=self.stop).place(x=190, y=300)

        self.stop_loop = False

    def start_thread(self):
        thread = threading.Thread(target=self.start)
        thread.start()

    def start(self, total_time):
        self.stop_loop = False

        while total_time > 0 and not self.stop_loop:
            mins, secs = divmod(total_time, 60)

            self.time_label.pack(anchor='center', pady=100)
            self.time_label.config(text=f"{mins:02d}:{secs:02d}", bg='pink', fg='white', font=('ArialRounded', 60))

            self.update()
            sleep(1)
            total_time -= 1

        if not self.stop_loop:
            self.time_label.config(text="00:00", bg='pink', fg='white', font=('ArialRounded', 60))

    def stop(self):
        self.stop_loop = True

    def pomodoro_time(self):
        self.long_label.forget()
        self.short_label.forget()
        total_time = 25 * 60

        self.long_break = tk.Button(self, text='Long Break', bg='pink', activeforeground='crimson',
                                    font=('ArialRounded', 16), command=self.long_time)
        self.long_break.place(x=230, y=100)

        self.short_break = tk.Button(self, text='Short Break', bg='pink', activeforeground='crimson',
                                     font=('ArialRounded', 16), command=self.short_time)
        self.short_break.place(x=430, y=100)

        self.new_pomodoro = tk.Button(self, text='Pomodoro', bg='crimson',
                                      font=('ArialRounded', 16), command=self.pomodoro_time)
        self.new_pomodoro.place(x=40, y=100)

        self.start(total_time)

    def long_time(self):
        self.pomodoro_label.forget()
        self.short_label.forget()
        total_time = 15 * 60

        self.pomodoro = tk.Button(self, text='Pomodoro', bg='pink', activeforeground='crimson',
                                  font=('ArialRounded', 16), command=self.pomodoro_time)
        self.pomodoro.place(x=40, y=100)

        self.short_break = tk.Button(self, text='Short Break', bg='pink', activeforeground='crimson',
                                     font=('ArialRounded', 16), command=self.short_time)
        self.short_break.place(x=430, y=100)

        self.new_long_break = tk.Button(self, text='Long Break', bg='crimson',
                                        font=('ArialRounded', 16), command=self.long_time)
        self.new_long_break.place(x=230, y=100)

        self.start(total_time)

    def short_time(self):
        self.pomodoro_label.forget()
        self.long_label.forget()
        total_time = 5 * 60

        self.pomodoro = tk.Button(self, text='Pomodoro', bg='pink', activeforeground='crimson',
                                  font=('ArialRounded', 16), command=self.pomodoro_time)
        self.pomodoro.place(x=40, y=100)

        self.long_break = tk.Button(self, text='Long Break', bg='pink', activeforeground='crimson',
                                    font=('ArialRounded', 16), command=self.long_time)
        self.long_break.place(x=230, y=100)

        self.new_short_break = tk.Button(self, text='Short Break', bg='crimson', font=('ArialRounded', 16),
                                         command=self.short_time)
        self.new_short_break.place(x=430, y=100)

        self.start(total_time)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()


if __name__ == "__main__":
    app = App()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()
