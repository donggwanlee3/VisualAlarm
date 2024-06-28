import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class LogWidget:
    def __init__(self, app):
        self.app = app
        self.root = app.root

        self.alarm_listbox = tk.Listbox(self.root, font=("Helvetica", 14), width=50)
        self.alarm_listbox.pack()
        self.alarm_listbox.bind('<<ListboxSelect>>', self.on_listbox_select)

        self.delete_button = ttk.Button(self.root, text="Delete Selected Alarm", command=self.delete_selected_alarm)
        self.delete_button.pack(pady=10)
    
    
    def on_listbox_select(self, event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            self.app.selected_index = selection[0]
        else:
            self.app.selected_index = None

    def delete_selected_alarm(self):
        if self.app.selected_index is not None:
            del self.app.alarms[self.app.selected_index]
            self.app.update_alarm_listbox()
        else:
            messagebox.showerror("Error", "No alarm selected")