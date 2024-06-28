import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class AlarmWidget:
    def __init__(self, app):
        self.app = app
        self.root = app.root

        self.label = tk.Label(self.root, text="Set Alarm Time in (HH:MM) format", font=("Helvetica", 14))
        self.label.pack(pady=20)

        self.time_entry = tk.Entry(self.root, font=("Helvetica", 14), width=10)
        self.time_entry.pack(pady=10)

        self.set_button = tk.Button(self.root, text="Set Alarm", font=("Helvetica", 14), command=self.set_alarm)
        self.set_button.pack(pady=20)

    def set_alarm(self):
        alarm_time = self.time_entry.get()
        if self.app.url_widget.url is None:
            messagebox.showerror("Invalid Input", "Please enter your URL")
            return
        url = self.app.url_widget.url
        self.app.add_alarm(alarm_time, url)



