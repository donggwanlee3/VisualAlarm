import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta

class TimerWidget:
    def __init__(self, app):
        self.app = app
        self.root = app.root

        self.label = tk.Label(self.root, text="Set Timer (minutes)", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.timer_entry = tk.Entry(self.root, font=("Helvetica", 14), width=10)
        self.timer_entry.pack(pady=10)

        self.set_button = tk.Button(self.root, text="Set Timer", font=("Helvetica", 14), command=self.set_timer)
        self.set_button.pack(pady=20)

    def set_timer(self):
        try:
            minutes = int(self.timer_entry.get())
            if minutes <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of minutes")
            return

        if self.app.url_widget.url is None:
            messagebox.showerror("Invalid Input", "Please enter your URL")
            return

        alarm_time = (datetime.now() + timedelta(minutes=minutes)).strftime("%H:%M")
        url = self.app.url_widget.url
        self.app.add_alarm(alarm_time, url)
